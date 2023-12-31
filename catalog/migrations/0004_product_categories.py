# Generated by Django 4.2.4 on 2023-10-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0003_product_alter_productclass_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="categories",
            field=models.ManyToManyField(
                related_name="categories", to="catalog.category"
            ),
        ),
    ]
