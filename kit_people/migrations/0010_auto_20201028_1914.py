# Generated by Django 3.1.2 on 2020-10-28 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kit_people', '0009_auto_20201025_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='kit_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kit_people.kitperson', verbose_name='kit person'),
        ),
        migrations.AlterField(
            model_name='kitperson',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kit_people.role', verbose_name='role'),
        ),
        migrations.AlterField(
            model_name='role',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
