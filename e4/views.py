from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, mm
from reportlab.lib.utils import getImageData
import PIL
from PIL import Image, ImageChops, ImageOps
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
from e4.models import *
from random import *
import string

lpc = [
    '0_x',
    '1_branco',
    '2_colorido',
]

llvc = [
    '0_x',
    '1_vermelho',
    '2_pb',
]

llv = [
    '0_x',
    '1_fixa',
    '2_variavel', 
    '3_multipla',   
    '4_larguravariavel',
    '5_outrospadroes',
]

def pdf(request):
	p0 = choice(P0.objects.all())
	response = def_pdf(p0)
	return response

def cartaz(request, m, f):
	def def_var(i, l):
		i = int(i)
		if i and i <= len(l):
			v = l[i-1]
		else:
			v = choice(l)
		return v
	def def_blocos(m0):
		b0 = m0.blocos.blocos.all()
		t0 = m0.blocos.informacoes.all()
		i0 = m0.blocos.logos.all()
		t1 = m0.blocos.textos.all()
		i1 = m0.blocos.imagens.all()
		fs = m0.formatos.all()
		return b0, t0, i0, t1, i1, fs
	def def_un(f0):
		un = f0.un
		if un == 'mm':
			u = mm/3 ############ unidade escalonada
		else:
			u = 1
		return un, u
	def def_lista(q7):
		l=[]
		for i in q7:
			l.append(i.n0)
		return l
	def def_infos(l):
		p.saveState()
		p.translate(ml, ph-mt)
		for i in l:
			def_itens(i[0], i[1])
			p.translate(int((pw-ml-mr)/len(l)), 0)
		p.restoreState()
	def def_itens(nome, lista):
		lh = int(ph/60)
		p.saveState()
		lista = ['%s:' % (nome)] + lista
		for t in lista:
			p.setFont(choice(["Courier-Bold", 'Helvetica-Bold']), lh)
			p.drawString(0, 0, t)
			p.translate(0, -lh)
		p.restoreState()
	def def_fonte(titulo):
		tt = []
		for j, car in enumerate(titulo):
			f = fonte[car]
			f = f.split()
			f.reverse()
			for i in range(len(f)):
				if j == 0:
					tt.insert(i, '--'+f[i]+'--')
				else:
					tt[i] += f[i]+'--'
		return tt

	fonte = {
		'e': '''
##########
##########
###-------
###-------
###-------
###-------
#######---
#######---
##########
##########
''',
		' ': '''
-------
-------
-------
-------
-------
-------
-------
-------
-------
-------
''',
	}

	# inicia pdf
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="e4_%s_%s.pdf"' % (m, f)
	buf = BytesIO()

	# pega objetos do banco d dados
	m0 = def_var(m, M0.objects.all())
	f0 = def_var(f, m0.formatos.all())
	b0, t0, i0, t1, i1, fs = def_blocos(m0)

	infos = def_lista(t0)
	logos = def_lista(i0)
	blocos = def_lista(b0)
	formatos = []
	for i in fs:
		formatos.append('%s_%s_%s' % (i.un, i.w, i.h))


	# define unidade
	un, u = def_un(f0)
	# define pagina
	pw = int(int(f0.w)*u)
	ph = int(int(f0.h)*u)
	# define margens
	mt = int(ph/12)
	mb = int(ph/20)
	ml = int(pw/8)
	mr = int(pw/15)
	# # define corfundo da pagina
	# pc = randrange(1,len(lpc))

	# desenha pagina pdf
	p = canvas.Canvas(buf, pagesize=(pw,ph))
	# colore a pagina
	def_pc(p, 2, pw, ph)

	# desenha infos
	def_infos([('infos', infos), ('logos', logos), ('blocos', blocos), ('formatos', formatos)])
	p.drawString(pw/2, ph/2, str(mm))
	p.drawString(pw/2, ph/3, str(cm))

	lw = randint(10,18)/10*u
	m = int(randint(10, 20)*u)
	n = range(mb, ph-mt, m)

	p.setLineWidth(lw)
	# p.rect(ml, mb, pw-ml-mr, ph-mb-mt) # desenha area entremargens
	for y in n:
		p.setStrokeColorCMYK(0,0,0,randint(50,100)/100)
		p.line(0, y, pw, y)

	p.setLineWidth(lw*1.5)
	p.setStrokeColorCMYK(0,0,0,1)
	p.line(ml, 0, ml, ph)

	# p.setLineCap(1)
	tt = def_fonte('ee ee')
	p.translate(ml, ph/2)
	for linha in tt:
		p.saveState()
		cont = 0
		for i, car in enumerate(linha):
			if not i:
				c = car
			else:
				if car != c:
					if car == '#':
						p.saveState()
						p.rotate(30)
						cont = 0
					elif car == '-':
						p.restoreState()
						p.translate(cont, 0)
					c = car
			p.line(0,0,m,0)
			p.translate(m,0)
			cont += m
		p.restoreState()
		p.translate(0, m)



	# finaliza pdf
	p.showPage()
	p.save()
	pdf = buf.getvalue()
	buf.close()
	response.write(pdf)
	return response


