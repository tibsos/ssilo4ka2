import os

from django.db import models as m

from django.contrib.auth.models import User

from uuid import uuid4 as u4

def upload_profile_photo(instance, filename):

    file_extension = filename.split('.')[-1]
    new_filename = f"{u4}.{file_extension}"

    return os.path.join('uploads/profile-pics', new_filename)

class Profile(m.Model):

    uid = m.UUIDField(default = u4)

    user = m.OneToOneField(User, on_delete=m.CASCADE)
    
    name = m.CharField(max_length = 100)

    bio = m.TextField(blank=True, null=True)
    
    profile_picture = m.ImageField(upload_to=upload_profile_photo, blank = True, null = True)


class Link(m.Model):

    uid = m.UUIDField(default = u4)

    profile = m.ForeignKey(Profile, on_delete=m.CASCADE, related_name='links')
    order = m.PositiveIntegerField(default=0)
    
    title = m.CharField(max_length=50)
    
    url = m.URLField(max_length=500)

    icon = m.ForeignKey('Icon', on_delete = m.DO_NOTHING, blank = True, null = True)
    

    redirect = m.BooleanField(default = False)

    class Meta:
        
        ordering = ['order']

    def __str__(self):
        return f'{self.title} - {self.url}'
    

class Icon(m.Model):

    title = m.TextField()
    file = m.TextField()

    def __str__(self):

        return self.title