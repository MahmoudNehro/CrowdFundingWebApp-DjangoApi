# Generated by Django 4.0.4 on 2022-05-15 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_projects_end_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replies',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='projects.comments'),
        ),
    ]
