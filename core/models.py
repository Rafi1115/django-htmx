from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    dute_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-name"]
        verbose_name_plural='1. Todo'