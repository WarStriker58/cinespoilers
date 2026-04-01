from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title