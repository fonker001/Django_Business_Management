// Sample Chart.js Configuration

const salesChartCtx = document.getElementById('salesChart').getContext('2d');
const clientChartCtx = document.getElementById('clientChart').getContext('2d');

const salesChart = new Chart(salesChartCtx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
            label: 'Sales',
            data: {{ sales_data|safe }},
            borderColor: '#1abc9c',
            fill: false,
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const clientChart = new Chart(clientChartCtx, {
    type: 'bar',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
            label: 'Clients',
            data: {{ client_data|safe }},
            backgroundColor: '#1abc9c',
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Show loader
function showLoader() {
    document.getElementById('loader').style.display = 'flex';
}

// Hide loader
function hideLoader() {
    document.getElementById('loader').style.display = 'none';
}

// Example usage: Show loader for 2 seconds
showLoader();
setTimeout(hideLoader, 2000); // Simulate a 2-second loading time


// Dark Mode Toggle
const themeToggle = document.getElementById('theme-icon');
const body = document.body;

if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        if (body.classList.contains('dark-mode')) {
            themeToggle.classList.remove('fa-moon');
            themeToggle.classList.add('fa-sun');
        } else {
            themeToggle.classList.remove('fa-sun');
            themeToggle.classList.add('fa-moon');
        }
    });
}