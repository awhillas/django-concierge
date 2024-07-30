from django.db import models


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True)
    user_agent = models.CharField(max_length=255, null=True)
    referrer = models.CharField(max_length=255, null=True)
    screen_width = models.PositiveIntegerField(default=0)
    screen_height = models.PositiveIntegerField(default=0)
    user_agent_family = models.CharField(max_length=50, null=True)
    user_agent_major = models.CharField(max_length=10, null=True)
    user_agent_minor = models.CharField(max_length=10, null=True)
    os_family = models.CharField(max_length=50, null=True)
    os_major = models.CharField(max_length=10, null=True)
    device_family = models.CharField(max_length=50, null=True)
    device_brand = models.CharField(max_length=50, null=True)
    device_model = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user_agent
