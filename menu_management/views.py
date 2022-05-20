from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Menu, Items


@api_view(['GET'])
def get_all_menu(request):
    data = request.data
    menu_list = Menu.objects.all()
    menu_data = []
    for menu in menu_list:
        dic = {
            "type":menu.type,
            "items":[]
        }
        for item in menu.items.all():
            dic['items'].append(
                {
                    "name":item.name,
                    "price":item.price,
                    "disc":item.discount
                }
            )

        menu_data.append(dic)

    result = {"Status": True, "msg": "Showing all Menu Items", "data": menu_data}
    return Response(result)


@api_view(['POST'])
def add_items(request):
    data = request.data
    items = Items(name=data['name'], price=data['price'], discount=data['discount']).save()
    result = {'Status': True, 'msg': 'Items added successfully'}
    return Response(result)


@api_view(['DELETE'])
def delete_items(request):
    data = request.data
    items = Items.objects.filter(name=data['name'])
    items.delete()
    result = {'Status': True, 'msg': 'Items deleted successfully'}
    return Response(result)


@api_view(['PUT'])
def edit_items(request):
    data = request.data
    items = Items.objects.get(name=data['name'])
    items.name = data['new_name']
    items.price = data['price']
    items.discount = data['discount']
    items.save()
    result = {'Status': True, 'msg': 'Items edited successfully'}
    return Response(result)


