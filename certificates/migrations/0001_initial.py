# Generated by Django 4.0 on 2023-07-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/certificates/%Y/%m/%d/', verbose_name='Sertifikat şəkli')),
            ],
        ),
    ]
