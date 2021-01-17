# Generated by Django 3.1 on 2020-09-05 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('link', models.URLField(verbose_name='link')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.section', verbose_name='section')),
            ],
        ),
    ]