# Generated by Django 3.2.25 on 2024-04-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0201_keypair_bookwyrm_ke_remote__472927_idx"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="user",
            index=models.Index(
                fields=["username"], name="bookwyrm_us_usernam_b2546d_idx"
            ),
        ),
    ]
