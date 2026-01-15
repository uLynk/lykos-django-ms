from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/reviews/', include('core.urls')), 
    path('api/reviews/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/reviews/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]