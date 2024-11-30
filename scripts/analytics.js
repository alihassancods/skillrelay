const dialogBoxAnalytics = document.getElementById("analytics-dialog");
const openDialogBtnAnalytics = document.querySelectorAll(".open-dialog-btn-analytics");
const closeDialogBtnAnalytics = document.querySelectorAll(".close-dialog-btn-analytics");

// openDialogBtnAnalytics.addEventListener("click", () => {
//     dialogBoxAnalytics.style.display = "flex";
// });
openDialogBtnAnalytics.forEach((btn) => {btn.addEventListener("click", () => {
    dialogBoxAnalytics.style.display = "flex";
});})
closeDialogBtnAnalytics.forEach((btn) => {btn.addEventListener("click", () => {
    dialogBoxAnalytics.style.display = "none";
});})
// closeDialogBtnAnalytics.addEventListener("click", () => {
//     dialogBoxAnalytics.style.display = "none";
// });

// Chart.js setup
const ctx = document.getElementById('analytics-graph').getContext('2d');
const analyticsChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
        datasets: [{
            label: 'Data',
            data: [12, 19, 3, 5, 2, 3, 7],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
