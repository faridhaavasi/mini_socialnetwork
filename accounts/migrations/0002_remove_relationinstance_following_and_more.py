# Generated by Django 4.0 on 2024-01-29 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationinstance',
            name='following',
        ),
        migrations.AddField(
            model_name='relationinstance',
            name='from_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='auth.user'),
            preserve_default=False,
        ),
    ]