# Generated by Django 2.2 on 2019-04-06 09:18

from django.db import migrations
import django.db.models.deletion
import river.models.fields.state


class Migration(migrations.Migration):

    dependencies = [
        ('river', '0001_initial'),
        ('hordak', '0029_auto_20190406_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='state_field',
        ),
        migrations.RemoveField(
            model_name='withdraw',
            name='state_field',
        ),
        migrations.AddField(
            model_name='deposit',
            name='satus',
            field=river.models.fields.state.StateField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rnaaa933a54c7341b898a7f0c002e16041', to='river.State'),
        ),
        migrations.AddField(
            model_name='withdraw',
            name='status',
            field=river.models.fields.state.StateField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rn585f107de0d34e27ba8f40bfa712376d', to='river.State'),
        ),
    ]
