
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import crud.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud.views.home, name="home"),
    path('crud/<int:blog_id>/', crud.views.detail, name="detail"),
    path('crud/new/', crud.views.create, name='new'),
    path('crud/gallery/', crud.views.gallery, name="gallery"),
    path('update/<int:pk>', crud.views.update, name='update'),
    path('delete/<int:pk>', crud.views.delete, name="delete"),
    path('account/', include('account.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
