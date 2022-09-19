# Generated by Django 4.1.1 on 2022-09-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0007_alter_book_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='checked',
            field=models.CharField(blank=True, choices=[('no', 'None')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Available'), ('n', 'No available')], max_length=200, null=True),
        ),
    ]