from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
from f7.models import *
import string
import random

def f7m3(request, t2='', v4r='', l8p='', f7='', b9='', a='', b='', c='', d=''):
	t2, v4r, l8p, f7, b9, a, b, c, d = def_var(t2, v4r, l8p, f7, b9, a, b, c, d)
	ur1 = reverse('m3', args=(t2, v4r, l8p, f7, b9, a, b, c, d))
	ur2 = reverse('f7', args=(t2, v4r, l8p, f7, b9, a, b, c, d))
	tt = 'f7/%s' % (t2)
	f = 'cols' # random.choice(['rows', 'cols'])
	f = '%s="%s,*" frameborder="1" border="15" bordercolor="#fff"' % (f, '15%')
	return render(request, 'm3/f7.html', {
		'tt':tt, 
		'ur1':ur1, 
		'ur2':ur2, 
		'f7':f,
		'n1':'f1',
		'n2':'f2',
	})

def m3(request, t2='', v4r='', l8p='', f7='', b9='', a='', b='', c='', d=''):
	c1, c2 = def_m3c()
	html, cs2 = def_m3(t2, v4r, l8p, f7, b9, a, b, c, d)
	tt = 'f7/m3'
	return render(request, 'm3/m3.html', {
		'tt':tt, 
		'cs2':cs2, 
		'html':html,
		'c1':c1,
		'c2':c2,
	})

def def_m3c():
	c1 = ['110', '011', '010']
	c2 = ['100', '101', '001']
	c1 = def_hxc(c1.pop(random.randrange(len(c1))))
	c2 = def_hxc(c2.pop(random.randrange(len(c2))))
	return c1, c2

def def_m3(t2, v4r, l8p, f7, b9, a, b, c, d):
	html = ''
	cs2 = ''
	var = [t2, v4r, l8p, f7, b9, a, b, c, d]
	r8 = random.randrange(T2.objects.all().count())
	for i, t in enumerate(T2.objects.all()):
		if i == r8:
			ur1 = reverse('f7m3', args=('', '', '', '', '', '', '', '', ''))
			nome = 'r8'
			html += '\n\t<a href="%s" target="_parent" onmouseover="an8(%s, %s)" onmouseout="an0(%s)">\n\t<div id="%s" class="b0">?</div></a>' % (ur1, "'b1'", "'an8'", "'b1'", nome)
			cs8 = def_bt3(nome, div = '#')

		h = '\n\t<div id="%s" class="b0">%s</div>' % (t.n0, t.n0)
		ur1 = var[:]
		ur1[i] = ''
		ur1 = reverse('f7m3', args=(ur1))
		nome = "'%s'" % (t.n0)
		html += '\n\t<a href="%s" target="_parent" onmouseover="an8(%s, %s)" onmouseout="an0(%s)">%s</a>' % (ur1, nome, "'an8'", nome, h)
		cs2 += def_bt3(t.n0, div = '#')
		for f in t.f7_set.all():
			ur1 = var[:]
			if '.' in f.n0:
				nome = f.n0.split('.')
				nome = nome[-1]
			else: nome = f.n0
			nome = '%s_%s' % (t.n0, nome)
			if f.n0 == var[i]:
				h = '\n\t<div class="b1 bs %s %s">%s</div>' % (nome, t.n0, f.n0)
			else:
				h = '\n\t<div class="b1 %s %s">%s</div>' % (nome, t.n0, f.n0)
				ur1[i] = f.n0
			ur1 = reverse('f7m3', args=(ur1))
			# ur1 += '#%s' % (t.n0)
			html += '\n\t<a href="%s" target="_parent">%s</a>' % (ur1, h)
			cs2 += def_bt3(nome)
	return html, cs2 + cs8

def def_bb(bh = 0, bw = 0, div = '.', nome = ''):
	s = ''
	bs = ['border-top: %s;', 'border-bottom: %s;', 'border-left: %s;', 'border-right: %s;', ]
	for j in range(2):
		if j == 0:
			var = bh
			n = 0
		else:
			var = bw
			n = 2
		if var == 0:
			for i in range(2):
				if div == '.':
					b = random.randint(2, 15)
					bc = '%spx solid %s' % (b, def_hxc('x'))
				elif div == '#':
					b = random.randint(15, 30)
					bc = '%spx solid %s' % (b, def_hxc(random.choice(d7o)))
				var += b
				s += bs[i+n] % (bc)
		else:		
			for i in range(2):
				if i == 0:
					b = random.randint(0, var)
					var -= b
				else:
					b = var
					var -= b
				if div == '.':
					bc = '%spx solid %s' % (b, def_hxc('x'))
				elif div == '#':
					bc = '%spx solid %s' % (b, def_hxc(random.choice(d7o)))
				s += bs[i+n] % (bc)
		if j: bw = var
		else: bh = var
	cs8 = ''
	if nome == 'r8':
		webkit = ['-webkit-', '']
		an3 = '%sanimation: %s %ss infinite;'
		anm = '''
@%skeyframes %s {%s
}'''
		if bw == 0:
			for i in webkit:
				s += '%sanimation: 0;' % (i)
		else:
			def stp(n):
				t = 100/(n+1)
				s8  = ''
				for i in range(n):
					i = t*(i+1)
					ss = ''
					for j in range(2):
						if j == 0:
							var = bh
							n = 0
						else:
							var = bw
							n = 2
						for k in range(2):
							if k == 0:
								b = random.randint(0, var)
								var -= b
							else:
								b = var
							bc = '%spx solid %s' % (b, def_hxc(random.choice(d7o)))
							ss += bs[k+n] % (bc)
					s8 += '\n%s  {%s}' % (str(i)+'%', ss)
				return s8
			n = random.randint(2,10)
			t = random.randint(1, 3) * (n)
			for i in webkit:
				cs8 += anm % (i, 'r8', stp(n))
				s += an3 % (i, 'r8', str(t))
	return s, bh, bw, cs8

