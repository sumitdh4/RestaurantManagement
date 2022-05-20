from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Orders
from menu_management.models import Items
from table_management.models import Table


@api_view(['POST'])
def place_order(request):
    data = request.data
    table_num = Table.objects.get(table_number=data['table_number'])
    create_order = Orders.objects.create(order_number=data['order_number'],
                                         table_number=table_num,
                                         discount=data['discount']
                                         )
    item_names = data['items'].split(",")

    for items in item_names:
        item = Items.objects.get(name=items)
        create_order.items.add(item)

    create_order.save()

    return Response({"status": True, "msg": "order placed successfully"})


@api_view(['PUT'])
def transfer_order(request):
    data = request.data
    order = Orders.objects.get(order_number=data['order_number'])
    table = Table.objects.get(table_number=data['table_number'])

    order.table_number = table
    order.save()

    return Response({"status": True, "msg": "order transferred successfully"})


@api_view(['GET'])
def all_orders(request):
    data = request.data

    order = Orders.objects.all()
    new_list = []
    for x in order:
        dic = {
            "order_number": x.order_number,
            "status": x.active
        }
        new_list.append(dic)

    result = ({"status": True, "msg": "showing all orders", "data": new_list})
    return Response(result)


@api_view(['PUT'])
def change_order_status(request):
    data = request.data
    order_status = Orders.objects.get(order_number=data['order_number'])
    active = data['active']
    order_status.active = active
    order_status.save()

    result = ({"status": True, "msg": "order status changed to", "active": data['active']})
    return Response(result)


@api_view(['GET'])
def all_active_orders(request):
    data = request.data
    order = Orders.objects.all()
    new_list = []
    for x in order:
        if x.active:
            new_list.append({
                "order_number": x.order_number,
                "status": x.active

            })

    result = ({"status": True, "msg": "showing all active orders", "data": new_list})
    return Response(result)


@api_view(['GET'])
def all_completed_orders(request):
    data = request.data
    order = Orders.objects.all()
    new_list = []
    for x in order:
        if x.active is False:
            new_list.append({
                "order_number": x.order_number,
                "status": x.active

            })

    result = ({"status": True, "msg": "showing all completed orders", "data": new_list})
    return Response(result)
