# Generated by Django 5.0.4 on 2024-05-13 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cores',
            options={'ordering': ['cor'], 'verbose_name': 'Cor', 'verbose_name_plural': 'Cores'},
        ),
        migrations.AlterModelOptions(
            name='produtos',
            options={'ordering': ['-produto'], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
    ]
