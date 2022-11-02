from django.shortcuts import render, HttpResponse


def login(request):
  return HttpResponse(request, "<h1>Login Page</h1>")