from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
    nickname = models.CharField(max_length=64, unique=True, null=False, blank=False)
    password = models.CharField(max_length=64, null=False, blank=False)
    icon = models.ImageField()
    age = models.IntegerField()
    sex = models.IntegerField()
    perm_id = models.IntegerField()

    def verify_password(self, password):
        return check_password(password, self.password)

    def save(self):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save()


# class Permission(models.Model):
#     '''权限'''
#     name = models.CharField(max_length=64, unique=True, null=False, blank=False)
#     perm = models.IntegerField(default=0)

class Permisson(models.Model):
    role_name = models.CharField()

    @property
    def _role(self):
        if not hasattr(self,'r_name'):
            self.r_name = Role.perm_name
        return self._role

class Role(models.Model):
    perm_name = models.IntegerField()

    @property
    def _perm(self):
        if not hasattr(self,'p_name'):
            self._perm = Permisson.r_name
        return self._perm


