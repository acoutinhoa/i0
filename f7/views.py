from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
# from f7.models import *
import string
import random

def f7(request, t2, v4r, l8p, f7, b9, a, b, c, d, e):
	t2, v4r, l8p, f7, b9, a, b, c, d, e = def_var(t2, v4r, l8p, f7, b9, a, b, c, d, e)
	ur1, ur2 = def_l8p(t2, v4r, l8p, f7, b9, a, b, c, d, e)
	v1, v2 = def_e(f7, e)
	d = def_d(f7, d)
	bg = def_f7bg(f7, t2, v4r, c)
	tt = 'f7/%s' % (t2)
	if l8p != '0':
		tt += ' l8p'
	if f7 != '0' and t2 == 'pi3t':
		fs1 = def_b(b, v4r)
		fs2 = def_b(b, v4r)
	else:
		fs1 = fs2 = ''
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
			'l8p':l8p,
			'ur1':ur1, 
			'ur2':ur2, 
			'v1':v1, 
			'v2':v2, 
			'fs1':fs1, 
			'fs2':fs2, 
			's':f,
		})

def b9(request, t2, v4r, l8p, f7, b9, a, b, c, d, e):
	t2, v4r, l8p, f7, b9, a, b, c, d, e = def_var(t2, v4r, l8p, f7, b9, a, b, c, d, e)
	ur1 = reverse('f7', args=(t2, v4r, l8p, f7, b9, a, b, c, d, e))
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
def def_var(t2, v4r, l8p, f7, b9, a, b, c, d, e):
	if t2 == '':
		t2 = random.choice(d7tp)

	if v4r == '':
		if t2 == 'im9':
			v4r = random.choice(d7o)
		else:
			v4r = random.choice(d7cor)
	if v4r == 'def':
		v4r = def_xxx()

	if l8p == '':
		l8p = random.choice(['0', random.choice(d7z)])

	if f7 == '':
		f7 = str(random.choice(range(3)))

	if b9 == '':
		b9 = random.choice(d7o)

	if a == '':
		a = random.choice(['x', random.choice(d7x)])

	if b == '':
		if t2 == 'im9':
			b = random.choice(['x', random.choice(d7d)])
		else:
			b = random.choice(d7x)

	if c == '': 
		c = '0'
	else:
		c = str(int(c)+1)

	if d == '':
		d = random.choice(['x', random.choice(d7x)])
	if f7 == '2':
		if len(d) == 1:
			d += random.choice(['x', random.choice(d7d)])
	else:
		if len(d) > 1:
			d = d[0]

	if e == '':
		e = random.choice(d7x)

	if t2 == 'im9' and b == '0' and a != '0':
		a = '0'

	return t2, v4r, l8p, f7, b9, a, b, c, d, e

def def_l8p(t2, v4r, l8p, f7, b9, a, b, c, d, e):
	if f7 == '2':
		ur1 = reverse('f7', args=(t2, v4r, l8p, f7, b9, a, b, c, d, e))
		ur2 = reverse('b9', args=(t2, v4r, l8p, f7, b9, a, b, c, d, e))
	else:
		if l8p == 'x':
			l8p = random.choice(['1', '2'])
		if l8p == '0':
			ur1 = ur2 = reverse('b9', args=(t2, v4r, l8p, f7, b9, a, b, c, d, e))
		elif l8p == '1':
			ur1 = reverse('f7', args=(t2, v4r, l8p, f7, b9, a, b, c, d, e))
			ur2 = reverse('b9', args=(t2, v4r, l8p, f7, b9, a, b, c, d, e))
		elif l8p == '2':
			ur1 = reverse('b9', args=(t2, v4r, l8p, f7, b9, a, b, c, d, e))
			ur2 = reverse('f7', args=(t2, v4r, l8p, f7, b9, a, b, c, d, e))
	return ur1, ur2

def def_bg(v4r):
	cor = def_c0r(v4r)
	return 'background: %s;' % (def_rgb(cor))

def def_b9bg(f7, t2, v4r, b):
	bg = ''
	if f7 == '0':
		if t2 == 'd0t' or t2 == 'qd2' and b == '0':
			bg = def_bg(v4r)
	return bg

def def_f7bg(f7, t2, v4r, c):
	bg = ''
	if f7 != '0':
		if f7 == '1':
			if c != '0':
				if random.choice([0, random.choice([0, random.randint(0,1)])]):
					c = '0'
		if c == '0':
			if t2 == 'im9':
				bg = def_im9('0', v4r)
			else:
				bg = def_bg(v4r)
	return bg

