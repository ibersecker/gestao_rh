# Generated by Django 2.2.7 on 2019-11-10 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BancoHoras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(help_text='Nome do Banco de horas', max_length=70)),
            ],
        ),
    ]