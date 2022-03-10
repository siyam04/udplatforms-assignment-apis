from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

# drf-yasg (API Documentation)
from .helpers import schema_view

# App router
from parent_child.urls import parent_child_router


# Main urls mapping
urlpatterns = [

    # django admin panel
    path('admin/', admin.site.urls),

    # root (API Documentation)
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # apps
    path('api/', include(parent_child_router.urls)),
    path('api/', include('parent_child.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


