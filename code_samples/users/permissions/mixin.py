from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    raise_exception = True

class SomeView(UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.id_staff

        