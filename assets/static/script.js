// static/script.js

document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('emailForm');
    const loadingIndicator = document.getElementById('loading');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        const emailInput = document.getElementById('email');
        const email = emailInput.value;

        // Simple email validation (basic regex)
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            alert("Please enter a valid email address.");
            return;
        }

        // Show loading indicator
        loadingIndicator.style.display = 'block';

        // Send the form data using fetch API
        fetch(`/send_phishing_email/${encodeURIComponent(email)}`)
            .then(response => response.text())
            .then(data => {
                loadingIndicator.style.display = 'none'; // Hide loading indicator
                alert(data); // Show success message
                form.reset(); // Reset the form
            })
            .catch(error => {
                loadingIndicator.style.display = 'none'; // Hide loading indicator
                alert("An error occurred while sending the email. Please try again.");
                console.error("Error:", error);
            });
    });
});