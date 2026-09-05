from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class ColorScheme(models.Model):
    name = models.CharField(max_length=50)
    primary_color = models.CharField(max_length=20, help_text="HEX color code")
    secondary_color = models.CharField(max_length=20, help_text="HEX color code")
    text_color = models.CharField(max_length=20, help_text="HEX color code")
    background_color = models.CharField(max_length=20, help_text="HEX color code")
    accent_color = models.CharField(max_length=20, help_text="HEX color code")
    is_dark_mode = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.is_active:
            # Set all other color schemes to inactive
            ColorScheme.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile/')
    banner_image = models.ImageField(upload_to='banner/', blank=True, null=True)
    job_title = models.CharField(max_length=100)
    bio_short = models.CharField(max_length=150, help_text="A short description for the home section")
    bio_long = models.TextField(help_text="Detailed about me description")
    resume = models.FileField(upload_to='documents/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='education/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"
    
    class Meta:
        ordering = ['order']
        verbose_name = "Education"
        verbose_name_plural = "Education"

class Skill(models.Model):
    CATEGORY_CHOICES = (
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('devops', 'DevOps'),
        ('tools', 'Tools'),
        ('soft', 'Soft Skills'),
        ('other', 'Other'),
    )
    
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    proficiency = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Proficiency level from 1-100"
    )
    icon = models.CharField(max_length=50, help_text="Font Awesome class name or other icon identifier", blank=True, null=True)
    logo = models.ImageField(upload_to='skills/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['category', 'order']

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='projects/', blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    technologies = models.ManyToManyField(Skill, related_name='projects')
    featured = models.BooleanField(default=False)
    completion_date = models.DateField()
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-featured', 'order']

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']

class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    company_logo = models.ImageField(upload_to='experience/', blank=True, null=True)
    company_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.position} at {self.company}"
    
    class Meta:
        ordering = ['order']

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)
    credential_id = models.CharField(max_length=100, blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.subject} from {self.name}"
    
    class Meta:
        ordering = ['-created_at']
