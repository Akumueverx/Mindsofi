from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Puedes añadir más campos aquí si lo necesitas en el futuro

    def __str__(self):
        return f'Perfil de {self.user.username}'

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Crea un perfil automáticamente cuando se crea un nuevo usuario.
    """
    if created:
        Profile.objects.create(user=instance)