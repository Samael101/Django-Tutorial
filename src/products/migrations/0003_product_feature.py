# Generated by Django 4.1.2 on 2022-10-14 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_product_summary"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="feature",
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