def def_bt3(nome, div = '.'):
	cs2 = cs8 = ''
	bh = bw = 0
	for i in range(2):
		if i:
			h = ':hover'
		else:
			h = ''
		s, bh, bw, s8 = def_bb(bh=bh, bw=bw, div=div, nome=nome)
		cs2 += '\n%s%s%s {%s}' % (div, nome, h, s)
		cs8 += s8
	return cs2 + cs8


def f7(request, t2='', v4r='', l8p='', f7='', b9='', a='', b='', c='', d='', n='0'):
	if t2 != 'ka8s': 
		t2, v4r, l8p, f7, b9, a, b, c, d = def_var(t2, v4r, l8p, f7, b9, a, b, c, d)
	tt = 'f7/%s' % (t2)
	if l8p != '0' and t2 != 'ka8s': tt += ' l8p'
	ur1, ur2 = def_l8p(t2, v4r, l8p, f7, b9, a, b, c, d, str(int(n)+1))
	if t2 == 'ka8s': 
		t2, v4r, l8p, f7, b9, a, b, c, d = def_var('', '', '', '', '', '', '', '', '')
	# if v4r == 'def': v4r = def_xxx()
	bg = def_f7bg(f7, t2, v4r, n)
	if t2 == 'pi3t' and f7 != '0':
		fs1 = def_b(b, v4r)
		fs2 = def_b(b, v4r)
	else: fs1 = fs2 = ''

	if f7 == '0':
		f = def_f0(v4r, b, c, d)
		return render(request, 'f7/f7.html', {
			'tt':tt, 
			'ur1':ur1, 
			'ur2':ur2, 
			'f7':f,
		})
	elif f7 == '1':
		w1, w2, h1, h2 = def_f1(c, d)
		return render(request, 'f7/f7i.html', {
			'b':bg, 
			'tt':tt, 
			'ur1':ur1, 
			'ur2':ur2, 
			'h1':h1, 
			'h2':h2, 
			'w1':w1, 
			'w2':w2, 
			'fs1':fs1, 
			'fs2':fs2, 
		})
	elif f7 == '2':
		f, w, h = def_f2(c, d)
		return render(request, 'f7/f7q.html', {
			'b':bg, 
			'tt':tt, 
			'ur1':ur1, 
			'ur2':ur2, 
			'w':w, 
			'h':h, 
			'fs1':fs1, 
			'fs2':fs2, 
			's':f,
		})

def b9(request, t2='', v4r='', l8p='', f7='', b9='', a='', b='', c='', d='', n='0'):
	if t2 != 'ka8s': t2, v4r, l8p, f7, b9, a, b, c, d = def_var(t2, v4r, l8p, f7, b9, a, b, c, d)
	if n == '0': ur1 = reverse('f7', args=(t2, v4r, l8p, f7, b9, a, b, c, d))
	else: ur1 = reverse('f7', args=(t2, v4r, l8p, f7, b9, a, b, c, d, str(int(n)+1)))
	if t2 == 'ka8s': t2, v4r, l8p, f7, b9, a, b, c, d = def_var('', '', '', '', '', '', '', '', '')
	# if v4r == 'def': v4r = def_xxx()
	tt = 'f7/b9/%s' % (t2)
	rf = def_a(t2, b9, a)
	bg = def_b9bg(f7, t2, v4r)
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

# cor = ['x']
# for i in range(3):
# 	for j in range(3):
# 		for k in range(3):
# 			c=l[i]+l[j]+l[k]
# 			cor.append(c)
# 			c = ''
# for c in cor:
# 	if 'x' in c and not v4r.f7_set.filter(n0=c).first():
# 		c



# defs
def def_var(t2, v4r, l8p, f7, b9, a, b, c, d):
	tp = T2.objects.all()
	var = [t2, v4r, l8p, f7, b9, a, b, c, d]
	for i,t in enumerate(tp):
		r1 = t.r1.first()
		if not var[i]:
			if r1:
				r = var[r1.id-1]
				v = r.r1.filter(t2=t).first()
			else:
				v = t.f7_set.first()
			var[i] = v
		else:
			if r1:
				r = var[r1.id-1]
				v = r.r1.filter(t2=t).filter(n0=var[i]).first()
			else:
				v = t.f7_set.filter(n0=var[i]).first()
			if v:
				var[i] = v
			else:
				return 'ka8s', v4r, l8p, f7, b9, a, b, c, d
	l =[]
	for i in var: 
		l.append(i.n0)
	return l

