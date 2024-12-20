# Generated by Django 5.1.4 on 2024-12-14 15:15

import django.core.validators
import re
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_options_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+\\Z'), 'O nome do usuário somente pode conter letras, números ou @/./+/-/_', 'invalid')], verbose_name='Nome de Usuário'),
        ),
    ]
