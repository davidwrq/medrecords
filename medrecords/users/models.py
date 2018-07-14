from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _



USER_TYPES = (
    ('1', 'Doctor'),
    ('2', 'Paciente'),
)
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    rut = CharField('Rut', max_length=255, blank=True)
    user_type = CharField(
        max_length=255, verbose_name='Tipo de usuario', choices=USER_TYPES,
        default='Paciente', blank=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
