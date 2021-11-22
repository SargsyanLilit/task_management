from django.db import models
from helpers.choices import STATUS_CHOICES

# Create your models here.


class Task(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        task = Task.objects.filter(name=self.name).first()

        if not self.id:
            if task and task.name == self.name:
                raise ValidationError("Name already exist")

        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.name} - {self.created_at} - {self.status}'