def def_im9(b, v4r):
	if v4r == '0' or v4r == '1':
		v4r = d7im9[int(v4r)]
	if v4r[-3:] == 'gif':
		bg = 'url(%s) no-repeat' % (v4r)
		bgs = '100vw 100vh'
	else:
		bg = 'url(%s) no-repeat center fixed' % (v4r)
		bgs = 'cover'
	return 'background: %s;\n\tbackground-size: %s;%s' % (bg, bgs, def_fi1(b))

def def_im9h(b):
	webkit = ['', '-webkit-', '-ms-']
	tdh = ''
	for i in range(len(webkit)):
		tdh += '%stransform: rotate(180deg);' % (webkit[i])
	if b != '0':
		tdh += def_fi1(b)
	return tdh

def def_fi1(b):
	fi1 = f1 = ''
	if b != '0':
		webkit = ['', '-webkit-',]
		l = ['blur', 'brightness', 'contrast', 'grayscale', 'hue-rotate', 'invert', 'opacity', 'saturate', ] # 'sepia', 'drop-shadow'
		if b == 'x':
			n = random.randint(1,3)
		else:
			n = random.randint(1,2)
		for i in range(n):
			if b != 'x' and i == 0:
			    f = l.pop(int(b)-1)
			else:
			    f = l.pop(random.randint(0, len(l)-1))
			if f == 'blur':
				v = str(random.randint(1, 50)/10) + 'vmin'
			elif f == 'brightness' or f == 'contrast':
				v = str(random.randint(10, 500)) + '%'
			elif f == 'grayscale' or f == 'invert':
				v = '1'
			elif f == 'hue-rotate':
				v = str(random.randint(0, 360)) + 'deg'
			elif f == 'opacity':
				v = str(random.randint(20, 100)) + '%'
			elif f == 'saturate':
				v = str(random.randint(10, 2000)) + '%'
			f1 += ' %s(%s)' % (f, v)
		for i in range(len(webkit)):
			fi1 += '\n\t%sfilter: %s;' % (webkit[i], f1)
	return fi1

def def_an3(a, b, b9, v4r, t2):
	def stp(n):
		stp = '\n%s  {%s}'
		t = 100/(n+1)
		s = ''
		for i in range(n):
			if t2 == 'd0t':
				s += stp % (str(t*(i+1))+'%', def_br(b, v4r))
			elif t2 == 'qd2':
				s += stp % (str(t*(i+1))+'%', def_bs(b, v4r))
			elif t2 == 'pi3t':
				s += stp % (str(t*(i+1))+'%', def_bg(v4r))
			elif t2 == 'im9':
				s += stp % (str(t*(i+1))+'%', def_fi1(b))
		return s

	cs2 = ''
	if t2 == 'd0t':
		td = def_br(b, v4r)
		tdh = def_br(b, v4r)
	elif t2 == 'qd2':
		td = def_bs(b, v4r)
		tdh = def_bs(b, v4r)
	elif t2 == 'pi3t':
		td = def_bg(v4r)
		tdh = def_bg(v4r)
	elif t2 == 'im9':
		td = def_im9(b, v4r)
		tdh = def_im9h(b)

	if b9 == '1':
		webkit = ['', '-webkit-',]
		an3 = '\n\t%sanimation: %s %ss infinite;'
		anm = '''
@%skeyframes %s {%s
}'''
		if a == '1':
			t = random.randint(5, 20)
			for i in range(len(webkit)):
				cs2 += anm % (webkit[i], 'an3', stp(1))
				td += an3 % (webkit[i], 'an3', str(t))
				tdh += '\n\t%sanimation: 0;' % (webkit[i])
		elif a == 'x':
			n = random.randint(2,10)
			t = random.randint(5, 15) * (n)
			for i in range(len(webkit)):
				cs2 += anm % (webkit[i], 'an3', stp(n))
				cs2 += anm % (webkit[i], 'an3h', stp(n))
				td += an3 % (webkit[i], 'an3', str(t))
				tdh += an3 % (webkit[i], 'an3h', '1')
	return cs2, td, tdh

def def_a(f7, b9, a):
	rf = ''
	if b9 == '0':
		if a == '1':
			rf = '0'
		elif a == 'x':
			if f7 == '2':
				rf = str(random.randint(1,5))
			else:
				rf = str(random.randint(5,15))
	return rf

