from django.db import models

# Create your models here.

class Customer(models.Model):

    real_gender = [('남자','남자'),('여자','여자')]
    name = models.CharField(max_length=40)
    birthdate = models.DateField(max_length=15)
    email = models.EmailField(max_length=30)
    gender = models.CharField(choices=real_gender,max_length=10)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name