# Generated by Django 5.1.3 on 2024-11-21 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]