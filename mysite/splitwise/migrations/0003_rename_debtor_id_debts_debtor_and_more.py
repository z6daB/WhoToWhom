# Generated by Django 5.1 on 2025-03-20 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("splitwise", "0002_debts"),
    ]

    operations = [
        migrations.RenameField(
            model_name="debts",
            old_name="debtor_id",
            new_name="debtor",
        ),
        migrations.RenameField(
            model_name="debts",
            old_name="event_id",
            new_name="event",
        ),
        migrations.RenameField(
            model_name="debts",
            old_name="payer_id",
            new_name="payer",
        ),
        migrations.RenameField(
            model_name="debts",
            old_name="purchase_id",
            new_name="purchase",
        ),
    ]
