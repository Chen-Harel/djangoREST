# Generated by Django 4.0.5 on 2022-06-13 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_loan_id_loan__id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='_id',
        ),
        migrations.AddField(
            model_name='loan',
            name='id',
            field=models.BigAutoField(auto_created=True, default='1', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
