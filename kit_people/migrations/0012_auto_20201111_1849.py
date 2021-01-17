# Generated by Django 3.1.2 on 2020-11-11 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kit_people', '0011_auto_20201106_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitperson',
            name='regularity',
        ),
        migrations.AddField(
            model_name='regularity',
            name='kit_person',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='kit_people.kitperson', verbose_name='kit person'),
        ),
    ]
