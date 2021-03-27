// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
const b = document.getElementById("mydata").textContent;
const dados2 = JSON.parse(b);
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Massa Muscular", "Gordura", "Social"],
    datasets: [{
      data: [dados2["musculo"][dados2["musculo"].length - 1], dados2["gordura"][dados2["musculo"].length - 1] , 15],
      backgroundColor: ['rgba(2, 89, 32, 1)', 'rgba(164, 0, 0, 1)', '#36b9cc'],
      hoverBackgroundColor: ['rgba(2, 89, 32, 0.5)', 'rgba(164, 0, 0, 0.5)', '#2c9faf'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
