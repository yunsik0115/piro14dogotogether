# Generated by Django 2.2.1 on 2021-02-09 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_placeaddbyuser_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeaddbyuser',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='placeaddbyuser',
            name='category',
            field=models.CharField(blank=True, choices=[('kr', '식당'), ('kr', '카페'), ('kr', '공원')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='placeaddbyuser',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='placeaddbyuser',
            name='created_by',
            field=models.ForeignKey(default='탈퇴한 유저', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
