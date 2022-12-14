# Generated by Django 4.0.4 on 2022-05-28 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0002_docente_curso_docente'),
    ]

    operations = [
        migrations.CreateModel(
            name='sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flial', models.CharField(max_length=20, verbose_name='filial')),
                ('direccion', models.CharField(max_length=50, verbose_name='direccion')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='sede',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academico.sede'),
        ),
    ]
