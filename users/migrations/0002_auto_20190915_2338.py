# Generated by Django 2.2.5 on 2019-09-15 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='office',
            field=models.CharField(choices=[('n', 'NIL'), ('ss', 'Sisters cod'), ('md', 'Music Director.'), ('p', 'President'), ('bs', 'Bible study secretary'), ('t', 'Treasurer'), ('as/f', 'Ass Secretary/Fin sec'), ('es', 'Evangelism secretary'), ('vp', 'Vice-president'), ('aes', 'Ass Evangelism sec'), ('pro', 'PRO'), ('a', 'As. Welfare'), ('s', 'Secretary'), ('ws', 'Welfare secretary')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('c', 'Corper'), ('p', 'Passed-Out')], default='', max_length=100),
        ),
    ]
