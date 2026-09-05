// Main JavaScript for Portfolio Application

document.addEventListener('DOMContentLoaded', function() {
    // Initialize particles.js for background animation
    initParticles();
    
    // Initialize AOS (Animate On Scroll) with mobile detection
    const isMobile = window.innerWidth < 768;
    AOS.init({
        duration: 800,
        easing: 'ease-in-out',
        once: true,
        mirror: false,
        disable: isMobile // Disable AOS on mobile for better performance
    });
    
    // Initialize project search and filter
    initProjectSearch();
    
    // Typing effect initialization
    initTypingEffect();
    
    // Navbar scroll effect
    initNavbarScroll();
    
    // Mobile menu functionality
    initMobileMenu();
    
    // Dark mode toggle
    initDarkModeToggle();
    
    // Skill bars animation
    initSkillBarsAnimation();
    
    // Contact form handling
    initContactForm();
    
    // Project gallery modal
    initProjectGallery();
    
    // Smooth scrolling for navigation links
    initSmoothScrolling();
    
    // Initialize counter animations
    initCounterAnimations();
    
    // Initialize parallax effects
    initParallaxEffects();
    
    // Initialize floating elements with random delays
    initFloatingElements();
    
    // Initialize 3D tilt effect
    initTiltEffect();
});

// Initialize particles.js for background animation
function initParticles() {
    const particlesContainer = document.getElementById('particles-js');
    if (!particlesContainer) return;
    
    // Detect if mobile for responsive particle density
    const isMobile = window.innerWidth < 768;
    const particleCount = isMobile ? 50 : 100;
    
    particlesJS('particles-js', {
        particles: {
            number: {
                value: particleCount,
                density: {
                    enable: true,
                    value_area: 800
                }
            },
            color: {
                value: ['#8A2BE2', '#4169E1', '#00BFFF', '#1E90FF']
            },
            shape: {
                type: ['circle', 'triangle', 'polygon'],
                stroke: {
                    width: 0,
                    color: '#000000'
                },
                polygon: {
                    nb_sides: 5
                }
            },
            opacity: {
                value: 0.5,
                random: true,
                anim: {
                    enable: true,
                    speed: 1,
                    opacity_min: 0.1,
                    sync: false
                }
            },
            size: {
                value: 5,
                random: true,
                anim: {
                    enable: true,
                    speed: 2,
                    size_min: 0.1,
                    sync: false
                }
            },
            line_linked: {
                enable: true,
                distance: 150,
                color: '#ffffff',
                opacity: 0.2,
                width: 1
            },
            move: {
                enable: true,
                speed: 2,
                direction: 'none',
                random: true,
                straight: false,
                out_mode: 'out',
                bounce: false,
                attract: {
                    enable: true,
                    rotateX: 600,
                    rotateY: 1200
                }
            }
        },
        interactivity: {
            detect_on: 'canvas',
            events: {
                onhover: {
                    enable: true,
                    mode: 'grab'
                },
                onclick: {
                    enable: true,
                    mode: 'push'
                },
                resize: true
            },
            modes: {
                grab: {
                    distance: 140,
                    line_linked: {
                        opacity: 0.5
                    }
                },
                push: {
                    particles_nb: 3
                }
            }
        },
        retina_detect: true
    });
}

// Initialize project search and filter functionality
function initProjectSearch() {
    const searchInput = document.getElementById('project-search');
    const technologyFilter = document.getElementById('technology-filter');
    const projectCards = document.querySelectorAll('.project-card');
    
    if (!searchInput || !technologyFilter) return;
    
    // Function to filter projects
    function filterProjects() {
        const searchTerm = searchInput.value.toLowerCase();
        const selectedTech = technologyFilter.value.toLowerCase();
        
        projectCards.forEach(card => {
            const title = card.querySelector('h4').textContent.toLowerCase();
            const description = card.querySelector('p').textContent.toLowerCase();
            const techTags = Array.from(card.querySelectorAll('.bg-primary\/10')).map(tag => tag.textContent.toLowerCase());
            
            const matchesSearch = title.includes(searchTerm) || description.includes(searchTerm);
            const matchesTech = selectedTech === '' || techTags.some(tech => tech.includes(selectedTech));
            
            if (matchesSearch && matchesTech) {
                card.style.display = '';
                // Add a subtle animation when showing cards
                card.style.opacity = '0';
                setTimeout(() => {
                    card.style.opacity = '1';
                    card.style.transition = 'opacity 0.3s ease-in-out';
                }, 50);
            } else {
                card.style.display = 'none';
            }
        });
    }
    
    // Add event listeners
    searchInput.addEventListener('input', filterProjects);
    technologyFilter.addEventListener('change', filterProjects);
    
    // Initialize tooltips for project cards
    const projectLinks = document.querySelectorAll('.project-links a');
    projectLinks.forEach(link => {
        const tooltip = document.createElement('div');
        tooltip.className = 'tooltip bg-gray-800 text-white text-xs rounded py-1 px-2 absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 opacity-0 transition-opacity duration-200';
        tooltip.textContent = link.getAttribute('data-tooltip') || (link.classList.contains('github') ? 'View Code' : 'Live Demo');
        
        link.appendChild(tooltip);
        
        link.addEventListener('mouseenter', () => {
            tooltip.style.opacity = '1';
        });
        
        link.addEventListener('mouseleave', () => {
            tooltip.style.opacity = '0';
        });
    });
}

