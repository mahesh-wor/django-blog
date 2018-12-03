# Generated by Django 2.1.3 on 2018-12-02 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20181202_0613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
        migrations.RemoveField(
            model_name='tag',
            name='blog_tag',
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='tagging',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='tagged_blog',
            field=models.ManyToManyField(through='blog.Tagging', to='blog.Post'),
        ),
    ]