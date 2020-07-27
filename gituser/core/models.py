from django.db import models

# uploding images in django 



class Image(models.Model):
    title    = models.CharField(max_length=60)
    image    = models.ImageField(upload_to ="images/")

    def __str__(self):
        return self.title



