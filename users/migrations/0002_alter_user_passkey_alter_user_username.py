# Generated by Django 4.1.6 on 2023-02-21 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='passkey',
            field=models.CharField(default='As0XoxgeYa', editable=False, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='Full Name'),
        ),
    ]
