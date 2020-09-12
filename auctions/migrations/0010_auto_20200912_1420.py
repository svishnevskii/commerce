# Generated by Django 3.1 on 2020-09-12 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20200911_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorylisting',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='auctions.category'),
        ),
        migrations.AlterField(
            model_name='categorylisting',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relation', to='auctions.listing'),
        ),
    ]
