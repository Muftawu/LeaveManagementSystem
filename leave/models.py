from django.db import models
from accounts.models import CustomUser

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    photo = models.ImageField(upload_to='staff_imgs')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Leave(models.Model):
    LEAVE_TYPE = (
        ('UNWELL', 'UNWELL'),
        ('EMERGENCY', 'EMERGENCY'),
        ('FUNERAL', 'FUNERAL'),
        ('WEDDING', 'WEDDING'),
        ('OTHER REASON', 'OTHER REASON')
        )
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True)
    reason = models.CharField(max_length=50, choices=LEAVE_TYPE, default='UNWELL')
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.reason