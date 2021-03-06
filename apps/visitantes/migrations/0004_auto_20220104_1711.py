# Generated by Django 3.0 on 2022-01-04 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0003_visitante_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitante',
            name='status',
            field=models.CharField(choices=[('AGUARDANDO', 'Aguardando Autorização'), ('EM_VISITA', 'Em Visita'), ('FINALIZADO', 'Visita Finalizada')], default='AGUARDANDO', max_length=10, verbose_name='Status'),
        ),
    ]
