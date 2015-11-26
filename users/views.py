from django.shortcuts import render
from django.http import HttpResponse

DB=[{
	"id":1,
	"nombre":"BliS",
	"edad":28,

},{
	"id":2,
	"nombre":"Gus",
	"edad":29,
},{
	"id":3,
	"nombre":"Viri",
	"edad":31,
},{
	"id":77,
	"nombre":"Brendi",
	"edad":22,
}]


def usuarios(request,nombre):
	# return HttpResponse("Tu nombre es: "+nombre)
	return render(request,'users/tuNombre.html', {"nombre":nombre})

def dar_usuario(request,id):
	for usr in DB:
		if int(id)==usr["id"]:
			return render(request,'users/tuNombre.html',{
				"nombre":usr["nombre"],
				"edad":usr["edad"]
				})
	return HttpResponse("<h1>Usuario no encontrado</h1>")
