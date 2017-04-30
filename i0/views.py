from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
from i0.models import *
import string
import random

def index0f(request):
	return HttpResponse('index0f')

def bg(request, c, d, rl):
	bg = def_cor(int(c))
	tt = 'f7bg'
	url = reverse('f7bg', kwargs={'c': c, 'd': d, 'rl': rl})
	t = 'f7/bg.html'
	rl = def_rl(int(rl))
	return render(request, t, {'tt':tt, 'url':url, 'bg':bg, 'rl':rl})

def f7bg(request, c, d, rl):
	tt = 'f7bg'
	t = 'f7/f7%s.html' % ( random.choice(['v', 'h']) )
	url1 = reverse('bg', kwargs={'c': c, 'd': d, 'rl': rl})
	if int(d) == 2:
		v1, v2 = def_v(0)
		url2 = reverse('f7bg', kwargs={'c': c, 'd': d, 'rl': rl})
	else:
		v1, v2 = def_v(int(d))
		url2 = url1
	return render(request, t, {'tt':tt, 'url1':url1, 'url2':url2, 'v1':v1, 'v2':v2})

def f7bg0(request):
	c = random.randint(0,3)
	d = random.randint(0,2)
	rl = random.randint(0,2)
	return redirect(f7bg, c=str(c), d=str(d), rl=str(rl) )

def def_cor(c):
	l = []
	for car in string.hexdigits:
		l.append(car)
	if c == 0:
		cor = '#'
		for i in range(6):
			cor += random.choice(l)
	elif c == 1:
		cor = ''
		for i in range(2):
			cor += random.choice(l)
		cor = '#0000%s' % (cor)
	elif c == 2:
		cor = ''
		for i in range(2):
			cor += random.choice(l)
		cor = '#ff00%s' % (cor)
	elif c == 3:
		cor = random.choice(['#f00', '#0f0', '#00f', '#000' ])
	return cor

def def_v(d):
	if d == 0:
		v1 = v2 = '50%'
	elif d == 1:
	    v1 = random.randint(25, 75)
	    v2 = 100 - v1
	    v1 = str(v1) + '%'
	    v2 = str(v2) + '%'
	return v1, v2

def def_rl(rl):
	if rl == 0:
		rl = str(rl)
	elif rl == 1:
		rl = str(random.randint(5,20))
	elif rl == 2:
		rl = ''
	return rl