def def_b(b, v4r):
	s = ''
	if b == 'x':
		b = random.choice(d7o)
	if b == '1':
		s += 'box-sizing: border-box;'
		bc = def_c0r(v4r, tp = 1)
		bs = ['border-top: %s;', 'border-bottom: %s;', 'border-left: %s;', 'border-right: %s;', ]
		for i in range(4):
			if random.randint(0, 1):
				b = '10px solid %s' % (def_hxc(bc))
				s += bs[i] % (b)
			else:
				s += bs[i] % ('0')
	return s

def def_bs(b, v4r):
    s = 'box-sizing: border-box;'
    bs = ['border-top: %s;', 'border-bottom: %s;', 'border-left: %s;', 'border-right: %s;', ]
    if b == '0':
        cor = def_rgb(def_c0r(v4r))
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
            bc0 = '50%s solid %s' % (u, def_rgb(def_c0r(v4r)))
            s += '\n\t' + bs[i] % (bc0)
            if i == 1:
                u = 'vw'
    elif b == 'x':
        u = 'vh'
        n = 0
        for i in range(2):
            v1 = random.randint(20, 80)
            v2 = 100-v1
            bc0 = '%s%s solid %s' % (str(v1), u, def_rgb(def_c0r(v4r)))
            bc1 = '%s%s solid %s' % (str(v2), u, def_rgb(def_c0r(v4r)))
            s += '\n\t' + bs[n] % (bc0)
            s += '\n\t' + bs[n+1] % (bc1)
            u = 'vw'
            n = 2
    return s

def def_br(b, v4r):
    s = 'border-radius: 50%;'
    bs = ['border-top: %s;', 'border-bottom: %s;', 'border-left: %s;', 'border-right: %s;', ]
    if b == '0':
        s += '\n\tbackground: %s;' % (def_rgb(def_c0r(v4r)))
    elif b == '1':
    	s += '\n\tbox-sizing: border-box;'
    	cor = def_rgb(def_c0r(v4r))
    	u = 'vh'
    	for i in range(4):
            bc0 = '50%s solid %s' % (u, random.choice([cor, 'transparent']))
            s += '\n\t' + bs[i] % (bc0)
            if i == 1:
                u = 'vw'
    elif b == 'x':
    	s += '\n\tbox-sizing: border-box;'
    	u = 'vh'
    	n = 0
    	for i in range(2):
            v1 = random.randint(20, 80)
            v2 = 100-v1
            bc0 = '%s%s solid %s' % (str(v1), u, def_rgb(def_c0r(v4r)))
            bc1 = '%s%s solid %s' % (str(v2), u, def_rgb(def_c0r(v4r)))
            s += '\n\t' + bs[n] % (bc0)
            s += '\n\t' + bs[n+1] % (bc1)
            u = 'vw'
            n = 2
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

def def_e(f7, e):
	if f7 == '2':
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

def def_f0(b, v4r, d, v1, v2):
	if b == 'x':
		b = random.choice(d7o)
	if b == '1':
		bc = def_c0r(v4r, tp = 1)
		return '%s="%s,%s" frameborder="1" border="10" bordercolor="%s"' % (d, v1, v2, def_hxc(bc))
	else:
		return '%s="%s,%s" frameborder="0"' % (d, v1, v2)

def def_f2(d, v1, v2):
	v1 = int(v1[:-1])
	v2 = int(v2[:-1])
	m1 = (100-v1)/2 # margem para centralizar horizontalmente
	m2 = (100-v2)/2 # margem para centralizar verticalmente
	# alinha
	if d[0] == '0':
		# sem margem
		a1 = a2 = 0 
	elif d[0] == '1':
		# margem proporcao fixa
		a1 = a2 = 5 
	elif d[0] == 'x':
		# margem aleatoria
		a1 = random.randint(0, int(m1))
		a2 = random.randint(0, int(m2))
	# margem
	if d[1] == 'x':
		d = random.randint(1, 8)
	else:
		d = int(d[1])
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
	return ' margin-left:%svw; margin-top:%svh;' % (str(m1), str(m2))

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
# / f7 / t2 + l8p / v4r / a / b / c / d / e /

# t2 = tipo
# l8p = loop
# v4r = cor/im9
# a = atualiza/animacao
# b = borda
# c = contador
# d = divisao
# e = proporcao

d7tp = [
	'd0t', 
	'qd2',
	'pi3t',
	'im9', 
]

d7im9 = [
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

d7z = d7x+['2']

d7l = ['underline', 'overline', 'line-through']

