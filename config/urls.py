from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

# importing app routers
from parent_child.urls import parent_child_router


# swagger config (API Documentation)
# schema_view = get_swagger_view(title='UDPlatforms Coding Assignment API Documentation')

# main routes mapping
urlpatterns = [

    # django admin panel
    path('admin/', admin.site.urls),

    # home
    # path('', schema_view),
    path('', include_docs_urls(title='UDPlatforms Assignment API Documentation')),

    # DRF config
    # path('api-auth/', include('rest_framework.urls')),

    # app
    path('api/', include(parent_child_router.urls)),
    path('api/', include('parent_child.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


