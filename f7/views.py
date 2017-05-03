from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
# from f7.models import *
import string
import random

def f7(request, tp, a, b, c, d, e):
	# randomiza
	tp, a, b, c, d, e = def_var(tp, a, b, c, d, e)
	# define
	tt = 'f7/%s' % (tp)
	url = reverse('bg', args=(tp, a, b, c, d, e))
	if tp == 'piet':
		f = def_f(b, c, d, e)
		return render(request, 'f7/f7.html', {'tt':tt, 'url1':url, 'url2':url, 'f7':f})
	else:
		t = def_d(d)
		v1, v2 = def_e(e)
		return render(request, t, {'tt':tt, 'url1':url, 'url2':url, 'v1':v1, 'v2':v2})

def bg(request, tp, a, b, c, d, e):
	# randomiza
	tp, a, b, c, d, e = def_var(tp, a, b, c, d, e)
	# define
	t = 'f7/bg.html'
	tt = 'f7/bg/%s' % (tp)
	url = reverse('f7', args=(tp, a, b, c, d, e))
	rl = def_a(a)
	bg = def_c(tp, c)
	return render(request, t, {'tt':tt, 'url':url, 'bg':bg, 'rl':rl})

# defs
def def_var(tp, a, b, c, d, e):
	if tp == '':
		tp = random.choice(list(d7.keys()))
	if a == '':
		a = random.choice(d7[tp]['a'])
		b = random.choice(d7[tp]['b'])
		c = random.choice(d7[tp]['c'])
		d = random.choice(d7[tp]['d'])
		e = random.choice(d7[tp]['e'])
	if c == 'def':
		c = def_xxx()
	if b[1:] == 'def':
		b = b[0] + def_xxx()
	return tp, a, b, c, d, e

def def_xxx():
	cor = ''
	for i in range(3):
		cor += random.choice(['0', '1', 'x',])
	if 'x' not in cor:
		if cor == '000' or cor == '111':
			cor = 'x'
		else:
			cor = def_xxx()
	return cor

def def_rgb(c):
	cor = ''
	for k in c:
		if k == 'x':
			k = str(random.randint(0, 255))
		elif k == '1':
			k = '255'
		cor += '%s,' % (k)
	if len(c) == 1:
		cor = cor*3
	return 'rgb(%s)' % (cor[:-1])

def def_hxc(c):
	cor = ''
	for k in c:
		if k == 'x':
			for i in range(2):
				cor += random.choice(list(string.hexdigits))
		elif k == '0':
			cor += '00'
		elif k == '1':
			cor += 'ff'
	if len(c) == 1:
		cor = cor*3
	return '#%s' % (cor)

def def_a(a):
	if a == '0':
		return ''
	elif a == '1':
		return '0'
	elif a == 'x':
		return str(random.randint(5,20))

def def_c(tp, c):
	if tp == 'img':
		return 'background: url(%s) no-repeat;' % (c)
	else:
		if c == 'pb':
			c = random.choice(['0', '1'])
		elif c == 'rgb':
			c = random.choice(['100', '010', '001', '0'])
		elif c == 'piet':
			c = random.choice(['1', random.choice(['100', '110', '001']) ])
		elif c == 'cmyx':
			c = random.choice(['011', '101', '110', random.choice(['0', '1']) ])
		return 'background: %s;' % (def_rgb(c))

def def_d(d):
	if d == 'x':
		d = random.choice(['v', 'h'])
	return 'f7/f7%s.html' % (d)

def def_e(e):
	if e == '0':
		v1 = v2 = 50
	elif e == '1':
		phi = [38.1966, 61.8034]
		v1 = phi.pop(random.randint(0, 1))
		v2 = phi[0]
	elif e == 'x':
	    v1 = random.randint(25, 75)
	    v2 = 100 - v1
	return str(v1) + '%', str(v2) + '%'

def def_f(b, c, d, e):
	# divisao
	if d == 'x':
		d = random.choice(['v', 'h'])
	if d == 'v':
		d = 'cols'
	elif d == 'h':
		d = 'rows'
	# proporcao
	if e == '0':
		e = 50
	elif e == '1':
		e = random.choice([40, 60])
	elif e == 'x':
	    e = random.randint(25, 75)
	# borda
	bc = ''
	if len(b) > 1:
		bc = b[1:]
		b = b[0]
	if b == 'x':
		b = random.choice(['0', '1'])
	if b == '1':
		# cor borda
		if bc == '':
			if c == 'pb':
				bc = 'x'
			elif c == 'rgb':
				bc = '1'
			elif c == 'piet':
				bc = '0'
			elif c == 'xxx':
				bc = c
			else:
				bc = random.choice(['0', '1'])
		elif bc == 'pb':
			bc = random.choice(['0', '1'])
		return '{0}="{1}%,*" frameborder="{2}" border="10" bordercolor="{3}"'.format(d, str(e), b, def_hxc(bc))
	else:
		return '{0}="{1}%,*" frameborder="{2}"'.format(d, str(e), b)

# variaveis
# atualiza
d7a = [
	'0', # nao atualiza
	'1', # atualiza 0s
	'x', # atualiza random()s
]
# borda
d7b = [
	'0', # sem borda
	'1', # com borda
	'x', # random
]
# cor / img
d7c = [
	'piet', # choice(r, y, b, w)
	'pb', # choice(p, b)
	'rgb', # choice(r, g, b, k)
	'cmyx', # choice(c, m, y, x)
	'xxx', # rgb random
	'10x', # magenta/vermelho random
	'00x', # azul/preto random
	'def', # def_xxx
]
# divisao
d7d = [
	'x', # /choice(v, h)
	'v', # /vertical
	'h', # /horizontal
]
# proporcao
d7e = [
	'0', # 50%
	'1', # phi
	'x', # random
]

d7 = {
	'rgb' : {
		'a' : d7a,
		'b' : d7b[0],
		'c' : d7c,
		'd' : d7d[0],
		'e' : d7e,
	},
	'img' : {
		'a' : d7a[0],
		'b' : d7b[0],
		'c' : ['/static/f7/hasselhoffian-recursion.gif',],
		'd' : d7d[0],
		'e' : d7e,
	},
	'piet' : {
		'a' : d7a,
		'b' : d7b,
		'c' : d7c,
		'd' : d7d[0],
		'e' : d7e,
	},
}

