const reports = { gallery_links };

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
