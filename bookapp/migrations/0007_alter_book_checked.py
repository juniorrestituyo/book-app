# Generated by Django 4.1.1 on 2022-09-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0006_book_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='checked',
            field=models.CharField(choices=[('no', 'None')], max_length=200),
        ),
    ]