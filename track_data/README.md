# **Track Data - Skill Badge Progress Storage**  

📂 This folder stores **your progress data** for Google Cloud Skill Badges.  

---

## 📌 Overview  

- `skill_badges.yaml` → **Active tracking file** (autosaved progress)  
- `archive_YYYYMMDD.yaml` → **Archived backups** (older progress snapshots)  
- `README.md` → **This file** (explains storage structure)  

This ensures **your progress is always saved and recoverable**.  

---

## 📂 Folder Structure  

```
📁 track_data
├── 📄 skill_badges.yaml      # Current progress (autosaved)
├── 📄 archive_YYYYMMDD.yaml  # Backup snapshots (manual save)
└── 📄 README.md              # This file
```

---

## 🛠 How It Works  

1️⃣ **Autosave:** Every time you update progress in the app, `skill_badges.yaml` updates automatically.  
2️⃣ **Manual Save:** Use the **"Save Progress"** button to store progress manually.  
3️⃣ **Backup & Restore:**  
   - The **"Export YAML"** option lets you download a copy.  
   - **Older progress snapshots** are stored as `archive_YYYYMMDD.yaml`.  

---

## 🔄 Example YAML Structure  

```yaml
- badge: Skill Badge 1
  name: Analyze BigQuery Data in Connected Sheets
  link: https://www.cloudskillsboost.google/course_templates/632
  labs:
    - Google Sheets: Getting Started
    - BigQuery: Qwik Start - Console

- badge: Skill Badge 2
  name: Streaming Analytics into BigQuery
  link: https://www.cloudskillsboost.google/course_templates/752
  labs:
    - Pub/Sub: Qwik Start - Console
    - Dataflow: Qwik Start - Templates
```

---

## 📝 Notes  

- **Do not manually edit `skill_badges.yaml`** while the app is running to prevent data loss.  
- **Backup files** (`archive_YYYYMMDD.yaml`) ensure **older progress is never lost**.  
- **To restore progress**, replace `skill_badges.yaml` with a backup.  

---

## 📜 License  

📝 Part of **GCP-SkillTracker** | Licensed under **MIT License**  

---