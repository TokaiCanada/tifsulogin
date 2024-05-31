function formatPostalCode(input) {
  let value = input.value.toUpperCase().replace(/\s/g, ''); // Remove existing spaces and convert to uppercase
  if (value.length > 3) {
    value = value.slice(0, 3) + ' ' + value.slice(3);
  }
  input.value = value.slice(0, 7); // Limit to 6 characters + 1 space
}