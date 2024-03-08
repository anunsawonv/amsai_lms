# Generated by Django 5.0.2 on 2024-02-14 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LmsAnnouncement',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=45, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('date_posted', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'lms_announcements',
                'managed': True,
            },
        ),
    ]
