from django.shortcuts import render
from CerelyApp.taske import add

# Create your views here.

add.delay(2, 2)
