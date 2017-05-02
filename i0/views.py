from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
from i0.models import *
import string
import random

def index0f(request):
	return HttpResponse('index0f')

def f7(request, tp, a, b, c, d, e):
	# randomiza variaveis
	if tp == '':
		tp = random.choice(list(d7.keys()))
	if a == '':
		a = random.choice(d7[tp]['a'])
		b = random.choice(d7[tp]['b'])
		c = random.choice(d7[tp]['c'])
		d = random.choice(d7[tp]['d'])
		e = random.choice(d7[tp]['e'])
	t = def_f7d(d)
	tt = 'f7'
	url = reverse('bg', args=(tp, a, b, c, d, e))
	v1, v2 = def_f7e(e)
	return render(request, t, {'tt':tt, 'url1':url, 'url2':url, 'v1':v1, 'v2':v2})

def bg(request, tp, a, b, c, d, e):
	# randomiza variaveis
	if tp == '':
		tp = random.choice(list(d7.keys()))
	if a == '':
		a = random.choice(d7[tp]['a'])
		b = random.choice(d7[tp]['b'])
		c = random.choice(d7[tp]['c'])
		d = random.choice(d7[tp]['d'])
		e = random.choice(d7[tp]['e'])
	t = 'f7/bg.html'
	tt = 'f7/bg'
	url = reverse('f7', args=(tp, a, b, c, d, e))
	rl = def_f7a(a)
	bg = def_f7c(tp, c)
	return render(request, t, {'tt':tt, 'url':url, 'bg':bg, 'rl':rl})


def def_f7a(a):
	if a == '0':
		return ''
	elif a == '1':
		return str(random.randint(5,20))
	elif a == '2':
		return '0'

def def_f7c(tp, c):
	if tp == 'rgb':
		if c == 'pb':
			c = random.choice(['0', '1'])
		elif c == 'rgb':
			c = random.choice(['100', '010', '001', '0'])
		elif c == 'piet':
			c = random.choice(['1', random.choice(['100', '110', '001']) ])
		elif c == 'cmyx':
			c = random.choice(['011', '101', '110', random.choice(['0', '1']) ])
		bg = ''
		for car in c:
			if car == 'x':
				car = str(random.randint(0, 255))
			elif car == '1':
				car = '255'
			bg += '%s,' % (car)
		if len(c) == 1:
			bg = bg*3
		return 'rgb(%s)' % (bg[:-1])
	elif tp == 'img':
		return 'url(/static/i0/gif/%s) no-repeat' % (c)

def def_f7d(d):
	if d == 'x':
		d = random.choice(['v', 'h'])
	return 'f7/f7%s.html' % (d)

def def_f7e(e):
	if e == '0':
		v1 = v2 = 50
	elif e == '1':
	    v1 = random.randint(25, 75)
	    v2 = 100 - v1
	elif e == '2':
		phi = [38.1966, 61.8034]
		v1 = phi.pop(random.randint(0, 1))
		v2 = phi[0]
	return str(v1) + '%', str(v2) + '%'

# atualiza
d7a = [
	'0', # nao atualiza
	'1', # atualiza random()s
	'2', # atualiza 0s
]
# borda
d7b = [
	'0', # sem borda
	'1', # com borda
]
# cor / img
d7c = [
	'pb', # choice(p, b)
	'rgb', # choice(r, g, b, k)
	'piet', # choice(r, y, b, w)
	'cmyx', # choice(c, m, y, x)
	'xxx', # rgb random
	'10x', # magenta/vermelho random
	'00x', # azul/preto random
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
	'1', # random()s
	'2', # phi
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
		'c' : ['hasselhoffian-recursion.gif',],
		'd' : d7d[0],
		'e' : d7e,
	}
}
