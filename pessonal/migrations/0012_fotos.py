# Generated by Django 3.1.1 on 2021-01-31 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pessonal', '0011_auto_20210101_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='fotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='corpo/')),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
