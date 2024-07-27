# Generated by Django 5.0 on 2024-07-21 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.CreateModel(
            name='Student1',
            fields=[
                ('contactinfo1_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.contactinfo1')),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
            ],
            bases=('testapp.contactinfo1',),
        ),
        migrations.CreateModel(
            name='Teacher1',
            fields=[
                ('contactinfo1_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.contactinfo1')),
                ('subject', models.CharField(max_length=30)),
                ('salary', models.FloatField()),
            ],
            bases=('testapp.contactinfo1',),
        ),
    ]
