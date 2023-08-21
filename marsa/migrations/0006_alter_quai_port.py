# Generated by Django 4.2.4 on 2023-08-21 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("marsa", "0005_alter_postenavire_quai_assigne_alter_quai_port"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quai",
            name="port",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="marsa.port",
            ),
        ),
    ]