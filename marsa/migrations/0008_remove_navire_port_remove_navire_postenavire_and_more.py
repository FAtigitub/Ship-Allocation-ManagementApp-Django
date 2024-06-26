# Generated by Django 4.2.4 on 2023-08-21 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("marsa", "0007_alter_navire_port_alter_navire_postenavire_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="navire",
            name="port",
        ),
        migrations.RemoveField(
            model_name="navire",
            name="posteNavire",
        ),
        migrations.RemoveField(
            model_name="navire",
            name="quai_de_preference",
        ),
        migrations.RemoveField(
            model_name="navire",
            name="save_by",
        ),
        migrations.RemoveField(
            model_name="port",
            name="save_by",
        ),
        migrations.RemoveField(
            model_name="postenavire",
            name="quai_assigne",
        ),
        migrations.RemoveField(
            model_name="postenavire",
            name="save_by",
        ),
        migrations.RemoveField(
            model_name="quai",
            name="port",
        ),
        migrations.RemoveField(
            model_name="quai",
            name="save_by",
        ),
        migrations.DeleteModel(
            name="Affectation",
        ),
        migrations.DeleteModel(
            name="Navire",
        ),
        migrations.DeleteModel(
            name="Port",
        ),
        migrations.DeleteModel(
            name="PosteNavire",
        ),
        migrations.DeleteModel(
            name="Quai",
        ),
    ]
