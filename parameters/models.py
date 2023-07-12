from django.db import models


class Phone(models.Model):
    phone = models.CharField(max_length=60, verbose_name='Telefon')

    def __str__(self):
        return str(self.phone)


class Email(models.Model):
    email = models.EmailField(verbose_name='E-mail')

    def __str__(self):
        return str(self.email)


class Social(models.Model):
    social_name = models.CharField(max_length=60, verbose_name='Şəbəkə adı')
    social_icon = models.CharField(max_length=60, verbose_name='Şəbəkə ikonu')
    social_link = models.URLField(verbose_name='Şəbəkə linki')

    def __str__(self):
        return self.social_name


class Parameters(models.Model):
    address = models.CharField(max_length=250, verbose_name='Ünvan')
    iframe_map = models.CharField(max_length=1500, verbose_name='Google map iframe')
    phone = models.ManyToManyField(Phone, verbose_name='Telefon')
    email = models.ManyToManyField(Email, verbose_name='E-mail')
    social = models.ManyToManyField(Social, verbose_name='Sosial şəbəkə')

    def __str__(self):
        return f"{self.address}"
