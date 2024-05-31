function formatADD(input) {
  let value = input.value;
  if (value === "") return;

  // Handle the input as cents if no decimal point is present
  let number;
  if (!value.includes(".")) {
    if (value.length === 1) {
      number = parseFloat("0.0" + value);
    } else if (value.length === 2) {
      number = parseFloat("0." + value);
    } else {
      number = parseFloat(value.slice(0, -2) + "." + value.slice(-2));
    }
  } else {
    number = parseFloat(value);
  }

  if (isNaN(number)) {
    input.value = "";
    return;
  }

  let formattedValue = number.toFixed(2);
  input.value = formattedValue;
}

function allowOnlyNumbers(event) {
  const key = event.key;
  if (!/[0-9]/.test(key) && key !== "Backspace" && key !== "ArrowLeft" && key !== "ArrowRight" && key !== "Tab" && key !== "." && key !== "-") {
    event.preventDefault();
  }
}

document.querySelectorAll('.r-l-data-table input[id^="add"]').forEach(input => {
  input.addEventListener('keydown', allowOnlyNumbers);
  input.addEventListener('blur', function () {
    formatADD(input);
  });
});
