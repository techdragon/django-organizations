from django.utils.importlib import import_module

from ..conf import settings


def invitation_backend():
    # TODO exception handling
    class_module, class_name = settings.ORGS_INVITATION_BACKEND.rsplit('.', 1)
    mod = import_module(class_module)
    return getattr(mod, class_name)()


def registration_backend():
    class_module, class_name = settings.ORGS_REGISTRATION_BACKEND.rsplit('.', 1)
    mod = import_module(class_module)
    return getattr(mod, class_name)()
