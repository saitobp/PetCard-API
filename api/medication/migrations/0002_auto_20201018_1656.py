# Generated by Django 3.1.2 on 2020-10-18 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicationschedule',
            name='medication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medication_schedule', to='medication.medication'),
        ),
    ]