from django.db import models

class C0(models.Model):
	nome = models.CharField(max_length=30)
	def __str__(self):
		return self.nome

class E1(models.Model):
	nome = models.CharField(max_length=30)
	def __str__(self):
		return self.nome
	class Meta:
		ordering = ['?']

class C4(models.Model):
	nome = models.CharField(max_length=30)
	def __str__(self):
		return self.nome
	class Meta:
		ordering = ['?']

class T2(models.Model):
	nome = models.CharField(max_length=30)
	def __str__(self):
		return self.nome
	class Meta:
		ordering = ['?']

class M8(models.Model):
	tipo = models.ForeignKey(T2, blank=True, null=True)
	nome = models.CharField(max_length=50, blank=True, null=True)
	cor = models.ManyToManyField(C0, blank=True)
	peso = models.FloatField()
	casa = models.ForeignKey(E1, blank=True, null=True)
	caixa = models.ForeignKey(C4, blank=True, null=True)

	def __str__(self):
		return '%s_%s' % (self.pk, self.nome)

	class Meta:
		ordering = ['pk']

