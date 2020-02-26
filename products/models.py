from django.db import models

# Create your models here.

class Perfume(models.Model):
    genderChoice = (
        ('U','Unisex'), ('M', 'Male'), ('F', 'Female'))
    volumeChoice = (('25',25), ('30',30),('40', 40),('50', 50), ('65', 65),('70', 70), ('90',90), 
    ('100',100), ('125',125), ('130',130), ('150',150), ('175',175), ('200',200), ('300',300))
    name = models.CharField(max_length=30, default='')
    brand = models.CharField(max_length=30, default='')
    gender = models.CharField(max_length=5, choices=genderChoice, default='U')
    volume = models.CharField(choices=volumeChoice, max_length=5)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    created = models.DateField()

    def __str__(self):
        return self.name
