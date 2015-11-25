from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request,number1,number2):

	return render(request,'home/home.html', {"n1":number1,"n2":number2,"suma":int(number1)+int(number2)})
	# number1=int(number1)
	# number2=int(number2)
	# return HttpResponse(number1+number2)
def hello(request):
	return HttpResponse("Hola Mijo")