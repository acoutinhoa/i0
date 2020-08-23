from django.db import models

##############################################

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
	n0 = models.CharField('titulo',max_length=100)
	t0 = models.CharField('titulo_original',max_length=100, blank=True, null=True)
	diretores = models.ManyToManyField(D1, blank=True)
	ano = models.CharField(max_length=4, blank=True, null=True)
	sinopse = models.TextField(blank=True, null=True)
	duracao = models.CharField(max_length=10, blank=True, null=True)
	cor = models.CharField(max_length=20, blank=True, null=True)
	formato = models.CharField(max_length=20, blank=True, null=True)
	def __str__(self):
		return self.n0[:10]

# textos
class T1(models.Model):
	d0 = models.DateTimeField(auto_now = True)
	filme = models.ForeignKey(F1, on_delete=models.CASCADE)
	autor = models.ForeignKey(A1, on_delete=models.CASCADE)

	tt = models.CharField('titulo', max_length=30)
	cit = models.TextField('citacao(info/linha)') # notas
	txt = models.TextField('txt') # notas
	ref = models.TextField('referencia/linha')
	def __str__(self):
		return self.tt[:10]

# imagens
class I1(models.Model):
	def def_caminho(instance, filename):
		return 'e4/i1/{0}/{1}'.format(instance.filme.n0, filename)

	d0 = models.DateTimeField(auto_now = True)
	filme = models.ForeignKey(F1, on_delete=models.CASCADE, blank=True, null=True)
	creditos = models.CharField(max_length=200, blank=True, null=True)
	img = models.ImageField(upload_to=def_caminho, height_field='h', width_field='w', blank=True, null=True)
	w = models.CharField(max_length=10, editable=False)
	h = models.CharField(max_length=10, editable=False)
	def __str__(self):
		return '%s_%s' % (self.filme.n0, self.id)

##############################################

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
	img = models.ImageField(upload_to='e4/i0', height_field='h', width_field='w', blank=True, null=True)
	w = models.CharField(max_length=10, editable=False)
	h = models.CharField(max_length=10, editable=False)
	def __str__(self):
		return self.n0

# blocos_grupos_ordem_organizacao
class B0(models.Model):
	d0 = models.DateTimeField(auto_now = True)
	n0 = models.CharField('nome_grupo', max_length=100)

	informacoes = models.ManyToManyField(T0, blank=True)
	logos = models.ManyToManyField(I0, blank=True)
	textos = models.ManyToManyField(T1, blank=True)
	imagens = models.ManyToManyField(I1, blank=True)
	blocos = models.ManyToManyField('self', blank=True)

	def __str__(self):
		return self.n0

# # organizacao
# class O0(models.Model):
# 	material = models.ForeignKey(M0)	
# 	bloco = models.ForeignKey(B0)
# 	ordem = models.IntegerField(default=0)

# 	def reordem(self, n):
# 		self.ordem = self.ordem + n
# 		self.save()
# 	def __str__(self):
# 		return '%s_%s' % (self.material.n0, self.bloco.n0)
# 	class Meta:
# 		ordering = ['material', 'pk+ordem']


# formatos
class F0(models.Model):
	d0 = models.DateTimeField(auto_now = True)
	un = models.CharField(max_length=2, choices=[('mm','mm'),('px','px')], default='mm')
	w = models.CharField('largura', max_length=10)
	h = models.CharField('altura', max_length=10)
	def __str__(self):
		return '%s_%s_%s' % (self.un, self.w, self.h)

# materiais
class M0(models.Model):
	d0 = models.DateTimeField(auto_now = True)
	n0 = models.CharField('nome', max_length=30)

	formatos = models.ManyToManyField(F0, through='P0', through_fields=('material','formato'), blank=True)
	blocos = models.ForeignKey(B0, on_delete=models.CASCADE, blank=True, null=True)
	# blocos = models.ManyToManyField(B00, through='O0', through_fields=('material','bloco'), blank=True)

	obs = models.TextField('obss', blank=True, null=True)

	def __str__(self):
		return self.n0

# pecas graficas
class P0(models.Model):
	d0 = models.DateTimeField(auto_now = True)
	material = models.ForeignKey(M0, on_delete=models.CASCADE)
	formato = models.ForeignKey(F0, on_delete=models.CASCADE)
	q = models.CharField('quantidade', max_length=10)
	verso = models.BooleanField('frenteverso')
	papel = models.CharField(max_length=30, blank=True, null=True)
	gramatura = models.CharField(max_length=10, blank=True, null=True)
	obs = models.TextField('obss', blank=True, null=True)

	def __str__(self):
		return '%s_%s' % (self.material.n0, self.formato)
	class Meta:
		ordering = ['material', 'formato']

