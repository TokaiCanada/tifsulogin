document.getElementById('togglePassword2').addEventListener('click', function (e) {
  const passwordInput = document.getElementById('customerRepeatPasswodRegisterInput');
  const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
  passwordInput.setAttribute('type', type);
  this.classList.toggle('fa-eye-slash');
});