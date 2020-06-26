from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    ip = models.GenericIPAddressField(
        protocol="both", unpack_ipv4=False, null=True, blank=True,
    )
    positv = models.PositiveSmallIntegerField(null=True, blank=True,)
    slug = models.SlugField(max_length=50, null=True, blank=True,)
    uuid = models.UUIDField(null=True, blank=True,)
    flot = models.FloatField(null=True, blank=True,)
    date = models.DateTimeField(null=True, blank=True,)

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
    aaa = models.EmailField(null=True, blank=True, max_length=254,)
    aaaa = models.URLField(null=True, blank=True,)
    cccc = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="homepage_cccc",
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
