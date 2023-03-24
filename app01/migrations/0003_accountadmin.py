# Generated by Django 4.1.7 on 2023-02-21 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_alter_userinfo_depart_alter_userinfo_entry_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, verbose_name='Mobile')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Price')),
                ('level', models.SmallIntegerField(choices=[(1, 'Used'), (2, 'Used With Good Condition'), (3, 'Like New'), (4, 'Brand New')], verbose_name='Level')),
                ('status', models.SmallIntegerField(choices=[(1, 'Occupied'), (2, 'Available')], default=2, verbose_name='Status')),
            ],
        ),
    ]
