# **GCP-SkillTracker**

_A Streamlit-powered tracker for Google Cloud Skill Badges_

![GCP-SkillTracker](https://img.shields.io/badge/Google%20Cloud-Skill%20Tracker-blue?style=for-the-badge&logo=google-cloud)

## 📌 Overview

🚀 **GCP-SkillTracker** helps you track your progress on **Google Cloud Skill Badges**.  
With an **interactive UI, search, sorting, and autosave features**, this app simplifies tracking your Cloud Arcade journey.

---

## ✨ Features

- ✅ **Track Skill Badges** (not individual labs)
- ✅ **Autosave & Manual Save** options for progress tracking
- ✅ **Search & Sort** badges by name or completion status
- ✅ **YAML Import/Export** for easy backup & restore
- ✅ **Compact UI** with a developer-friendly layout

---

## 📂 Folder Structure

```
📁 GCP-SkillTracker
├── 📄 main.py                 # Streamlit App
├── 📂 parser                  # Converts Markdown → YAML
│   ├── parse.py               # Markdown to YAML parser
│   ├── sample.md              # Example 85 Skill Badge Markdown
│   ├── sample.yaml            # Example 85 Skill Badge YAML
│   └── README.md              # Parser details
├── 📂 track_data              # Live tracking & archives
│   ├── skill_badges.yaml      # Active tracking file (autosaves here)
│   ├── archive_YYYYMMDD.yaml  # Archived backup files
│   └── README.md              # Data storage info
├── 📂 dev_notes               # Developer-only folder (Personal stuff)
|   ├── private.py             # Streamlit App (For Personal Use)
│   ├── private.yaml           # Personal tracking
│   └── README.md              # Notes for private use
├── 📂 assets                  # (Optional) UI resources & images
│   └── banner.png             # Repo banner (if needed)
├── 📄 requirements.txt        # Python dependencies
├── 📄 README.md               # This file
└── 📄 .gitignore              # Excludes unnecessary files
```

> **🔴 Note:** `dev_notes/` is for **personal tracking**...Ignore it!.

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/cjspd-oly/GCP-SkillTracker.git
cd GCP-SkillTracker
```

### 2️⃣ Set Up a Virtual Environment (Recommended)

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 4️⃣ Run the App

```sh
streamlit run main.py
```

---

## 🛠 Usage Guide

### 📤 Saving & Loading Progress

- **Autosave:** Progress is automatically stored in `track_data/skill_badges.yaml`.
- **Manual Save:** Click the **Save Progress** button in the sidebar.
- **Export:** Download a backup YAML file using **Export YAML**.
- **Archive:** Old progress files are stored in `track_data/archive_YYYYMMDD.yaml`. **{TODO}**

### 🔍 Searching & Sorting

- Use the **search bar** to find badges by name.
- Sort badges by **completion status** or **skill badge number**.

---

## 🎨 UI Preview (TODO)

_(Add screenshots or a demo GIF here.)_

---

## 🤝 Contributing

💡 **Ideas & improvements are welcome!** Feel free to:

- Open an **issue** for feature requests or bug reports.
- Submit a **pull request** with your improvements.
- Share feedback to improve this tracker.

---

## 📜 License

📝 This project is **open-source** under the **MIT License**.

---