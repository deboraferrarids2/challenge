# Generated by Django 3.2.13 on 2024-01-29 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=600, null=True)),
                ('transaction', models.CharField(blank=True, max_length=600, null=True)),
                ('products', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('em aberto', 'em aberto'), ('recebido', 'recebido'), ('em preparacao', 'em preparacao'), ('pronto', 'pronto'), ('finalizado', 'finalizado'), ('cancelado', 'cancelado')], default='em aberto', max_length=20, verbose_name='status')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='atualizado em')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
