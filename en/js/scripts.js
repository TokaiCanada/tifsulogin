var customSelects = document.getElementsByClassName("custom-select");
for (var i = 0; i < customSelects.length; i++) {
  var select = customSelects[i].getElementsByTagName("select")[0];
  var selectedOption = select.options[select.selectedIndex];
  var selectedText = selectedOption.textContent || selectedOption.innerText;

  var selectSelected = document.createElement("div");
  selectSelected.classList.add("select-selected");
  selectSelected.innerHTML = selectedText;
  customSelects[i].appendChild(selectSelected);

  var selectItems = document.createElement("div");
  selectItems.classList.add("select-items");
  for (var j = 0; j < select.length; j++) {
    var option = select.options[j];
    var item = document.createElement("div");
    item.innerHTML = option.textContent || option.innerText;
    item.addEventListener("click", function () {
      selectSelected.innerHTML = this.innerHTML;
      select.value = this.innerHTML;
      selectItems.style.display = "none";
    });
    selectItems.appendChild(item);
  }
  customSelects[i].appendChild(selectItems);

  selectSelected.addEventListener("click", function () {
    this.nextSibling.style.display = "block";
  });

  document.addEventListener("click", function (e) {
    if (!e.target.matches(".select-selected")) {
      var items = document.getElementsByClassName("select-items");
      for (var k = 0; k < items.length; k++) {
        items[k].style.display = "none";
      }
    }
  });
}