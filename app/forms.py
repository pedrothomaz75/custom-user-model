from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUsuario

class CustomUsuarioCreationForm(UserCreationForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')
        labels = {'username': 'Username/E-mail'}
    
    def save(self, commit=True):
        # Guarda os dados do usuário antes de mandar direto pro banco
        user = super().save(commit=False)
        # Pega a senha e não a repetição dela
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['username']
        if commit:
            user.save()
        return user
    

class CustomUsuarioChangeForm(UserChangeForm):
    
    class Meta:
            model = CustomUsuario
            fields = ('first_name', 'last_name', 'fone')
            