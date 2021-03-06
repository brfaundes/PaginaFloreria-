# Generated by Django 4.0.5 on 2022-06-09 00:30

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre',models.CharField(max_length=40)),
                ('precio',models.IntegerField()),
                ('stock',models.IntegerField()),
                ('descripcion',models.CharField(max_length=150)),
                ('categoria',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Categoria')), 
    
            ],
        )
    ]
