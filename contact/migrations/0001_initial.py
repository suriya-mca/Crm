# Generated by Django 5.0.6 on 2024-05-30 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('category', models.CharField(choices=[('customer', 'Customer'), ('prospect', 'Prospect')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CommunicationLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('email', 'Email'), ('call', 'Call'), ('meeting', 'Meeting')], max_length=10)),
                ('notes', models.TextField()),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='contact.contact')),
            ],
        ),
    ]