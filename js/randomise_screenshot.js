const reports = [
  {
    link: "./reports/pages/unleashing-blockchain's-transformative-potential.html",
    src: "./reports/unleashing-blockchain-s-transformative-potential/StudyRecon_Unleashing Blockchain's Transformative Potential_20230813_search_results.png",
    alt: "Report Screenshot",
  },
  {
    link: "./reports/pages/mindfulness:-a-stress-reducing-workplace-practice.html",
    src: "./reports/mindfulness-a-stress-reducing-workplace-practice/StudyRecon_Mindfulness: A Stress-Reducing Workplace Practice_20230814_search_results.png",
    alt: "Report Screenshot",
  },
];

// Function to display a random report
function displayRandomReport() {
  const randomIndex = Math.floor(Math.random() * reports.length);
  const selectedReport = reports[randomIndex];

  const screenshotGallery = document.querySelector(".screenshot-gallery");
  const anchor = screenshotGallery.querySelector("a");
  const img = screenshotGallery.querySelector(".screenshot");

  anchor.href = selectedReport.link;
  img.src = selectedReport.src;
  img.alt = selectedReport.alt;
}

// Call the function to display a report when the page loads
document.addEventListener("DOMContentLoaded", displayRandomReport);