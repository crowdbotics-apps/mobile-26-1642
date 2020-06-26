from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    abc = models.BigIntegerField(null=True, blank=True,)
    abcd = models.DateField(null=True, blank=True,)
    boolean = models.BooleanField(null=True, blank=True,)
    aaa = models.EmailField(max_length=254, null=True, blank=True,)
    aaaa = models.URLField(null=True, blank=True,)
    cccc = models.ForeignKey(
        "home.CustomText",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="homepage_cccc",
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
