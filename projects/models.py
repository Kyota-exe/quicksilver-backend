from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ("DESIGN", "In design"),
            ("READY", "Ready for deployment"),
            ("ACTIVE", "Active"),
        ],
        default="DESIGN",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
