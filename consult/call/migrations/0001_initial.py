# Generated by Django 4.2 on 2023-06-16 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Call",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("consult_audio", models.TextField()),
                ("consult_text", models.TextField()),
                ("consult_date", models.DateTimeField(auto_now_add=True)),
                ("summary", models.TextField()),
                (
                    "satisfaction",
                    models.CharField(
                        choices=[
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                        ],
                        max_length=1,
                    ),
                ),
                (
                    "counselor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="call_counselor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="call_customer",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
