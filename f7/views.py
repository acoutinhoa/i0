from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
# from f7.models import *
import string
import random

def f7(request, t2, v4r, f7, b9, l8p, a, b, c, d, e):
	t2, v4r, f7, b9, l8p, a, b, c, d, e = def_var(t2, v4r, f7, b9, l8p, a, b, c, d, e)
	tt = 'f7/%s' % (t2)
	if l8p != '0' and t2 != 'ka8s': tt += ' l8p'
	ur1, ur2 = def_l8p(t2, v4r, f7, b9, l8p, a, b, c, d, e)
	t2, v4r, f7, b9, l8p, a, b, c, d, e = def_ka8s(t2, v4r, f7, b9, l8p, a, b, c, d, e)
	bg = def_f7bg(f7, t2, v4r, c)
	v1, v2 = def_e(f7, e)
	d = def_d(f7, d)
	if t2 == 'pi3t' and f7 != '0':
		fs1 = def_b(b, v4r)
		fs2 = def_b(b, v4r)
	else: fs1 = fs2 = ''

	if f7 == '0':
		f = def_f0(b, v4r, d, v1, v2)
		return render(request, 'f7/f7.html', {
			'tt':tt, 
			'ur1':ur1, 
			'ur2':ur2, 
			'f7':f,
		})
	elif f7 == '1':
		return render(request, 'f7/f7i.html', {
			'b':bg, 
			'd':d,
			'tt':tt, 
			'ur1':ur1, 
			'ur2':ur2, 
			'v1':v1, 
			'v2':v2, 
			'fs1':fs1, 
			'fs2':fs2, 
		})
	elif f7 == '2':
		f = def_f2(d, v1, v2)
		return render(request, 'f7/f7q.html', {
			'b':bg, 
			'tt':tt, 
			'ur1':ur1, 
			'ur2':ur2, 
			'v1':v1, 
			'v2':v2, 
			'fs1':fs1, 
			'fs2':fs2, 
			's':f,
		})

def b9(request, t2, v4r, f7, b9, l8p, a, b, c, d, e):
	t2, v4r, f7, b9, l8p, a, b, c, d, e = def_var(t2, v4r, f7, b9, l8p, a, b, c, d, e)
	ur1 = reverse('f7', args=(t2, v4r, f7, b9, l8p, a, b, c, d, e))
	t2, v4r, f7, b9, l8p, a, b, c, d, e = def_ka8s(t2, v4r, f7, b9, l8p, a, b, c, d, e)
	tt = 'f7/b9/%s' % (t2)
	rf = def_a(t2, b9, a)
	bg = def_b9bg(f7, t2, v4r, b)
	cs2, td, tdh = def_an3(a, b, b9, v4r, t2)
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
def def_var(t2, v4r, f7, b9, l8p, a, b, c, d, e):
	c = def_c(c)
	if not t2:
		if random.randrange(10): t2 = random.choice(d7tp)
		else: t2 = 'ka8s'
	if t2 == 'ka8s':
		return t2, v4r, f7, b9, l8p, a, b, c, d, e
	else:
		if not v4r:
			if t2 == 'im9': v4r = random.choice(d7im9)
			else: v4r = random.choice(d7cor)
		if v4r == 'def': v4r = def_xxx()
		if not f7: f7 = random.choice(d7y)
		if not b9: b9 = random.choice(d7o)
		if not l8p: l8p = random.choice(['0', random.choice(d7z)])
		if not a: a = random.choice(['x', random.choice(d7x)])
		if not b:
			if t2 == 'im9': b = random.choice(['x', random.choice(d7d)])
			elif t2 == 'd9d': b = random.choice(d7z) + random.choice(d7z)
			else: b = random.choice(d7x)
		if not d: 
			d = random.choice(['x', random.choice(d7x)])
			if f7 == '2': d += random.choice(['x', random.choice(d7d)])
		if not e: e = random.choice(d7x)
		if t2 == 'im9' and b == '0' and a != '0': a = '0'
		return t2, v4r, f7, b9, l8p, a, b, c, d, e

