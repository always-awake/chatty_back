# Generated by Django 2.0.8 on 2018-08-22 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChattyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, null=True)),
                ('unique_user_id', models.CharField(max_length=40, null=True)),
            ],
        ),
    ]