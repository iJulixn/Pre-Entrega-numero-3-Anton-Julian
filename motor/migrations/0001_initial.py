# Generated by Django 5.1.3 on 2024-12-09 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='motori4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cilindrada', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=50)),
                ('año', models.IntegerField()),
                ('potencia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='motorv6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cilindrada', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=50)),
                ('año', models.IntegerField()),
                ('potencia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='motorv8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cilindrada', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=50)),
                ('año', models.IntegerField()),
                ('potencia', models.IntegerField()),
            ],
        ),
    ]