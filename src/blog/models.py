from django.db import models
from django.urls import reverse, reverse_lazy

# Create your models here.


class Article(models.Model):
    title   = models.CharField(max_length=120)
    content = models.TextField()
    active  = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse_lazy('articles:article-detail', kwargs={"id": self.id})


