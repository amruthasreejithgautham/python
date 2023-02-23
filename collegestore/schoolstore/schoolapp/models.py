from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=80)
    dept = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Course(models.Model):
    dept = models.CharField(max_length=80)
    course = models.CharField(max_length=100)

    def __str__(self):
        return str(self.course)

class Register(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=8)

    def __str__(self):
        return str(self.username)