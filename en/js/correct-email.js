document.addEventListener('DOMContentLoaded', function () {
  const emailInput = document.getElementById('customerEmailRegisterInput');
  const emailError = document.getElementById('emailError');

  emailInput.addEventListener('input', function () {
    validateEmail(emailInput.value);
  });

  window.validateEmail = function (email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailPattern.test(email)) {
      emailError.style.display = 'none';
      emailInput.classList.remove('is-invalid');
      emailInput.classList.add('is-valid');
      return true;
    } else {
      emailError.style.display = 'block';
      emailInput.classList.remove('is-valid');
      emailInput.classList.add('is-invalid');
      return false;
    }
  }
});
