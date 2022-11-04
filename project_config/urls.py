"""project_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
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
from django.urls import path, include

urlpatterns = [
    # url for the admin site
    path('admin/', admin.site.urls),

    # urls for user authentication using Django's auth app
    path("accounts/", include(("django.contrib.auth.urls", "auth"), namespace="auth")),

    # urls for local apps
    path("accounts/", include(("accounts_app.urls", "accounts_app"), namespace="accounts_app")), # note same endpoint
                                                                                                 # as for auth app
    path("", include("pages_app.urls")),

]
