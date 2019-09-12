from django.db import models

class ProductDetail(models.Model):
    name = models.CharField(max_length=120)
    skin_color = models.CharField(max_length=120)
    blood_type = models.CharField(max_length=120)
    amputation_date = models.DateTimeField(auto_now_add=True)
    expiary_date = models.DateTimeField(auto_now_add=True)
    reason_for_amputation = models.TextField()
    quantity = models.IntegerField()
    image = models.ImageField(blank=True, null=True)
    # content = models.TextField()
    # author = models.CharField(max_length=120)

    def __str__(self):
        return self.title

# class User(models.Model):
# 	username = models.CharField(max_length=120)
# 	civil_ID = models.IntegerField()