from django.db import models


class Foo(models.Model):
    bar = models.CharField(max_length=100)

    class Meta:
        permissions = (
                ('view_foo', 'Can view foo'),
                )
