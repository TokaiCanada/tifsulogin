function handleFrameMaterialChange() {
  const frameMaterialSelect = document.getElementById('frameMaterial');
  const selectedValue = frameMaterialSelect.value;

  if (selectedValue === 'Other') {
    const parentDiv = frameMaterialSelect.parentElement;

    // Create input container
    const inputContainer = document.createElement('div');
    inputContainer.classList.add('input-container');

    // Create text input field
    const inputField = document.createElement('input');
    inputField.type = 'text';
    inputField.id = 'frameMaterial';
    inputField.name = 'frameMaterial';
    inputField.placeholder = 'Specify material';
    inputField.classList.add('form-control');

    // Create arrow icon
    const arrowIcon = document.createElement('span');
    arrowIcon.innerHTML = '&#x25C0;'; // Left arrow symbol
    arrowIcon.classList.add('arrow-icon');
    arrowIcon.onclick = function () {
      // Replace input container with select element
      parentDiv.removeChild(inputContainer);
      parentDiv.appendChild(frameMaterialSelect);
      frameMaterialSelect.value = ''; // Reset select value
    };

    // Append input field and arrow icon to the input container
    inputContainer.appendChild(inputField);
    inputContainer.appendChild(arrowIcon);

    // Replace select element with input container
    parentDiv.removeChild(frameMaterialSelect);
    parentDiv.appendChild(inputContainer);
  }
}

document.getElementById('frameMaterial').addEventListener('change', handleFrameMaterialChange);