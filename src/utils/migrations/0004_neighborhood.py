# Generated by Django 4.2.7 on 2023-12-28 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0003_district_erp_id_district_soato_code_region_erp_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('attr', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('erp_id', models.PositiveIntegerField(blank=True, null=True)),
                ('soato_code', models.PositiveIntegerField(blank=True, null=True)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='neighborhoods', to='utils.district')),
            ],
            options={
                'verbose_name': 'Neighborhood',
                'verbose_name_plural': 'Neighborhoods',
                'db_table': 'neighborhoods',
            },
        ),
    ]
