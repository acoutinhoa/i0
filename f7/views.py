from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
# from f7.models import *
import string
import random

def f7(request, f7tp, l8p, tp, a, b, c, d, e):
	f7tp, l8p, tp, a, b, c, d, e = def_var(f7tp, l8p, tp, a, b, c, d, e)
	ur1, ur2 = def_l8p(f7tp, l8p, tp, a, b, c, d, e)
	v1, v2 = def_e(f7tp, e)
	b, bc = def_b(tp, b)
	d = def_d(f7tp, d)
	tt = 'f7/%s' % (f7tp)
	if l8p != '0':
		tt += ' l8p'
	# html framset
	if f7tp == 'pi3t':
		if b == '1':
			f = '%s="%s,%s" frameborder="%s" border="10" bordercolor="%s"' % (d, v1, v2, b, def_hxc(bc))
		else:
			f = '%s="%s,%s" frameborder="%s"' % (d, v1, v2, b)
		return render(request, 'f7/f7.html', {'tt':tt, 'ur1':ur1, 'ur2':ur2, 'f7':f})
	# html iframe
	if f7tp == 'qd2':
		bg, bgs = def_tp(f7tp, tp)
		fs = def_bs(b, bc)
		s = def_s(d, v1, v2)
		return render(request, 'f7/f7q.html', {'tt':tt, 'ur1':ur1, 'ur2':ur2, 'v1':v1, 'v2':v2, 's':s, 'fs':fs, 'bg':bg, 'bgs':bgs,})
	else:
		fs1 = def_bs(b, bc)
		fs2 = def_bs(b, bc)
		return render(request, 'f7/f7i.html', {'tt':tt, 'ur1':ur1, 'ur2':ur2, 'v1':v1, 'v2':v2, 'fs1':fs1, 'fs2':fs2, 'd':d})

def b9(request, f7tp, l8p, tp, a, b, c, d, e):
	f7tp, l8p, tp, a, b, c, d, e = def_var(f7tp, l8p, tp, a, b, c, d, e)
	t = 'f7/b9.html'
	tt = 'f7/b9/%s' % (f7tp)
	ur1 = reverse('f7', args=(f7tp, l8p, tp, a, b, c, d, e))
	rf = def_a(f7tp, a)
	bg, bgs = def_tp(f7tp, tp)
	return render(request, t, {'tt':tt, 'ur1':ur1, 'bg':bg, 'bgs':bgs, 'rf':rf})

# defs
def def_var(f7tp, l8p, tp, a, b, c, d, e):
	if f7tp == '':
		f7tp = random.choice(d7tp)

	if l8p == '':
		if f7tp == 'qd2':
			l8p = random.choice([ '0', random.choice([ '0', '1' ]) ])
		else:
			l8p = random.choice([ '0', random.choice(d7l8p) ])

	if tp == '':
		if f7tp == 'im9':
			tp = random.choice(d7img)
		else:
			tp = random.choice(d7cor)

	if a == '':
		if f7tp == 'im9':
			a = '0'
			b = '0'
		else:
			a = random.choice([ 'x', random.choice(d7x) ])
			b = random.choice(d7x)
		if f7tp == 'qd2':
			d = random.choice([ 'x', random.choice(d7d) ])
		d += random.choice([ 'x', random.choice(d7x) ])
		e = random.choice(d7x)

	if c == '': 
		c = '0'
	else:
		c = str(int(c)+1)

	if tp == 'def':
		tp = def_xxx()
	if b[1:] == 'def':
		b = b[0] + def_xxx()

	return f7tp, l8p, tp, a, b, c, d, e

