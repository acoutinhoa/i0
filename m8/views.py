from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
from m8.models import *
import string
import random

def m8(request):
	tt = 'm8'
	pda = M8.objects.filter(casa__pk=7).order_by('-peso')
	poderosa=pda[0]
	pedra=pda[1]
	concha=pda[2]
	pda=pda.exclude(nome__in=['poderosa','elba','naga'])
	return render(request, 'm8/m8.html', {
		'tt':tt, 
		'pda':pda,
	})
