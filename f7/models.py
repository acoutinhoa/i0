from django.db import models

class T2(models.Model):
	d0 = models.DateTimeField(auto_now = True)
	n0 = models.CharField(max_length=10)
	r1 = models.ManyToManyField('self', blank=True, symmetrical=False)

	def __str__(self):
		return self.n0

	class Meta:
		ordering = ['pk']

class F7(models.Model):
	def def_caminho(instance, filename):
		return 'f7/{0}/{1}'.format(instance.t2.n0, filename)

	d0 = models.DateTimeField(auto_now = True)
	n0 = models.CharField(max_length=30)
	t2 = models.ForeignKey(T2)
	r1 = models.ManyToManyField('self', blank=True)
	# r1 = models.ManyToManyField('self', blank=True, symmetrical=False)
	img = models.ImageField(upload_to=def_caminho, height_field='h', width_field='w', blank=True, null=True)
	w = models.CharField(max_length=10, editable=False, blank=True, null=True)
	h = models.CharField(max_length=10, editable=False, blank=True, null=True)

	def __str__(self):
		return '%s_%s' % (self.t2, self.n0)

	class Meta:
		ordering = ['?']

