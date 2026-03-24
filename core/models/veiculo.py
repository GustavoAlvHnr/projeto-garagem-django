from django.db import models


class veiculo(models.Model):
    modelo = models.ForeignKey('modelo', on_delete=models.PROTECT, related_name='veiculos')
    cor = models.ForeignKey('cor', on_delete=models.PROTECT, related_name='veiculos')
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0)
    acessorios = models.ManyToManyField('acessorios', related_name='veiculos')

    def __str__(self):
        return f'{self.id} - {self.modelo} - {self.cor} - {self.ano} - R${self.preco}'

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'
