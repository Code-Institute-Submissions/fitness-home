# Generated by Django 3.1 on 2020-08-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NutritionPlans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('purpose', models.CharField(max_length=120)),
                ('meal_plan', models.CharField(max_length=120)),
                ('grocery_list', models.CharField(max_length=120)),
                ('message', models.CharField(max_length=120)),
                ('coaching', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
