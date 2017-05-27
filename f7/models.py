from django.db import models

class T2(models.Model):
	n3 = models.CharField(max_length=10)
	d0 = models.DateTimeField(auto_now_add = True)
	r1 = models.ManyToManyField('self', blank=True, symmetrical=False)

	def __str__(self):
		return self.n3

	class Meta:
		ordering = ['pk']

class F7(models.Model):
	n3 = models.CharField(max_length=30)
	t2 = models.ForeignKey(T2)
	r1 = models.ManyToManyField('self', blank=True)
	# r1 = models.ManyToManyField('self', blank=True, symmetrical=False)
	d0 = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return '%s_%s' % (self.t2, self.n3)

	class Meta:
		ordering = ['?']

