# Generated by Django 4.2.13 on 2024-06-22 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=250)),
                ('can_trade', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MarginMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PositionSide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField()),
                ('message_id', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=6000)),
                ('reply_to_msg_id', models.CharField(max_length=15, null=True)),
                ('edit_date', models.CharField(max_length=100, null=True)),
                ('is_predict_msg', models.BooleanField(default=False, null=True)),
                ('channel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.channel')),
            ],
        ),
        migrations.CreateModel(
            name='PostStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='SettingConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_channels_set_order', models.BooleanField(default=False, null=True)),
                ('max_entry_money', models.FloatField(default=5, null=True)),
                ('max_leverage', models.PositiveBigIntegerField(default=1, null=True)),
                ('leverage_effect', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20, null=True)),
                ('fee_rate', models.CharField(max_length=20, null=True)),
                ('currency', models.CharField(max_length=20, null=True)),
                ('asset', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TakeProfitTarget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=False, null=True)),
                ('period', models.CharField(max_length=60, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('profit', models.FloatField(default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.post')),
            ],
        ),
        migrations.CreateModel(
            name='Predict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leverage', models.IntegerField(default=1, null=True)),
                ('stopLoss', models.CharField(max_length=50, null=True)),
                ('profit', models.FloatField(default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.CharField(max_length=50, null=True)),
                ('margin_mode', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='panel.marginmode')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.market')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.positionside')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.post')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.poststatus')),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.symbol')),
            ],
        ),
        migrations.CreateModel(
            name='EntryTarget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=False, null=True)),
                ('period', models.CharField(max_length=60, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.post')),
            ],
        ),
    ]
