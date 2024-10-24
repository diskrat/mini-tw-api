from django.db import models

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(
        'auth.User',
        related_name='posts',
        on_delete=models.CASCADE
    )

    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


class Like(models.Model):
    
    user = models.ForeignKey(
        'auth.User',
        related_name='likes',
        on_delete=models.CASCADE
    )
    
    post = models.ForeignKey(
        Post,
        related_name='likes',
        on_delete=models.CASCADE
    )
    
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user','post')
