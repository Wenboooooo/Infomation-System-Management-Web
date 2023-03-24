# Generated by Django 4.1.7 on 2023-02-27 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.admin', verbose_name='principal'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.CharField(max_length=64, verbose_name='OrderNumber')),
                ('title', models.CharField(max_length=32, verbose_name='Title')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('status', models.SmallIntegerField(choices=[(1, 'Pending'), (2, 'Finished')], default=1, verbose_name='Status')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.admin', verbose_name='Administrator')),
            ],
        ),
    ]
