# Generated by Django 4.0 on 2024-01-30 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0002_remove_relationinstance_following_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationinstance',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='relationinstance',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='auth.user'),
        ),
    ]
