document.addEventListener("DOMContentLoaded", function () {
    const pages = document.querySelectorAll(".page");
    const prevButton = document.getElementById("prevPage");
    const nextButton = document.getElementById("nextPage");
    const count = document.getElementById("countPage");
    let currentPage = 0;
  
    function showPage(pageNumber) {
      pages.forEach((page, index) => {
        if (index === pageNumber) {
          page.style.display = "block";
        } else {
          page.style.display = "none";
        }
      });
    }
  
    function updateButtons() {
      prevButton.disabled = currentPage === 0;
      nextButton.disabled = currentPage === pages.length - 1;
      count.innerHTML = currentPage + 1;
    }
  
    prevButton.addEventListener("click", function () {
      if (currentPage > 0) {
        currentPage--;
        showPage(currentPage);
        updateButtons();
      }
    });
  
    nextButton.addEventListener("click", function () {
      if (currentPage < pages.length - 1) {
        currentPage++;
        showPage(currentPage);
        updateButtons();
      }
    });
  
    showPage(currentPage);
    updateButtons();
  });
  