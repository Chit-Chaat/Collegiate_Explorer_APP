from django.db import models


class Task(models.Model):
    title = models.CharField('title', max_length=100)
    description = models.TextField('description')

    def __unicode__(self):
        return self.title
