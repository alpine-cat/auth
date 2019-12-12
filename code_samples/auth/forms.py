from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


class MyAuthForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass


class MyLoginView(LoginView):
    pass