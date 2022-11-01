# Generated by Django 4.1 on 2022-10-28 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('showcase', '0006_alter_umkm_shop_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='umkm_shop',
            name='owner',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
