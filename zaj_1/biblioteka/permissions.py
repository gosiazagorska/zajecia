import copy

from rest_framework import permissions

class CustomDjangoModelPermissions(permissions.DjangoModelPermissions):

   def __init__(self):
       self.perms_map = copy.deepcopy(self.perms_map)
       self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']

from rest_framework.permissions import BasePermission

class CanViewOsoba(BasePermission):
   def has_permission(self, request, view):
       return request.user.has_perm('biblioteka.view_osoba')