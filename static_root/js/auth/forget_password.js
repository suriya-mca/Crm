document.addEventListener('DOMContentLoaded', () => {
    const emailInput = document.getElementById('email-input');
    const dangerEmail = document.getElementById('danger-email');

    emailInput.addEventListener('input', () => {
        if (dangerEmail.innerHTML !== '') {
            dangerEmail.innerHTML = '';
            emailInput.classList.remove('is-danger');
        }
    });

    document.addEventListener('htmx:afterRequest', (event) => {
        if (event.detail.target.id === 'danger-email' && event.detail.successful) {
            emailInput.classList.add('is-danger');
        }
    });
});

document.addEventListener('htmx:afterOnLoad', function(evt) {
    const emailButton = document.getElementById('email-button');
    if (evt.detail.target.id === 'email-button' && evt.detail.xhr.responseText.includes('Email Sent')) {
        emailButton.classList.add('is-static', 'has-text-primary');
        emailButton.textContent = 'Email Sent';
        setTimeout(() => {
            emailButton.classList.remove('is-static', 'has-text-primary');
            emailButton.textContent = 'Send Mail';
        }, 60000);
    }
});