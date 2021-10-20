# Generated by Django 2.2.24 on 2021-10-20 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0024_markordersstatuscompleteconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicationevent',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communication.CommunicationEventType', verbose_name='Event Type'),
        ),
        migrations.CreateModel(
            name='Surcharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Surcharge')),
                ('code', models.CharField(max_length=128, verbose_name='Surcharge code')),
                ('incl_tax', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Surcharge (inc. tax)')),
                ('excl_tax', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Surcharge (excl. tax)')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surcharges', to='order.Order', verbose_name='Surcharges')),
            ],
            options={
                'ordering': ['pk'],
                'abstract': False,
            },
        ),
    ]
