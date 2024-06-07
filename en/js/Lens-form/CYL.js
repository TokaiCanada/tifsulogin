function formatCYL(input) {
  let value = input.value;
  if (value === "") return;

  let number = parseFloat(value);

  if (isNaN(number)) {
    input.value = "";
    return;
  }

  let formattedValue = number.toFixed(2);

  if (number > 0 && !formattedValue.startsWith("-")) {
    formattedValue = "-" + formattedValue;
  }

  input.value = formattedValue;
}

function allowOnlyNumbers(event) {
  const key = event.key;
  if (!/[0-9]/.test(key) && key !== "Backspace" && key !== "ArrowLeft" && key !== "ArrowRight" && key !== "Tab" && key !== "." && key !== "-") {
    event.preventDefault();
  }
}

document.querySelectorAll('.r-l-data-table input[id^="cyl"]').forEach(input => {
  input.addEventListener('keydown', allowOnlyNumbers);
  input.addEventListener('blur', function () {
    formatCYL(input);
  });
});