def def_l8p(f7tp, l8p, tp, a, b, c, d, e):
	if f7tp == 'qd2':
		ur1 = ur2 = reverse('f7', args=(f7tp, l8p, tp, a, b, c, d, e))
		if l8p == '0':
			ur2 = reverse('b9', args=(f7tp, l8p, tp, a, b, c, d, e))
	else:
		ur1 = ur2 = reverse('b9', args=(f7tp, l8p, tp, a, b, c, d, e))
		if l8p == 'x':
			if random.randint(0,1):
				ur1 = reverse('f7', args=(f7tp, l8p, tp, a, b, c, d, e))
			else:
				ur2 = reverse('f7', args=(f7tp, l8p, tp, a, b, c, d, e))
		elif l8p == '1':
			ur1 = reverse('f7', args=(f7tp, l8p, tp, a, b, c, d, e))
		elif l8p == '2':
			ur2 = reverse('f7', args=(f7tp, l8p, tp, a, b, c, d, e))
	return ur1, ur2

def def_tp(f7tp, tp):
	if f7tp == 'im9':
		if tp[-3:] == 'gif':
			bg = 'url(%s) no-repeat' % (tp)
			bgs = '100vw 100vh'
		else:
			bg = 'url(%s) no-repeat center fixed' % (tp)
			bgs = 'cover'
		return bg, bgs
	else:
		if tp == 'pb':
			tp = random.choice(['0', '1'])
		elif tp == 'rgb':
			tp = random.choice(['100', '010', '001', '0'])
		elif tp == 'piet':
			tp = random.choice(['1', random.choice(['100', '110', '001']) ])
		elif tp == 'cmyx':
			tp = random.choice(['011', '101', '110', random.choice(['0', '1']) ])
		return def_rgb(tp), ''

def def_a(f7tp, a):
	if a == '0':
		return ''
	elif a == '1':
		return '0'
	elif a == 'x':
		if f7tp == 'qd2':
			return str(random.randint(1,5))
		else:
			return str(random.randint(5,15))

def def_b(tp, b):
	bc = ''
	if len(b) > 1:
		b = b[0]
		bc = b[1:]
	if b == 'x':
		b = random.choice(['0', '1'])
	if b == '1':
		# cor borda
		if bc == '':
			if tp == 'pb':
				bc = 'x'
			elif tp == 'rgb':
				bc = '1'
			elif tp == 'piet':
				bc = '0'
			elif tp == 'xxx':
				bc = tp
			else:
				bc = random.choice(['0', '1'])
		elif bc == 'pb':
			bc = random.choice(['0', '1'])
	return b, bc

def def_bs(b, bc):
	if b == '1':
		s = ''
		b = ['border-top: %s;', 'border-bottom: %s;', 'border-left: %s;', 'border-right: %s;', ]
		for i, bt in enumerate(b):
			o = random.randint(0, 1)
			if o:
				t = '10px solid %s' % (def_hxc(bc))
				s += b[i] % (t)
			else:
				s += b[i] % ('0')
		s += 'box-sizing: border-box;'
	else:
		s = ''
	return s

def def_d(f7tp, d):
	if d == 'x':
		d = random.choice(['0', '1'])
	if f7tp == 'pi3t':
		if d == '0':
			return 'rows'
		else:
			return 'cols'
	else:
		return d

def def_e(f7tp, e):
	if f7tp == 'qd2':
		if e == '0':
			v1 = v2 = 80
		elif e == '1':
			v1 = v2 = 60
		elif e == 'x':
		    v1 = random.randint(50, 95)
		    v2 = random.randint(50, 95)
		return str(v1) + '%', str(v2) + '%'
	else:
		if e == '0':
			v1 = 50
		elif e == '1':
			v1 = random.choice([40, 60])
			# v1 = random.choice([38.1966, 61.8034])
		elif e == 'x':
		    v1 = random.randint(25, 75)
		if f7tp == 'pi3t':
			return str(v1) + '%', '*'
		else:
			v2 = 100-v1
			return str(v1) + '%', str(v2) + '%'
