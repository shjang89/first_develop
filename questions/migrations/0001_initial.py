# Generated by Django 4.2.11 on 2024-04-12 07:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('type', models.CharField(choices=[('M', '객관식'), ('S', '주관식')], max_length=1)),
                ('title', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('m1', models.CharField(blank=True, max_length=300)),
                ('m2', models.CharField(blank=True, max_length=300)),
                ('m3', models.CharField(blank=True, max_length=300)),
                ('m4', models.CharField(blank=True, max_length=300)),
                ('answer_m', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('answer_s', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('e_mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='User_Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_m', models.CharField(blank=True, max_length=10)),
                ('content_s', models.CharField(blank=True, max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='test_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.test_user'),
        ),
    ]