# Generated by Django 4.1 on 2022-10-28 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0003_alter_umkm_shop_shop_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='umkm_shop',
            name='owner',
        ),
    ]