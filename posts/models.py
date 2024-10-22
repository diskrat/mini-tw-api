from django.db import models

# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
