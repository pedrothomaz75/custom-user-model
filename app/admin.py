from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsuarioCreationForm, CustomUsuarioChangeForm 
from .models import CustomUsuario

@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreationForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')

    # Dados de cadastro do usuário
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantres', {'fields': ('last_login', 'date_joined')}),
    ) 