def def_ka8s(t2, v4r, f7, b9, l8p, a, b, c, d, e):
	if t2 == 'ka8s':
		t2 = random.choice(d7tp)
		v4r = l8p = f7 = b9 = a = b = d = e = ''
		t2, v4r, f7, b9, l8p, a, b, c, d, e = def_var(t2, v4r, f7, b9, l8p, a, b, c, d, e)
	return t2, v4r, f7, b9, l8p, a, b, c, d, e

def def_l8p(t2, v4r, f7, b9, l8p, a, b, c, d, e):
	if t2 == 'ka8s': lp = random.choice([0, random.randrange(3)])
	else:
		if l8p == 'x': lp = random.randint(random.randrange(2), 2)
		else: lp = int(l8p)
	ur1 = reverse('b9', args=(t2, v4r, f7, b9, l8p, a, b, c, d, e))
	if lp == 0: ur2 = ur1
	elif lp == 1 and f7 != '2':
		ur2 = ur1
		ur1 = reverse('f7', args=(t2, v4r, f7, b9, l8p, a, b, c, d, e))
	else: ur2 = reverse('f7', args=(t2, v4r, f7, b9, l8p, a, b, c, d, e))
	return ur1, ur2

def def_d9d(b, v4r):
	d9a, d9b = b
	if d9a == 'x': d9a = random.choice(d7y)
	if d9a == '0':
		xg = 'linear-gradient'
		tp = str(random.randrange(0, 360, 90)) + 'deg'
	elif d9a == '1':
		xg = 'linear-gradient'
		tp = str(random.randrange(0, 360)) + 'deg'
	elif d9a == '2':
		xg = 'radial-gradient'
		tp = random.choice(['circle', 'ellipse'])

	if d9b == 'x': d9b = random.choice(d7y)
	if d9b == '0':
		l = ['transparent', def_rgb(def_c0r(v4r))] 
		cor = l.pop(random.randint(0,1)) + ', ' + l[0]
	else:
		n = random.randint(2, 5)
		cor = ''
		for i in range(n):
			if random.randrange(4):
				cor += def_rgb(def_c0r(v4r)) + ', '
			else: cor += 'transparent, '
		cor = cor[:-2]
		if d9b == '2':
			xg = 'repeating-' + xg
			cor += ' {0}%'.format(str(random.randint(10, 50)))

	cor = '%s(%s, %s)' % (xg, tp, cor)
	webkit = ['-webkit-', '-ms-', '']
	bg = ''
	for i in webkit: bg += 'background: %s%s;' % (i, cor)
	return bg

def def_bg(v4r):
	cor = def_rgb(def_c0r(v4r))
	return 'background: %s;' % (cor)

def def_b9bg(f7, t2, v4r, b):
	bg = ''
	if f7 == '0':
		if t2 == 'd0t' or t2 == 'd9d' or t2 == 'qd2' and b == '0': bg = def_bg(v4r)
	return bg

def def_f7bg(f7, t2, v4r, c):
	bg = ''
	if f7 != '0':
		if f7 == '1' and c != '0':
			if not random.randrange(5): c = '0'
		if c == '0':
			if t2 == 'im9': bg = def_im9('0', v4r)
			else: bg = def_bg(v4r)
	return bg

def def_im9(b, v4r):
	if v4r in d7im9: v4r = '/static/f7/' + v4r
	if v4r[-3:] == 'gif':
		bg = 'url(%s) no-repeat' % (v4r)
		bgs = '100vw 100vh'
	else:
		bg = 'url(%s) no-repeat center fixed' % (v4r)
		bgs = 'cover'
	return 'background: %s;\n\tbackground-size: %s;%s' % (bg, bgs, def_fi1(b))

