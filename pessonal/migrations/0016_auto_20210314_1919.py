# Generated by Django 3.1.1 on 2021-03-14 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessonal', '0015_musculos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercicio',
            name='musclulo_primario',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='exercicio',
            name='musculos_secundarios',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
