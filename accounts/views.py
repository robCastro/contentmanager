from django.contrib.auth.views import LoginView as DjangoLoginView
from django.urls import reverse

from accounts.forms import AuthenticationForm

# Create your views here.


class LoginView(DjangoLoginView):
    template_name = 'accounts/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

    def get_default_redirect_url(self):
        # TODO: Manejar aquí redirect segun quien inicia sesión
        return reverse('instituciones:home')
