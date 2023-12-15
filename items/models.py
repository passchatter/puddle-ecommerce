from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    nama = models.CharField(max_length=200);

    class Meta:
        ordering = ('nama',)
    
    def __str__(self):
        return self.nama
    

class Items(models.Model):
    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
    nama = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="item_images", blank=True, null=True )
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.nama
    