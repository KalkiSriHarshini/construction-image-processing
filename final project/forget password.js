const forgotPasswordForm = document.getElementById('forgotPasswordForm');
const statusMessage = document.getElementById('statusMessage');

forgotPasswordForm.addEventListener('submit', (event) => {
  event.preventDefault(); 
  const email = document.getElementById('email').value;

  // Validate email (optional)
  if (!isValidEmail(email)) {
    statusMessage.textContent = "Please enter a valid email address.";
    statusMessage.classList.remove('hidden');
    return;
  }

  // Send email request (replace with your actual email sending logic)
  // ... (e.g., using AJAX to send a request to a server-side script)

  statusMessage.textContent = "A password reset link has been sent to your email.";
  statusMessage.classList.remove('hidden');

});

function isValidEmail(email) {
  // Basic email validation (you might need a more robust validation)
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}