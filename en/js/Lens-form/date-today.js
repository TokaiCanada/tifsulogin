function formatDate(date) {
  const options = { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric',
  };
  return date.toLocaleDateString(undefined, options);
}

function setTodayDate() {
  const today = new Date();
  const formattedDate = formatDate(today);
  document.getElementById('setTodayDateButton').textContent = formattedDate;
}

document.getElementById('setTodayDateButton').addEventListener('click', setTodayDate);
