# Generated by Django 4.2.4 on 2023-08-21 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('static_app', '0002_alter_memberbadge_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='badge_image',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='badge',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='static_app.category'),
            preserve_default=False,
        ),
    ]