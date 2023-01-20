# Generated by Django 3.2.16 on 2023-01-20 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20230119_1456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['play']},
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='playing',
            new_name='viewing',
        ),
        migrations.AddField(
            model_name='booking',
            name='amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='booking',
            name='play',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='booking.play'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='nowplaying',
            name='seats',
            field=models.IntegerField(default=41),
        ),
    ]
