# Generated by Django 3.1.1 on 2020-09-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('INACTIVE', 'Inactive'), ('ACTIVE', 'Active')], default='ACTIVE', max_length=10, null=True),
        ),
    ]
