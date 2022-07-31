from django.contrib import admin
from django.urls import path 
from .views import categorylist, categorydetail, booklist, bookdetail, productlist, productdetail

urlpatterns = [
    path('admin/', admin.site.urls),
   path('categorylist/', categorylist.as_view(), name=categorylist ),
   path('categorydetail<int:pk>/', categorylist.as_view(), name=categorydetail),
   path('booklist/', booklist.as_view(), name=booklist),
   path('bookdetail<int:pk>/', bookdetail.as_view(), name=bookdetail),
   path('productlist/', productlist.as_view(), name=productlist),
   path('productdetail/<int:pk>', productdetail.as_view(), name=productdetail),
]
