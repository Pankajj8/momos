# Generated by Django 2.2.4 on 2019-09-19 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20190918_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('Mid', models.AutoField(primary_key=True, serialize=False)),
                ('sender_username', models.CharField(max_length=3000)),
                ('receiver_username', models.CharField(max_length=3000)),
                ('content', models.CharField(max_length=45000)),
            ],
            options={
                'db_table': 'message',
            },
        ),
    ]