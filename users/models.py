from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from PIL import Image, ExifTags


class Profile(models.Model):
    GENDER_CHOICES =(
        ('M','Male'),
        ('F','Female'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg', 
                upload_to='profiles_img/',
                verbose_name="Avatar",
                null=True,
                )
    
    gender = models.CharField(max_length=1, 
                              choices=GENDER_CHOICES, default='M')
    bio = models.TextField(max_length=1024, null=True, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        try:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                        break
            exif = dict(img._getexif().items())

            if exif[orientation] == 3:
                img = img.rotate(180, expand=True)
            elif exif[orientation] == 6:
                img = img.rotate(270, expand=True)
            elif exif[orientation] == 8:
                img = img.rotate(90, expand=True)
        except (AttributeError, KeyError, IndexError):
            print('no data to rotate image')
            pass

        if img.height > 300 or img.width > 300:
            new_size = (300,300)
            img.thumbnail(new_size)
        
        img.save(self.image.path)

    @receiver(post_save, sender=User) 
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User) 
    def save_profile(sender, instance, **kwargs):
            instance.profile.save()