# Generated by Django 4.2.4 on 2023-08-29 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=4, primary_key=True, serialize=False),
        ),
    ]