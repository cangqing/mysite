# Generated by Django 2.1.1 on 2018-10-08 07:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_consult'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAppraise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_logo', models.ImageField(upload_to='customers')),
                ('customer_appraise', models.CharField(max_length=2000, verbose_name='评价')),
                ('appraise_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='评价时间')),
            ],
        ),
    ]