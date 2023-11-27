from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework import routers
from filmyweb.views import UserViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('filmyweb.urls')),
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name ='logout'),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

