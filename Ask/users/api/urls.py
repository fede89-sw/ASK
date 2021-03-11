from django.urls import path
from .views import LoggedUsername

urlpatterns = [
    path('user/', LoggedUsername.as_view(), name="current-user")
]