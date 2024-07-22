# Generated by Django 4.0.4 on 2022-05-13 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('category', models.CharField(choices=[('Computer', 'Computer'), ('Accessories', 'Acessories'), ('Printer', 'Printer'), ('Health', 'Health'), ('Web Apps', 'Web Apps'), ('Mobile Apps', 'Mobile Apps'), ('Desktop Apps', 'Desktop Apps'), ('Website', 'Website'), ('Graphic Design', 'Graphic Design'), ('Others', 'Others')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=500, null=True)),
                ('project_no', models.CharField(max_length=20, null=True)),
                ('client_name', models.CharField(max_length=500, null=True)),
                ('project_category', models.CharField(choices=[('Computer', 'Computer'), ('Accessories', 'Acessories'), ('Printer', 'Printer'), ('Health', 'Health'), ('Web Apps', 'Web Apps'), ('Mobile Apps', 'Mobile Apps'), ('Desktop Apps', 'Desktop Apps'), ('Website', 'Website'), ('Graphic Design', 'Graphic Design'), ('Others', 'Others')], max_length=100, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('team_lead', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_quantity', models.PositiveIntegerField(null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.product')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_purchase', models.IntegerField(default=0, null=True)),
                ('total_paid', models.IntegerField(default=0, null=True)),
                ('total_balance', models.IntegerField(default=0, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
