"""RestaurantManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from table_management import views as table_views
from menu_management import views as menu_views
from orders_management import views as order_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_table/', table_views.add_table),
    path('delete_table/', table_views.delete_table),
    path('get_all_menu/', menu_views.get_all_menu),
    path('add_items/', menu_views.add_items),
    path('delete_items/', menu_views.delete_items),
    path('edit_items/', menu_views.edit_items),
    path('place_order/', order_views.place_order),
    path('transfer_order/', order_views.transfer_order),
    path('all_orders/', order_views.all_orders),
    path('change_order_status/', order_views.change_order_status),
    path('all_active_orders/', order_views.all_active_orders),
    path('all_completed_orders/', order_views.all_completed_orders)

]
