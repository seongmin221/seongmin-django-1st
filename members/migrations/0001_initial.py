# Generated by Django 3.1.5 on 2021-01-15 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='사용자')),
                ('useremail', models.EmailField(max_length=128, verbose_name='이메일')),
            ],
            options={
                'db_table': 'blankproject1_users',
            },
        ),
    ]
