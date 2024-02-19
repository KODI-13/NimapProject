from django.db import models

# Create your models here.
class Client(models.Model):
    client_name=models.CharField(max_length=200,null=True)
    uniqueid=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    project_name=models.CharField(max_length=200,null=True)
    created_at=models.DateTimeField(null=True)
    created_by=models.CharField(max_length=200,null=True)
    assigned_user=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=200,null=True)
    updated_at=models.DateTimeField(null=True)


class User(models.Model):
    name=models.CharField(max_length=200)


