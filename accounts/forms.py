from django import forms
from django.contrib.auth.forms import AuthenticationForm as DjangoAuthenticationForm, UsernameField
from django.contrib.auth.base_user import AbstractBaseUser


class AuthenticationForm(DjangoAuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def confirm_login_allowed(self, user: AbstractBaseUser) -> None:
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``ValidationError``.

        If the given user may log in, this method should return None.
        """
        # TODO controlar aquí de donde se hace el login, si institucion o administrativo
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages["inactive"],
                code="inactive",
            )
