from django.contrib import admin
from django.urls import path
from users.views import SignupView, SigninView, MeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignupView.as_view()),
    path('signin/', SigninView.as_view()), 
    path('me/', MeView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)