from django.contrib.auth.base_user import BaseUserManager


class SmsUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(username, password, **extra_fields)
    
    def create_teacher(self,username,password,**extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_teacher", True)
        return self.create_user(username, password, **extra_fields)
    
    def create_student(self,username,password,**extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_student", True)
        return self.create_user(username, password, **extra_fields)
    