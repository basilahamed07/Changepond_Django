from django.contrib import admin
from django.urls import path,re_path, include
# from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="book store",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="basilahamed@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
#    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
path('admin/', admin.site.urls),
  path("api/author/",include('author_app.urls')),
  path("api/book/",include('book_app.urls')),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   
]  +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)