// Initialize typing effect
function initTypingEffect() {
    const typedElement = document.getElementById('typed-text');
    if (!typedElement) return;
    
    // Get job title from data attribute or use default
    const jobTitle = typedElement.getAttribute('data-job-title') || 'Full Stack Developer';
    
    const options = {
        strings: [jobTitle, "Passionate Developer", "Creative Designer"],
        typeSpeed: 50,
        backSpeed: 30,
        backDelay: 2000,
        loop: true
    };
    
    new Typed('#typed-text', options);
}

// Initialize navbar scroll effect
function initNavbarScroll() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;
    
    // Add active class to nav link based on current section
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section');
    
    window.addEventListener('scroll', function() {
        // Navbar appearance change on scroll
        if (window.scrollY > 50) {
            navbar.classList.add('py-2');
            navbar.classList.add('shadow-md');
        } else {
            navbar.classList.remove('py-2');
            navbar.classList.remove('shadow-md');
        }
        
        // Highlight active nav link
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            
            if (window.scrollY >= (sectionTop - 200)) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('text-primary');
            link.classList.add('text-text', 'dark:text-gray-200');
            
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.remove('text-text', 'dark:text-gray-200');
                link.classList.add('text-primary');
            }
        });
    });
}

// Initialize mobile menu functionality
function initMobileMenu() {
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    if (!mobileMenuButton || !mobileMenu) return;
    
    mobileMenuButton.addEventListener('click', function() {
        mobileMenu.classList.toggle('translate-x-full');
        
        // Change icon based on menu state
        const icon = mobileMenuButton.querySelector('i');
        if (mobileMenu.classList.contains('translate-x-full')) {
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        } else {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-times');
        }
    });
    
    // Close mobile menu when clicking a link
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');
    mobileNavLinks.forEach(link => {
        link.addEventListener('click', function() {
            mobileMenu.classList.add('translate-x-full');
            const icon = mobileMenuButton.querySelector('i');
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        });
    });
}

// Initialize dark mode toggle
function initDarkModeToggle() {
    const themeToggle = document.getElementById('theme-toggle');
    if (!themeToggle) return;
    
    const htmlElement = document.documentElement;
    
    // Check for saved theme preference or use system preference
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (savedTheme === 'dark' || (savedTheme === null && systemPrefersDark)) {
        htmlElement.classList.add('dark');
    } else {
        htmlElement.classList.remove('dark');
    }
    
    themeToggle.addEventListener('click', function() {
        htmlElement.classList.toggle('dark');
        
        // Save preference to localStorage
        if (htmlElement.classList.contains('dark')) {
            localStorage.setItem('theme', 'dark');
        } else {
            localStorage.setItem('theme', 'light');
        }
    });
}

// Initialize skill bars animation
function initSkillBarsAnimation() {
    const skillBars = document.querySelectorAll('.skill-progress');
    if (skillBars.length === 0) return;
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const width = entry.target.getAttribute('data-width');
                entry.target.style.width = width;
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    skillBars.forEach(bar => {
        observer.observe(bar);
    });
}

