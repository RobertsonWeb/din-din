# coding: utf-8
from datetime import datetime, timedelta
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

class LancamentoManager(models.Manager):

    def projetados(self):
        return self.filter(situacao='P')

    def concretizado(self):
        return self.filter(situacao='C')

    def pendentes(self):
        print datetime.now()+timedelta(days=7)
        return self.filter(data_lancamento__lt=datetime.now()+timedelta(days=7), conta__ativa=True, situacao='P')

class Lancamento(models.Model):
    SITUACOES = (
        ('P',_('Projetado')),
        ('C',_('Concretizado')),
    )

    CLASSIFICACOES = (
        ('F', _('Fixo')),
        ('V', _(u'Variável')),
    )

    conta = models.ForeignKey('conta.Conta')
    descricao = models.CharField(_(u'descrição'), max_length=70)
    valor = models.DecimalField(_(u'valor'), max_digits=10, decimal_places=2)
    situacao = models.CharField(_(u'situação'), max_length=1, default=None, choices=SITUACOES)
    classificacao = models.CharField(_(u'classificação'), max_length=1, choices=CLASSIFICACOES, default=None)
    observacao = models.TextField(_(u'observação'), blank=True, null=True)
    data_cadastro = models.DateTimeField(_('data do cadastro'), auto_now_add=True)
    data_lancamento = models.DateField(_('data'), default=None, blank=True, null=True)


    objects = LancamentoManager()

    class Meta:
        ordering            =   [u'data_lancamento']
        verbose_name        =   _(u'lançamento')
        verbose_name_plural =   _(u'lançamentos')

    def __unicode__(self):
        return self.descricao.upper()

    @property
    def get_absolute_url(self):
        return reverse('lancamento_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('lancamento_delete', args=[str(self.id)])

    @property
    def get_tipo(self):
        if self.valor > 0.00:
            if self.situacao == 'P':
                return 'A receber'
            else:
                return 'Recebido'
        else:
            if self.situacao == 'P':
                return 'A pagar'
            else:
                return 'Pago'

    @property
    def get_prazo(self):
        if self.situacao == 'C':
            return ''

        if self.data_lancamento > datetime.now():
            print 'No prazo'
            return 'No prazo'
        else:
            print 'Vencido'
            return 'Vencido'
