# Generated by Django 4.1.4 on 2022-12-21 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_relations_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relations',
            name='materials',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.materials'),
        ),
    ]