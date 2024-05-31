const lensData = [
  { concatenated: "1.60 Neuro 3 Daily", type: "prog" },
  { concatenated: "1.60 Neuro 3 Home", type: "prog" },
  { concatenated: "1.60 Neuro 3X Daily", type: "prog" },
  { concatenated: "1.60 Neuro 3X Home", type: "prog" },
  { concatenated: "1.60 Neuro 5 Daily", type: "prog" },
  { concatenated: "1.60 Neuro 5 Home", type: "prog" },
  { concatenated: "1.60 Neuro 5X Daily", type: "prog" },
  { concatenated: "1.60 NEURO 5X Home", type: "prog" },
  { concatenated: "1.60 NEURO 7X Daily", type: "prog" },
  { concatenated: "1.60 Neuro 7X Home", type: "prog" },
  { concatenated: "1.60 NEURO 9X Daily", type: "prog" },
  { concatenated: "1.60 NEURO 9X Home", type: "prog" },
  { concatenated: "1.60 ClairArte", type: "prog" },
  { concatenated: "1.60 Polarized ClairArte", type: "prog" },
  { concatenated: "1.60 Polarized Single Vision", type: "sv" },
  { concatenated: "1.60 Single Vision", type: "sv" },
  { concatenated: "1.60 Aspheric Single Vision", type: "sv" },
  { concatenated: "1.60 Bi-AS Single Vision", type: "sv" },
  { concatenated: "1.67 Polarized Single Vision", type: "sv" },
  { concatenated: "1.70 Neuro 3 Daily", type: "prog" },
  { concatenated: "1.70 Neuro 3 Home", type: "prog" },
  { concatenated: "1.70 Neuro 3X Daily", type: "prog" },
  { concatenated: "1.70 Neuro 3X Home", type: "prog" },
  { concatenated: "1.70 Neuro 5 Daily", type: "prog" },
  { concatenated: "1.70 Neuro 5 Home", type: "prog" },
  { concatenated: "1.70 Neuro 5X Daily", type: "prog" },
  { concatenated: "1.70 NEURO 5X Home", type: "prog" },
  { concatenated: "1.70 NEURO 7X Daily", type: "prog" },
  { concatenated: "1.70 Neuro 7X Home", type: "prog" },
  { concatenated: "1.70 NEURO 9X Daily", type: "prog" },
  { concatenated: "1.70 NEURO 9X Home", type: "prog" },
  { concatenated: "1.70 ClairArte", type: "prog" },
  { concatenated: "1.70 Aspheric Single Vision", type: "sv" },
  { concatenated: "1.70 Bi-AS Single Vision", type: "sv" },
  { concatenated: "1.76 Neuro 3 Daily", type: "prog" },
  { concatenated: "1.76 Neuro 3 Home", type: "prog" },
  { concatenated: "1.76 Neuro 3X Daily", type: "prog" },
  { concatenated: "1.76 Neuro 3X Home", type: "prog" },
  { concatenated: "1.76 Neuro 5 Daily", type: "prog" },
  { concatenated: "1.76 Neuro 5 Home", type: "prog" },
  { concatenated: "1.76 Neuro 5X Daily", type: "prog" },
  { concatenated: "1.76 NEURO 5X Home", type: "prog" },
  { concatenated: "1.76 NEURO 7X Daily", type: "prog" },
  { concatenated: "1.76 Neuro 7X Home", type: "prog" },
  { concatenated: "1.76 NEURO 9X Daily", type: "prog" },
  { concatenated: "1.76 NEURO 9X Home", type: "prog" },
  { concatenated: "1.76 ClairArte", type: "prog" },
  { concatenated: "1.70 Aspheric Single Vision", type: "sv" },
  { concatenated: "1.70 Bi-AS Single Vision", type: "sv" },
  { concatenated: "1.60 Lutina  Single Vision", type: "sv" },
  { concatenated: "1.60 Lutina  Bi-AS Single Vision", type: "sv" },
  { concatenated: "1.60 Lutina  Neuro 3 Daily", type: "prog" },
  { concatenated: "1.60 Lutina  Neuro 3 Home", type: "prog" },
  { concatenated: "1.60 Lutina  Neuro 3X Daily", type: "prog" },
  { concatenated: "1.60 Lutina  Neuro 3X Home", type: "prog" },
  { concatenated: "1.60 Lutina  Neuro 5 Daily", type: "prog" },
  { concatenated: "1.60 Lutina  Neuro 5 Home", type: "prog" },
  { concatenated: "1.60 Lutina  Neuro 5X Daily", type: "prog" },
  { concatenated: "1.60 Lutina  NEURO 5X Home", type: "prog" },
  { concatenated: "1.60 Lutina  NEURO 7X Daily", type: "prog" },
  { concatenated: "1.60 Lutina  Neuro 7X Home", type: "prog" },
  { concatenated: "1.60 Lutina  NEURO 9X Daily", type: "prog" },
  { concatenated: "1.60 Lutina  NEURO 9X Home", type: "prog" },
  { concatenated: "1.60 Lutina  Aspheric Single Vision", type: "sv" },
  { concatenated: "1.67 Lutina  Bi-AS Single Vision", type: "sv" },
  { concatenated: "1.67 Lutina  Neuro 3 Daily", type: "prog" },
  { concatenated: "1.67 Lutina  Neuro 3 Home", type: "prog" },
  { concatenated: "1.67 Lutina  Neuro 3X Daily", type: "prog" },
  { concatenated: "1.67 Lutina  Neuro 3X Home", type: "prog" },
  { concatenated: "1.67 Lutina  Neuro 5 Daily", type: "prog" },
  { concatenated: "1.67 Lutina  Neuro 5 Home", type: "prog" },
  { concatenated: "1.67 Lutina  Neuro 5X Daily", type: "prog" },
  { concatenated: "1.67 Lutina  NEURO 5X Home", type: "prog" },
  { concatenated: "1.67 Lutina  NEURO 7X Daily", type: "prog" },
  { concatenated: "1.67 Lutina  Neuro 7X Home", type: "prog" },
  { concatenated: "1.67 Lutina  NEURO 9X Daily", type: "prog" },
  { concatenated: "1.67 Lutina  NEURO 9X Home", type: "prog" },
  { concatenated: "1.67 Lutina  Aspheric Single Vision", type: "sv" },
  { concatenated: "1.76 Lutina  Bi-AS Single Vision", type: "sv" },
  { concatenated: "1.76 Lutina  Neuro 3 Daily", type: "prog" },
  { concatenated: "1.76 Lutina  Neuro 3 Home", type: "prog" },
  { concatenated: "1.76 Lutina  Neuro 3X Daily", type: "prog" },
  { concatenated: "1.76 Lutina  Neuro 3X Home", type: "prog" },
  { concatenated: "1.76 Lutina  Neuro 5 Daily", type: "prog" },
  { concatenated: "1.76 Lutina  Neuro 5 Home", type: "prog" },
  { concatenated: "1.76 Lutina  Neuro 5X Daily", type: "prog" },
  { concatenated: "1.76 Lutina  NEURO 5X Home", type: "prog" },
  { concatenated: "1.76 Lutina  NEURO 7X Daily", type: "prog" },
  { concatenated: "1.76 Lutina  Neuro 7X Home", type: "prog" },
  { concatenated: "1.76 Lutina  NEURO 9X Daily", type: "prog" },
  { concatenated: "1.76 Lutina  NEURO 9X Home", type: "prog" },
  { concatenated: "1.76 Lutina  Aspheric Single Vision", type: "sv" },
  { concatenated: "1.60 Photo Brown Bi-AS Single Vision", type: "sv" },
  { concatenated: "1.60 Photo Grey Bi-AS Single Vision", type: "sv" },
  { concatenated: "1.60 Photo Brown Neuro 3 Daily", type: "prog" },
  { concatenated: "1.60 Photo Grey Neuro 3 Daily", type: "prog" },
  { concatenated: "1.60 Photo Brown Neuro 3 Home", type: "prog" },
  { concatenated: "1.60 Photo Grey Neuro 3 Home", type: "prog" },
  { concatenated: "1.60 Photo Brown Neuro 3X Daily", type: "prog" },
  { concatenated: "1.60 Photo Grey Neuro 3X Daily", type: "prog" },
  { concatenated: "1.60 Photo Brown Neuro 3X Home", type: "prog" },
  { concatenated: "1.60 Photo Grey Neuro 3X Home", type: "prog" },
  { concatenated: "1.60 Photo Brown Neuro 5 Daily", type: "prog" },
  { concatenated: "1.60 Photo Grey Neuro 5 Daily", type: "prog" },
  { concatenated: "1.60 Photo Brown Neuro 5 Home", type: "prog" },
  { concatenated: "1.60 Photo Grey Neuro 5 Home", type: "prog" },
  { concatenated: "1.60 Photo Brown Neuro 5X Daily", type: "prog" },
  { concatenated: "1.60 Photo Grey Neuro 5X Daily", type: "prog" },
  { concatenated: "1.60 Photo Brown NEURO 5X Home", type: "prog" },
  { concatenated: "1.60 Photo Grey NEURO 5X Home", type: "prog" },
  { concatenated: "1.60 Photo Brown NEURO 7X Daily", type: "prog" },
  { concatenated: "1.60 Photo Grey NEURO 7X Daily", type: "prog" },
  { concatenated: "1.60 Photo Brown Neuro 7X Home", type: "prog" },
  { concatenated: "1.60 Photo Grey Neuro 7X Home", type: "prog" },
  { concatenated: "1.60 Photo Brown NEURO 9X Daily", type: "prog" },
  { concatenated: "1.60 Photo Grey NEURO 9X Daily", type: "prog" },
  { concatenated: "1.60 Photo Brown NEURO 9X Home", type: "prog" },
  { concatenated: "1.60 Photo Grey NEURO 9X Home", type: "prog" },
  { concatenated: "1.60 Photo Brown ClairArte", type: "prog" },
  { concatenated: "1.60 Photo Grey ClairArte", type: "prog" },
  { concatenated: "1.60 Photo Brown Aspheric Single Vision", type: "sv" },
  { concatenated: "1.60 Photo Grey Aspheric Single Vision", type: "sv" },
  { concatenated: "1.67 Photo Brown  Bi-AS Single Vision", type: "sv" },
  { concatenated: "1.67 Photo Grey Bi-AS Single Vision", type: "sv" },
  { concatenated: "1.67 Photo Brown  Neuro 3 Daily", type: "prog" },
  { concatenated: "1.67 Photo Grey Neuro 3 Daily", type: "prog" },
  { concatenated: "1.67 Photo Brown  Neuro 3 Home", type: "prog" },
  { concatenated: "1.67 Photo Grey Neuro 3 Home", type: "prog" },
  { concatenated: "1.67 Photo Brown  Neuro 3X Daily", type: "prog" },
  { concatenated: "1.67 Photo Grey Neuro 3X Daily", type: "prog" },
  { concatenated: "1.67 Photo Brown  Neuro 3X Home", type: "prog" },
  { concatenated: "1.67 Photo Grey Neuro 3X Home", type: "prog" },
  { concatenated: "1.67 Photo Brown  Neuro 5 Daily", type: "prog" },
  { concatenated: "1.67 Photo Grey Neuro 5 Daily", type: "prog" },
  { concatenated: "1.67 Photo Brown  Neuro 5 Home", type: "prog" },
  { concatenated: "1.67 Photo Grey Neuro 5 Home", type: "prog" },
  { concatenated: "1.67 Photo Brown  Neuro 5X Daily", type: "prog" },
  { concatenated: "1.67 Photo Grey Neuro 5X Daily", type: "prog" },
  { concatenated: "1.67 Photo Brown  NEURO 5X Home", type: "prog" },
  { concatenated: "1.67 Photo Grey NEURO 5X Home", type: "prog" },
  { concatenated: "1.67 Photo Brown  NEURO 7X Daily", type: "prog" },
  { concatenated: "1.67 Photo Grey NEURO 7X Daily", type: "prog" },
  { concatenated: "1.67 Photo Brown  Neuro 7X Home", type: "prog" },
  { concatenated: "1.67 Photo Grey Neuro 7X Home", type: "prog" },
  { concatenated: "1.67 Photo Brown  NEURO 9X Daily", type: "prog" },
  { concatenated: "1.67 Photo Grey NEURO 9X Daily", type: "prog" },
  { concatenated: "1.67 Photo Brown  NEURO 9X Home", type: "prog" },
  { concatenated: "1.67 Photo Grey NEURO 9X Home", type: "prog" },
  { concatenated: "1.67 Photo Brown  ClairArte", type: "prog" },
  { concatenated: "1.67 Photo Grey ClairArte", type: "prog" },
  { concatenated: "1.67 Photo Brown  Aspheric Single Vision", type: "sv" },
  { concatenated: "1.67 Photo Grey Aspheric Single Vision", type: "sv" },
  { concatenated: "1.76 Photo Brown  Bi-AS Single Vision", type: "sv" },
  { concatenated: "1.76 Photo Grey Bi-AS Single Vision", type: "sv" },
  { concatenated: "1.76 Photo Brown  Neuro 3 Daily", type: "prog" },
  { concatenated: "1.76 Photo Grey Neuro 3 Daily", type: "prog" },
  { concatenated: "1.76 Photo Brown  Neuro 3 Home", type: "prog" },
  { concatenated: "1.76 Photo Grey Neuro 3 Home", type: "prog" },
  { concatenated: "1.76 Photo Brown  Neuro 3X Daily", type: "prog" },
  { concatenated: "1.76 Photo Grey Neuro 3X Daily", type: "prog" },
  { concatenated: "1.76 Photo Brown  Neuro 3X Home", type: "prog" },
  { concatenated: "1.76 Photo Grey Neuro 3X Home", type: "prog" },
  { concatenated: "1.76 Photo Brown  Neuro 5 Daily", type: "prog" },
  { concatenated: "1.76 Photo Grey Neuro 5 Daily", type: "prog" },
  { concatenated: "1.76 Photo Brown  Neuro 5 Home", type: "prog" },
  { concatenated: "1.76 Photo Grey Neuro 5 Home", type: "prog" },
  { concatenated: "1.76 Photo Brown  Neuro 5X Daily", type: "prog" },
  { concatenated: "1.76 Photo Grey Neuro 5X Daily", type: "prog" },
  { concatenated: "1.76 Photo Brown  NEURO 5X Home", type: "prog" },
  { concatenated: "1.76 Photo Grey NEURO 5X Home", type: "prog" },
  { concatenated: "1.76 Photo Brown  NEURO 7X Daily", type: "prog" },
  { concatenated: "1.76 Photo Grey NEURO 7X Daily", type: "prog" },
  { concatenated: "1.76 Photo Brown  Neuro 7X Home", type: "prog" },
  { concatenated: "1.76 Photo Grey Neuro 7X Home", type: "prog" },
  { concatenated: "1.76 Photo Brown  NEURO 9X Daily", type: "prog" },
  { concatenated: "1.76 Photo Grey NEURO 9X Daily", type: "prog" },
  { concatenated: "1.76 Photo Brown  NEURO 9X Home", type: "prog" },
  { concatenated: "1.76 Photo Grey NEURO 9X Home", type: "prog" },
  { concatenated: "1.76 Photo Brown  ClairArte", type: "prog" },
  { concatenated: "1.76 Photo Grey ClairArte", type: "prog" },
  { concatenated: "1.76 Photo Brown  Aspheric Single Vision", type: "sv" },
  { concatenated: "1.76 Photo Grey Aspheric Single Vision", type: "sv" },
  { concatenated: "1.60 Transition Gen8 Brown Single Vision", type: "sv" },
  { concatenated: "1.60 Transitions Gen8 Grey Single Vision", type: "sv" },
  { concatenated: "1.60 Transition Gen8 Brown Neuro 3 Daily", type: "prog" },
  { concatenated: "1.60 Transitions Gen8 Grey Neuro 3 Daily", type: "prog" },
  { concatenated: "1.60 Transition Gen8 Brown Neuro 3 Home", type: "prog" },
  { concatenated: "1.60 Transitions Gen8 Grey Neuro 3 Home", type: "prog" },
  { concatenated: "1.60 Transition Gen8 Brown Neuro 5 Daily", type: "prog" },
  { concatenated: "1.60 Transitions Gen8 Grey Neuro 5 Daily", type: "prog" },
  { concatenated: "1.60 Transition Gen8 Brown Neuro 5 Home", type: "prog" },
  { concatenated: "1.60 Transitions Gen8 Grey Neuro 5 Home", type: "prog" },
  { concatenated: "1.60 Transition Gen8 Brown ClairArte", type: "prog" },
  { concatenated: "1.60 Transitions Gen8 Grey ClairArte", type: "prog" },
  { concatenated: "1.70 Transition Gen8 Brown Neuro 3 Daily", type: "prog" },
  { concatenated: "1.70 Transitions Gen8 Grey Neuro 3 Daily", type: "prog" },
  { concatenated: "1.70 Transition Gen8 Brown Neuro 3 Home", type: "prog" },
  { concatenated: "1.70 Transitions Gen8 Grey Neuro 3 Home", type: "prog" },
  { concatenated: "1.70 Transition Gen8 Brown Neuro 5 Daily", type: "prog" },
  { concatenated: "1.70 Transitions Gen8 Grey Neuro 5 Daily", type: "prog" },
  { concatenated: "1.70 Transition Gen8 Brown Neuro 5 Home", type: "prog" },
  { concatenated: "1.70 Transitions Gen8 Grey Neuro 5 Home", type: "prog" },
  { concatenated: "1.70 Transition Gen8 Brown ClairArte", type: "prog" },
  { concatenated: "1.70 Transitions Gen8 Grey ClairArte", type: "prog" },
  { concatenated: "1.70 Transition Gen8 Brown Aspheric Single Vision", type: "sv" },
  { concatenated: "1.70 Transitions Gen8 Grey Aspheric Single Vision", type: "sv" },
  { concatenated: "1.76 Transition Gen8 Brown Neuro 3 Daily", type: "prog" },
  { concatenated: "1.76 Transitions Gen8 Grey Neuro 3 Daily", type: "prog" },
  { concatenated: "1.76 Transition Gen8 Brown Neuro 3 Home", type: "prog" },
  { concatenated: "1.76 Transitions Gen8 Grey Neuro 3 Home", type: "prog" },
  { concatenated: "1.76 Transition Gen8 Brown Neuro 3X Daily", type: "prog" },
  { concatenated: "1.76 Transitions Gen8 Grey Neuro 3X Daily", type: "prog" },
  { concatenated: "1.76 Transition Gen8 Brown Neuro 5 Daily", type: "prog" },
  { concatenated: "1.76 Transitions Gen8 Grey Neuro 5 Daily", type: "prog" },
  { concatenated: "1.76 Transition Gen8 Brown Neuro 5 Home", type: "prog" },
  { concatenated: "1.76 Transitions Gen8 Grey Neuro 5 Home", type: "prog" },
  { concatenated: "1.76 Transition Gen8 Brown Neuro 5X Daily", type: "prog" },
  { concatenated: "1.76 Transitions Gen8 Grey Neuro 5X Daily", type: "prog" },
  { concatenated: "1.76 Transition Gen8 Brown NEURO 7X Daily", type: "prog" },
  { concatenated: "1.76 Transitions Gen8 Grey NEURO 7X Daily", type: "prog" },
  { concatenated: "1.76 Transition Gen8 Brown Neuro 7X Home", type: "prog" },
  { concatenated: "1.76 Transitions Gen8 Grey Neuro 7X Home", type: "prog" },
  { concatenated: "1.76 Transition Gen8 Brown NEURO 9X Daily", type: "prog" },
  { concatenated: "1.76 Transitions Gen8 Grey NEURO 9X Daily", type: "prog" },
  { concatenated: "1.76 Transition Gen8 Brown ClairArte", type: "prog" },
  { concatenated: "1.76 Transitions Gen8 Grey ClairArte", type: "prog" },
  { concatenated: "1.60 Transition XtrActive Single Vision", type: "sv" },
  { concatenated: "1.60 Transition XtrActive Neuro 3 Daily", type: "prog" },
  { concatenated: "1.60 Transition XtrActive Neuro 3 Home", type: "prog" },
  { concatenated: "1.60 Transition XtrActive Neuro 5 Daily", type: "prog" },
  { concatenated: "1.60 Transition XtrActive Neuro 5 Home", type: "prog" },
];

