# Generated by Django 4.2.2 on 2023-07-08 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_review_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('Новый', 'New'), ('Оплачено', 'Paid'), ('Принят', 'Accepted'), ('В пути', 'Ontheway'), ('Доставлен', 'Delivered')], default='Новый', max_length=255, null=True, verbose_name='Статус'),
        ),
    ]
