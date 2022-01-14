from django.urls import path
from . import views


urlpatterns = [
    # This is the api overview page
    path("", views.apiOverview.as_view() ,name="apiOverview"),
    # All the operations that the shop owners can do (CRUD)
    path("product-list/", views.productList.as_view(), name="productList"),
    path("product-detail/<str:pk>/", views.productDetail.as_view(), name="productDetail"),
]
