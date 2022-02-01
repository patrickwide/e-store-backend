from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # This is the api overview page
    path("", views.apiOverview.as_view() ,name="apiOverview"),
    # products
    path("product-list/", views.productList.as_view(), name="productList"),
    path("product-detail/<str:pk>/", views.productDetail.as_view(), name="productDetail"),
    path("productQuery-category/<str:name>/",views.productQueryCategory.as_view(), name="productQueryCategory"),
    path("productQuery-shop/<str:name>/", views.productQueryShop.as_view(), name="productQueryShop"),

    # shoppingCache
    path("shoppingCache-list/", views.shoppingCacheList.as_view(), name="shoppingCacheList"),

    # purchase
    path("purchase-list/", views.purchaseList.as_view(), name="purchaseList"),
    path("purchase-create/", views.purchaseCreate.as_view(), name="purchaseCreate"),
    
    # accounts
    path('accounts/', include('rest_registration.api.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
