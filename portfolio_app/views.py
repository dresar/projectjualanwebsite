from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json

from .models import (
    ColorScheme, Profile, Education, Skill, Project, 
    Experience, Certificate, ContactMessage
)

def index(request):
    # Get active color scheme or default to first one
    try:
        color_scheme = ColorScheme.objects.filter(is_active=True).first() or ColorScheme.objects.first()
    except:
        color_scheme = None
    
    # Get profile information
    try:
        profile = Profile.objects.first()
    except:
        profile = None
    
    # Get all other data
    education = Education.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    certificates = Certificate.objects.all()
    
    # Group skills by category
    skills_by_category = {}
    for skill in skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    # Featured projects
    featured_projects = projects.filter(featured=True)
    
    context = {
        'color_scheme': color_scheme,
        'profile': profile,
        'education': education,
        'skills_by_category': skills_by_category,
        'projects': projects,
        'featured_projects': featured_projects,
        'experiences': experiences,
        'certificates': certificates,
    }
    
    return render(request, 'index.html', context)

@csrf_exempt
def contact_submit(request):
    if request.method == 'POST':
        try:
            # Handle both form submissions and AJAX
            if request.headers.get('Content-Type') == 'application/json':
                data = json.loads(request.body)
                name = data.get('name')
                email = data.get('email')
                subject = data.get('subject')
                message = data.get('message')
            else:
                name = request.POST.get('name')
                email = request.POST.get('email')
                subject = request.POST.get('subject')
                message = request.POST.get('message')
            
            # Create contact message
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            # Return success response
            if request.headers.get('Content-Type') == 'application/json':
                return JsonResponse({'success': True, 'message': 'Your message has been sent successfully!'})
            else:
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('/#contact')
                
        except Exception as e:
            # Return error response
            if request.headers.get('Content-Type') == 'application/json':
                return JsonResponse({'success': False, 'message': str(e)}, status=400)
            else:
                messages.error(request, f'Error: {str(e)}')
                return redirect('/#contact')
    
    # If not POST, redirect to home
    return redirect('/')
