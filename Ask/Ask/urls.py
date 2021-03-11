"""Ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django_registration.backends.one_step.views import RegistrationView
from django.urls import include, path, re_path
from users.forms import CustomRegistrationForm
from utils.views import IndexRender

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/register/',
        RegistrationView.as_view(
            form_class=CustomRegistrationForm,
            success_url="/"
        ),
        name='django_registration_register',
    ),

    # altri URL forniti da Django Registration
    path('accounts/', include('django_registration.backends.one_step.urls')),

    # URL per il LOGIN, fornito da Django
    path('accounts/', include('django.contrib.auth.urls')),

    # Login con BrowsableAPI
    path('api-auth/', include('rest_framework.urls')),

    # Login tramite REST API (con rest-auth)
    path('api/rest-auth/', include('rest_auth.urls')), 
    
    # endpoint di registrazione tramite REST API (con rest-auth)
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),

    # app 'question' urls
    path('api/', include('question.api.urls')),

    # app 'users' urls
    path('api/', include('users.api.urls')),

    # SPA
    re_path(r'^.*$', IndexRender.as_view(), name="single-page")
]