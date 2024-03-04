from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category_choices = [
        ('DEV', 'Development'),
        ('SAL', 'Sales'),
        ('FIN', 'Finance'),
        ('HR', 'HR'),
        ('INS', 'Installation'),
    ]
    category = models.CharField(max_length=3, choices=category_choices)
    assignee = models.ManyToManyField(User, related_name='assigned_tasks', blank=True)
    scheduled_date = models.DateField(null=True, blank=True)
    estimation_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return self.title
