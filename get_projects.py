import os
import requests
from bs4 import BeautifulSoup


def download_project_pages(base_url, project_links):
    # Create projects folder if it doesn't exist
    os.makedirs("projects", exist_ok=True)

    # Download each project page
    for link in project_links:
        try:
            full_url = base_url + link
            response = requests.get(full_url)

            # Create a filename from the link, replacing / with _
            filename = os.path.join("projects", link.replace("/", "_") + ".html")

            with open(filename, "w", encoding="utf-8") as f:
                f.write(response.text)

            print(f"Downloaded: {filename}")
        except Exception as e:
            print(f"Error downloading {link}: {e}")


def main():
    base_url = "https://oscars-project.eu"
    # Use local HTML pages to extract project links
    project_links = []
    for page_file in os.listdir("pages"):
        if page_file.endswith(".html"):
            with open(os.path.join("pages", page_file), "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")

                # Find all links starting with /projects/
                page_project_links = [
                    a["href"]
                    for a in soup.find_all("a", href=True)
                    if a["href"].startswith("/projects/")
                ]

                project_links.extend(page_project_links)

    # Download project pages
    download_project_pages(base_url, project_links)


if __name__ == "__main__":
    main()