def def_im9h(b):
	webkit = ['-webkit-', '-ms-', '']
	tdh = ''
	for i in webkit: tdh += '%stransform: rotate(180deg);' % (i)
	if b != '0': tdh += def_fi1(b)
	return tdh

def def_fi1(b):
	fi1 = f1 = ''
	if b != '0':
		webkit = ['-webkit-', '']
		l = ['blur', 'brightness', 'contrast', 'grayscale', 'hue-rotate', 'invert', 'opacity', 'saturate', ] # 'sepia', 'drop-shadow'
		if b == 'x': n = random.randint(1,4)
		else: n = random.randint(1,2)
		for i in range(n):
			if i == 0 and b != 'x': f = l.pop(int(b)-1)
			else: f = l.pop(random.randint(0, len(l)-1))
			if f == 'blur': v = str(random.randint(1, 50)/10) + 'vmin'
			elif f == 'brightness' or f == 'contrast': v = str(random.randint(10, 500)) + '%'
			elif f == 'grayscale' or f == 'invert': v = '1'
			elif f == 'hue-rotate': v = str(random.randint(0, 360)) + 'deg'
			elif f == 'opacity': v = str(random.randint(20, 100)) + '%'
			elif f == 'saturate': v = str(random.randint(10, 2000)) + '%'
			f1 += ' %s(%s)' % (f, v)
		for i in webkit: fi1 += '\n\t%sfilter: %s;' % (i, f1)
	return fi1

def def_an3(a, b, b9, v4r, t2):
	def stp(n):
		t = 100/(n+1)
		s7 = ''
		for i in range(n):
			i = t*(i+1)
			if t2 == 'd0t': s = def_br(b, v4r)
			elif t2 == 'qd2': s = def_bs(b, v4r)
			elif t2 == 'pi3t': s = def_bg(v4r)
			elif t2 == 'd9d': s = def_d9d(b, v4r)
			elif t2 == 'im9': s = def_fi1(b)
			s7 += '\n%s  {%s}' % (str(i)+'%', s)
		return s7

	cs2 = ''
	if t2 == 'pi3t':
		td = def_bg(v4r)
		tdh = def_bg(v4r)
	elif t2 == 'd9d':
		td = def_d9d(b, v4r)
		tdh = def_d9d(b, v4r)
	elif t2 == 'd0t':
		td = def_br(b, v4r)
		tdh = def_br(b, v4r)
	elif t2 == 'qd2':
		td = def_bs(b, v4r)
		tdh = def_bs(b, v4r)
	elif t2 == 'im9':
		td = def_im9(b, v4r)
		tdh = def_im9h(b)

	if b9 == '1':
		webkit = ['-webkit-', '']
		an3 = '\n\t%sanimation: %s %ss infinite;'
		anm = '''
@%skeyframes %s {%s
}'''
		if a == '1':
			t = random.randint(5, 20)
			for i in webkit:
				cs2 += anm % (i, 'an3', stp(1))
				td += an3 % (i, 'an3', str(t))
				tdh += '\n\t%sanimation: 0;' % (i)
		elif a == 'x':
			n = random.randint(2,10)
			t = random.randint(5, 15) * (n)
			for i in webkit:
				cs2 += anm % (i, 'an3', stp(n))
				cs2 += anm % (i, 'an3h', stp(n))
				td += an3 % (i, 'an3', str(t))
				tdh += an3 % (i, 'an3h', '1')
	return cs2, td, tdh

def def_a(f7, b9, a):
	rf = ''
	if b9 == '0':
		if a == '1': rf = '0'
		elif a == 'x':
			if f7 == '2': rf = str(random.randint(1,5))
			else: rf = str(random.randint(5,15))
	return rf

def def_b(b, v4r):
	s = ''
	if b == 'x': b = random.choice(d7o)
	if b == '1':
		s += 'box-sizing: border-box;'
		bc = def_c0r(v4r, tp = 1)
		bs = ['border-top: %s;', 'border-bottom: %s;', 'border-left: %s;', 'border-right: %s;', ]
		for i in range(4):
			if random.randint(0, 1):
				b = '10px solid %s' % (def_hxc(bc))
				s += bs[i] % (b)
			else: s += bs[i] % ('0')
	return s

