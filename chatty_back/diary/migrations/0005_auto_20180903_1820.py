# Generated by Django 2.0.8 on 2018-09-03 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_auto_20180831_1735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_answer',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='single_diary',
            name='weather',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
