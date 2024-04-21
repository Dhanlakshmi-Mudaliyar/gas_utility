from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cus_name = models.CharField(max_length=70)
    cus_email = models.EmailField(unique=True)
    cus_phone_no = models.CharField(max_length=12)
    cus_add = models.TextField()


class Request(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    req_type = models.CharField(max_length=200)
    details = models.TextField()
    status = models.CharField(max_length=15, default="Pending")
    submit_at = models.DateTimeField(auto_now_add=True)
    solved_at = models.DateTimeField(auto_now=True)

# Create your models here.
