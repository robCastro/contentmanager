from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('content.api.v1.urls'))
]
