from django.contrib import admin
from django.urls import include, path

from logistic.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('logistic.urls')),
    path('api/v1/test/', health_check)
]
