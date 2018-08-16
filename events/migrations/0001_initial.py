# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-02 07:29


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_object_id', models.PositiveIntegerField()),
                ('eventid', models.CharField(max_length=32)),
                ('when', models.DateTimeField(db_index=True)),
                ('seq', models.IntegerField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedname', models.CharField(db_index=True, max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('is_default', models.BooleanField(default=False)),
                ('email', models.IntegerField(choices=[(0, b'No Email Updates'), (1, b'Daily'), (2, b'Weekly')], default=0)),
                ('last_event_mailed', models.IntegerField(blank=True, null=True)),
                ('last_email_sent', models.DateTimeField(blank=True, null=True)),
                ('public_id', models.CharField(blank=True, db_index=True, max_length=16, null=True)),
                ('trackers', models.ManyToManyField(related_name='tracked_in_lists', to='events.Feed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_lists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Feed'),
        ),
        migrations.AddField(
            model_name='event',
            name='source_content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterUniqueTogether(
            name='subscriptionlist',
            unique_together=set([('user', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('feed', 'id'), ('feed', 'when', 'source_content_type', 'source_object_id', 'eventid'), ('when', 'source_content_type', 'source_object_id', 'seq', 'feed'), ('source_content_type', 'source_object_id', 'eventid', 'feed')]),
        ),
    ]