def def_bs(b, v4r):
	s = 'box-sizing: border-box;'
	bs = ['border-top: %s;', 'border-bottom: %s;', 'border-left: %s;', 'border-right: %s;', ]
	if b == '0':
		cor = def_rgb(def_c0r(v4r))
		n = 0
		u = 'vh'
		for i in range(2):
			c = [cor, 'transparent']
			for j in range(2):
				if not j: c0 = c.pop(random.randint(0,1))
				else: c0 = c[0]
				bc = '50%s solid %s' % (u, c0)
				s += '\n\t' + bs[n] % (bc)
				n += 1
			u = 'vw'
	elif b == '1':
		u = 'vh'
		for i in range(4):
			if random.randrange(4): cor = def_rgb(def_c0r(v4r))
			else: cor = 'transparent'
			bc = '50%s solid %s' % (u, cor)
			s += '\n\t' + bs[i] % (bc)
			if i == 1: u = 'vw'
	elif b == 'x':
		n = 0
		u = 'vh'
		for i in range(2):
			v1 = random.randint(20, 80)
			v2 = 100-v1
			for j in range(2):
				if random.randrange(4): cor = def_rgb(def_c0r(v4r))
				else: cor = 'transparent'
				if not j: v = str(v1)
				else: v = str(v2)
				bc = '%s%s solid %s' % (v, u, cor)
				s += '\n\t' + bs[n] % (bc)
				n += 1
			u = 'vw'
	return s

def def_br(b, v4r):
	s = 'border-radius: 50%;'
	bs = ['border-top: %s;', 'border-bottom: %s;', 'border-left: %s;', 'border-right: %s;', ]
	if b == '0': s += '\n\tbackground: %s;' % (def_rgb(def_c0r(v4r)))
	elif b == '1':
		s += '\n\tbox-sizing: border-box;'
		cor = def_rgb(def_c0r(v4r))
		u = 'vh'
		for i in range(4):
			bc0 = '50%s solid %s' % (u, random.choice([cor, 'transparent']))
			s += '\n\t' + bs[i] % (bc0)
			if i == 1: u = 'vw'
	elif b == 'x':
		s += '\n\tbox-sizing: border-box;'
		u = 'vh'
		n = 0
		for i in range(2):
			v1 = random.randint(20, 80)
			v2 = 100-v1
			for j in range(2):
				if random.randrange(4): cor = def_rgb(def_c0r(v4r))
				else: cor = 'transparent'
				if not j: v = str(v1)
				else: v = str(v2)
				bc = '%s%s solid %s' % (v, u, cor)
				s += '\n\t' + bs[n] % (bc)
				n += 1
			u = 'vw'
	return s

def def_c(c):
	if not c: c = '0'
	else: c = str(int(c)+1)
	return c

def def_d(f7, d):
	if d == 'x': d = random.choice(d7o)
	if f7 == '0':
		if d == '0': 
			return 'rows'
		else: 
			return 'cols'
	else: 
		return d

def def_e(f7, e):
	if f7 == '2':
		if e == '0': v1 = v2 = 80
		elif e == '1': v1 = v2 = 60
		elif e == 'x':
		    v1 = random.randint(50, 95)
		    v2 = random.randint(50, 95)
	else:
		if e == '0': v1 = 50
		elif e == '1': v1 = random.choice([40, 60]) # v1 = random.choice([38.1966, 61.8034])
		elif e == 'x': v1 = random.randint(10, 90)
		v2 = 100-v1
	return str(v1) + '%', str(v2) + '%'