def def_pdf(p0):
	# variaveis gerais
	un = p0.formato.un
	if un == 'mm': u = mm/2
	else: u = 1
	pw = int(int(p0.formato.w)*u)
	ph = int(int(p0.formato.h)*u)
	# margens
	mt = int(22*u)
	mb = int(10*u)
	ml = int(20*u)
	mr = int(10*u)
	# cor do fundo da pagina
	pc = randrange(1,len(lpc))
	# linha vertical
	lv = randrange(1,len(llv))
	lvc = randrange(1,len(llvc))
	lve = 0.2*u
	# linha horizontal




	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="pdf.pdf"'
	buf = BytesIO()
	p = canvas.Canvas(buf, pagesize=(pw,ph))
	# colore a pagina
	def_pc(p, pc, pw, ph)

	# escolhe altura da linha
	n = int(randint(20, 40)*u)

	# desenha linhas horizontais e texto
	lhe = 1*u
	tt = T0.objects.get(id=1).txt
	p.setFont(choice(["Courier-Bold", 'Helvetica-Bold']), randint(5,100))
	linhas = randint(0,1)
	p.saveState()
	p.translate(0, mb)
	for i in range(mb, ph-mt, n):
		c = 1,random(),0,0
		if linhas:
			p.setLineWidth(lve)
			p.setStrokeColorCMYK(*c)
			p.line(0, 0, pw, 0)
		# p.setFillColorCMYK(*c)
		# p.drawString(randint(10,100)*u, n, (tt+' ')*randint(1, 20))
		p.translate(0, n)
	p.restoreState()

	# desenha imagem
	img = choice(I1.objects.all())
	im = Image.open(img.img.path)
	# im.convert(mode='L')
	im = ImageOps.grayscale(im)

	im8 = Image.new('RGBA', (pw,ph), color='#fff')
	iw = img.w
	ih = img.h
	w = randint(int(pw/2), int(pw-100*u))
	e = w/int(iw)
	h = int(e*int(ih))
	im = im.resize(size=(w, h))
	for i in range(mt, int(ph-mb-h), n):
		ww = int(randint(10,50)*u)
		im8.paste(im, box=(ww, i, w+ww, h+i))
		# im = Image.composite(im, im, mask)
	
	# datas = im8.getdata()
	# newData = []
	# for item in datas:
	#     if item[0] == 255 and item[1] == 255 and item[2] == 255:
	#         newData.append((255, 255, 255, 0))
	#     else:
	#         newData.append(item)

	# im8.putdata(newData)
	im8.convert('L')
	caminho = 'e4/teste.png'
	im8.save(caminho)
	# p.saveState()
	# p.translate(0, mb)
	p.drawImage(caminho, 0, 0, mask=[155, 255, 155, 255, 155, 255])
	# p.drawInlineImage(im8, 0, 0)
	# for i in range(mb, int(ph-mt-h), n):
	# 	p.drawInlineImage(im, randint(10,50)*u, 0, width=w, height=h)
	# 	p.translate(0, n)
	# p.restoreState()

	p.showPage()
	p.save()
	pdf = buf.getvalue()
	buf.close()
	response.write(pdf)
	return response

	# desenha linha vertical
	p.saveState()
	p.setLineWidth(lve)
	if lv == 1 or lv == 5:
		pos = ml
	else:
		pos = randrange(ml,pw-mr)
	if lv == 3 or lv == 4:
		n = randint(1,5)
	elif lv == 5:
		nn = randint(int(u),int(pw/2))
		n = len(range(ml, pw-mr, nn))
	else:
		n = 1
	for i in range(n):
		if lvc == 1:
			p.setStrokeColorCMYK(0,1,random(),0)
		elif lvc == 2:
			d = randint(int(10*u), int(ph/2))
			p.setDash(d, d)
			p.setFillColorCMYK(0,0,0,1)
		if lv == 4:
			p.setLineWidth(lve * randint(1,10))
		p.line(pos, 0, pos, ph)
		if lv == 3 or lv == 4:
			pos = randrange(ml,pw-mr)
		if lv == 5:
			pos += nn
	p.restoreState()

########################

# colore a pagina
def def_pc(p, pc, pw, ph):
	p.saveState()
	if pc == 2:
		c = randint(2, 5)
		x = 0.2
		if c == 2:
			p.setFillColorCMYK(0,0,x,0)
		elif c == 3:
			p.setFillColorCMYK(x,0,0,0)
		elif c == 4:
			p.setFillColorCMYK(0,x,0,0)
		elif c == 5:
			p.setFillColorCMYK(x,0,x,0)
		p.rect( 0, 0, pw, ph, stroke=0, fill=1)
	p.restoreState()




