from django.core.management.base import BaseCommand
from django.utils import timezone
from portfolio_app.models import ColorScheme, Profile, Education, Skill, Project, ProjectImage, Experience, Certificate
from django.core.files.base import ContentFile
import random
import datetime
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Creates fake data for the portfolio application'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating fake data...'))
        
        # Create color schemes
        self.create_color_schemes()
        
        # Create profile
        self.create_profile()
        
        # Create education
        self.create_education()
        
        # Create skills
        self.create_skills()
        
        # Create projects
        self.create_projects()
        
        # Create experience
        self.create_experience()
        
        # Create certificates
        self.create_certificates()
        
        self.stdout.write(self.style.SUCCESS('Fake data created successfully!'))
    
    def create_color_schemes(self):
        # Delete existing color schemes
        ColorScheme.objects.all().delete()
        
        # Create light theme
        ColorScheme.objects.create(
            name="Light Theme",
            primary_color="#3b82f6",  # Blue
            secondary_color="#10b981",  # Green
            text_color="#1f2937",  # Dark gray
            background_color="#ffffff",  # White
            accent_color="#f59e0b",  # Amber
            is_dark_mode=False,
            is_active=True
        )
        
        # Create dark theme
        ColorScheme.objects.create(
            name="Dark Theme",
            primary_color="#60a5fa",  # Lighter blue
            secondary_color="#34d399",  # Lighter green
            text_color="#f3f4f6",  # Light gray
            background_color="#111827",  # Dark blue/gray
            accent_color="#fbbf24",  # Lighter amber
            is_dark_mode=True,
            is_active=False
        )
        
        # Create purple theme
        ColorScheme.objects.create(
            name="Purple Theme",
            primary_color="#8b5cf6",  # Purple
            secondary_color="#ec4899",  # Pink
            text_color="#1f2937",  # Dark gray
            background_color="#ffffff",  # White
            accent_color="#f43f5e",  # Rose
            is_dark_mode=False,
            is_active=False
        )
        
        self.stdout.write(self.style.SUCCESS('Color schemes created'))
    
    def create_profile(self):
        # Delete existing profiles
        Profile.objects.all().delete()
        
        # Create profile
        Profile.objects.create(
            full_name="John Doe",
            job_title="Full Stack Developer",
            bio_short="Passionate developer with expertise in web development, machine learning, and software engineering.",
            bio_long="I am a full-stack developer with over 5 years of experience building web applications using modern technologies. My expertise includes front-end development with React, Angular, and Vue.js, as well as back-end development with Django, Node.js, and Flask. I am passionate about creating clean, efficient, and user-friendly applications that solve real-world problems.\n\nIn addition to my technical skills, I have strong problem-solving abilities and excellent communication skills. I enjoy working in collaborative environments and am always eager to learn new technologies and methodologies to improve my craft.",
            email="john.doe@example.com",
            phone="+1 (555) 123-4567",
            location="San Francisco, CA",
            github="https://github.com/johndoe",
            linkedin="https://linkedin.com/in/johndoe",
            twitter="https://twitter.com/johndoe",
            instagram="https://instagram.com/johndoe",
            facebook="https://facebook.com/johndoe",
            website="https://johndoe.dev"
        )
        
        self.stdout.write(self.style.SUCCESS('Profile created'))
    
    def create_education(self):
        # Delete existing education
        Education.objects.all().delete()
        
        # Create education entries
        Education.objects.create(
            institution="Stanford University",
            degree="Master of Science",
            field_of_study="Computer Science",
            start_date=datetime.date(2018, 9, 1),
            end_date=datetime.date(2020, 6, 30),
            description="Specialized in Artificial Intelligence and Machine Learning. Completed thesis on 'Deep Learning Applications in Natural Language Processing'.",
            order=1
        )
        
        Education.objects.create(
            institution="University of California, Berkeley",
            degree="Bachelor of Science",
            field_of_study="Computer Engineering",
            start_date=datetime.date(2014, 9, 1),
            end_date=datetime.date(2018, 5, 31),
            description="Graduated with honors. Participated in various hackathons and coding competitions. Member of the Computer Science Club.",
            order=2
        )
        
        self.stdout.write(self.style.SUCCESS('Education entries created'))
    
    def create_skills(self):
        # Delete existing skills
        Skill.objects.all().delete()
        
        # Frontend skills
        frontend_skills = [
            {"name": "HTML5", "proficiency": 95, "icon": "fab fa-html5"},
            {"name": "CSS3", "proficiency": 90, "icon": "fab fa-css3-alt"},
            {"name": "JavaScript", "proficiency": 92, "icon": "fab fa-js"},
            {"name": "React", "proficiency": 88, "icon": "fab fa-react"},
            {"name": "Vue.js", "proficiency": 85, "icon": "fab fa-vuejs"},
            {"name": "Angular", "proficiency": 80, "icon": "fab fa-angular"},
            {"name": "Tailwind CSS", "proficiency": 90, "icon": "fas fa-wind"}
        ]
        
        # Backend skills
        backend_skills = [
            {"name": "Python", "proficiency": 95, "icon": "fab fa-python"},
            {"name": "Django", "proficiency": 92, "icon": "fas fa-server"},
            {"name": "Node.js", "proficiency": 88, "icon": "fab fa-node-js"},
            {"name": "Express", "proficiency": 85, "icon": "fas fa-server"},
            {"name": "PHP", "proficiency": 75, "icon": "fab fa-php"},
            {"name": "Java", "proficiency": 80, "icon": "fab fa-java"}
        ]
        
        # Database skills
        database_skills = [
            {"name": "PostgreSQL", "proficiency": 90, "icon": "fas fa-database"},
            {"name": "MySQL", "proficiency": 88, "icon": "fas fa-database"},
            {"name": "MongoDB", "proficiency": 85, "icon": "fas fa-database"},
            {"name": "Redis", "proficiency": 80, "icon": "fas fa-database"}
        ]
        
        # DevOps skills
        devops_skills = [
            {"name": "Docker", "proficiency": 85, "icon": "fab fa-docker"},
            {"name": "AWS", "proficiency": 80, "icon": "fab fa-aws"},
            {"name": "CI/CD", "proficiency": 82, "icon": "fas fa-sync-alt"},
            {"name": "Git", "proficiency": 95, "icon": "fab fa-git-alt"}
        ]
        
        # Tools skills
        tools_skills = [
            {"name": "VS Code", "proficiency": 95, "icon": "fas fa-code"},
            {"name": "Figma", "proficiency": 85, "icon": "fab fa-figma"},
            {"name": "Photoshop", "proficiency": 75, "icon": "fas fa-paint-brush"},
            {"name": "Jira", "proficiency": 88, "icon": "fab fa-jira"}
        ]
        
        # Soft skills
        soft_skills = [
            {"name": "Communication", "proficiency": 90, "icon": "fas fa-comments"},
            {"name": "Teamwork", "proficiency": 95, "icon": "fas fa-users"},
            {"name": "Problem Solving", "proficiency": 92, "icon": "fas fa-puzzle-piece"},
            {"name": "Time Management", "proficiency": 88, "icon": "fas fa-clock"}
        ]
        
        # Create all skills
        order = 1
        for skill in frontend_skills:
            Skill.objects.create(
                name=skill["name"],
                category="frontend",
                proficiency=skill["proficiency"],
                icon=skill["icon"],
                order=order
            )
            order += 1
        
        order = 1
        for skill in backend_skills:
            Skill.objects.create(
                name=skill["name"],
                category="backend",
                proficiency=skill["proficiency"],
                icon=skill["icon"],
                order=order
            )
            order += 1
        
        order = 1
        for skill in database_skills:
            Skill.objects.create(
                name=skill["name"],
                category="database",
                proficiency=skill["proficiency"],
                icon=skill["icon"],
                order=order
            )
            order += 1
        
        order = 1
        for skill in devops_skills:
            Skill.objects.create(
                name=skill["name"],
                category="devops",
                proficiency=skill["proficiency"],
                icon=skill["icon"],
                order=order
            )
            order += 1
        
        order = 1
        for skill in tools_skills:
            Skill.objects.create(
                name=skill["name"],
                category="tools",
                proficiency=skill["proficiency"],
                icon=skill["icon"],
                order=order
            )
            order += 1
        
        order = 1
        for skill in soft_skills:
            Skill.objects.create(
                name=skill["name"],
                category="soft",
                proficiency=skill["proficiency"],
                icon=skill["icon"],
                order=order
            )
            order += 1
        
        self.stdout.write(self.style.SUCCESS('Skills created'))
    
    def create_projects(self):
        # Delete existing projects
        Project.objects.all().delete()
        
        # Get all skills for random assignment
        skills = list(Skill.objects.all())
        
        # Create projects
        projects = [
            {
                "title": "E-Commerce Platform",
                "description": "A full-featured e-commerce platform built with Django and React. Features include user authentication, product catalog, shopping cart, payment processing, and order management.",
                "featured": True,
                "completion_date": datetime.date(2022, 5, 15),
                "order": 1
            },
            {
                "title": "Task Management App",
                "description": "A task management application built with Vue.js and Node.js. Features include task creation, assignment, due dates, status tracking, and team collaboration.",
                "featured": True,
                "completion_date": datetime.date(2022, 2, 10),
                "order": 2
            },
            {
                "title": "Real-time Chat Application",
                "description": "A real-time chat application built with Socket.io and React. Features include private messaging, group chats, file sharing, and message history.",
                "featured": False,
                "completion_date": datetime.date(2021, 11, 20),
                "order": 3
            },
            {
                "title": "Portfolio Website",
                "description": "A responsive portfolio website built with Django and Tailwind CSS. Features include dynamic content management, dark mode, and contact form.",
                "featured": False,
                "completion_date": datetime.date(2021, 8, 5),
                "order": 4
            },
            {
                "title": "Weather Forecast App",
                "description": "A weather forecast application built with React and OpenWeatherMap API. Features include current weather, 5-day forecast, location search, and weather alerts.",
                "featured": False,
                "completion_date": datetime.date(2021, 6, 12),
                "order": 5
            },
            {
                "title": "Blog Platform",
                "description": "A blog platform built with Django and Bootstrap. Features include user authentication, post creation, comments, categories, and search functionality.",
                "featured": False,
                "completion_date": datetime.date(2021, 3, 25),
                "order": 6
            }
        ]
        
        for project_data in projects:
            project = Project.objects.create(
                title=project_data["title"],
                description=project_data["description"],
                featured=project_data["featured"],
                completion_date=project_data["completion_date"],
                order=project_data["order"],
                live_url="https://example.com",
                github_url="https://github.com/example/project"
            )
            
            # Add random skills (3-6) to each project
            num_skills = random.randint(3, 6)
            project_skills = random.sample(skills, num_skills)
            project.technologies.set(project_skills)
        
        self.stdout.write(self.style.SUCCESS('Projects created'))
    
    def create_experience(self):
        # Delete existing experience
        Experience.objects.all().delete()
        
        # Create experience entries
        Experience.objects.create(
            company="Tech Innovations Inc.",
            position="Senior Full Stack Developer",
            start_date=datetime.date(2021, 3, 1),
            is_current=True,
            description="• Led the development of a high-traffic e-commerce platform using Django and React\n• Implemented CI/CD pipelines using GitHub Actions and Docker\n• Mentored junior developers and conducted code reviews\n• Optimized database queries resulting in a 40% improvement in page load times",
            company_url="https://example.com",
            order=1
        )
        
        Experience.objects.create(
            company="WebSolutions Co.",
            position="Full Stack Developer",
            start_date=datetime.date(2019, 6, 1),
            end_date=datetime.date(2021, 2, 28),
            description="• Developed and maintained multiple client websites using Vue.js and Node.js\n• Implemented responsive designs and ensured cross-browser compatibility\n• Integrated third-party APIs for payment processing and social media\n• Participated in agile development processes and sprint planning",
            company_url="https://example.com",
            order=2
        )
        
        Experience.objects.create(
            company="Digital Creations",
            position="Frontend Developer",
            start_date=datetime.date(2017, 9, 1),
            end_date=datetime.date(2019, 5, 31),
            description="• Created responsive and interactive user interfaces using HTML, CSS, and JavaScript\n• Collaborated with designers to implement pixel-perfect designs\n• Optimized web applications for maximum speed and scalability\n• Developed and maintained the company's component library",
            company_url="https://example.com",
            order=3
        )
        
        self.stdout.write(self.style.SUCCESS('Experience entries created'))
    
    def create_certificates(self):
        # Delete existing certificates
        Certificate.objects.all().delete()
        
        # Create certificates
        Certificate.objects.create(
            name="AWS Certified Solutions Architect",
            issuing_organization="Amazon Web Services",
            issue_date=datetime.date(2022, 3, 15),
            expiration_date=datetime.date(2025, 3, 15),
            credential_id="AWS-123456",
            credential_url="https://aws.amazon.com/certification/verify",
            description="Validates expertise in designing distributed systems on AWS",
            order=1
        )
        
        Certificate.objects.create(
            name="Professional Scrum Master I",
            issuing_organization="Scrum.org",
            issue_date=datetime.date(2021, 11, 10),
            credential_id="PSM-123456",
            credential_url="https://www.scrum.org/certificates/verify",
            description="Demonstrates understanding of Scrum framework and ability to apply it",
            order=2
        )
        
        Certificate.objects.create(
            name="React Developer Certification",
            issuing_organization="Meta",
            issue_date=datetime.date(2021, 7, 22),
            credential_id="FB-123456",
            credential_url="https://www.coursera.org/verify",
            description="Validates expertise in building applications with React",
            order=3
        )
        
        Certificate.objects.create(
            name="Python for Data Science",
            issuing_organization="IBM",
            issue_date=datetime.date(2021, 4, 5),
            credential_id="IBM-123456",
            credential_url="https://www.coursera.org/verify",
            description="Covers fundamentals of Python programming for data science applications",
            order=4
        )
        
        self.stdout.write(self.style.SUCCESS('Certificates created'))