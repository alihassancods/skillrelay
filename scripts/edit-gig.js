const dialogBoxGigs = document.getElementById("gig-dialog");
const openDialogBtnGigs = document.querySelector(".open-dialog-btn-gigs");
const closeDialogBtnGigs = document.querySelector(".close-dialog-btn-gigs");

openDialogBtnGigs.addEventListener("click", () => {
    dialogBoxGigs.style.display = "flex";
});

closeDialogBtnGigs.addEventListener("click", () => {
    dialogBoxGigs.style.display = "none";
});

// Skills input functionality
const skillsInput = document.getElementById("skills-input");
const skillsContainer = document.getElementById("skills-container");

skillsInput.addEventListener("keyup", (e) => {
    if (e.key === "Enter" || e.key === ",") {
        const skillText = skillsInput.value.trim().replace(/,$/, "");
        if (skillText) {
            const skillElement = document.createElement("div");
            skillElement.className = "skill";
            skillElement.innerHTML = `${skillText} <span>&times;</span>`;
            skillsContainer.appendChild(skillElement);
            skillsInput.value = "";

            // Remove skill on click
            skillElement.querySelector("span").addEventListener("click", () => {
                skillElement.remove();
            });
        }
    }
});
