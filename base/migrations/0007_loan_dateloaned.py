# Generated by Django 4.0.5 on 2022-06-14 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_user_loan_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='dateLoaned',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
