# Generated by Django 4.0.5 on 2022-06-19 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hood',
            fields=[
                ('hood_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('occupants', models.IntegerField()),
                ('police_station_address', models.EmailField(max_length=50)),
                ('police_station_name', models.CharField(max_length=50)),
                ('health_care_address', models.EmailField(max_length=50)),
                ('health_care_name', models.CharField(max_length=50)),
                ('posts', models.ImageField(upload_to='posts/')),
                ('description', models.TextField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.admin')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('post', models.TextField()),
                ('image', models.ImageField(upload_to='posts/')),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.hood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.user')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.admin')),
                ('hood_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.hood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.user')),
            ],
        ),
    ]