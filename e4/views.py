from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm, mm
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
	p3 = choice(P3.objects.all())
	response = def_pdf(p3)
	return response

def def_pdf(p3):
	# variaveis gerais
	un = p3.formato.un
	if un == 'mm': u = mm
	else: u = 1
	pw = int(int(p3.formato.w)*u)
	ph = int(int(p3.formato.h)*u)
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

	lhe = 1*u
	tt = T0.objects.get(id=1).txt
	n = int(randint(10, 30)*u)
	p.setFont(choice(["Courier-Bold", 'Helvetica-Bold']), randint(5,100))
	linhas = randint(0,1)
	for i in range(mb, ph-mt, n):
		c = 1,random(),0,0
		p.setFillColorCMYK(*c)
		p.drawString(randint(10,100)*u, n, (tt+' ')*randint(1, 20))
		p.translate(0, n)
		if linhas:
			p.setLineWidth(lve)
			p.setStrokeColorCMYK(*c)
			p.line(0, 0, pw, 0)

	p.showPage()
	p.save()
	pdf = buf.getvalue()
	buf.close()
	response.write(pdf)
	return response

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




