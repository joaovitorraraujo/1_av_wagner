const valueForm = document.getElementById("value");

valueForm.addEventListener("input", () => {
  if (valueForm.value.length > 8) {
    valueForm.value = valueForm.value.slice(0, 8);
  }
});
