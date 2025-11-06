// ===== Mobile Menu Toggle =====
const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
const mainNav = document.querySelector('.main-nav');
const userMenu = document.querySelector('.user-menu');
const body = document.body;

mobileMenuToggle.addEventListener('click', () => {
    mobileMenuToggle.classList.toggle('active');
    mainNav.classList.toggle('active');
    userMenu.classList.toggle('active');
    body.style.overflow = mainNav.classList.contains('active') ? 'hidden' : 'auto';
});

// ===== Dropdown Menu Mobile =====
const dropdownItems = document.querySelectorAll('.dropdown');

dropdownItems.forEach(dropdown => {
    const dropdownLink = dropdown.querySelector('.nav-link');

    dropdownLink.addEventListener('click', (e) => {
        // Sur mobile, empêcher la navigation et toggle le dropdown
        if (window.innerWidth <= 992) {
            e.preventDefault();
            dropdown.classList.toggle('active');

            // Fermer les autres dropdowns
            dropdownItems.forEach(otherDropdown => {
                if (otherDropdown !== dropdown) {
                    otherDropdown.classList.remove('active');
                }
            });
        }
    });
});

// ===== Search Bar Toggle =====
const searchBtn = document.querySelector('.search-btn');
const searchBar = document.querySelector('.search-bar');
const searchClose = document.querySelector('.search-close');
const searchInput = document.querySelector('.search-bar input');

searchBtn.addEventListener('click', () => {
    searchBar.classList.add('active');
    setTimeout(() => {
        searchInput.focus();
    }, 300);
});

searchClose.addEventListener('click', () => {
    searchBar.classList.remove('active');
    searchInput.value = '';
});

// Fermer la recherche avec Escape
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && searchBar.classList.contains('active')) {
        searchBar.classList.remove('active');
        searchInput.value = '';
    }
});

// ===== Search Submit =====
const searchSubmit = document.querySelector('.search-submit');

searchSubmit.addEventListener('click', () => {
    const searchQuery = searchInput.value.trim();
    if (searchQuery) {
        console.log('Recherche:', searchQuery);
        // Ici, vous pouvez ajouter la logique de recherche
        alert(`Recherche de: ${searchQuery}`);
    }
});

searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        searchSubmit.click();
    }
});

// ===== Sticky Header with Shadow =====
let lastScroll = 0;
const header = document.querySelector('.main-header');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 50) {
        header.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)';
    } else {
        header.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1)';
    }

    lastScroll = currentScroll;
});

// ===== Active Nav Link =====
const navLinks = document.querySelectorAll('.nav-link');

navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        // Ne pas changer l'active state pour les dropdowns
        if (!link.parentElement.classList.contains('dropdown')) {
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
        }
    });
});

// ===== Notification Button =====
const notificationBtn = document.querySelector('.notification-btn');

notificationBtn.addEventListener('click', () => {
    // Ici, vous pouvez afficher un panneau de notifications
    console.log('Notifications clicked');
    alert('Vous avez 3 nouvelles notifications');
});

// ===== Login and Signup Buttons =====
const loginBtn = document.querySelector('.login-btn');
const signupBtn = document.querySelector('.signup-btn');

loginBtn.addEventListener('click', () => {
    console.log('Login clicked');
    // Ici, vous pouvez ouvrir un modal de connexion
    alert('Ouverture du formulaire de connexion');
});

signupBtn.addEventListener('click', () => {
    console.log('Signup clicked');
    // Ici, vous pouvez ouvrir un modal d'inscription
    alert('Ouverture du formulaire d\'inscription');
});

// ===== Close Mobile Menu on Link Click =====
const mobileNavLinks = document.querySelectorAll('.nav-link');

mobileNavLinks.forEach(link => {
    link.addEventListener('click', () => {
        if (window.innerWidth <= 992 && !link.parentElement.classList.contains('dropdown')) {
            mobileMenuToggle.classList.remove('active');
            mainNav.classList.remove('active');
            userMenu.classList.remove('active');
            body.style.overflow = 'auto';
        }
    });
});

// ===== Resize Handler =====
let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        if (window.innerWidth > 992) {
            // Réinitialiser le menu mobile
            mobileMenuToggle.classList.remove('active');
            mainNav.classList.remove('active');
            userMenu.classList.remove('active');
            body.style.overflow = 'auto';

            // Fermer tous les dropdowns actifs
            dropdownItems.forEach(dropdown => {
                dropdown.classList.remove('active');
            });
        }
    }, 250);
});

// ===== Smooth Scroll =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#') {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

// ===== Animation on Scroll (Features Cards) =====
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Appliquer l'animation aux cartes de fonctionnalités
document.querySelectorAll('.feature-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(30px)';
    card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(card);
});

// ===== Console Info =====
console.log('%c FinanceAcademy ', 'background: #1e40af; color: white; font-size: 20px; padding: 10px;');
console.log('Plateforme de cours en finance bancaire - Version 1.0');
console.log('Développé avec HTML, CSS et JavaScript');
