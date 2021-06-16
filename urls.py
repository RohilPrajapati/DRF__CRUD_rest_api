from django.urls import path,include
from .views import ListProduct, DetailProduct,DetailProductByName

urlpatterns = [
    path('', ListProduct.as_view(), name ='listproduct' ),
    path('id/<int:pk>', DetailProduct.as_view(), name ='detailproduct' ),
    path('name/<str:name>', DetailProductByName.as_view(), name ='detailproductname' ),
]
