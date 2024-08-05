# Generated by Django 5.0.2 on 2024-06-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0049_delete_dashboard_sidebar'),
    ]

    operations = [
        migrations.CreateModel(
            name='sidebar_dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=100)),
                ('subdivision', models.CharField(default='', max_length=100)),
            ],
        ),
    ]