from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
from i0.models import *
import string
import random

def index0f(request):
	return HttpResponse('index0f')

def f7(request, tp, a, b, c):
	# randomiza variaveis
	if tp == '':
		tp = random.choice(list(d7.keys()))
		a = random.choice(d7[tp]['a'])
		b = random.choice(d7[tp]['b'])
		c = random.choice(d7[tp]['c'])
	tt = 'f7'
	t = 'f7/f7%s.html' % ( random.choice(['v', 'h']) )
	url = reverse('bg', args=(tp, a, b, c,))
	v1, v2 = def_b(b)
	return render(request, t, {'tt':tt, 'url1':url, 'url2':url, 'v1':v1, 'v2':v2})

def bg(request, tp, a, b, c):
	# randomiza variaveis
	if tp == '':
		tp = random.choice(list(d7.keys()))
		a = random.choice(d7[tp]['a'])
		b = random.choice(d7[tp]['b'])
		c = random.choice(d7[tp]['c'])
	tt = 'f7/bg'
	t = 'f7/bg.html'
	url = reverse('f7', args=(tp, a, b, c,))
	rl = def_a(a)
	bg, bgs = def_c(tp, c)
	return render(request, t, {'tt':tt, 'url':url, 'bg':bg, 'bgs':bgs, 'rl':rl})

def def_a(a):
	if a == '0':
		a = ''
	elif a == '1':
		a = str(random.randint(5,20))
	elif a == '2':
		a = '0'
	return a

def def_b(b):
	if b == '0':
		v1 = v2 = '50%'
	elif b == '1':
	    v1 = random.randint(25, 75)
	    v2 = 100 - v1
	    v1 = str(v1) + '%'
	    v2 = str(v2) + '%'
	return v1, v2

def def_c(tp, c):
	if tp == 'rgb':
		if c == 'pb':
			c = random.choice(['0', '1'])
		elif c == 'rgb':
			c = random.choice(['100', '010', '001', '0'])
		elif c == 'piet':
			c = random.choice(['1', random.choice(['100', '110', '001']) ])
		bg = ''
		for car in c:
			if car == 'x':
				car = str(random.randint(0, 255))
			elif car == '1':
				car = '255'
			bg += '%s,' % (car)
			if len(c) == 1:
				bg = bg*3
		bg = 'rgb(%s)' % (bg[:-1])
		bgs = ''
	elif tp == 'img':
		bg = 'url(/static/i0/gif/%s) no-repeat' % (c)
		bgs = '100vw 100vh'
	return bg, bgs


d7a = [
	'0', # nao atualiza
	'1', # atualiza random()s
	'2', # atualiza 0s
]
d7b = [
	'0', # 50%
	'1', # random()s
	# '2', # phi
]
d7c = [
	'pb', # choice(p, b)
	'rgb', # choice(r, g, b, k)
	'piet', # choice(r, y, b, w)
	'xxx', # rgb random
	'10x', # magenta/vermelho random
	'00x', # azul/preto random
]

d7 = {
	'rgb' : {
		'a' : d7a,
		'b' : d7b,
		'c' : d7c,
	},
	'img' : {
		'a' : d7a[0],
		'b' : d7b,
		'c' : ['hasselhoffian-recursion.gif',],
	}
}
