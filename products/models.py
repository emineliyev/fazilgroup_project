# from django.db import models
# from django.utils import timezone
#
#
# class Product(models.Model):
#     class Status(models.Model):
#         choices = None
#         DRAFT = 'DF', 'Deaktiv'
#         PUBLISH = 'PB', 'Aktiv'
#
#     product_name = models.CharField(max_length=250, verbose_name='Məhsulun adı')
#     # category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Məhsulun kateqoriyası')
#     slag = models.SlugField(max_length=250, verbose_name='Məhsulun slaqı')
#     description = models.TextField(verbose_name='Açıqlama')
#     packaging = models.CharField(max_length=250, verbose_name='Qablaşdırma')
#     consumption = models.CharField(max_length=250, verbose_name='Sərfiyyat')
#     image = models.ImageField(upload_to="image/product/%Y/%m/%d/", null=True, blank=True, verbose_name='Şəkil')
#     status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
#     publish = models.DateTimeField(default=timezone.now, verbose_name='Yerləçdirmə tarixi')
#     created = models.DateTimeField(auto_now_add=True, verbose_name='Yaranma tarixi')
#     update = models.DateTimeField(auto_now=True, verbose_name='Yenilənmə tarixi')
#
#     def __str__(self):
#         return f"{self.product_name}"
#
#     class Meta:
#         ordering = ['-publish']
#         indexes = [
#             models.Index(fields=['-publish'])
#         ]