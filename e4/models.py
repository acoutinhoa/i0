from django.db import models

# autores
class A1(models.Model):
	d0 = models.DateTimeField(auto_now=True)
	n0 = models.CharField('nome', max_length=50)
	i0 = models.TextField('info')
	def __str__(self):
		return self.n0[:10]

# diretores
class D1(models.Model):
	d0 = models.DateTimeField(auto_now=True)
	n0 = models.CharField('nome', max_length=50)
	def __str__(self):
		return self.n0[:10]

# filmes
class F1(models.Model):
	d0 = models.DateTimeField(auto_now=True)
	dx = models.DateTimeField(auto_now=True)
	n0 = models.CharField('titulo',max_length=100)
	diretores = models.ManyToManyField(D1)
	ano = models.CharField(max_length=4)
	sinopse = models.TextField()
	duracao = models.CharField(max_length=10, blank=True, null=True)
	cor = models.CharField(max_length=20, blank=True, null=True)
	formato = models.CharField(max_length=20, blank=True, null=True)
	def __str__(self):
		return self.n0[:10]

# formatos
class F0(models.Model):
	d0 = models.DateTimeField(auto_now = True)
	un = models.CharField(max_length=2, choices=[('mm','mm'),('px','px')], default='mm')
	w = models.CharField('largura', max_length=10)
	h = models.CharField('altura', max_length=10)
	def __str__(self):
		return '%s_%s_%s' % (self.un, self.w, self.h)

# texto informacao
class T0(models.Model): 
	d0 = models.DateTimeField(auto_now = True)
	n0 = models.CharField('nome', max_length=30)
	txt = models.TextField('txts(info/linha)')
	def __str__(self):
		return self.n0

# logos
class I0(models.Model):
	d0 = models.DateTimeField(auto_now = True)
	n0 = models.CharField('nome', max_length=30)
	# imagem =
	def __str__(self):
		return self.n0

# textos
class T3(models.Model):
	d0 = models.DateTimeField(auto_now = True)
	filme = models.ForeignKey(F1)
	autor = models.ForeignKey(A1)

	tt = models.CharField('nome', max_length=30)
	cit = models.TextField('citacao(info/linha)') # notas
	txt = models.TextField('txt') # notas
	ref = models.TextField('referencia/linha')
	def __str__(self):
		return self.n0

# imagens
class I3(models.Model): 
	d0 = models.DateTimeField(auto_now = True)
	filme = models.ForeignKey(F1)
	creditos = models.CharField(max_length=200)
	# imagem = 

# blocos_grupos_ordem_organizacao
class B1(models.Model):
	d0 = models.DateTimeField(auto_now = True)
	n0 = models.CharField('nome_grupo', max_length=100)

	informacoes = models.ManyToManyField(T0, blank=True)
	logos = models.ManyToManyField(I0, blank=True)
	textos = models.ManyToManyField(T3, blank=True)
	imagens = models.ManyToManyField(I3, blank=True)
	blocos = models.ManyToManyField('self', blank=True)

# # organizacao
# class O0(models.Model):
# 	material = models.ForeignKey(M4)	
# 	bloco = models.ForeignKey(B10)
# 	ordem = models.IntegerField(default=0)

# 	def reordem(self, n):
# 		self.ordem = self.ordem + n
# 		self.save()
# 	def __str__(self):
# 		return '%s_%s' % (self.material.n0, self.bloco.n0)
# 	class Meta:
# 		ordering = ['material', 'pk+ordem']

# materiais
class M4(models.Model):
	d0 = models.DateTimeField(auto_now = True)
	n0 = models.CharField('nome', max_length=30)

	formatos = models.ManyToManyField(F0, through='P3', through_fields=('material','formato'), blank=True)
	# blocos = models.ManyToManyField(B10, through='O0', through_fields=('material','bloco'), blank=True)

	obs = models.TextField('obss', blank=True, null=True)

	def __str__(self):
		return self.n0

# pecas graficas
class P3(models.Model):
	d0 = models.DateTimeField(auto_now = True)
	material = models.ForeignKey(M4)
	formato = models.ForeignKey(F0)
	q = models.CharField('quantidade', max_length=10)
	verso = models.BooleanField('frenteverso')
	papel = models.CharField(max_length=30, blank=True, null=True)
	gramatura = models.CharField(max_length=10, blank=True, null=True)
	obs = models.TextField('obss', blank=True, null=True)

	def __str__(self):
		return '%s_%s' % (self.material.n0, self.formato.un)
	class Meta:
		ordering = ['material', 'formato']