def def_s(d, v1, v2):
	v1 = int(v1[:-1])
	v2 = int(v2[:-1])
	m1 = (100-v1)/2 # meio
	m2 = (100-v2)/2 # meio
	# alinha
	if d[1] == 'x':
		a1 = random.randint(0, int(m1))
		a2 = random.randint(0, int(m2))
	elif d[1] == '1':
		a1 = a2 = 5
	else:
		a1 = a2 = 0
	# margem
	if d[0] == 'x':
		d = random.randint(1, 8)
	else:
		d = int(d[0])
	if d == 1:
		m1 = 0 + a1
		m2 = 0 + a2
	elif d == 2:
		m1 = m1*2 - a1
		m2 = 0 + a2
	elif d == 3:
		m1 = 0 + a1
		m2 = m2*2 - a2
	elif d == 4:
		m1 = m1*2 - a1
		m2 = m2*2 - a2
	elif d == 5:
		m2 = 0 + a2
	elif d == 6:
		m2 = m2*2 - a2
	elif d == 7:
		m1 = 0 + a1
	elif d == 8:
		m1 = m1*2 - a1
	return 'margin-left: %svw; margin-top: %svh;' % (str(m1), str(m2))

def def_xxx():
	cor = ''
	for i in range(3):
		cor += random.choice(d7x)
	if 'x' not in cor:
		if cor == '000' or cor == '111':
			cor = 'x'
		else:
			cor = def_xxx()
	return cor

def def_rgb(c):
	cor = ''
	for i in c:
		if i == 'x':
			i = str(random.randint(0, 255))
		elif i == '1':
			i = '255'
		cor += '%s,' % (i)
	if len(c) == 1:
		cor = cor*3
	return 'rgb(%s)' % (cor[:-1])

def def_hxc(c):
	cor = ''
	for i in c:
		if i == 'x':
			for j in range(2):
				cor += random.choice(list(string.hexdigits))
		elif i == '0':
			cor += '00'
		elif i == '1':
			cor += 'ff'
	if len(c) == 1:
		cor = cor*3
	return '#%s' % (cor)


# variaveis
# / f7 / f7tp + l8p / tp / a / b / c / d / e /

# f7tp = tipo
	# pi3t = frameset html0ldschool
	# rg6 = iframe bg-color
	# im9 = iframe img
# l8p = loop
	# 0 = sem l8p
	# 1 = l8p ur1
	# 2 = l8p ur2
	# x = l8p ur1/ur2
# tp = cor/img
# a = atualiza
	# 0 = nao atualiza
	# 1 = 0s
	# x = 5-20s
# b = borda
	# 0 = sem borda
	# 1 = com borda
	# x = 0/1
# c = contador
# d = divisao
	# 0 = horizontal
	# 1 = vertical
	# x = 0/1
# e = proporcao
	# 0 = 50%
	# 1 = phi
	# x = 25-75%

# f7tp
d7tp = [
	'pi3t', # frameset html0ldschool
	'rg6', # iframe bg-color
	'im9', # iframe img
	'qd2', # qd2 ht# josef jo5ef jos3f jose# j0sef
]
# tp
d7img = [
		'/static/f7/hasselhoffian-recursion.gif', 
		'/static/f7/guido-van-rossum_python.jpg',
]
d7cor = [
		'piet', # choice(r, y, b, w)
		'pb', # choice(p, b)
		'rgb', # choice(r, g, b, k)
		'cmyx', # choice(c, m, y, choice(p, b))
		'xxx', # rgb random
		'10x', # magenta/vermelho random
		'00x', # azul/preto random
		'def', # def_xxx
]
# 01x
d7x = [
	'0',
	'1',
	'x',
]

d7l8p = [
	'0', 
	'1', 
	'2',
	'x',
]

d7d = [
	'0', # centralizado
	'1', # t l
	'2', # t r
	'3', # b l
	'4', # b r
	'5', # t
	'6', # b
	'7', # l
	'8', # r
	'x', # aleatorio
]
