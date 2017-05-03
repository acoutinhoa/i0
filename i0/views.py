from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse
# from i0.models import *
import string
import random

def index0f(request):
	return HttpResponse('index0f')