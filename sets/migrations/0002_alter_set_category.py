# Generated by Django 4.0.3 on 2022-03-19 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='category',
            field=models.CharField(choices=[('warmup', 'Warm-Up'), ('set', 'Set'), ('cooldown', 'Cool-Down')], default='set', max_length=20),
        ),
    ]
