# Generated by Django 5.1.4 on 2024-12-20 17:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_enrollment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment', to='courses.course', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Inscrição Pendente'), (1, 'Inscrição Aprovada'), (2, 'Inscrição Cancelada')], default=1, verbose_name='Situação'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollment', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
