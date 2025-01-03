# Generated by Django 5.1.2 on 2024-12-24 03:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactUs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=200)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="LatestProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("number_of_bids", models.PositiveIntegerField(default=0)),
                ("bid_data", models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name="EmployerProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="employer_profiles/"
                    ),
                ),
                ("display_name", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("projects_posted", models.PositiveIntegerField(default=0)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employer_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FreelancerProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="freelancer_profiles/"
                    ),
                ),
                ("description", models.TextField()),
                ("display_name", models.CharField(max_length=100)),
                ("username", models.CharField(max_length=100, unique=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="freelancer_profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Gig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("thumbnail", models.ImageField(upload_to="gig_thumbnails/")),
                ("title", models.CharField(max_length=200)),
                ("skills", models.TextField()),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "pricing_type",
                    models.CharField(
                        choices=[("Fixed", "Fixed Price"), ("Hourly", "Hourly Price")],
                        max_length=20,
                    ),
                ),
                ("impressions", models.PositiveIntegerField(default=0)),
                ("clicks", models.PositiveIntegerField(default=0)),
                ("sales", models.PositiveIntegerField(default=0)),
                ("monthly_data", models.JSONField(default=dict)),
                ("top_keywords", models.JSONField(default=list)),
                (
                    "freelancer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gigs",
                        to="skillrelay.freelancerprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "pricing_type",
                    models.CharField(
                        choices=[("Fixed", "Fixed Price"), ("Hourly", "Hourly Rate")],
                        max_length=20,
                    ),
                ),
                (
                    "documents",
                    models.FileField(
                        blank=True, null=True, upload_to="project_documents/"
                    ),
                ),
                (
                    "images",
                    models.ImageField(
                        blank=True, null=True, upload_to="project_images/"
                    ),
                ),
                (
                    "employer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects",
                        to="skillrelay.employerprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Bid",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price_quoted", models.DecimalField(decimal_places=2, max_digits=10)),
                ("proposal_text", models.TextField()),
                ("sample_links", models.URLField(blank=True, null=True)),
                (
                    "images",
                    models.ImageField(blank=True, null=True, upload_to="bid_images/"),
                ),
                (
                    "documents",
                    models.FileField(blank=True, null=True, upload_to="bid_documents/"),
                ),
                (
                    "videos",
                    models.FileField(blank=True, null=True, upload_to="bid_videos/"),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bids",
                        to="skillrelay.project",
                    ),
                ),
            ],
        ),
    ]
