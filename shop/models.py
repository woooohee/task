from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    photo = models.ImageField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = models.TextField(blank=True) ###

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:item_detail', args=[self.pk])