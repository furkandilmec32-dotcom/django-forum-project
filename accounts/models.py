from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """Kullanici profil modeli - her kullanicinin bir profili olacak"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True, help_text="Hakkinda kisa bilgi")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, help_text="Profil resmi")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'in profili"
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


# Yeni kullanici olusturuldugunda otomatik profil olustur
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()