from django_registration.forms import RegistrationForm
from .models import CustomUser


# MODIFICO RegistrationForm PER IL MIO CUSTOMUSER,IN QUANTO DI DEFAULT SI BASA SU User
class CustomRegistrationForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomUser