# Generated by Django 3.1.6 on 2021-04-17 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='status',
            field=models.CharField(choices=[('draft', 'Taslak'), ('published', 'Yayinlandi'), ('deleted', 'Silindi')], default='draft', max_length=10),
        ),
    ]
