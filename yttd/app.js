document.getElementById('contactForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // Grab values
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();
    const output = document.getElementById('formMessage');

    // Simple validation
    if (name && email && message) {
        output.style.color = 'green';
        output.textContent = "Thanks for reaching out! I'll get back to you soon.";
        this.reset(); // Clear form
    } else {
        output.style.color = 'red';
        output.textContent = "Please fill in all fields.";
    }
    const menuIcon = document.getElementById('menu-icon');
const navbar = document.getElementById('navbar');

menuIcon.addEventListener('click', () => {
    navbar.classList.toggle('show');
});

});
