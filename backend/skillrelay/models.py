from django.db import models
from django.contrib.auth.models import User

# User Profile Models
class FreelancerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='freelancer_profile')
    profile_picture = models.ImageField(upload_to='freelancer_profiles/', blank=True, null=True)
    description = models.TextField()
    display_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.display_name

class Gig(models.Model):
    freelancer = models.ForeignKey(FreelancerProfile, on_delete=models.CASCADE, related_name='gigs')
    thumbnail = models.ImageField(upload_to='gig_thumbnails/')
    title = models.CharField(max_length=200)
    skills = models.TextField()  # Could be a comma-separated list of skills
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pricing_type = models.CharField(max_length=20, choices=(('Fixed', 'Fixed Price'), ('Hourly', 'Hourly Price')))
    impressions = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)
    sales = models.PositiveIntegerField(default=0)
    monthly_data = models.JSONField(default=dict)  # e.g., {"January": {"impressions": 0, "clicks": 0, "sales": 0}}
    top_keywords = models.JSONField(default=list)  # e.g., ["keyword1", "keyword2"]

    def __str__(self):
        return self.title

# Employer Profile Model
class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
    image = models.ImageField(upload_to='employer_profiles/', blank=True, null=True)
    display_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    projects_posted = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.display_name

# Project Model
class Project(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pricing_type = models.CharField(max_length=20, choices=(('Fixed', 'Fixed Price'), ('Hourly', 'Hourly Rate')))
    documents = models.FileField(upload_to='project_documents/', blank=True, null=True)
    images = models.ImageField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return self.title

# Bid Model
class Bid(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bids')
    price_quoted = models.DecimalField(max_digits=10, decimal_places=2)
    proposal_text = models.TextField()
    sample_links = models.URLField(blank=True, null=True)
    images = models.ImageField(upload_to='bid_images/', blank=True, null=True)
    documents = models.FileField(upload_to='bid_documents/', blank=True, null=True)
    videos = models.FileField(upload_to='bid_videos/', blank=True, null=True)

    def __str__(self):
        return f"Bid by {self.project.employer.user.username} for {self.project.title}"

# Contact Us Model
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

# Latest Projects Model
class LatestProject(models.Model):
    title = models.CharField(max_length=200)
    number_of_bids = models.PositiveIntegerField(default=0)
    bid_data = models.JSONField(default=list)  # e.g., [{"price": 100, "proposal_text": "Sample proposal", ...}]

    def __str__(self):
        return self.title
