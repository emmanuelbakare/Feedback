# Generated by Django 3.2.5 on 2022-05-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competence', '0004_rename_competencegroup_bundle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bundle',
            name='competence',
        ),
        migrations.AddField(
            model_name='competence',
            name='bundles',
            field=models.ManyToManyField(to='competence.Bundle'),
        ),
    ]