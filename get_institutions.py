import os
import pandas as pd
from bs4 import BeautifulSoup


def extract_project_institutions():
    # List to store institution and project name pairs
    institution_data = []

    # Iterate through HTML files in the projects folder
    for filename in os.listdir("projects"):
        if filename.endswith(".html"):
            filepath = os.path.join("projects", filename)

            # Read the HTML file
            with open(filepath, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")

                # Get project title from banner details
                project_title_elem = soup.select_one(".banner-details h1")
                project_title = (
                    project_title_elem.get_text(strip=True)
                    if project_title_elem
                    else "Unknown Project"
                )

                # Find partners div
                partners_elem = soup.select_one("div.partners div.value")

                # Extract and process institutions if partners element exists
                if partners_elem:
                    # Split institutions by comma and strip whitespace
                    institutions = [
                        inst.strip()
                        for inst in partners_elem.get_text(strip=True).split(",")
                    ]

                    # Add each institution with the project name
                    for institution in institutions:
                        if institution:  # Ensure non-empty institution
                            institution_data.append(
                                {
                                    "institution": institution,
                                    "project_name": project_title,
                                }
                            )

    # Create DataFrame and sort by institution
    df = pd.DataFrame(institution_data)
    df_sorted = df.sort_values("institution")

    return df_sorted


def main():
    # Get and print the institutions DataFrame
    institutions_df = extract_project_institutions()
    print(institutions_df)

    # Optional: Save to CSV
    institutions_df.to_csv("project_institutions.csv", index=False)


if __name__ == "__main__":
    main()
