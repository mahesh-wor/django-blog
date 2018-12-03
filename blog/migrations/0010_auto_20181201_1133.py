# Generated by Django 2.1.3 on 2018-12-01 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post1',
            name='author',
        ),
        migrations.AlterField(
            model_name='tags',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='blog.Post'),
        ),
        migrations.DeleteModel(
            name='Post1',
        ),
    ]
