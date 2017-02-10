from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SingUp(models.Model):
	name = models.CharField(max_length=120, blank=True, null=True)
	semder = models.EmailField()
	pwd = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.sender