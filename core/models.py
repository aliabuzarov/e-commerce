from django.db import models
from .validators import validate_email




class AbstarctModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True





class Subscribe(AbstarctModel):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Contact(AbstarctModel):

    first_name = models.CharField('First Name', max_length=200)
    last_name = models.CharField('Last Name', max_length=200, null=True, blank=True)
    email = models.EmailField('Email', max_length=200, validators=[validate_email])
    phone = models.CharField('phone', max_length=200)
    message = models.TextField('message', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'