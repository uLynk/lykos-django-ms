from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Avaliacao(models.Model):
    # Quem está sendo avaliado
    freelancer_id = models.BigIntegerField()
    
    # Quem avaliou
    avaliador_id = models.BigIntegerField()
    
    # serviço fornecido
    pacote_id = models.BigIntegerField()
    
    # A Nota com base em estrelas (1 a 5)
    nota = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    
    comentario = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['-data_criacao']

    def __str__(self):
        return f"Nota {self.nota} para Freelancer {self.freelancer_id}"