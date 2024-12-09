from django.db import models

class Posts(models.Model):
    titulo = models.CharField(max_length=20)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.titulo