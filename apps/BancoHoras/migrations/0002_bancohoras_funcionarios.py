# Generated by Django 2.2.7 on 2019-11-10 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionarios', '0001_initial'),
        ('BancoHoras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bancohoras',
            name='Funcionarios',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Funcionarios.Funcionarios'),
            preserve_default=False,
        ),
    ]