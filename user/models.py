from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # 여기 staff가 User로 기본 제공되는 사람이랑 연관돼 있는것 같은데 확실히 모르겠음
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(default='avatar.PNG', upload_to='Profile_Images')

    def __str__(self):
        return f'{self.staff.username}-Profile'