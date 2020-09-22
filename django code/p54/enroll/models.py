from django.db import models


# Create your models here.
class User(models.Model):
    """Model definition for User."""

    name = models.CharField(max_length=70)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of User."""
        pass
