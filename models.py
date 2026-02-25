from django.db import models

# Create your models here.

class User_Accounts(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50,unique=True,primary_key=True)
    password=models.CharField(max_length=50)
    created_by=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_accounts"

    def __str__(self):
        return self.email


