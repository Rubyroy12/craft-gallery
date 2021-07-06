from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30,unique='True')

    def __str__(self):
        return self.name




class Category(models.Model):
    name = models.CharField(max_length=30,unique='True')

    def __str__(self):
        return self.name


class Images(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    posted = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to= 'photos/')


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image(cls):
        image= cls.objects.get(pk=id)
        return image

    @classmethod
    def search_by_category(cls,search_term):
        image_category = cls.objects.filter(name__icontains=search_term)

        return image_category









