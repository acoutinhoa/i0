from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
from i0.models import *
import string
import random

d7 = {
	# atualiza
	'a' : [
		'0', # atualiza 0s
		'1', # atualiza random()s
		'2', # nao atualiza
	],
	# tipo
	'b' : [
		'bg', # bg
		# 'img', # img
	],
	# cor / img 
	'c' : {
		'bg' : [
			'rrr', # rgb random
			'10r', # magenta/vermelho random
			'00r', # azul/preto random
			'r', # preto/branco random
			'pb', # choice(p, b)
			'rgb', # choice(r, g, b, k)
			'piet', # choice(r, y, b, w)
		],
	},
	# divisao
	'd' : [
		'0', # 50%
		'1', # random()s
		# '2', # phi
	],
}

def index0f(request):
	return HttpResponse('index0f')

def bg(request, a, b, c, d):
	tt = 'f7/bg'
	t = 'f7/bg.html'
	rl = def_a(a)
	rgb = def_c(b, c)
	url = reverse('f7', args=(a, b, c, d,))
	return render(request, t, {'tt':tt, 'url':url, 'bg':rgb, 'rl':rl})

def f7(request, a, b, c, d):
	tt = 'f7'
	t = 'f7/f7%s.html' % ( random.choice(['v', 'h']) )
	d1, d2 = def_d(d)
	url = reverse(b, args=(a, b, c, d,))
	return render(request, t, {'tt':tt, 'url1':url, 'url2':url, 'v1':d1, 'v2':d2})

def f70(request):
	# randomiza variaveis
	a = random.choice(d7['a'])
	b = random.choice(d7['b'])
	c = random.choice(d7['c'][b])
	d = random.choice(d7['d'])
	return redirect(f7, a=a, b=b, c=c, d=d)

def def_a(a):
	if a == '1':
		a = str(random.randint(5,20))
	elif a == '2':
		a = ''
	return a

def def_c(b, c):
	if c == 'pb':
		c = random.choice(['0', '1'])
	elif c == 'rgb':
		c = random.choice(['100', '010', '001', '0'])
	elif c == 'piet':
		c = random.choice(['1', random.choice(['100', '110', '001']) ])
	cor = ''
	for car in c:
		if car == 'r':
			car = str(random.randint(0, 255))
		elif car == '1':
			car = '255'
		cor += '%s,' % (car)
		if len(c) == 1:
			cor = cor*3
	cor = cor[:-1]
	return cor

def def_d(d):
	if d == '0':
		d1 = d2 = '50%'
	elif d == '1':
	    d1 = random.randint(25, 75)
	    d2 = 100 - d1
	    d1 = str(d1) + '%'
	    d2 = str(d2) + '%'
	return d1, d2


