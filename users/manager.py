from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User should contain a email")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    # Required to create the super user through the cmd
    def create_superuser(self, email, password, auth_type):
        user = self.create_user(email, password=password)
        user.auth_type = auth_type
        user.is_staff = True
        user.save(using=self._db)
        return user
