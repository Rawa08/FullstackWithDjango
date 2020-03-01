from django.db import models
from products.models import Perfume

# Create your models here.
class Comment(models.Model):
    scoreChoice=(('1',1),('2',2),('3',3),('4',4),('5',5),('0',0))
    product = models.ForeignKey(Perfume,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    Comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    score = models.CharField(choices=scoreChoice,max_length=1, default=5)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.Comment, self.name)