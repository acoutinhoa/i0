from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
# from f7.models import *
import string
import random

def f7(request, f7tp, v4r, l8p, f7, b9, a, b, c, d, e):
	f7tp, v4r, l8p, f7, b9, a, b, c, d, e = def_var(f7tp, v4r, l8p, f7, b9, a, b, c, d, e)
	ur1, ur2 = def_l8p(f7tp, v4r, l8p, f7, b9, a, b, c, d, e)
	if f7 == 'x':
		f7 = random.choice(d7o)
	tt = 'f7/%s' % (f7tp)
	b, bc = def_b(v4r, b)
	v1, v2 = def_e(f7tp, e)
	d = def_d(f7, d)
	if l8p != '0':
		tt += ' l8p'
	if f7 == '0':
		f = def_f1(d, v1, v2, b, bc)
		return render(request, 'f7/f7.html', {
			'tt':tt, 
			'ur1':ur1, 
			'ur2':ur2, 
			'f7':f,
		})
	else:
		if f7tp == 'qd2':
			bg, cs2, td, tdh = def_an3(a, b, b9, v4r, f7tp)
			f = def_f2(d, v1, v2)
			fs = def_bc(bc)
			return render(request, 'f7/f7q.html', {
				'f':f, # css
				'td':td, # css
				'tdh':tdh, # hover
				'cs2':cs2,
				'tt':tt, 
				'ur1':ur1, 
				'ur2':ur2, 
				'v1':v1, 
				'v2':v2, 
				'fs':fs, 
			})
		else:
			if f7tp == 'tr1' or f7tp == 'd0t' or f7tp == 'im9':
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

def b9(request, f7tp, v4r, l8p, f7, b9, a, b, c, d, e):
	f7tp, v4r, l8p, f7, b9, a, b, c, d, e = def_var(f7tp, v4r, l8p, f7, b9, a, b, c, d, e)
	ur1 = reverse('f7', args=(f7tp, v4r, l8p, f7, b9, a, b, c, d, e))
	tt = 'f7/b9/%s' % (f7tp)
	rf = def_a(f7tp, b9, a)
	if f7tp == 'im9':
		bg = cs2 = ''
		td, tdh = def_img(v4r)
	else:
		bg, cs2, td, tdh = def_an3(a, b, b9, v4r, f7tp)
	return render(request, 'f7/b9.html', {
		'b':bg, 
		'td':td, 
		'tdh':tdh, 
		'cs2':cs2,
		'rf':rf, 
		'tt':tt, 
		'ur1':ur1, 
	})
    
# defs
def def_var(f7tp, v4r, l8p, f7, b9, a, b, c, d, e):
	if f7tp == '':
		f7tp = random.choice(d7tp)
	if v4r == '':
		if f7tp == 'im9':
			v4r = random.choice(d7img)
		else:
			v4r = random.choice(d7cor)
	if v4r == 'def':
		v4r = def_xxx()
	if l8p == '':
		if f7tp == 'qd2':
			l8p = random.choice(['0', random.choice(d7o)])
		else:
			l8p = random.choice(['0', random.choice(d7l8p)])
	if f7 == '':
		if f7tp == 'qd2':
			f7 = '1'
		else:
			f7 = random.choice(d7x)
	if b9 == '':
		b9 = random.choice(d7o)
	if a == '':
		if f7tp == 'im9':
			a = '0'
		else:
			a = random.choice(['x', random.choice(d7x)])
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
			d = random.choice(['x', random.choice(d7d)]) + random.choice(['x', random.choice(d7x)])
		else:
			d = random.choice(['x', random.choice(d7x)])
	if e == '':
		e = random.choice(d7x)
	return f7tp, v4r, l8p, f7, b9, a, b, c, d, e

def def_l8p(f7tp, v4r, l8p, f7, b9, a, b, c, d, e):
	if f7tp == 'qd2':
		if l8p == '0':
			ur1 = reverse('f7', args=(f7tp, v4r, l8p, f7, b9, a, b, c, d, e))
			ur2 = reverse('b9', args=(f7tp, v4r, l8p, f7, b9, a, b, c, d, e))
		elif l8p == '1':
			ur1 = ur2 = reverse('f7', args=(f7tp, v4r, l8p, f7, b9, a, b, c, d, e))
	else:
		if l8p == 'x':
			l8p = random.choice(['1', '2'])
		if l8p == '0':
			ur1 = ur2 = reverse('b9', args=(f7tp, v4r, l8p, f7, b9, a, b, c, d, e))
		elif l8p == '1':
			ur1 = reverse('f7', args=(f7tp, v4r, l8p, f7, b9, a, b, c, d, e))
			ur2 = reverse('b9', args=(f7tp, v4r, l8p, f7, b9, a, b, c, d, e))
		elif l8p == '2':
			ur1 = reverse('b9', args=(f7tp, v4r, l8p, f7, b9, a, b, c, d, e))
			ur2 = reverse('f7', args=(f7tp, v4r, l8p, f7, b9, a, b, c, d, e))
	return ur1, ur2

