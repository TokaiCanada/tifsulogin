function formatToOneDecimal(input) {
  let value = input.value;
  if (value === "") return;

  let number = parseFloat(value);

  let formattedValue = number.toFixed(1);

  input.value = formattedValue;
}

function allowOnlyNumbers(event) {
  const key = event.key;
  if (!/[0-9]/.test(key) && key !== "Backspace" && key !== "ArrowLeft" && key !== "ArrowRight" && key !== "Tab" && key !== ".") {
    event.preventDefault();
  }
}

function calculateFPD() {
  const a = parseFloat(document.getElementById('a').value);
  const bridge = parseFloat(document.getElementById('bridge').value);

  if (!isNaN(a) && !isNaN(bridge)) {
    const fpd = a + bridge;
    document.getElementById('fpd').value = fpd.toFixed(1);
  } else {
    document.getElementById('fpd').value = '';
  }
}

document.querySelectorAll('.r-l-data-table input[id^="pd"], .r-l-data-table input[id^="height"], #b, #a, #bridge').forEach(input => {
  input.addEventListener('keydown', allowOnlyNumbers);
  input.addEventListener('blur', function () {
    formatToOneDecimal(input);
  });
});

document.getElementById('a').addEventListener('blur', calculateFPD);
document.getElementById('bridge').addEventListener('blur', calculateFPD);