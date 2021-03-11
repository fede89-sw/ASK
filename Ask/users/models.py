from  django.contrib.auth.models import AbstractUser
# Create your models here.

# DOCUMENTAZIONE CUSTOM USER :
# https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#substituting-a-custom-user-model

# creo CustomUser per possibità di modifiche ai campi in futuro
class CustomUser(AbstractUser):
    pass