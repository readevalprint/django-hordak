# Generated by Django 2.2 on 2019-04-06 09:22

from django.db import migrations
import django.db.models.deletion
import river.models.fields.state


class Migration(migrations.Migration):

    dependencies = [
        ('river', '0001_initial'),
        ('hordak', '0030_auto_20190406_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='satus',
        ),
        migrations.AddField(
            model_name='deposit',
            name='status',
            field=river.models.fields.state.StateField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rn765952cee0f048ceae937cddde467edf', to='river.State'),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='status',
            field=river.models.fields.state.StateField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rn8d1e508a53764b3497f55123bb75c249', to='river.State'),
        ),
    ]
