from django.db import models
from django.utils.text import slugify

# Create your models here.

class Ordem_de_servico(models.Model):
    os = models.CharField(max_length=12)
    p_a = models.CharField(max_length=9)
    p_c = models.CharField(max_length=9)
    operacao = models.CharField(max_length=30)
    n_operacao = models.CharField(max_length=4)
    nome_pc = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    uo = models.CharField(max_length=3)
    fixacao = models.CharField(max_length=15)
    data = models.DateField()
    hora = models.TimeField()
    slug = models.SlugField(unique=True, max_length=100)

    def save(self, *args, **kwargs):
        # Garante que o slug será igual ao campo `os`
        if not self.slug or self.slug != self.os:
            self.slug = slugify(self.os)  # Transforma em um slug válido (opcional)
        super().save(*args, **kwargs)