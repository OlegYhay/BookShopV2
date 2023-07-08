# Generated by Django 4.2.2 on 2023-06-26 16:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('cover', models.ImageField(blank=True, upload_to='covers/', verbose_name='Фото')),
                ('description', models.TextField(default='without decription', null=True, verbose_name='Описание')),
                ('age_control', models.CharField(default='0+', max_length=20, null=True, verbose_name='Возрастное ограничение')),
                ('copyright', models.CharField(default='', max_length=200, null=True, verbose_name='Права')),
                ('ISBN', models.CharField(default='', max_length=33, null=True)),
                ('is_popular', models.BooleanField(default=False, verbose_name='Популярное')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'db_table_comment': 'Книги для продажи',
                'ordering': ['title'],
                'permissions': [('special_status', 'Can read all books')],
            },
        ),
        migrations.CreateModel(
            name='CategoryBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('secondname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('fulladdress', models.CharField(max_length=255, verbose_name='Область(республика),город,улица,дом,квартира,индекс:')),
                ('notification', models.BooleanField(default=False, verbose_name='СМС уведомление о статусе заказа')),
                ('status', models.CharField(choices=[('Новый', 'New'), ('Оплачено', 'Paid'), ('Принят', 'Accepted'), ('В пути', 'Ontheway'), ('Доставлен', 'Delivered')], default='Новый', max_length=255, verbose_name='Статус')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='OrderBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('summ', models.PositiveIntegerField(default=0, verbose_name='Сумма')),
            ],
            options={
                'verbose_name': 'Состав заказа',
            },
        ),
        migrations.CreateModel(
            name='Paymentmethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Вид оплаты',
                'verbose_name_plural': 'Виды оплат',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=255, verbose_name='Комментарий')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['date'],
            },
        ),
    ]
