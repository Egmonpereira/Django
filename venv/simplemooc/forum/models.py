from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings

# Create your models here.

class Thread(models.Model):

    title = models.CharField(
        'Título', max_length=100
    )
    body = models.TextField(
        'Mensagem'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Autor', 
        related_name='threads', on_delete=models.CASCADE
    )
    views = models.IntegerField(
        'Visualizações', blank=True, default=0
    )
    answers = models.IntegerField(
        'Respostas', blank=True, default=0
    )
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    modified_at = models.DateTimeField(
        'Modificado em', auto_now=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tópico'
        verbose_name_plural = 'Tópicos'
        ordering = ['-modified_at']

class Reply(models.Model):

    thread = models.ForeignKey(
        Thread, verbose_name='Tópicos', related_name='replies',
        on_delete=models.CASCADE
    )
    reply = models.TextField(
        'Resposta'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Autor', related_name='replies',
        on_delete=models.CASCADE
    )
    correct = models.BooleanField(
        'Correta?', blank=True, default=False
    )
    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True
    )

    def __str__(self):
        return selr.reply[:100]

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'
        ordering = ['-correct', 'created_at']

    tags = TaggableManager()