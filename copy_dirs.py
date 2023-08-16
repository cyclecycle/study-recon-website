# Copy named dirs from ../grounded-dev/recon-tools/data/workspaces to reports/

import os
import shutil

overwrite = False

from_dir = "../grounded-dev/recon-tools/data/workspaces-gallery"
to_dir = "reports"

# List of dirs to copy
dirs = [
    "advancements-in-superconductors-promising-applications",
    "mindfulness-for-mental-well-being",
    "ai-and-machine-learning-in-healthcare",
    "climate-change-and-global-food-security",
    "work-life-balance-and-employee-satisfaction",
    "quantum-computing-market-analysis",
    "advancements-in-endometriosis-treatments",
    "covid-19-and-the-future-of-remote-work",
    "gender-diversity-and-company-performance",
    "virtual-reality-in-education-impact-analysis",
    "childhood-nutrition-and-long-term-health",
]
dirs = [os.path.join(from_dir, d) for d in dirs]

for d in dirs:
    if os.path.exists(os.path.join(to_dir, os.path.basename(d))):
        if overwrite:
            shutil.rmtree(os.path.join(to_dir, os.path.basename(d)))
        else:
            print(f"Directory {os.path.basename(d)} already exists. Skipping.")
            continue
    shutil.copytree(d, os.path.join(to_dir, os.path.basename(d)))

# Remove all json files except report_config.json
for dirpath, dirnames, filenames in os.walk(to_dir):
    for filename in filenames:
        if filename.endswith(".json") and filename != "report_config.json":
            os.remove(os.path.join(dirpath, filename))
