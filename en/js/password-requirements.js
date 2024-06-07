document.addEventListener('DOMContentLoaded', function () {
    const passwordInput = document.getElementById('customerPasswordRegisterInput');
    const passwordSpecialMessage = document.getElementById('passwordSpecial');
    const passwordCapitalMessage = document.getElementById('passwordCapital');
    const passwordLengthMessage = document.getElementById('passwordLength');
    const togglePassword = document.getElementById('togglePassword');
  
    passwordInput.addEventListener('input', function () {
      window.validatePassword();
    });
  
    togglePassword.addEventListener('click', function () {
      togglePasswordVisibility(passwordInput, togglePassword);
    });
  
    window.validatePassword = function () {
      const password = passwordInput.value;
      let isValid = true;
  
      if (!/[^a-zA-Z0-9]/.test(password)) {
        passwordSpecialMessage.style.display = 'flex';
        isValid = false;
      } else {
        passwordSpecialMessage.style.display = 'none';
      }
  
      if (!/[A-Z]/.test(password)) {
        passwordCapitalMessage.style.display = 'flex';
        isValid = false;
      } else {
        passwordCapitalMessage.style.display = 'none';
      }
  
      if (password.length < 8) {
        passwordLengthMessage.style.display = 'flex';
        isValid = false;
      } else {
        passwordLengthMessage.style.display = 'none';
      }
  
      if (isValid) {
        passwordInput.classList.remove('is-invalid');
        passwordInput.classList.add('is-valid');
      } else {
        passwordInput.classList.remove('is-valid');
        passwordInput.classList.add('is-invalid');
      }
  
      return isValid;
    };
  
    function togglePasswordVisibility(input, toggleIcon) {
      const type = input.getAttribute('type') === 'password' ? 'text' : 'password';
      input.setAttribute('type', type);
      toggleIcon.classList.toggle('fa-eye-slash');
      toggleIcon.classList.toggle('fa-eye');
    }
  });
  