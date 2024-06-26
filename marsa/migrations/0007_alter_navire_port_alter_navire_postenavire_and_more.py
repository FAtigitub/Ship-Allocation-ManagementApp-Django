# Generated by Django 4.2.4 on 2023-08-21 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("marsa", "0006_alter_quai_port"),
    ]

    operations = [
        migrations.AlterField(
            model_name="navire",
            name="port",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="marsa.port"
            ),
        ),
        migrations.AlterField(
            model_name="navire",
            name="posteNavire",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="marsa.postenavire"
            ),
        ),
        migrations.AlterField(
            model_name="navire",
            name="quai_de_preference",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="marsa.quai"
            ),
        ),
        migrations.AlterField(
            model_name="postenavire",
            name="quai_assigne",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="marsa.quai"
            ),
        ),
        migrations.AlterField(
            model_name="quai",
            name="port",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                to="marsa.port",
            ),
        ),
    ]
