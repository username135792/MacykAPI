from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    source = models.CharField(max_length=200, blank=True)
    themes = models.ManyToManyField(Theme, related_name='quotes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'"{self.text[:50]}..." - {self.author}'