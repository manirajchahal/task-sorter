📌 Task Auto-Categorizer
========================
A lightweight, zero-friction tool that reads a plain `tasks.txt` file and automatically sorts your tasks into categories using simple keyword rules.
Perfect for organizing messy thoughts into planned and ready-for-action tasks!

🚀 Features
-----------

*   Write your tasks in **simple plain text**
    
*   Automatically categorize tasks using **keyword-based matching**
    
*   Output a clean, readable **Markdown summary**
    
*   Categories are fully customizable via categories.json
    
*   No dependencies, just **pure Python**
    

📥 Installation
---------------

Clone the repository:


```
git clone https://github.com/manirajchahal/task-sorter.git
cd task-sorter
```

**OR**

1. Click Code → Download ZIP

2. Extract the folder

3. Open `categorize_tasks.py` with Python (Using Powershell / CMD or Git Bash)


🔧 Making the Script Automatable (Linux/macOS Only)
---------------------------------------------------

If you're on Linux or macOS, make the helper script executable:

`chmod +x run_categorizer_unix.sh`

Then run it:

`./run_categorizer_unix.sh`

This will allow `cron` to schedule automatic updates on the tasks.txt files so you don't have to continually run the Python script.

📝 Usage
--------

### 1. Add your tasks to tasks.txt

```
Example: 
To-Do:
- Terminate both ends of Ethernet cable
- Capstone for CodePath  
- Homelab LinkedIn/Medium Post  
- Cisco Plug and Play TAC Case  
- VLAN Changes documentation for Helpdesk  
- Homelab Raspberry Pi Configs  
- Homelab Proxmox
```

Lines beginning with - are extracted as tasks.

### 2. Customize categories in categories.json

Categories match based on **case-insensitive keyword presence**.

### 3. Run the categorizer

` python3 categorize_tasks.py `

This produces:

*   Console output of categorized tasks
    
*   A generated file: categorized\_tasks.md

🔧 Customization
----------------

You can adjust:

*   Category names
    
*   Keywords
    
*   Matching rules
    

All through categories.json and the logic in categorize\_tasks.py.

⭐ Why This Tool Exists
----------------------

Most task apps are overkill. This script gives you:

*   Simplicity
    
*   Speed
    
*   Plain-text control
    
*   Total customization
    

Write your tasks however you want. Let the script do the sorting.
