# from rest_framework import permissions

# #자기 프로필만 수정가능하게
# class EditOnly(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.user == request.user