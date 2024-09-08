from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import settings
from django.utils.timezone import datetime
from django.utils.safestring import mark_safe

# Create your models here.

class Tweet(models.Model):

    objects = models.Manager

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='photo/')

    is_active = models.BooleanField(
         default=True, null=True, blank=True, editable=False)
    # created_by = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    created_on = models.DateField(
        default=datetime.now, editable=False, null=True, blank=True)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="30" />'.format(self.photo.url))
    
    admin_photo.short_description = 'Photo'
    admin_photo.allow_tags = True

    class Meta:
        verbose_name_plural = "Tweets"
        verbose_name = "Tweet"

    def __str__(self):
        return self.user.username
    
