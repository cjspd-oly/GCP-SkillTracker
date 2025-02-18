# **Parser - Markdown to YAML**  

🚀 This folder contains the **Markdown to YAML parser** for converting Google Cloud Skill Badge data into a structured YAML format.  

---

## 📌 Overview  

The parser extracts **Skill Badge names, links, and labs** from a Markdown file and converts them into a **clean YAML format** for tracking progress.  

---

## 📂 Files in this Folder  

```
📁 parser
├── 📄 parse.py      # Main parser script
├── 📄 sample.md     # Example Skill Badge Markdown input
├── 📄 sample.yaml   # Example Skill Badge YAML output
└── 📄 README.md     # This file
```

---

## 🛠 How It Works  

1️⃣ **Input:** A Markdown file containing Google Cloud Skill Badges and Labs  
2️⃣ **Processing:**  
   - Extracts **Skill Badge name, link, and labs**  
   - Formats the data into YAML  
3️⃣ **Output:** A structured YAML file ready for tracking  

---

## 🔧 Usage  

### 1️⃣ Run the Parser  
```sh
python parse.py sample.md output.yaml
```

### 2️⃣ Example Input (`sample.md`)  

```markdown
## Skill Badge 1: [Analyze BigQuery Data in Connected Sheets](https://www.cloudskillsboost.google/course_templates/632)

- 🏆 Lab 1 - GSP469 - [Google Sheets: Getting Started](https://www.cloudskillsboost.google/course_templates/632/labs/464080)
- 🏆 Lab 2 - GSP072 - [BigQuery: Qwik Start - Console](https://www.cloudskillsboost.google/course_templates/632/labs/464081)
```

### 3️⃣ Example Output (`output.yaml`)  

```yaml
- badge: Skill Badge 1
  name: Analyze BigQuery Data in Connected Sheets
  link: https://www.cloudskillsboost.google/course_templates/632
  labs:
    - Google Sheets: Getting Started
    - BigQuery: Qwik Start - Console
```

---

## 📝 Notes  

- Ensure the Markdown follows the **correct format** with `## Skill Badge` headers.  
- The parser **only extracts Skill Badges and Lab Names** (not descriptions or durations).  

---

## 🤝 Contributing  

🔹 **Found an issue or want to improve the parser?**  
Feel free to submit a **pull request** or open an **issue** in the repo!  

---

## 📜 License  
📝 This parser is part of **GCP-SkillTracker** and follows the **MIT License**.  

---