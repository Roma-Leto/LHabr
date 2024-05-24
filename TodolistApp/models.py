from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=255)
    datetime_create = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    owner = models.ForeignKey('TaskUsers', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class TaskUsers(models.Model):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.login

    # TODO: Прикрутить к приложению todo приложение генерации паролей.
