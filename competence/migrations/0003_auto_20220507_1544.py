# Generated by Django 3.2.5 on 2022-05-07 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competence', '0002_delete_newmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competencegroup',
            name='competence',
        ),
        migrations.AddField(
            model_name='competencegroup',
            name='competence',
            field=models.ManyToManyField(to='competence.Competence'),
        ),
    ]
