# Generated by Django 3.1.7 on 2021-03-29 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('producers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producers',
            name='id',
        ),
        migrations.RemoveField(
            model_name='producers',
            name='name',
        ),
        migrations.RemoveField(
            model_name='producers',
            name='short_description',
        ),
        migrations.AddField(
            model_name='producers',
            name='about',
            field=models.TextField(default='Utilizatorul nu a adaugat descriere', max_length=500),
        ),
        migrations.AlterField(
            model_name='producers',
            name='producer_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
