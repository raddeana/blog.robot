# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def robot (request):
  context = {}
  context["env"] = settings.PY_ENV
  return render(request, "robot.html", context)

def talk (request):
  context = {}
  context["env"] = settings.PY_ENV
  return render(request, "talk.html", context)

def admin_login (request):
  context = {}
  context["env"] = settings.PY_ENV
  return render(request, "admin/login.html", context)

def admin (request):
  context = {}
  context["env"] = settings.PY_ENV
  return render(request, "admin/index.html", context)
