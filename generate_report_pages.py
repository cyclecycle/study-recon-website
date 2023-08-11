import os
import json


def generate_report_page(directory):
    # Read the report_config.json file
    dir_name = os.path.basename(directory)
    config_path = os.path.join(directory, "report_config.json")
    if os.path.exists(config_path) is False:
        return

    with open(config_path, "r") as file:
        config = json.load(file)

    # Read the template
    with open("report-page-template.html", "r") as file:
        template = file.read()

    # Replace placeholders with actual content
    title = config["title"]
    name = title.lower().replace(" ", "-")
    page_content = template.replace("{report_title}", title)
    page_content = page_content.replace("{report_prompt}", config["prompt"])
    page_content = page_content.replace("{dir_name}", dir_name)

    # Write the populated template to a new HTML file
    outpath = os.path.join(directory, f"../pages/{name}.html")
    with open(outpath, "w") as file:
        file.write(page_content)


def main():
    # Iterate over all directories in "reports"
    for directory in os.listdir("reports"):
        dir_path = os.path.join("reports", directory)
        if os.path.isdir(dir_path):
            generate_report_page(dir_path)


if __name__ == "__main__":
    main()
