from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsuarioCreationForm, CustomUsuarioChangeForm 
from .models import CustomUsuario

@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):

    # Formulário de cadastro
    add_form = CustomUsuarioCreationForm

    # Formulário de alteração
    form = CustomUsuarioChangeForm

    # Usando o CustomUsuario
    model = CustomUsuario

    # Vai ser mostrar no 127.0.0.1/admin
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')

    # Dados de cadastro do usuário
    fieldsets = (

        # Usuário e senha
        (None, {'fields': ('email', 'password')}),

        # admin page
        ('Informações pessoais', {'fields': ('first_name', 'last_name', 'fone')}),

        # admin page
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),

        #admin page
        ('Datas importantres', {'fields': ('last_login', 'date_joined')}),
    ) 