# Generated by Django 3.0.7 on 2021-01-31 16:14

import bookwyrm.models.activitypub_mixin
import bookwyrm.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookwyrm', '0040_auto_20210122_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('remote_id', bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id])),
                ('name', bookwyrm.models.fields.CharField(max_length=100)),
                ('description', bookwyrm.models.fields.TextField(blank=True, null=True)),
                ('privacy', bookwyrm.models.fields.CharField(choices=[('public', 'Public'), ('unlisted', 'Unlisted'), ('followers', 'Followers'), ('direct', 'Direct')], default='public', max_length=255)),
                ('curation', bookwyrm.models.fields.CharField(choices=[('closed', 'Closed'), ('open', 'Open'), ('curated', 'Curated')], default='closed', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(bookwyrm.models.activitypub_mixin.OrderedCollectionMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('remote_id', bookwyrm.models.fields.RemoteIdField(max_length=255, null=True, validators=[bookwyrm.models.fields.validate_remote_id])),
                ('notes', bookwyrm.models.fields.TextField(blank=True, null=True)),
                ('approved', models.BooleanField(default=True)),
                ('order', bookwyrm.models.fields.IntegerField(blank=True, null=True)),
                ('added_by', bookwyrm.models.fields.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('book', bookwyrm.models.fields.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bookwyrm.Edition')),
                ('book_list', bookwyrm.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookwyrm.List')),
                ('endorsement', models.ManyToManyField(related_name='endorsers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_date',),
                'unique_together': {('book', 'book_list')},
            },
            bases=(bookwyrm.models.activitypub_mixin.ActivitypubMixin, models.Model),
        ),
        migrations.AddField(
            model_name='list',
            name='books',
            field=models.ManyToManyField(through='bookwyrm.ListItem', to='bookwyrm.Edition'),
        ),
        migrations.AddField(
            model_name='list',
            name='user',
            field=bookwyrm.models.fields.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