def def_bg(v4r):
	cor = def_c0r(v4r)
	return 'background: %s;' % (def_rgb(cor))

def def_img(v4r):
	webkit = ''
	tdh = '%stransform: rotate(180deg);' % (webkit)
	if v4r[-3:] == 'gif':
		bg = 'url(%s) no-repeat' % (v4r)
		bgs = '100vw 100vh'
	else:
		bg = 'url(%s) no-repeat center fixed' % (v4r)
		bgs = 'cover'
	td = 'background: %s;\n\tbackground-size: %s;' % (bg, bgs)
	return td, tdh

def def_an3(a, b, b9, v4r, f7tp):
	def stp(n):
		stp = '\n\t%s  {%s}'
		t = 100/(n+1)
		s = ''
		for i in range(n):
			if f7tp == 'tr1':
				s += stp % (str(t*(i+1))+'%', def_bs(b, v4r))
			elif f7tp == 'd0t':
				s += stp % (str(t*(i+1))+'%', def_br(b, v4r))
			else:
				s += stp % (str(t*(i+1))+'%', def_bg(v4r))
		return s

	bg = cs2 = ''
	if f7tp == 'tr1':
		bg = def_bg(v4r)
		td = def_bs(b, v4r)
		tdh = def_bs(b, v4r)
	elif f7tp == 'd0t':
		bg = def_bg(v4r)
		td = def_br(b, v4r)
		tdh = def_br(b, v4r)
	else:
		td = def_bg(v4r)
		tdh = def_bg(v4r)

	if b9 == '1':
		webkit = ''
		an3 = '\n\t%sanimation: %s %ss infinite;'
		anm = '''
@%skeyframes %s {%s
}'''
		if a == '1':
			t = random.randint(5, 20)
			cs2 += anm % (webkit, 'an3', stp(1))
			td += an3 % (webkit, 'an3', str(t))
			tdh += '\n\tanimation: 0;'
		elif a == 'x':
			n = random.randint(2,10)
			t = random.randint(5, 15) * (n)
			cs2 += anm % (webkit, 'an3', stp(n))
			cs2 += anm % (webkit, 'an3h', stp(n))
			td += an3 % (webkit, 'an3', str(t))
			tdh += an3 % (webkit, 'an3h', '1')
	return bg, cs2, td, tdh

def def_a(f7tp, b9, a):
	rf = ''
	if b9 == '0':
		if a == '1':
			rf = '0'
		elif a == 'x':
			if f7tp == 'qd2':
				rf = str(random.randint(1,5))
			else:
				rf = str(random.randint(5,15))
	return rf

def def_b(v4r, b):
	bc = ''
	if b == 'x':
		b = random.choice(d7o)
	if b == '1':
		bc = def_c0r(v4r, tp = 1)
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

def def_d(f7, d):
	if d == 'x':
		d = random.choice(d7o)
	if f7 == '0':
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

def def_c0r(v4r, tp = 0):
	if tp == 1: 
		# cor borda
		if v4r == 'pb':
			cor = 'x'
		elif v4r == 'rgb':
			cor = '1'
		elif v4r == 'piet':
			cor = '0'
		elif v4r == 'xxx':
			cor = v4r
		else:
			cor = random.choice(d7o)
	else:
		if v4r == 'pb':
			cor = random.choice(d7o)
		elif v4r == 'rgb':
			cor = random.choice(['100', '010', '001', '0'])
		elif v4r == 'cmyx':
			cor = random.choice(['011', '101', '110', random.choice(d7o) ])
		elif v4r == 'piet':
			cor = random.choice(['1', random.choice(['100', '110', '001', '0']) ])
		else:
			cor = v4r
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
# / f7 / f7tp + l8p / v4r / a / b / c / d / e /

# f7tp = tipo
	# d7tp
# l8p = loop
	# 0 = sem l8p
	# 1 = l8p ur1
	# 2 = l8p ur2
	# x = l8p ur1/ur2
# v4r = cor/img
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
	'tr1', # tr1 cs5 ss2 cs2 c5s
	'qd2', # qd2 ht# josef jo5ef jos3f jose# j0sef
	'pi3t', # frameset html0ldschool
	# 'rg6', # iframe bg-color
	# 'b4b_', # babe1 babe2 bab3l b4bel ba5el ba6el borges jorge jo-g3 b4_ b6_ b_abe1 ba_e1 b4b_ bbl bb1 b6_
	'im9', # iframe img
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

d7o = ['0','1']

d7x = d7o+['x']

d7l8p = d7x+['2']

d7l = ['underline', 'overline', 'line-through']

