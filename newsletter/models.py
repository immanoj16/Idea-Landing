from __future__ import unicode_literals

from django.db import models


class Join(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.email
