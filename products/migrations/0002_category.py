# Generated by Django 5.1.1 on 2024-09-20 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
                "db_table": "category",
                "ordering": ["pk"],
                "permissions": [
                    ["autorizar_category", "Puede Autorizar Categorias"],
                    ["viewcrud_category", "Puede Visualizar Categorias en el menú"],
                ],
            },
        ),
    ]
