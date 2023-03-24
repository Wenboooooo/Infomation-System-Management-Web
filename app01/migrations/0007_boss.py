# Generated by Django 4.1.7 on 2023-02-28 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_alter_task_user_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='name')),
                ('age', models.IntegerField(verbose_name='age')),
                ('img', models.CharField(max_length=128, verbose_name='photo')),
            ],
        ),
    ]
