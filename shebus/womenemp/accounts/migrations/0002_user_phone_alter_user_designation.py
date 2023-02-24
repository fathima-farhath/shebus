# Generated by Django 4.1.7 on 2023-02-24 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(choices=[('C', 'Catering'), ('W', 'Women')], default='W', max_length=1),
        ),
    ]