// Initialize contact form handling
function initContactForm() {
    const contactForm = document.getElementById('contact-form');
    if (!contactForm) return;
    
    const formStatus = document.getElementById('form-status');
    const successMessage = document.getElementById('success-message');
    const errorMessage = document.getElementById('error-message');
    
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = new FormData(contactForm);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });
        
        // Get the CSRF token from the form
        const csrfToken = formData.get('csrfmiddlewaretoken');
        
        fetch(contactForm.getAttribute('action'), {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            formStatus.classList.remove('hidden');
            
            if (data.success) {
                successMessage.classList.remove('hidden');
                errorMessage.classList.add('hidden');
                contactForm.reset();
            } else {
                successMessage.classList.add('hidden');
                errorMessage.classList.remove('hidden');
                errorMessage.querySelector('span').textContent = data.message || 'There was a problem sending your message. Please try again.';
            }
            
            // Hide the message after 5 seconds
            setTimeout(() => {
                formStatus.classList.add('hidden');
            }, 5000);
        })
        .catch(error => {
            formStatus.classList.remove('hidden');
            successMessage.classList.add('hidden');
            errorMessage.classList.remove('hidden');
            errorMessage.querySelector('span').textContent = 'There was a problem sending your message. Please try again.';
            
            // Hide the message after 5 seconds
            setTimeout(() => {
                formStatus.classList.add('hidden');
            }, 5000);
        });
    });
}

// Initialize project gallery modal
function initProjectGallery() {
    const galleryItems = document.querySelectorAll('.gallery-item');
    if (galleryItems.length === 0) return;
    
    const modal = document.createElement('div');
    modal.className = 'modal';
    modal.innerHTML = `
        <span class="modal-close">&times;</span>
        <img class="modal-content" id="modal-image">
    `;
    document.body.appendChild(modal);
    
    const modalImg = document.getElementById('modal-image');
    const closeBtn = modal.querySelector('.modal-close');
    
    galleryItems.forEach(item => {
        item.addEventListener('click', function() {
            const img = item.querySelector('img');
            modal.style.display = 'block';
            modalImg.src = img.src;
        });
    });
    
    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
    });
    
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
}

// Initialize smooth scrolling for navigation links
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            // Only prevent default if the href is not just '#'
            if (this.getAttribute('href') !== '#') {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                
                if (targetElement) {
                    // Get navbar height for offset
                    const navbar = document.getElementById('navbar');
                    const navbarHeight = navbar ? navbar.offsetHeight : 0;
                    
                    const targetPosition = targetElement.offsetTop - navbarHeight;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
}

// Initialize counter animations
function initCounterAnimations() {
    const counters = document.querySelectorAll('.count-up');
    if (counters.length === 0) return;
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = entry.target;
                const countTo = parseInt(target.getAttribute('data-count'));
                let count = 0;
                const interval = setInterval(() => {
                    if (count >= countTo) {
                        clearInterval(interval);
                    } else {
                        count += Math.ceil(countTo / 100);
                        if (count > countTo) count = countTo;
                        target.textContent = count;
                    }
                }, 30);
                observer.unobserve(target);
            }
        });
    }, { threshold: 0.5 });
    
    counters.forEach(counter => {
        observer.observe(counter);
    });
}

// Initialize parallax effects
function initParallaxEffects() {
    const parallaxElements = document.querySelectorAll('.parallax-element');
    if (parallaxElements.length === 0) return;
    
    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        
        parallaxElements.forEach(element => {
            const speed = element.getAttribute('data-parallax-speed') || 0.2;
            const offsetTop = element.offsetTop;
            const distance = offsetTop - scrollY;
            const translation = distance * speed;
            
            element.style.transform = `translateY(${translation}px)`;
        });
    });
}

// Initialize floating elements
function initFloatingElements() {
    // Add random animation delays to floating elements for more natural movement
    const floatingElements = document.querySelectorAll('.animate-float');
    
    floatingElements.forEach(element => {
        if (!element.style.animationDelay) {
            const randomDelay = Math.floor(Math.random() * 2000);
            element.style.animationDelay = `${randomDelay}ms`;
        }
    });
    
    // Add random animation durations for more variety
    const pulseElements = document.querySelectorAll('.animate-pulse-slow');
    
    pulseElements.forEach(element => {
        if (!element.style.animationDuration) {
            const randomDuration = 3 + Math.floor(Math.random() * 3);
            element.style.animationDuration = `${randomDuration}s`;
        }
    });
}

// Initialize 3D tilt effect
function initTiltEffect() {
    const tiltElements = document.querySelectorAll('.tilt-element');
    if (tiltElements.length === 0) return;
    
    tiltElements.forEach(element => {
        element.addEventListener('mousemove', e => {
            const rect = element.getBoundingClientRect();
            const centerX = rect.left + rect.width / 2;
            const centerY = rect.top + rect.height / 2;
            const rotateX = (e.clientY - centerY) / 10;
            const rotateY = (centerX - e.clientX) / 10;
            
            element.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        });
        
        element.addEventListener('mouseleave', () => {
            element.style.transform = 'perspective(1000px) rotateX(0) rotateY(0)';
        });
    });
}