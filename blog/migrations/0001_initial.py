# Generated by Django 4.0.2 on 2022-09-27 14:32

import ckeditor.fields
import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255)),
                ('subtitulo', models.CharField(max_length=255)),
                ('resumo', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('conteudo', ckeditor_uploader.fields.RichTextUploadingField()),
                ('imagem_capa', models.ImageField(blank=True, null=True, upload_to='static/blog/')),
                ('data_publicacao', models.DateTimeField(verbose_name=datetime.datetime(2022, 9, 27, 14, 32, 13, 177333, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]