from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    #Propiedades
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    #Acciones
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        # pass

    def __str__(self):
        return self.title
        # pass
