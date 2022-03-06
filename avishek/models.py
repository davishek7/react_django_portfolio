from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=200, blank=True, null=True)
    details = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(
        default='placeholder.png', upload_to='thumbnails')
    live_url = models.URLField(max_length=200, blank=True, null=True)
    github_repo = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class Contact(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.name} | {self.email}'

    class Meta:
        ordering = ['id']
