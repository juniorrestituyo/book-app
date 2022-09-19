from pyexpat import model
from django.db import models
import uuid


class Book(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    STATUS = (
        ("a", "Available"),
        ("n", "No available"),
    )
    status = models.CharField(max_length=200, choices=STATUS, null=True, blank=True)
    CHECKED = (
        ("no", "None"),
    )
    checked = models.CharField(max_length=200, choices=CHECKED, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid1, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
