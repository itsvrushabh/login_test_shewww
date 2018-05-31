from django.db import models

# Create your models here.


class LoginDetail(object):
    def __init__(self, **kwargs):
        for field in ('username', 'password', 'host', 'device_type'):
            setattr(self, field, kwargs.get(field, None))
