import os
import json


def make_html_link(href, text, new_tab=False):
    target = 'target="_blank"' if new_tab else ""
    return f'<a href="{href}" {target}>{text}</a>'


def make_list_item(text):
    return f"<li>{text}</li>"


def make_links(config, dir_name):
    search_results_pdf = config["output_files"]["search_results_pdf"]
    doc_summary_pdf = config["output_files"].get("doc_summary_pdf")
    classic_report_pdf = config["output_files"].get("classic_report_pdf")
    download_files = [
        search_results_pdf,
        doc_summary_pdf,
        classic_report_pdf,
    ]
    download_files = [f for f in download_files if f is not None]
    download_files = [os.path.basename(f) for f in download_files]
    download_links = ""
    for f in download_files:
        download_links += make_list_item(
            make_html_link(
                f"../{dir_name}/{f}",
                f"Download Results (PDF)",
                new_tab=True,
            )
        )

    search_results_html = config["output_files"]["search_results_html"]
    html_files = [search_results_html]
    html_files = [f for f in html_files if f is not None]
    html_files = [os.path.basename(f) for f in html_files]
    html_links = ""
    for f in html_files:
        html_links += make_list_item(
            make_html_link(
                f"../{dir_name}/{f}",
                f"View Results",
                new_tab=False,
            )
        )

    return {
        "download_links": download_links,
        "html_links": html_links,
    }


def make_report_page(config):
    # Read the report_config.json file
    directory = config["directory"]
    dir_name = os.path.basename(directory)

    # Read the template
    with open("report-page-template.html", "r") as file:
        template = file.read()

    # Replace placeholders with actual content
    title = config["title"]
    name = title.lower().replace(" ", "-")
    page_content = template.replace("{report_title}", title)
    page_content = page_content.replace("{report_prompt}", config["prompt"])

    links = make_links(config, dir_name)
    download_links, html_links = links["download_links"], links["html_links"]
    page_content = page_content.replace("{download_links}", download_links)
    page_content = page_content.replace("{html_links}", html_links)
    page_content = page_content.replace("{dir_name}", dir_name)

    # Write the populated template to a new HTML file
    outpath = os.path.join(directory, f"../pages/{name}.html")
    with open(outpath, "w") as file:
        file.write(page_content)


def make_gallery_links(configs):
    links = ""
    for config in configs:
        directory = config["directory"]
        dir_name = os.path.basename(directory)
        title = config["title"]
        png = config["output_files"]["search_results_png"]
        png = os.path.basename(png)
        name = title.lower().replace(" ", "-")
        links += f"""<a
          href="./reports/pages/{name}.html"
          class="report-link"
        >
          <div class="report-item">
            <h3>{title}</h3>
            <img
              src="./reports/{dir_name}/{png}"
              alt="Report 1 Thumbnail"
              class="report-image"
            />
          </div>
        </a>"""
    return links


def main():
    # Iterate over all directories in "reports"
    configs = []
    front_page_gallery_links = []
    directories = os.listdir("reports")
    directories = sorted(directories)
    for directory in directories:
        dir_path = os.path.join("reports", directory)
        if os.path.isdir(dir_path):
            config_path = os.path.join(dir_path, "report_config.json")
            if not os.path.exists(config_path):
                continue
            with open(config_path, "r") as file:
                config = json.load(file)
            config["directory"] = dir_path
            configs.append(config)
            make_report_page(config)
            front_page_gallery_links.append(
                {
                    "link": f"./reports/pages/{directory}.html",
                    "src": f"./reports/{directory}/{config['output_files']['search_results_png']}",
                    "alt": f"{config['title']} Report Screenshot",
                }
            )

    # Embed links into js
    with open("js/randomise_screenshot_template.js", "r") as file:
        template = file.read()
    template = template.replace(
        "{ gallery_links }", json.dumps(front_page_gallery_links, indent=2)
    )
    with open("js/randomise_screenshot.js", "w") as file:
        file.write(template)

    default_link = front_page_gallery_links[0]["link"]
    default_src = front_page_gallery_links[0]["src"]
    default_alt = front_page_gallery_links[0]["alt"]
    with open("index.html", "r") as file:
        template = file.read()
    template = template.replace("{default_report_link}", default_link)
    template = template.replace("{default_report_img}", default_src)
    template = template.replace("{default_report_alt}", default_alt)
    with open("index.html", "w") as file:
        file.write(template)

    # Make the gallery page
    with open("gallery-template.html", "r") as file:
        template = file.read()

    gallery_links = make_gallery_links(configs)
    page_content = template.replace("{gallery_links}", gallery_links)
    with open("gallery.html", "w") as file:
        file.write(page_content)


if __name__ == "__main__":
    main()