function filterOptions(value, side) {
  const optionsDiv = document.getElementById(`lens${side}-options`);
  optionsDiv.innerHTML = '';

  const filteredData = value.length > 0 ?
    lensData.filter(item => item.concatenated.toLowerCase().includes(value.toLowerCase())) :
    lensData;

  filteredData.forEach(item => {
    const option = document.createElement('div');
    option.textContent = item.concatenated;
    option.onclick = () => selectOption(item.concatenated, side, item.type);
    optionsDiv.appendChild(option);
  });

  optionsDiv.classList.add('show');
}

function showAllOptions(side) {
  filterOptions('', side);
}

function toggleDropdown(side) {
  const optionsDiv = document.getElementById(`lens${side}-options`);
  if (optionsDiv.classList.contains('show')) {
    optionsDiv.classList.remove('show');
  } else {
    filterOptions('', side);
  }
}

function selectOption(value, side, type) {
  const targetInput = document.getElementById(`lens${side}`);
  targetInput.value = value;
  document.getElementById(`lens${side}-options`).innerHTML = '';
  document.getElementById(`lens${side}-options`).classList.remove('show');

  if (type === 'sv') {
    document.querySelectorAll('.prog-only').forEach(el => el.style.display = 'none');
  } else {
    document.querySelectorAll('.prog-only').forEach(el => el.style.display = 'table-cell');
  }

  syncLensValues(side);
}

function toggleDuplicate() {
  syncLensValues();
}

function syncLensValues(changedSide) {
  const isDuplicate = document.getElementById('duplicateLens').checked;
  if (isDuplicate) {
    const lensR = document.getElementById('lensR');
    const lensL = document.getElementById('lensL');
    if (changedSide === 'R' || !changedSide) {
      lensL.value = lensR.value;
    } else if (changedSide === 'L') {
      lensR.value = lensL.value;
    }
  }
}

document.addEventListener('click', function (event) {
  const dropdowns = document.querySelectorAll('.dropdown-content');
  dropdowns.forEach(dropdown => {
    if (!dropdown.parentElement.contains(event.target)) {
      dropdown.classList.remove('show');
    }
  });
});

document.querySelectorAll('.prog-only').forEach(el => el.style.display = 'none');