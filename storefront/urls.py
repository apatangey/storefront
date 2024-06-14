
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from userbox import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='userbox/login.html'), name='login'),
    path("logout/", user_views.logout_view, name="logout"),
    path('', include("sandbox.urls")) # path left empty to set blog as homepage 
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)