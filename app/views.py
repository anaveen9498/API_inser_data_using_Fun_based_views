from django.shortcuts import render



from rest_framework.decorators import api_view,permission_classes
from app.models import *
from app.serializers import *
from rest_framework.permissions import IsAuthenticated


from rest_framework.response import Response
# Create your views here.

@api_view()
@permission_classes([IsAuthenticated])
def EmployeeJData(request):
    EDO=Employee.objects.all()
    JSO=EmployeeMS(EDO,many=True)
    return Response(JSO.data)
