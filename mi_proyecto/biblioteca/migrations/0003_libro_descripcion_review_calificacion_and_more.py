# Generated by Django 5.1.3 on 2024-12-02 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_rename_correo_usuario_email_remove_libro_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='descripcion',
            field=models.TextField(default='No disponible'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='calificacion',
            field=models.PositiveIntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='biblioteca.libro'),
        ),
        migrations.AlterField(
            model_name='review',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='biblioteca.usuario'),
        ),
    ]
