from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import AbstractUser

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, national_id, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number field must be set')
        if not national_id:
            raise ValueError('The National ID field must be set')
        
        user = self.model(phone_number=phone_number, national_id=national_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, national_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, national_id, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=10, unique=True, editable=False)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    national_id = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

#chatgpt
    is_occupant = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    has_chosen_initial_role = models.BooleanField(default=False)  # New field
    current_role = models.CharField(
        max_length=10,
        choices=[('owner', 'Owner'), ('occupant', 'Occupant')],
        null=True,
        blank=True
        )

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['national_id', 'name', 'date_of_birth']

    def save(self, *args, **kwargs):
        if not self.user_id:
            # Generate a unique user ID (you can customize this logic)
            last_user = CustomUser.objects.order_by('-id').first()
            if last_user:
                last_id = int(last_user.user_id[3:])
                new_id = f"USR{last_id + 1:06d}"
            else:
                new_id = "USR000001"
            self.user_id = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
