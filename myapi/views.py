from django.shortcuts import render
from rest_framework import viewsets
from myapi.models import Company,Employee
from myapi.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action

from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
# comany/{company id}/employess
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            emps=employee=Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'company might not exist'
            })
        
        # response = JsonResponse({"foo": "bar"})
        # response.content

        pass

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer