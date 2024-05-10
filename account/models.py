from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserToken(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	token = models.CharField(max_length=21)
	expiration_date = models.DateTimeField()
	used = models.BooleanField(default=False) 
	expired = models.BooleanField(default=False)

	def __str__(self):
		return str(self.token)

	def save(self, *args, **kwargs):
		self.expired = self.is_expired()
		super().save(*args, **kwargs)

	def is_expired(self):
		return self.expiration_date < timezone.now() or self.used

	def mark_as_used(self):
		self.used = True
		self.save()