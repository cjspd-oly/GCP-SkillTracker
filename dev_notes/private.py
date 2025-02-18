import streamlit as st
import yaml
import os
import re

# 🛠️ Fix: file path
script_dir = os.path.dirname(os.path.abspath(__file__))

# 🛠️ Set a wide layout for a more compact view
st.set_page_config(page_title="🏆 Skill Badge Tracker", layout="wide")

# 📄 YAML file to store progress
YAML_FILE = os.path.join(script_dir, "private.yaml")


# 📂 Function to load YAML data
def load_yaml(file_path):
    """Loads the YAML file and ensures each badge has a 'done' flag."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or []
            for badge in data:
                if "done" not in badge:
                    badge["done"] = False  # Ensure all badges have a 'done' flag
            return data
    return []


# 💾 Function to save progress to YAML
def save_yaml(data, file_path):
    """Saves the current progress to a YAML file."""
    with open(file_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


# 🔢 Function to extract badge number (e.g., 'Skill Badge 1' → 1)
def get_badge_number(badge):
    """Extracts the numeric part from the badge string for sorting."""
    match = re.search(r"(\d+)", badge.get("badge", ""))
    return int(match.group(1)) if match else 0


# 🏆 Main App
def main():
    st.title("🏆 Skill Badge Progress Tracker")

    # 📂 Load badges from YAML
    original_badges = load_yaml(YAML_FILE)
    if not original_badges:
        st.warning("⚠️ No badges found in YAML file!")
        st.stop()

    # 🎛️ Sidebar: Customization Options
    st.sidebar.header("⚙️ Options")

    # 🔍 Search input to filter badges by ID or name
    search_term = st.sidebar.text_input("🔍 Search Skill Badge", "").strip()

    # 📊 Sorting options
    sort_option = st.sidebar.selectbox(
        "📌 Sort by", ["Default (Badge Order)", "✅ Done first", "❌ Not done first"]
    )

    # 💾 Manual Save button
    if st.sidebar.button("💾 Manual Save"):
        save_yaml(original_badges, YAML_FILE)
        st.sidebar.success("✅ Progress manually saved!")

    # 📂 Export YAML file button
    yaml_text = yaml.dump(original_badges, default_flow_style=False, allow_unicode=True)
    st.sidebar.download_button(
        "📤 Export YAML",
        yaml_text,
        file_name="skill_badges_export.yaml",
        mime="text/yaml",
    )

    # 🎛️ Sidebar: Filter by Completion Status
    filter_option = st.sidebar.radio("📌 Filter by:", ["All", "✅ Done", "❌ Not Done"])

    # 📋 Filter badges based on search & completion status
    badges = original_badges.copy()

    if search_term:
        badges = [
            b
            for b in badges
            if search_term.lower() in b.get("name", "").lower()
            or search_term.lower() in b.get("badge", "").lower()
        ]

    # Apply "Done / Not Done" filter
    if filter_option == "✅ Done":
        badges = [b for b in badges if b.get("done", False)]
    elif filter_option == "❌ Not Done":
        badges = [b for b in badges if not b.get("done", False)]

    # 🔄 Sorting logic
    if sort_option == "Default (Badge Order)":
        badges = sorted(badges, key=get_badge_number)
    elif sort_option == "✅ Done first":
        badges = sorted(
            badges, key=lambda x: (not x.get("done", False), get_badge_number(x))
        )
    elif sort_option == "❌ Not done first":
        badges = sorted(
            badges, key=lambda x: (x.get("done", False), get_badge_number(x))
        )

    # 📌 Displaying Skill Badges
    for idx, badge in enumerate(badges):
        with st.expander(f"🏅 {badge['badge']}: [{badge['name']}]({badge['link']})"):
            # ✅ Checkbox to mark the badge as completed
            done = st.checkbox(
                "✅ Mark as Done", value=badge.get("done", False), key=f"badge_{idx}"
            )
            badge["done"] = done  # Update the 'done' status

            # 📚 Display labs (if available)
            if "labs" in badge and badge["labs"]:
                st.markdown("**📚 Labs:**")
                for lab in badge["labs"]:
                    st.markdown(f"- 📌 {lab}")

    # 🔄 Autosave progress
    save_yaml(original_badges, YAML_FILE)
    st.success("💾 Progress autosaved!")


# 🚀 Run the app
if __name__ == "__main__":
    main()
