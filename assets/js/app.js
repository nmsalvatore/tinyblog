const dropdownArrow = document.querySelector(".blog-list-dropdown-arrow");
const dropdown = document.querySelector(".blog-list-dropdown");

document.addEventListener("click", (e) => {
    if (e.target === dropdownArrow) {
        if (dropdown.style.display === "none") {
            dropdown.style.display = "block";
        } else {
            dropdown.style.display = "none";
        }
    } else if (e.target !== dropdown || e.target.parentElement !== dropdown) {
        dropdown.style.display = "none";
    }
});
