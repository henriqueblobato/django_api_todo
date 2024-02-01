from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=1_024, unique=True)
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'[{self.done}] - {self.title}'
