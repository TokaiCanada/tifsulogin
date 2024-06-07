function updateReference2() {
  const customerCode = document.getElementById('customerCode').value;
  const reference = document.getElementById('reference').value;
  document.getElementById('reference2').value = customerCode + " | " + reference;
}

document.getElementById('customerCode').addEventListener('input', updateReference2);
document.getElementById('reference').addEventListener('input', updateReference2);