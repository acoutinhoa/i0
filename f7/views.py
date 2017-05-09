from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
# from f7.models import *
import string
import random

def f7(request, f7tp, l8p, tp, a, b, c, d, e):
	f7tp, l8p, tp, a, b, c, d, e = def_var(f7tp, l8p, tp, a, b, c, d, e)
	ur1, ur2 = def_l8p(f7tp, l8p, tp, a, b, c, d, e)
	b, bc = def_b(tp, b)
	d = def_d(f7tp, d)
	v1, v2 = def_e(f7tp, e)
	tt = 'f7/%s' % (f7tp)
	if l8p != '0':
		tt += ' l8p'
	if f7tp == 'pi3t':
		f = def_f1(d, v1, v2, b, bc)
		return render(request, 'f7/f7.html', {
			'tt':tt, 
			'ur1':ur1, 
			'ur2':ur2, 
			'f7':f,
		})
	elif f7tp == 'qd2':
		bg = def_bg(tp)
		th = def_bg(tp)
		f = def_f2(d, v1, v2)
		fs = def_bc(bc)
		return render(request, 'f7/f7q.html', {
			'f':f, # css
			'b':bg, # css
			'th':th, # hover
			'tt':tt, 
			'ur1':ur1, 
			'ur2':ur2, 
			'v1':v1, 
			'v2':v2, 
			'fs':fs, 
		})
	else:
		if f7tp == 'cs5' or f7tp == 'd0t':
			fs1 = fs2 = ''
		else:
			fs1 = def_bc(bc)
			fs2 = def_bc(bc)
		return render(request, 'f7/f7i.html', {
			'd':d, # divisao
			'tt':tt, 
			'ur1':ur1, 
			'ur2':ur2, 
			'v1':v1, 
			'v2':v2, 
			'fs1':fs1, 
			'fs2':fs2, 
		})

def b9(request, f7tp, l8p, tp, a, b, c, d, e):
	f7tp, l8p, tp, a, b, c, d, e = def_var(f7tp, l8p, tp, a, b, c, d, e)
	tt = 'f7/b9/%s' % (f7tp)
	ur1 = reverse('f7', args=(f7tp, l8p, tp, a, b, c, d, e))
	rf = def_a(f7tp, a)
	bg = def_bg(tp)
	if f7tp == 'cs5':
		td = def_bs(b, tp)
		tdh = def_bs(b, tp)
		return render(request, 'f7/b9.html', {
			'b':bg, 
			't':td, 
			'th':tdh, 
			'rf':rf, 
			'tt':tt, 
			'ur1':ur1, 
		})
	elif f7tp == 'd0t':
		td = def_br(b, tp)
		tdh = def_br(b, tp)
		return render(request, 'f7/b9.html', {
			'b':bg, 
			't':td, 
			'th':tdh, 
			'rf':rf, 
			'tt':tt, 
			'ur1':ur1, 
		})
	else:
		if f7tp == 'im9':
			bg = ''
			td, tdh = def_img(tp)
		else:
			td = ''
			tdh = def_bg(tp)
		return render(request, 'f7/b9.html', {
			'b':bg, 
			't': td,
			'th':tdh, # hover 
			'rf':rf, # refresh
			'tt':tt, 
			'ur1':ur1, 
		})

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
		else:
			a = random.choice([ 'x', random.choice(d7x) ])

	if b == '':
		if f7tp == 'im9':
			b = '0'
		else:
			b = random.choice(d7x)

	if c == '': 
		c = '0'
	else:
		c = str(int(c)+1)

	if d == '':
		if f7tp == 'qd2':
			d = random.choice([ 'x', random.choice(d7d) ]) + random.choice([ 'x', random.choice(d7x) ])
		else:
			d = random.choice([ 'x', random.choice(d7x) ])

	if e == '':
		e = random.choice(d7x)

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

def def_bg(tp):
	cor = def_c0r(tp)
	return 'background: %s;' % (def_rgb(cor))

def def_img(tp):
	tdh = '''-ms-transform: rotate(180deg); /* IE 9 */
	-webkit-transform: rotate(180deg); /* Safari */
	transform: rotate(180deg);'''
	if tp[-3:] == 'gif':
		bg = 'url(%s) no-repeat' % (tp)
		bgs = '100vw 100vh'
	else:
		bg = 'url(%s) no-repeat center fixed' % (tp)
		bgs = 'cover'
	td = 'background: %s;\n\tbackground-size: %s;' % (bg, bgs)
	return td, tdh

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
	if b == 'x':
		b = random.choice(['0', '1'])
	if b == '1':
		bc = def_c0r(tp, var = 1)
	return b, bc

def def_bc(bc):
	s = ''
	bs = ['border-top: %s;', 'border-bottom: %s;', 'border-left: %s;', 'border-right: %s;', ]
	if bc:
		for i in range(4):
			if random.randint(0, 1):
				b = '10px solid %s' % (def_hxc(bc))
				s += bs[i] % (b)
			else:
				s += bs[i] % ('0')
		s += '\n\tbox-sizing: border-box;'
	return s

