# coding: utf-8
from django.db import models
from django.db.models import Sum
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from lancamento.models import Lancamento

class ContaManager(models.Manager):

    def ativas(self):
        return self.filter(ativa=True)

    def inativas(self):
        return self.filter(ativa=False)

    def get_somatorio_saldo_contas_ativas(self):
        somatorio = 0.00
        for conta in self.ativas():
            somatorio += conta.get_saldo
        return somatorio

class Conta(models.Model):
    descricao = models.CharField(_(u'descrição'), max_length=30)
    ativa     = models.BooleanField(_(u'ativa'), default=True)

    objects = ContaManager()

    class Meta:
        ordering            =   [u'descricao']
        verbose_name        =   _(u'conta')
        verbose_name_plural =   _(u'contas')

    def __unicode__(self):
        return self.descricao.upper()

    @property
    def get_absolute_url(self):
        return reverse('conta_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('conta_delete', args=[str(self.id)])

    @property
    def get_saldo(self):
        total = Lancamento.objects.filter(conta=self).aggregate(total=Sum('valor'))['total']
        if not total:
            return float('0.00')
        return float(total)
