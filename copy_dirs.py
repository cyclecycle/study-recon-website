# Copy named dirs from ../grounded-dev/recon-tools/data/workspaces to reports/

import os
import shutil

overwrite = False

from_dir = "../grounded-dev/recon-tools/data/workspaces"
to_dir = "reports"

# List of dirs to copy
dirs = ["unleashing-blockchain-s-transformative-potential"]
dirs = [os.path.join(from_dir, d) for d in dirs]

for d in dirs:
    if os.path.exists(os.path.join(to_dir, os.path.basename(d))):
        if overwrite:
            shutil.rmtree(os.path.join(to_dir, os.path.basename(d)))
        else:
            print(f"Directory {os.path.basename(d)} already exists. Skipping.")
            continue

# Remove all json files except report_config.json
for dirpath, dirnames, filenames in os.walk(to_dir):
    for filename in filenames:
        if filename.endswith(".json") and filename != "report_config.json":
            os.remove(os.path.join(dirpath, filename))