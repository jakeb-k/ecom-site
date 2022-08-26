# Generated by Django 4.0.5 on 2022-07-04 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_options_productcustomfield_option1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcustomfield',
            name='option1',
        ),
        migrations.RemoveField(
            model_name='productcustomfield',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='productcustomfield',
            name='option3',
        ),
        migrations.RemoveField(
            model_name='productcustomfield',
            name='option4',
        ),
        migrations.RemoveField(
            model_name='productcustomfield',
            name='option5',
        ),
        migrations.RemoveField(
            model_name='productcustomfield',
            name='option6',
        ),
        migrations.AddField(
            model_name='productcustomfield',
            name='options',
            field=models.CharField(blank=True, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], max_length=500),
        ),
    ]