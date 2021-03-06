from rest_framework import permissions

class ProductIsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow productOwner of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the productOwner of the product.
        return obj.shop.user == request.user

class ShopIsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow productOwner of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the productOwner of the product.
        return obj.user == request.user
