from django.http import FileResponse
from rest_framework import viewsets
from content.api.v1.permissions import ArchivoPermission
from content.api.v1.serializers import ArchivoSerializer
from content.models import Archivo
from rest_framework.decorators import action


class ArchivoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer
    permission_classes = [ArchivoPermission,]

    # https://stackoverflow.com/questions/38697529/how-to-return-generated-file-download-with-django-rest-framework
    @action(methods=['get'], detail=True)
    def download(self, *args, **kwargs):
        instance: Archivo = self.get_object()
        file_handle = instance.file.open()
        response = FileResponse(file_handle)
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
        return response
