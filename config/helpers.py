# drf-yasg - Yet another Swagger generator config (API Documentation)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="UDPlatforms Assignment APIs",
        default_version='v1',
        description="Django Admin Site: http://127.0.0.1:8000/admin/",
   ),
    public=True
)


