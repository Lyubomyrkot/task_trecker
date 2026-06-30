document.addEventListener("DOMContentLoaded", function () {

    const canvas = document.getElementById("priorityChart");

    if (!canvas) {
        console.log("Chart canvas not found");
        return;
    }

    if (typeof Chart === "undefined") {
        console.log("Chart.js not loaded");
        return;
    }

    new Chart(canvas, {
        type: "doughnut",
        data: {
            labels: ["High", "Medium", "Low"],
            datasets: [{
                data: [
                    HIGH_TASKS,
                    MEDIUM_TASKS,
                    LOW_TASKS
                ],
                backgroundColor: ["#dc3545", "#ffc107", "#198754"],
                borderWidth: 0
            }]
        },
        options: {
            cutout: "70%",
            plugins: {
                legend: { display: false }
            }
        }
    });

});