
from django.contrib import admin
from django.urls import path, include
import functionapp.urls
import functionapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', functionapp.views.welcome, name="welcome"),
    path('funccrud/', include(functionapp.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
