from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from advocates.models import Advocates, Company
from .serializers import AdvocatesSerializer, CompanySerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    data = ['/advocates', '/advocates/username', '/companies', '/companies/id']
    return Response(data)

@api_view(['GET'])
def advocates(request):
    advocates_list = Advocates.objects.all()
    serializer = AdvocatesSerializer(advocates_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def advocate(request, username):
    ad = Advocates.objects.get(username=username)
    serializer = AdvocatesSerializer(ad, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def companies(request):
    com = Company.objects.all()
    serializer = CompanySerializer(com, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def company(request, id):
    com = Company.objects.get(id=id)
    serializer = CompanySerializer(com, many=False)
    return Response(serializer.data)