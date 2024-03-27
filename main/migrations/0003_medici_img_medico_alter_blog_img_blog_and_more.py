# Generated by Django 4.2.6 on 2023-11-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_medici_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='medici',
            name='img_medico',
            field=models.ImageField(blank=True, default='mediciimg/no_img.png', null=True, upload_to='mediciimg/', verbose_name='Immagine del profilo'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='img_blog',
            field=models.ImageField(blank=True, default='blogimg/no_img.jpeg', null=True, upload_to='blogimg/', verbose_name='Immagine di copertina'),
        ),
        migrations.AlterField(
            model_name='medici',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, null=True),
        ),
    ]