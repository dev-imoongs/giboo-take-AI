# Generated by Django 4.2.4 on 2023-08-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neulhaerang_review', '0003_alter_fundusagehistory_neulhaerang_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neulhaerangreview',
            name='thumbnail_image',
            field=models.ImageField(upload_to='neulhaerang_review/thumbnail/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='reviewinnerphotos',
            name='inner_photo',
            field=models.ImageField(upload_to='neulhaerang_review/innerphoto/%Y/%m/%d'),
        ),
    ]