from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/v1/auth', include('user_authentication.urls')),
    path('api/v1/analyse', include('analytics.urls')),
    path('api/v1/feedbacks', include('feedbacks.urls')),
    path('api/v1/pricings', include('pricing_manager.urls'))
]
