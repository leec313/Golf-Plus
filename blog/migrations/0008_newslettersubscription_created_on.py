# Generated by Django 3.2.22 on 2023-10-20 19:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20231020_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslettersubscription',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]