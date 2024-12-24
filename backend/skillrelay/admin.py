from django.contrib import admin
from .models import (
    FreelancerProfile,
    Gig,
    EmployerProfile,
    Project,
    Bid,
    ContactUs,
)

# Customize FreelancerProfile admin
@admin.register(FreelancerProfile)
class FreelancerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name', 'username', 'description')
    search_fields = ('display_name', 'username')
    list_filter = ('user',)

# Customize Gig admin
@admin.register(Gig)
class GigAdmin(admin.ModelAdmin):
    list_display = ('title', 'freelancer', 'price', 'get_price_type', 'thumbnail')
    search_fields = ('title', 'freelancer__username')
    list_filter = ('skills',)

    def get_price_type(self, obj):
        return obj.get_price_type_display()  # For choices fields
    get_price_type.short_description = 'Price Type'

# Customize EmployerProfile admin
@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name', 'country', 'projects_posted')
    search_fields = ('display_name', 'country')
    list_filter = ('country',)

# Customize Project admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'price', 'get_price_type',)
    search_fields = ('title', 'employer__username')
    list_filter = ('employer',)

    def get_price_type(self, obj):
        return obj.get_price_type_display()  # For choices fields
    get_price_type.short_description = 'Price Type'

# Customize Bid admin
@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('project', 'get_bidder', 'price_quoted', 'proposal_text')
    search_fields = ('project__title', 'bidder__username')
    list_filter = ('project',)

    def get_bidder(self, obj):
        return obj.bidder.username
    get_bidder.short_description = 'Bidder'

# Customize ContactUs admin
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
