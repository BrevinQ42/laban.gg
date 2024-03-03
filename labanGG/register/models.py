from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def validate_contact_number(value):
    """
    Validate that the mobile number has the format #### ### ###
    """
    if len(value) != 11 or not value.replace(' ', '').isdigit():
        raise ValidationError('Mobile number must be in the format #### ### ###')

class Account(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=32)
    isOrganizer = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.email

class OrganizerAccount(Account):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=32)
    contact_number = models.CharField(max_length=15, validators=[validate_contact_number])
    past_experience = models.TextField()
    additional_comments = models.TextField()

    def __str__(self) -> str:
        return self.email