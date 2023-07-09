from django.db import models


class Certificate(models.Model):
    image = models.ImageField(upload_to="image/certificates/%Y/%m/%d/", null=True, blank=True,
                              verbose_name='Sertifikat şəkli')
