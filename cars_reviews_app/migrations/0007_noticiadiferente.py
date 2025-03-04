# Generated by Django 5.1.3 on 2024-12-08 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_reviews_app', '0006_noticia1_noticia_cars_review_fecha_c_e18b19_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticiaDiferente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('img_url', models.ImageField(blank=True, null=True, upload_to='other_images/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'indexes': [models.Index(fields=['fecha_creacion'], name='cars_review_fecha_c_106602_idx')],
            },
        ),
    ]
