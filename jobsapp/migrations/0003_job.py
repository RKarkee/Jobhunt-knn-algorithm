# Generated by Django 2.2.4 on 2019-08-12 17:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=300)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=150)),
                ('type', models.CharField(choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')], max_length=10)),
                ('category', models.CharField(default='', max_length=100)),
                ('last_date', models.DateTimeField()),
                ('skillRequired1', models.CharField(default='', max_length=100)),
                ('skillRequired2', models.CharField(default='', max_length=100)),
                ('skillRequired3', models.CharField(blank=True, max_length=100, null=True)),
                ('skillRequired4', models.CharField(blank=True, max_length=100, null=True)),
                ('work_experience', models.IntegerField(default=0)),
                ('company_name', models.CharField(max_length=100)),
                ('company_description', models.CharField(max_length=300)),
                ('website', models.CharField(default='', max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('filled', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobsapp.User')),
            ],
        ),
    ]