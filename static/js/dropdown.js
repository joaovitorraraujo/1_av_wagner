document.addEventListener("DOMContentLoaded", function () {
  const dropdownButton = document.getElementById("dropdownNavbarLink");
  const dropdownMenu = document.getElementById("dropdownNavbar");

  dropdownButton.addEventListener("click", function () {
    const isHidden = dropdownMenu.classList.contains("hidden");

    if (isHidden) {
      dropdownMenu.classList.remove("hidden", "opacity-0", "scale-95");
      dropdownMenu.classList.add("opacity-100", "scale-100");
    } else {
      dropdownMenu.classList.add("opacity-0", "scale-95");
      setTimeout(() => {
        dropdownMenu.classList.add("hidden");
      }, 300); // Espera a transição terminar antes de esconder
    }
  });

  // Fecha o dropdown ao clicar fora dele
  document.addEventListener("click", function (event) {
    if (
      !dropdownButton.contains(event.target) &&
      !dropdownMenu.contains(event.target)
    ) {
      dropdownMenu.classList.add("opacity-0", "scale-95");
      setTimeout(() => {
        dropdownMenu.classList.add("hidden");
      }, 300);
    }
  });
});
