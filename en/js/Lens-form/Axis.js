function allowOnlyNumbers(event) {
  const key = event.key;
  if (!/[0-9]/.test(key) && key !== "Backspace" && key !== "ArrowLeft" && key !== "ArrowRight" && key !== "Tab") {
    event.preventDefault();
  }
}

document.querySelectorAll('.r-l-data-table input[id^="axis"]').forEach(input => {
  input.addEventListener('keydown', allowOnlyNumbers);
});
