from django.db import models

"""
    - Existem dois jeitos de se trabalhar com user model customizado,
        usando AbstractBaseUser ou AbstractUser

"""

from django.contrib.auth.models import AbstractUser, BaseUserManager # Importando fazer o segundo import

# Classe de gerenciamento de criação de usuário
class UsuarioManager(BaseUserManager):

    # Vai ser colocado no banco para autenticação do usuário, ou seja
    # ele vai estar lá quando for rodado o makemigrations
    use_in_migrations = True

    # Função de criação de usuário
    def _create_user(self, email, password, **extra_fields):

        # Caso o campo de email não seja preenchido, mostrar o ValueError
        if not email:
            raise ValueError('O e-mail é obrigatório')
        
        # faz a correção de e-mail, e formata para o padrão
        email = self.normalize_email(email)

        # Criando o model do usuário
        user = self.model(email=email, username=email, **extra_fields)

        # Criptografa a senha que foi passada pelo usuário 
        user.set_password(password)

        # Salvado os dados
        user.save(using=self._db)

        # Retornado o usuário
        return user
    

    # Função de criação normal de usuário
    def create_ser(self, email, password, **extra_fields):

        # Pros campos extras eu vou colocar o usuário como normal, e não como super
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    # Função de criação de admins
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        # Condição de is_staff
        if extra_fields('is_superuse') is not True:
            raise ValueError('Permissão negada')
        
        return self._create_user(email, password, extra_fields)
    

# Classe de usuário cutomizado
class CustomUsuario(AbstractUser):

    # Colocando o email como único, tipo uma pk
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)

    # Por padrão o custom usuário vai ser como True 
    is_staff = models.BooleanField('Membro da equipe', default=True)

    # O campo padrão de user vai ser o email
    USERNAME_FIELD = 'email'

    # Campos requeridos, não passa o email e senha, por que eles já são pedidos por padrão
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self):
        return self.email
    
    # Os objetos desse model são gerenciados pelo UsuarioManager
    objects = UsuarioManager()