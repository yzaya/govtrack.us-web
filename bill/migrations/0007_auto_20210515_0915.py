# Generated by Django 2.1.7 on 2021-05-15 09:15

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0006_auto_20200316_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='statement_admin_policy',
            field=jsonfield.fields.JSONField(blank=True, default=[], help_text='Statement of Administration Policy metadata', null=True),
        ),
    ]