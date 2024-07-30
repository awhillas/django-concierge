# Generated by Django 5.0.7 on 2024-07-30 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('user_agent', models.CharField(max_length=255, null=True)),
                ('referrer', models.CharField(max_length=255, null=True)),
                ('screen_width', models.PositiveIntegerField(default=0)),
                ('screen_height', models.PositiveIntegerField(default=0)),
                ('user_agent_family', models.CharField(max_length=50, null=True)),
                ('user_agent_major', models.CharField(max_length=10, null=True)),
                ('user_agent_minor', models.CharField(max_length=10, null=True)),
                ('os_family', models.CharField(max_length=50, null=True)),
                ('os_major', models.CharField(max_length=10, null=True)),
                ('device_family', models.CharField(max_length=50, null=True)),
                ('device_brand', models.CharField(max_length=50, null=True)),
                ('device_model', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
