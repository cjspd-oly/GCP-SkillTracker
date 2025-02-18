import re
import os
import yaml


def parse_markdown(md_file):
    with open(md_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    skill_badges = []
    current_badge = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Match Skill Badge header line.
        # Example:
        # ## Skill Badge 1: [Analyze BigQuery Data in Connected Sheets](https://www.cloudskillsboost.google/course_templates/632) - 2 hours 45 minutes
        badge_match = re.match(
            r"^##\s+Skill Badge\s+(\d+):\s+\[(.+?)\]\((https?://[^\)]+)\)", line
        )
        if badge_match:
            # Save the previous badge if exists.
            if current_badge:
                skill_badges.append(current_badge)
            badge_number = badge_match.group(1)
            badge_name = badge_match.group(2)
            badge_link = badge_match.group(3)
            current_badge = {
                "badge": f"Skill Badge {badge_number}",
                "name": badge_name,
                "link": badge_link,
                "labs": [],
            }
            continue

        # Match Lab lines.
        # Example:
        # - 🏆 Lab 1 - GSP469 - [Google Sheets: Getting Started](https://www.cloudskillsboost.google/course_templates/632/labs/464080) - 15 minutes - Introductory - No cost
        lab_match = re.match(
            r"^- (🏆|💻) Lab \d+ - \S+ - \[(.+?)\]\((https?://[^\)]+)\)", line
        )
        if lab_match and current_badge is not None:
            lab_name = lab_match.group(2)
            current_badge["labs"].append(lab_name)

    if current_badge:
        skill_badges.append(current_badge)
    return skill_badges


def save_to_yaml(data, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the file path relative to the script location
    file_path = os.path.join(script_dir, "output.txt")

    markdown_file = os.path.join(script_dir, "sample.md")  # Your Markdown file name
    yaml_file = os.path.join(script_dir, "sample.yaml")  # Desired output YAML file name
    data = parse_markdown(markdown_file)
    save_to_yaml(data, yaml_file)
    print(f"YAML saved to {yaml_file}")
