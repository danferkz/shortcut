document.addEventListener("DOMContentLoaded", function() {
    const newLinkButton = document.getElementById("new-link-btn");
    const newLinkPopup = document.getElementById("new-link-popup");
    const cancelButton = document.getElementById("cancel-btn");

    newLinkButton.addEventListener("click", function() {
        newLinkPopup.style.display = "block";
    });

    cancelButton.addEventListener("click", function() {
        newLinkPopup.style.display = "none";
    });
});
