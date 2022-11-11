from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User

from django.core.validators import MaxLengthValidator
# Create your models here.


class Card(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    firstName = models.CharField(max_length = 200)
    middleName = models.CharField(max_length = 200, null=True, blank=True)
    lastName = models.CharField(max_length = 200)
    nickName = models.CharField(max_length = 200, null=True, blank=True)
    gender = models.CharField(max_length=50, choices=(
        ('Male', 'Male'),
        ('Female', 'Female')
    ))
    info = models.CharField(max_length=30, null=True, blank=True)
    emailAddress = models.EmailField(max_length = 200, null=True, blank=True)
    Address	= models.CharField(max_length = 256, null=True, blank=True)
    City = models.CharField(max_length = 200, null=True, blank=True)
    postalCode = models.IntegerField(null=True, blank=True)
    State = models.CharField(max_length = 200, null=True, blank=True)
    Country = models.CharField(max_length = 200, null=True, blank=True, default = "India")
    image = models.ImageField(upload_to='images/', null=True, blank = True)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.firstName

    #For making the newly added data to appear first
    class Meta:
        ordering = ['-id']

# class additionalWorkInfo(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     card = models.ForeignKey(Card, on_delete = models.CASCADE)
#     workType = models.CharField(max_length=50, null=True, blank=True, choices=(
#         ('job', 'Job'),
#         ('business', 'Business')
#     ))
#     workEmailAddress = models.EmailField(max_length = 200, null=True, blank=True)
#     workAddress	= models.CharField(max_length = 256, null=True, blank=True)
#     workCity = models.CharField(max_length = 200, null=True, blank=True)
#     workPostalCode = models.IntegerField(null=True, blank=True)
#     workState = models.CharField(max_length = 200, null=True, blank=True)
#     workCountry	= models.CharField(max_length = 200, null=True, blank=True, default = "India")
#     workWebsite = models.CharField(max_length = 200, null=True, blank=True)
#     workMobile = models.IntegerField(null=True, blank=True)
#     workPhone = models.IntegerField(null=True, blank=True)
#     workFax = models.IntegerField(null=True, blank=True)
#     workCompany	= models.CharField(max_length = 200, null=True, blank=True)
#     workJobTitle = models.CharField(max_length = 200, null=True, blank=True)


#     def __str__(self):
#         return str(self.card)

    #For making the newly added data to appear first
    class Meta:
        ordering = ['-id']

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    card = models.ForeignKey(Card, on_delete = models.CASCADE)
    type = models.CharField(max_length=100, choices = (
                    ('Landline', 'LandLine'),
                    ('Mobile', 'Mobile'),
                    ('Fax', 'Fax')
                )
            )
    number = models.CharField(max_length=10)

    def __str__(self):
        return (str(self.card)+ " | "+str(self.type))