def def_f0(b, v4r, d, v1, v2):
	b = b[0]
	if b not in d7o: b = random.choice(d7o)
	if b == '0': 
		return '%s="%s,%s" frameborder="0"' % (d, v1, v2)
	elif b == '1': 
		bc = def_hxc(def_c0r(v4r, tp = 1))
		return '%s="%s,%s" frameborder="1" border="10" bordercolor="%s"' % (d, v1, v2, bc)

def def_f2(d, v1, v2):
	v1 = int(v1[:-1])
	v2 = int(v2[:-1])
	m1 = (100-v1)/2 # margem para centralizar horizontalmente
	m2 = (100-v2)/2 # margem para centralizar verticalmente
	a, d = d
	# alinha
	if a == '0': a1 = a2 = 0 # sem margem
	elif a == '1': a1 = a2 = 5 # margem proporcao fixa 
	elif a == 'x': # margem aleatoria
		a1 = random.randint(0, int(m1))
		a2 = random.randint(0, int(m2))
	# margem
	if d == 'x': d = random.randint(1, 8)
	else: d = int(d)
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
	elif d == 5: m2 = 0 + a2
	elif d == 6: m2 = m2*2 - a2
	elif d == 7: m1 = 0 + a1
	elif d == 8: m1 = m1*2 - a1
	return ' margin-left:%svw; margin-top:%svh;' % (str(m1), str(m2))

def def_c0r(v4r, tp = 0):
	if tp == 1: # cor borda
		if v4r == 'pb': cor = 'x'
		elif v4r == 'rgb': cor = '1'
		elif v4r == 'piet': cor = '0'
		elif v4r == 'xxx': cor = v4r
		else: cor = random.choice(d7o)
	else:
		if v4r == 'pb': cor = random.choice(d7o)
		elif v4r == 'rgb': cor = random.choice(['100', '010', '001', '0'])
		elif v4r == 'cmyx': cor = random.choice(['011', '101', '110', random.choice(d7o) ])
		elif v4r == 'piet': cor = random.choice(['1', '100', '110', '001', '1', '0'])
		else: cor = v4r
	return cor

def def_dxd():
	cor = '-'
	for i in range(2): cor += random.choice(d7z)
	return cor

def def_xxx():
	cor = ''
	for i in range(3): cor += random.choice(d7x)
	if 'x' not in cor:
		if cor == '000' or cor == '111': cor = 'x'
		else: cor = def_xxx()
	return cor

def def_rgb(c):
	cor = ''
	for i in c:
		if i == 'x': i = str(random.randint(0, 255))
		elif i == '1': i = '255'
		cor += '%s,' % (i)
	if len(c) == 1: cor = cor*3
	return 'rgb(%s)' % (cor[:-1])

def def_hxc(c):
	cor = ''
	for i in c:
		if i == 'x':
			for j in range(2): cor += random.choice(list(string.hexdigits))
		elif i == '0': cor += '00'
		elif i == '1': cor += 'ff'
	if len(c) == 1: cor = cor*3
	return '#%s' % (cor)


# variaveis
# -/t2=/v4r=/f7=/b9=/l8p=/a=/b=/c=/d=/e=/

# t2 = tipo
# v4r = cor/im9
# f7 = organizacao dos frames
# b9 = tipo de bg
# l8p = loop
# a = atualiza/animacao
# b = borda/filtro/degrade
# c = contador
# d = divisao
# e = proporcao

d7tp = [
	'd0t', 
	'qd2',
	'pi3t',
	'd9d',
	'im9', 
]

d7im9 = [
		'hasselhoffian-recursion.gif', 
		'guido-van-rossum_python.jpg',
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
	'1', # alinhar t l
	'2', # alinhar t r
	'3', # alinhar b l
	'4', # alinhar b r
	'5', # alinhar t
	'6', # alinhar b
	'7', # alinhar l
	'8', # alinhar r
	'x', # aleatorio
]

d7o = ['0','1']

d7x = d7o+['x']

d7y = d7o+['2']

d7z = d7y+['x']

d7l = ['underline', 'overline', 'line-through']

