# Generated by Django 5.0.6 on 2024-06-06 03:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0002_alter_cores_options_alter_produtos_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.FloatField(default=0, verbose_name='Preço')),
                ('quantidade', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produtos', verbose_name='Produto')),
            ],
        ),
    ]
