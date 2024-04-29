from django.db import models

# Create your models here.
class Places(models.Model):
    id=models.IntegerField(primary_key=True)
    places=models.CharField(max_length=50,null=False)
    rating=models.CharField(max_length=5,null=False)

    def __str__(self):
        return self.places