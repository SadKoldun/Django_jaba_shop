# Generated by Django 5.0.1 on 2024-03-07 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_product_rate_alter_comment_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_timestamp'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
