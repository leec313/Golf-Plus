# Generated by Django 3.2.22 on 2023-10-20 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20231020_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsletterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='NewsletterSubscription',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='email',
            field=models.ManyToManyField(to='blog.NewsletterUser'),
        ),
    ]
