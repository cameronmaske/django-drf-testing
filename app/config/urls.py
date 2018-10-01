"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Example:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from app.journal.urls import router as journal_router

api_urlpatterns_v1 = [
    path("", include((journal_router.urls, "journal"))),
    path("auth/", include("rest_auth.urls")),
    path("registration/", include("rest_auth.registration.urls")),
]

urlpatterns = [
    path("api/", include((api_urlpatterns_v1, "api"))),
    path("admin/", admin.site.urls),
]
