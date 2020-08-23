from django.db import models
from django.contrib.auth.models import User

class TP(models.Model):
	cn = models.SlugField(max_length=50, unique=True)
	d0 = models.DateTimeField(auto_now_add = True)
	pae = models.ForeignKey(User, on_delete=models.CASCADE)
	tptp = models.ForeignKey('self', on_delete=models.CASCADE, limit_choices_to={'tptp__isnull':True}, blank=True, null=True)

	def __str__(self):
		return '%s_%s' % (self.id, self.cn)

	class Meta:
		ordering = ['id']

class I0(models.Model):
	# i0 = id
	cn = models.SlugField(max_length=100, unique=True,)
	d0 = models.DateTimeField(auto_now_add = True)
	pae = models.ForeignKey(User, on_delete=models.CASCADE)
	tp = models.ForeignKey(TP, on_delete=models.CASCADE, limit_choices_to={'tptp__isnull':True})

	def __str__(self):
		return '%s_%s' % (self.id, self.cn)

	class Meta:
		ordering = ['id']

class TXT(models.Model):
	i0 = models.OneToOneField(I0, on_delete=models.CASCADE, limit_choices_to={'tp_id':2})
	tt = models.CharField(max_length=400, blank=True,)
	txt = models.TextField()
	tp = models.ForeignKey(TP, on_delete=models.CASCADE, limit_choices_to={'tptp_id':2})
	dt = models.DateField(blank=True, null=True)
	hr = models.TimeField(blank=True, null=True)

	def __str__(self):
		return '%s' % (self.i0)

	class Meta:
		ordering = ['id']
