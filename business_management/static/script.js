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


