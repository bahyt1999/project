from django.db import models
from django.shortcuts import reverse
# Create your mod


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="images/", null=True, blank=True,default=True)
    create_date = models.DateTimeField()
    viewer = models.IntegerField()
    balls = models.FloatField(default=True)
    final_payment = models.IntegerField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.id})
#новый гетюрл2

    def get_absolut_url2(self):
        return reverse('total', kwargs={'pk': self.id})

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url



