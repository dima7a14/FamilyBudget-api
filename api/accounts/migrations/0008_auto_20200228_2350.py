# Generated by Django 3.0.3 on 2020-02-28 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200225_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Category'),
        ),
    ]