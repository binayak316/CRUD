from django.db import models

# Create your models here.
class curdmodels(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # last_modified = models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to="images/", blank=True, null=True)


    def __str__(self):
        return self.title





