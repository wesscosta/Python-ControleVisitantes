# Generated by Django 3.0 on 2022-01-04 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0002_auto_20211206_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitante',
            name='status',
            field=models.CharField(choices=[('AGUARDANDO', 'Aguardando Autorização'), ('EM_VISITA', 'Em Visita'), ('Finalizado', 'Visita Finalizada')], default='AGUARDANDO', max_length=10, verbose_name='Status'),
        ),
    ]
