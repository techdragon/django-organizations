from django.conf import settings  # NOQA
# TODO use the chosen User model
from django.contrib.auth.models import User
from appconf import AppConf
from .utils import model_field_attr


class OrgsConf(AppConf):
    EMAIL_LENGTH = model_field_attr(User, 'email', 'max_length')
    INVITATION_BACKEND = 'organizations.backends.defaults.InvitationBackend'
    REGISTRATION_BACKEND = 'organizations.backends.defaults.RegistrationBackend'
    SLUGFIELD = 'django_extensions.db.fields.AutoSlugField'
    TIMESTAMPED_MODEL = 'django_extensions.db.models.TimeStampedModel'

    class Meta:
        prefix = 'orgs'
