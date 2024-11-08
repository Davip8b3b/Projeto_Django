from django.db import models

class Topic(models.Model):
    """Um assunto de teste para aprendizado"""

    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.text
    
