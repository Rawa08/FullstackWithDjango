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
    image = models.ImageField(upload_to='images/product_image')
    created = models.DateField()

    def __str__(self):
        return self.name


#https://djangocentral.com/creating-comments-system-with-django/
class CommentPerfume(models.Model):
    product = models.ForeignKey(Perfume,on_delete=models.CASCADE,related_name='review')
    name = models.CharField(max_length=80)
    body = models.TextField()
    score = models.IntegerField(range(1, 5))
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)