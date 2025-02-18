# **Dev Notes - Private Tracking & Configuration**  

📂 This folder is for **developer-specific files** that will be **excluded from version control**.  

---

## 📌 Overview  

- `private.yaml` → **Personal tracking file** (ignored by Git)  
- `private.py` → **Personal app file** (ignored by Git)  
- `README.md` → **This file** (explains the purpose of this folder)  

This ensures **personal progress & notes** remain private while keeping the main repo clean.  

---

## 📂 Folder Structure  

```
📁 dev_notes
├── 📄 private.py    # Personal app
├── 📄 private.yaml  # Personal tracking
└── 📄 README.md     # This file
```

---

## 🚀 Purpose  

🔹 **Personal Skill Badge Tracking** (separate from the public YAML)  
🔹 **Experimental Features or Configs** for testing  
🔹 **Excluded from Git** (via `.gitignore`)  

---

## 🛠 How It Works  

1️⃣ **Personal Progress:**  
   - Store additional tracking data in `private.yaml` without affecting `skill_badges.yaml`.  

2️⃣ **Custom Experiments:**  
   - Use this space to test **new features, sorting methods, or different YAML formats**.  

3️⃣ **Data Privacy:**  
   - **This folder is ignored in `.gitignore`**, ensuring personal data is **never committed**.  

---

## 🔒 Example `private.yaml` Structure  

```yaml
- badge: Personal Learning Badge
  name: AI & ML on Google Cloud
  link: https://www.cloudskillsboost.google/course_templates/900
  labs:
    - Machine Learning APIs
    - Vertex AI Fundamentals
```

---

## 📝 Notes  

- 🚨 **Do NOT rename this folder** unless you update `.gitignore`.  
- 📌 **Keep personal YAML separate** from `track_data/skill_badges.yaml`.  
- 🔄 **This folder is for private use only** and **won't sync with GitHub**.  

---

## 📜 License  

📝 Part of **GCP-SkillTracker** | Licensed under **MIT License**  

---