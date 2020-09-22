from django.db import models


# Create your models here.
class Blog(models.Model):
    """Model definition for Blog."""
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)

    class Meta:
        """Meta definition for Blog."""

        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        """Unicode representation of Blog."""
        pass
