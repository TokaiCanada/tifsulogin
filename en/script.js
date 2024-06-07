document.addEventListener('DOMContentLoaded', () => {
  const nameInput = document.getElementById("name");
  const lastNameInput = document.getElementById("lastName");
  const emailInput = document.getElementById("email");
  const birthdateInput = document.getElementById("customerDateInput");
  const passwordInput = document.getElementById("password");
  const togglePasswordIcon = document.getElementById("togglePassword");

  togglePasswordIcon.addEventListener('click', () => {
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
    togglePasswordIcon.classList.toggle('fa-eye-slash');
    togglePasswordIcon.classList.toggle('fa-eye');
  });

  const nameError = document.getElementById("name-error");
  const lastNameError = document.getElementById("lastName-error");
  const emailError = document.getElementById("email-error");
  const passwordError = document.getElementById("password-error");

  const birthdateError = document.createElement('p');
  birthdateError.id = 'birthdateError';
  birthdateError.classList.add('error-message');
  birthdateError.style.display = 'none';
  birthdateError.innerHTML = 'Please enter a valid birthdate.';
  birthdateInput.parentNode.appendChild(birthdateError);

  nameInput.addEventListener('input', validateName);
  lastNameInput.addEventListener('input', validateLastName);
  emailInput.addEventListener('input', validateEmail);
  passwordInput.addEventListener('input', validatePassword);
  birthdateInput.addEventListener('input', formatAndValidateBirthdate);
  birthdateInput.addEventListener('change', markBirthdateAsValid);

  document.getElementById('myForm').addEventListener('submit', function (event) {
    let isValid = true;
    isValid &= validateName();
    isValid &= validateLastName();
    isValid &= validateEmail();
    isValid &= validatePassword();
    isValid &= validateBirthdate(birthdateInput.value);

    if (!isValid) {
      event.preventDefault();
    }
  });

  function validateName() {
    nameError.textContent = "";
    if (nameInput.value === "" || /\d/.test(nameInput.value)) {
      nameError.textContent = "Please enter your name properly.";
      nameInput.classList.add('is-invalid');
      nameInput.classList.remove('is-valid');
      return false;
    } else {
      nameInput.classList.remove('is-invalid');
      nameInput.classList.add('is-valid');
    }
    return true;
  }

  function validateLastName() {
    lastNameError.textContent = "";
    if (lastNameInput.value === "" || /\d/.test(lastNameInput.value)) {
      lastNameError.textContent = "Please enter your last name properly.";
      lastNameInput.classList.add('is-invalid');
      lastNameInput.classList.remove('is-valid');
      return false;
    } else {
      lastNameInput.classList.remove('is-invalid');
      lastNameInput.classList.add('is-valid');
    }
    return true;
  }

  function validateEmail() {
    emailError.textContent = "";
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailInput.value === "" || !emailRegex.test(emailInput.value)) {
      emailError.textContent = "Please enter a valid email address.";
      emailInput.classList.add('is-invalid');
      emailInput.classList.remove('is-valid');
      return false;
    } else {
      emailInput.classList.remove('is-invalid');
      emailInput.classList.add('is-valid');
    }
    return true;
  }

  function validatePassword() {
    passwordError.textContent = "";
    const password = passwordInput.value;
    const passwordErrors = [];

    if (password.length < 8) {
      passwordErrors.push("8 characters long");
    }
    if (!/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
      passwordErrors.push("one special character");
    }
    if (!/[A-Z]/.test(password)) {
      passwordErrors.push("one uppercase letter");
    }
    if (!/[a-z]/.test(password)) {
      passwordErrors.push("one lowercase letter");
    }

    if (passwordErrors.length > 0) {
      const concatenatedErrors = `Password must contain at least ${passwordErrors.join(', ')}.`;
      passwordError.textContent = concatenatedErrors;
      passwordInput.classList.add('is-invalid');
      passwordInput.classList.remove('is-valid');
    } else {
      passwordInput.classList.remove('is-invalid');
      passwordInput.classList.add('is-valid');
    }
    return true;
  }

  function formatAndValidateBirthdate() {
    let value = birthdateInput.value.replace(/[^0-9]/g, ''); // Remove all non-numeric characters
    let formattedValue = '';

    if (value.length > 0) {
      formattedValue += value.substring(0, 2); // Add day part
      if (value.length > 2) {
        formattedValue += '/' + value.substring(2, 4); // Add month part
        if (value.length > 4) {
          formattedValue += '/' + value.substring(4, 8); // Add year part
        }
      }
    }

    birthdateInput.value = formattedValue;
    validateBirthdate(formattedValue);
  }

  function validateBirthdate(value) {
    const birthdatePattern = /^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/\d{4}$/;
    if (birthdatePattern.test(value)) {
      birthdateError.style.display = 'none';
      birthdateInput.classList.remove('is-invalid');
      birthdateInput.classList.add('is-valid');
    } else {
      birthdateError.style.display = 'block';
      birthdateInput.classList.remove('is-valid');
      birthdateInput.classList.add('is-invalid');
    }
  }

  function markBirthdateAsValid() {
    birthdateInput.classList.remove('is-invalid');
    birthdateInput.classList.add('is-valid');
    birthdateError.style.display = 'none';
  }
});
