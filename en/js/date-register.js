document.addEventListener('DOMContentLoaded', function () {
  const birthdateInput = document.getElementById('customerDateInput');
  const birthdateError = document.createElement('p');
  birthdateError.id = 'birthdateError';
  birthdateError.classList.add('error-message');
  birthdateError.style.display = 'none';
  birthdateError.innerHTML = '<i class="fa fa-exclamation-circle" aria-hidden="true"></i> Please enter a valid birthdate.';
  birthdateInput.parentNode.appendChild(birthdateError);

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

    validateBirthdate(birthdateInput.value);
  });

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
});
