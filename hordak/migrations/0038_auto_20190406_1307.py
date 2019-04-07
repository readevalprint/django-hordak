# Generated by Django 2.0.13 on 2019-04-06 13:07

from django.db import migrations
import django.db.models.deletion
import river.models.fields.state


class Migration(migrations.Migration):

    dependencies = [
        ('hordak', '0037_auto_20190406_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='status',
            field=river.models.fields.state.StateField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rn98698d38458944559da0434ad9dfebe7', to='river.State'),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='status',
            field=river.models.fields.state.StateField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rnaf3db365f99541ad9b685024b3ada1b0', to='river.State'),
        ),
    ]