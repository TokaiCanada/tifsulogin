document.getElementById('customerNumberInput').addEventListener('input', function (e) {
  var input = e.target;
  var inputValue = input.value;

  // Remove all non-numeric characters
  inputValue = inputValue.replace(/\D/g, '');

  // Format the input value
  if (inputValue.length > 3 && inputValue.length <= 6) {
    input.value = `(${inputValue.slice(0, 3)}) ${inputValue.slice(3)}`;
  } else if (inputValue.length > 6) {
    input.value = `(${inputValue.slice(0, 3)}) ${inputValue.slice(3, 6)}-${inputValue.slice(6, 10)}`;
  } else {
    input.value = inputValue;
  }
});

document.getElementById('customerNumberInput').addEventListener('keydown', function (e) {
  var key = e.key;
  // Allow control keys (backspace, arrow keys, delete)
  if (key === 'Backspace' || key === 'ArrowLeft' || key === 'ArrowRight' || key === 'Delete') {
    return;
  }

  // Prevent non-numeric keys
  if (!/\d/.test(key)) {
    e.preventDefault();
  }
});