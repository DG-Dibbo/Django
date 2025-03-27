from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name='homepage'),
    path('category/<slug:category_slug>', views.homepage,name='category_wise_slug'),
    path('author/', include('author.urls')),
    path('category/', include('categories.urls')),
    path('post/', include('posts.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)