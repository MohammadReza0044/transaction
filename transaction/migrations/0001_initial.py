# Generated by Django 4.0.4 on 2022-05-31 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_code', models.IntegerField()),
                ('branch_code', models.CharField(choices=[('branch_1000', 'branch_1000'), ('branch_1001', 'branch_1001'), ('branch_1002', 'branch_1002')], max_length=20)),
                ('transaction', models.IntegerField()),
            ],
        ),
    ]
