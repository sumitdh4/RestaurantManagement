from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Table


@api_view(['POST'])
def add_table(request):
    data = request.data
    table = Table(table_number=data['table_number'], table_capacity=data['table_capacity']).save()
    result = {"Status": True, "msg": "Table added Successfully"}
    return Response(result)


@api_view(['DELETE'])
def delete_table(request):
    data = request.data
    table = Table.objects.filter(table_number=data['table_number'])
    table.delete()
    result = {"Status": True, "msg": "Table deleted Successfully"}
    return Response(result)

