from django.db import models

# Create your models here.

class ModelBase(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, null=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True