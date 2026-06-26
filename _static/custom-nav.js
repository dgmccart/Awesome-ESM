document.addEventListener('DOMContentLoaded', function() {
    // Initialize accordion
    initializeAccordion();
    
    // Initialize sidebar toggle for mobile
    initializeSidebarToggle();
    
    // Initialize active link detection
    updateActiveNavigation();
    
    // Handle theme switching for logo
    initializeThemeToggle();
});

function initializeAccordion() {
    const navItems = document.querySelectorAll('.nav-item');
    
    navItems.forEach(item => {
        const link = item.querySelector('.nav-link');
        const children = item.querySelector('.nav-children');
        
        if (!children) return;
        
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const isExpanded = item.classList.contains('expanded');
            
            // Close other items
            navItems.forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove('expanded');
                }
            });
            
            // Toggle current item
            item.classList.toggle('expanded');
            
            // Store preference in localStorage
            localStorage.setItem(`nav-expanded-${link.href}`, !isExpanded);
        });
        
        // Restore previous state
        const wasExpanded = localStorage.getItem(`nav-expanded-${link.href}`) === 'true';
        if (wasExpanded) {
            item.classList.add('expanded');
        }
    });
}

function initializeSidebarToggle() {
    const toggleBtn = document.getElementById('sidebar-toggle');
    const sidebar = document.querySelector('.custom-left-sidebar');
    const body = document.body;
    
    if (!toggleBtn) return;
    
    toggleBtn.addEventListener('click', function() {
        sidebar.classList.toggle('open');
        body.classList.toggle('sidebar-open');
    });
    
    // Close sidebar when clicking main content
    document.querySelector('.main-content')?.addEventListener('click', function() {
        if (window.innerWidth <= 768) {
            sidebar.classList.remove('open');
            body.classList.remove('sidebar-open');
        }
    });
}

function updateActiveNavigation() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link, .nav-children a');
    
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        
        // Check if this is the current page
        if (currentPath.endsWith(href) || currentPath.includes(href)) {
            link.classList.add('active');
            
            // Expand parent accordion
            const navItem = link.closest('.nav-item');
            if (navItem) {
                navItem.classList.add('expanded');
            }
        }
    });
}

function initializeThemeToggle() {
    // Listen for theme changes
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.attributeName === 'data-md-color-scheme') {
                // Update logo visibility
                updateLogoDisplay();
            }
        });
    });
    
    observer.observe(document.documentElement, {
        attributes: true,
        attributeFilter: ['data-md-color-scheme']
    });
}

function updateLogoDisplay() {
    const scheme = document.documentElement.getAttribute('data-md-color-scheme');
    const logo = document.querySelector('.sidebar-logo');
    
    if (logo && logo.dataset.theme) {
        logo.style.display = logo.dataset.theme === scheme ? 'block' : 'none';
    }
}
