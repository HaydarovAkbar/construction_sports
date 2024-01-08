# Generated by Django 4.2.7 on 2024-01-08 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_constructiontype_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seasonstat',
            name='construction_type',
        ),
        migrations.AddField(
            model_name='seasonstat',
            name='basis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.basis'),
        ),
    ]