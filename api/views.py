import json
from django.http.response import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json
# Create your views here.

class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self,request,idUsuario=0):
        if(idUsuario>0):
            users=  list(Usuario.objects.filter(idUsuario=idUsuario).values())
            if len(users) > 0:
                datos = {'Users': users}

            
            return JsonResponse(datos)
        
        else:
            users = list(Usuario.objects.values())
            if len(users) > 0:
                datos = {'Users': users}
             
            
            return JsonResponse(datos)
    
    

    def post(self,request):
        jsonData= json.loads(request.body)
        Usuario.objects.create(nombreUsuario = jsonData['nombreUsuario'],email=jsonData['email'],password=jsonData['password'])
        datos = {'message': "Usuario Agregado"}
        return JsonResponse(datos)

    def put(self,request,idUsuario):
        jsonData= json.loads(request.body)
        users=  list(Usuario.objects.filter(idUsuario=idUsuario).values())
        if len(users) > 0:
            user=Usuario.objects.get(idUsuario=idUsuario)
            user.email= jsonData['email']
            user.password= jsonData['password']
            user.save()
            datos = {'message': "Usuario Actualizado"}
        
        else:
            datos = {'message': "Usuarios no encontrados"}
        
        return JsonResponse(datos)

    def delete(self,request,idUsuario):
        users=  list(Usuario.objects.filter(idUsuario=idUsuario).values())
        if len(users) > 0:
            user=Usuario.objects.filter(idUsuario=idUsuario).delete()
            datos = {'message': "Usuario Eliminado"}
        else:
            datos = {'message': "Usuarios no encontrados"}
        
        return JsonResponse(datos)
