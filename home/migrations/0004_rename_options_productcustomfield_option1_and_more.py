# Generated by Django 4.0.5 on 2022-06-30 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product_snipcartsettings_productcustomfield'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcustomfield',
            old_name='options',
            new_name='option1',
        ),
        migrations.AddField(
            model_name='productcustomfield',
            name='option2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productcustomfield',
            name='option3',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productcustomfield',
            name='option4',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productcustomfield',
            name='option5',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='productcustomfield',
            name='option6',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
