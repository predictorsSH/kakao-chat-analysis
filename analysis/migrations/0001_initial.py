# Generated by Django 4.1 on 2023-04-23 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advanced_analyis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('f_id', models.BigAutoField(help_text='File id', primary_key=True, serialize=False)),
                ('attached', models.FileField(upload_to='uploads/', verbose_name='첨부파일')),
            ],
        ),
        migrations.CreateModel(
            name='Basic_stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_count', models.TextField()),
                ('active_time', models.IntegerField(default=3)),
                ('user_words_count', models.TextField(null=True)),
                ('f_id', models.ForeignKey(db_column='f_id', on_delete=django.db.models.deletion.CASCADE, related_name='File', to='analysis.fileupload')),
            ],
        ),
    ]
