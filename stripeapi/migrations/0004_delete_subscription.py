# Generated by Django 5.0.7 on 2024-07-18 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stripeapi', '0003_customuser_remove_subscription_is_active'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
