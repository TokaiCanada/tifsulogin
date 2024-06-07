document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form[name="register-form"]');
  const firstNameInput = document.getElementById('customerFirstNameInput');
  const lastNameInput = document.getElementById('customerLastNameInput');
  const birthdateInput = document.getElementById('customerDateInput');
  const firstNameError = document.getElementById('firstNameError');
  const lastNameError = document.getElementById('lastNameError');
  const birthdateError = document.getElementById('birthdateError');

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    event.stopPropagation();

    const emailInput = document.getElementById('customerEmailRegisterInput');
    const isFirstNameValid = validateName(firstNameInput, firstNameError);
    const isLastNameValid = validateName(lastNameInput, lastNameError);
    const isBirthdateValid = validateBirthdate(birthdateInput, birthdateError);
    const isEmailValid = window.validateEmail(emailInput.value);
    const isPasswordValid = window.validatePassword();

    if (isFirstNameValid && isLastNameValid && isBirthdateValid && isEmailValid && isPasswordValid) {
      form.classList.add('was-validated');
      // You can submit the form here if needed
      // form.submit();
    } else {
      form.classList.add('was-validated');
    }
  });

  // Utility function to validate name fields
  function validateName(input, errorElement) {
    const namePattern = /^[a-zA-Z]+$/;
    if (namePattern.test(input.value.trim())) {
      errorElement.style.display = 'none';
      input.classList.remove('is-invalid');
      input.classList.add('is-valid');
      return true;
    } else {
      errorElement.style.display = 'block';
      input.classList.remove('is-valid');
      input.classList.add('is-invalid');
      return false;
    }
  }

  // Utility function to validate birthdate field
  function validateBirthdate(input, errorElement) {
    const birthdatePattern = /^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/\d{4}$/;
    if (birthdatePattern.test(input.value.trim())) {
      errorElement.style.display = 'none';
      input.classList.remove('is-invalid');
      input.classList.add('is-valid');
      return true;
    } else {
      errorElement.style.display = 'block';
      input.classList.remove('is-valid');
      input.classList.add('is-invalid');
      return false;
    }
  }

  // Formatting the birthdate input
  birthdateInput.addEventListener('input', function () {
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
  });
});
