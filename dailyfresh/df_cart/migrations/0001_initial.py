# Generated by Django 2.0.2 on 2018-03-10 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('df_goods', '0002_auto_20180308_0226'),
        ('df_user', '0002_auto_20180307_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.GoodsInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_user.UserInfo')),
            ],
        ),
    ]
