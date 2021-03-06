# Generated by Django 2.2 on 2019-04-06 09:33

from django.db import migrations
import django.db.models.deletion
import river.models.fields.state


class Migration(migrations.Migration):

    dependencies = [
        ('hordak', '0034_auto_20190406_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='status',
            field=river.models.fields.state.StateField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rn93c9d58bd59b4d90840681b49130628c', to='river.State'),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='status',
            field=river.models.fields.state.StateField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rncea4095e13d04b25bdaece6ca0b297c0', to='river.State'),
        ),
    ]