def def_l8p(t2, v4r, l8p, f7, b9, a, b, c, d, n):
	if t2 == 'ka8s': lp = random.choice([0, random.randrange(3)])
	else:
		if l8p == 'x': lp = random.randint(random.randrange(2), 2)
		else: lp = int(l8p)
	ur1 = reverse('b9', args=(t2, v4r, l8p, f7, b9, a, b, c, d, n))
	if lp == 0: ur2 = ur1
	elif lp == 1: ur2 = reverse('f7', args=(t2, v4r, l8p, f7, b9, a, b, c, d, n))
	elif lp == 2:
		ur2 = ur1
		ur1 = reverse('f7', args=(t2, v4r, l8p, f7, b9, a, b, c, d, n))
	return ur1, ur2

def def_bg(v4r):
	cor = def_rgb(def_c0r(v4r))
	return 'background: %s;' % (cor)

def def_b9bg(f7, t2, v4r):
	bg = ''
	if f7 == '0':
		if t2 == 'd0t' or t2 == 'd9d' or t2 == 'qd2': bg = def_bg(v4r)
	return bg

def def_f7bg(f7, t2, v4r, n):
	bg = ''
	if f7 != '0':
		if f7 == '1' and n != '0':
			if not random.randrange(5): n = '0'
		if n == '0':
			if t2 == 'im9': bg = def_im9('0', v4r)
			else: bg = def_bg(v4r)
	return bg

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
		cor = l.pop(random.randrange(2)) + ', ' + l[0]
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

def def_im9(b, v4r):
	t2 = F7.objects.get(n0='im9').r1.filter(t2__n0='v4r')
	v4r = F7.objects.get(n0=v4r)
	if v4r in t2: v4r = v4r.img.url
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
		for i in webkit: fi1 += '%sfilter:%s;' % (i, f1)
	return '\n\t' + fi1

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
	if c == '0': return 50
	elif c == '1': return random.choice([40, 60]) # random.choice([38.1966, 61.8034])
	elif c == 'x': return random.randint(10, 90)

def def_f0(v4r, b, c, d):
	c = '{0}%,*'.format(str(def_c(c)))

	if d == 'x': d = random.choice(d7o)
	if d == '0': d = 'rows'
	else: d = 'cols'

	b = b[0]
	if b not in d7o: b = random.choice(d7o)
	if b == '0': return '%s="%s" frameborder="0"' % (d, c)
	else: 
		bc = def_hxc(def_c0r(v4r, tp = 1))
		return '%s="%s" frameborder="1" border="10" bordercolor="%s"' % (d, c, bc)

def def_f1(c, d):
	v1 = def_c(c)
	v2 = 100-v1

	if d == 'x': d = random.choice(d7o)
	if d == '0':
		h1 = str(v1) + 'vh'
		h2 = str(v2) + 'vh'
		w1 = w2 = ''
	else:
		w1 = str(v1) + 'vw'
		w2 = str(v2) + 'vw'
		h1 = h2 = ''
	return w1, w2, h1, h2

def def_f2(c, d):
	if c == '0': v1 = v2 = 80
	elif c == '1': v1 = v2 = 60
	elif c == 'x':
	    v1 = random.randint(50, 95)
	    v2 = random.randint(50, 95)
	w = str(v1) + 'vw'
	h = str(v2) + 'vh'
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
	f = ' margin-left:%svw; margin-top:%svh;' % (str(m1), str(m2))
	return f, w, h

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
# -/t2=/v4r=/f7=/b9=/l8p=/a=/b=/c=/d=/n/

# t2 = tipo
# v4r = cor/im9
# f7 = organizacao dos frames
# b9 = tipo de bg
# l8p = loop
# a = atualiza/animacao
# b = borda/filtro/degrade
# c = proporcao
# d = divisao
# n = contador

# d7tp = [
# 	'd0t', 
# 	'qd2',
# 	'pi3t',
# 	'd9d',
# 	'im9', 
# ]

# d7im9 = [
# 		'0.gif', 
# 		'1.jpg',
# ]

# d7cor = [
# 		'piet', # choice(r, y, b, w)
# 		'pb', # choice(p, b)
# 		'rgb', # choice(r, g, b, k)
# 		'cmyx', # choice(c, m, y, choice(p, b))
# 		'xxx', # rgb random
# 		'10x', # magenta/vermelho random
# 		'00x', # azul/preto random
# 		'def', # def_xxx
# ]

# d7d = [
# 	'0', # centralizado
# 	'1', # alinhar t l
# 	'2', # alinhar t r
# 	'3', # alinhar b l
# 	'4', # alinhar b r
# 	'5', # alinhar t
# 	'6', # alinhar b
# 	'7', # alinhar l
# 	'8', # alinhar r
# 	'x', # aleatorio
# ]

d7o = ['0','1']

d7x = d7o+['x']

d7y = d7o+['2']

d7z = d7y+['x']

d7l = ['underline', 'overline', 'line-through']

