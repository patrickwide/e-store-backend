from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # This is the api overview page
    path("", views.apiOverview.as_view(), name="apiOverview"),

    #PRODUCT
    path("product-list/", views.productList.as_view(), name="productList"),
    path("product-detail/<str:pk>/", views.productDetail.as_view(), name="productDetail"),
    path("product-create/<str:pk>/", views.productCreate.as_view(), name="productCreate"),
    path("product-update/<str:pk>/", views.productUpdate.as_view(), name="productUpdate"),
    path("product-delete/<str:pk>/", views.productDelete.as_view(), name="productDelete"),

    # SHOP
    path("shop-list/", views.shopList.as_view(), name="shopList"),
    path("shop-detail/<str:pk>/", views.shopDetail.as_view(), name="shopDetail"),
    path("shop-create/", views.shopCreate.as_view(), name="shopCreate"),
    path("shop-update/<str:pk>/", views.shopUpdate.as_view(), name="shopUpdate"),
    path("shop-delete/<str:pk>/", views.shopDelete.as_view(), name="shopDelete"),


    path("sign-in/", views.productSignIn.as_view(), name="SignIn"),
    path("sign-up/", views.productSignUp.as_view(), name="SignUp"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
