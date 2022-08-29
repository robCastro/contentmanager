from rest_framework.request import Request
from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet
from content.models import Archivo


class ArchivoPermission(permissions.BasePermission):

    def has_permission(self, request: Request, view: ReadOnlyModelViewSet) -> bool:
        return True

    def has_object_permission(self, request: Request, view: ReadOnlyModelViewSet, obj: Archivo) -> bool:
        if view.action == 'download' and obj.validar_api_key:
            api_key = request.query_params.get('api_key', None)
            return obj.sistemas.filter(api_key=api_key).exists()
        return True