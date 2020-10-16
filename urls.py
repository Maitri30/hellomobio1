from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.welcome),
    path('load_form',views.load_form),
    path('add',views.add),
    path('padd/',views.padd),
    path('show',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('addproduct/', views.addproduct),
]