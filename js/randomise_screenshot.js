const reports = [
  {
    "link": "./reports/pages/advancements-in-endometriosis-treatments.html",
    "src": "./reports/advancements-in-endometriosis-treatments/StudyRecon_Advancements in Endometriosis Treatments_20230816_search_results.png",
    "alt": "Advancements in Endometriosis Treatments Report Screenshot"
  },
  {
    "link": "./reports/pages/advancements-in-superconductors-promising-applications.html",
    "src": "./reports/advancements-in-superconductors-promising-applications/StudyRecon_Advancements in Superconductors: Promising Applications_20230816_search_results.png",
    "alt": "Advancements in Superconductors: Promising Applications Report Screenshot"
  },
  {
    "link": "./reports/pages/ai-and-machine-learning-in-healthcare.html",
    "src": "./reports/ai-and-machine-learning-in-healthcare/StudyRecon_AI and Machine Learning in Healthcare_20230816_search_results.png",
    "alt": "AI and Machine Learning in Healthcare Report Screenshot"
  },
  {
    "link": "./reports/pages/childhood-nutrition-and-long-term-health.html",
    "src": "./reports/childhood-nutrition-and-long-term-health/StudyRecon_Childhood Nutrition and Long-Term Health_20230816_search_results.png",
    "alt": "Childhood Nutrition and Long-Term Health Report Screenshot"
  },
  {
    "link": "./reports/pages/climate-change-and-global-food-security.html",
    "src": "./reports/climate-change-and-global-food-security/StudyRecon_Climate Change and Global Food Security_20230816_search_results.png",
    "alt": "Climate Change and Global Food Security Report Screenshot"
  },
  {
    "link": "./reports/pages/covid-19-and-the-future-of-remote-work.html",
    "src": "./reports/covid-19-and-the-future-of-remote-work/StudyRecon_COVID-19 and the Future of Remote Work_20230816_search_results.png",
    "alt": "COVID-19 and the Future of Remote Work Report Screenshot"
  },
  {
    "link": "./reports/pages/gender-diversity-and-company-performance.html",
    "src": "./reports/gender-diversity-and-company-performance/StudyRecon_Gender Diversity and Company Performance_20230816_search_results.png",
    "alt": "Gender Diversity and Company Performance Report Screenshot"
  },
  {
    "link": "./reports/pages/mindfulness-for-mental-well-being.html",
    "src": "./reports/mindfulness-for-mental-well-being/StudyRecon_Mindfulness for Mental Well-being_20230816_search_results.png",
    "alt": "Mindfulness for Mental Well-being Report Screenshot"
  },
  {
    "link": "./reports/pages/quantum-computing-market-analysis.html",
    "src": "./reports/quantum-computing-market-analysis/StudyRecon_Quantum Computing Market Analysis_20230816_search_results.png",
    "alt": "Quantum Computing Market Analysis Report Screenshot"
  },
  {
    "link": "./reports/pages/virtual-reality-in-education-impact-analysis.html",
    "src": "./reports/virtual-reality-in-education-impact-analysis/StudyRecon_Virtual Reality in Education: Impact Analysis_20230816_search_results.png",
    "alt": "Virtual Reality in Education: Impact Analysis Report Screenshot"
  },
  {
    "link": "./reports/pages/work-life-balance-and-employee-satisfaction.html",
    "src": "./reports/work-life-balance-and-employee-satisfaction/StudyRecon_Work-Life Balance and Employee Satisfaction_20230816_search_results.png",
    "alt": "Work-Life Balance and Employee Satisfaction Report Screenshot"
  }
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