def def_bs(b, bc):
	s = ''
	bs = ['border-top: %s;', 'border-bottom: %s;', 'border-left: %s;', 'border-right: %s;', ]
	if b == '0':
		cor = def_rgb(def_c0r(bc))
		u = 'vh'
		n = 0
		for i in range(2):
			c = [cor, 'transparent']
			bc0 = '50%s solid %s' % (u, c.pop(random.randint(0,1)))
			bc1 = '50%s solid %s' % (u, c[0])
			s += '\n\t' + bs[n] % (bc0)
			s += '\n\t' + bs[n+1] % (bc1)
			u = 'vw'
			n = 2
	elif b == '1':
		u = 'vh'
		for i in range(4):
			bc0 = '50%s solid %s' % (u, def_rgb(def_c0r(bc)))
			s += '\n\t' + bs[i] % (bc0)
			if i == 1:
				u = 'vw'
	elif b == 'x':
		u = 'vh'
		n = 0
		for i in range(2):
			v1 = random.randint(20, 80)
			v2 = 100-v1
			bc0 = '%s%s solid %s' % (str(v1), u, def_rgb(def_c0r(bc)))
			bc1 = '%s%s solid %s' % (str(v2), u, def_rgb(def_c0r(bc)))
			s += '\n\t' + bs[n] % (bc0)
			s += '\n\t' + bs[n+1] % (bc1)
			u = 'vw'
			n = 2
	s += '\n\tbox-sizing: border-box;'
	return s

def def_br(b, bc):
	s = 'border-radius: 50%;'
	bs = ['border-top: %s;', 'border-bottom: %s;', 'border-left: %s;', 'border-right: %s;', ]
	if b == '0':
		cor = def_rgb(def_c0r(bc))
		u = 'vh'
		for i in range(4):
			bc0 = '50%s solid %s' % (u, cor)
			s += '\n\t' + bs[i] % (bc0)
			if i == 1:
				u = 'vw'
	elif b == '1':
		cor = def_rgb(def_c0r(bc))
		u = 'vh'
		for i in range(4):
			bc0 = '50%s solid %s' % (u, random.choice([cor, 'transparent']))
			s += '\n\t' + bs[i] % (bc0)
			if i == 1:
				u = 'vw'
	elif b == 'x':
		u = 'vh'
		n = 0
		for i in range(2):
			v1 = random.randint(20, 80)
			v2 = 100-v1
			bc0 = '%s%s solid %s' % (str(v1), u, def_rgb(def_c0r(bc)))
			bc1 = '%s%s solid %s' % (str(v2), u, def_rgb(def_c0r(bc)))
			s += '\n\t' + bs[n] % (bc0)
			s += '\n\t' + bs[n+1] % (bc1)
			u = 'vw'
			n = 2
	s += '\n\tbox-sizing: border-box;'
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
		    v1 = random.randint(10, 90)
		if f7tp == 'pi3t':
			return str(v1) + '%', '*'
		else:
			v2 = 100-v1
			return str(v1) + '%', str(v2) + '%'

def def_f1(d, v1, v2, b, bc):
	if b == '1':
		return '%s="%s,%s" frameborder="%s" border="10" bordercolor="%s"' % (d, v1, v2, b, def_hxc(bc))
	else:
		return '%s="%s,%s" frameborder="%s"' % (d, v1, v2, b)

def def_f2(d, v1, v2):
	v1 = int(v1[:-1])
	v2 = int(v2[:-1])
	m1 = (100-v1)/2 # margem para centralizar horizontalmente
	m2 = (100-v2)/2 # margem para centralizar verticalmente
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
	return 'margin-left: %svw;\n\tmargin-top: %svh;' % (str(m1), str(m2))

def def_c0r(tp, var = 0):
	if var == 1: 
		# cor borda
		if tp == 'pb':
			cor = 'x'
		elif tp == 'rgb':
			cor = '1'
		elif tp == 'piet':
			cor = '0'
		elif tp == 'xxx':
			cor = tp
		else:
			cor = random.choice(['0', '1'])
	else:
		if tp == 'pb':
			cor = random.choice(['0', '1'])
		elif tp == 'rgb':
			cor = random.choice(['100', '010', '001', '0'])
		elif tp == 'cmyx':
			cor = random.choice(['011', '101', '110', random.choice(['0', '1']) ])
		elif tp == 'piet':
			cor = random.choice(['1', random.choice(['100', '110', '001', '0']) ])
		else:
			cor = tp
	return cor

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
	# d7tp
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

d7tp = [
	'd0t', 
	'qd2', # qd2 ht# josef jo5ef jos3f jose# j0sef
	'pi3t', # frameset html0ldschool
	# 'b4b_', # babe1 babe2 bab3l b4bel ba5el ba6el borges jorge jo-g3 b4_ b6_ b_abe1 ba_e1 b4b_ bbl bb1 b6_
	'cs5', # cs5 css2 cs2 c5s
	'rg6', # iframe bg-color
	'im9', # iframe img
]

d7l8p = [
	'0', 
	'1', 
	'2',
	'x',
]

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

d7x = [
	'0',
	'1',
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

d7bb1 = [
	'bbl',
	'bb1',
	'b6_',
]

d7l = ['underline', 'overline', 'line-through']
