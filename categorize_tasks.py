import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

TASKS_FILE = BASE_DIR / "tasks.txt"
CATEGORIES_FILE = BASE_DIR / "categories.json"
OUTPUT_FILE = BASE_DIR / "categorized_tasks.md"


def load_categories():
    with CATEGORIES_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_tasks():
    """
    Reads tasks.txt and returns a list of task strings.
    Assumes tasks are lines starting with '- '.
    """
    if not TASKS_FILE.exists():
        return []

    bullet_chars = ["-", "*", "+", "•"]

    tasks = []
    with TASKS_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()

            # Skip empty
            if not stripped:
                continue

            # Check if line starts with a bullet character
            if stripped[0] in bullet_chars:
                # Remove the bullet + any surrounding spaces
                task = stripped[1:].strip()

                if task:  # don't add empty strings
                    tasks.append(task)
    return tasks


def categorize_task(task, categories):
    """
    Return the name of the first matching category, or 'Uncategorized'.
    """
    task_lower = task.lower()
    for category, keywords in categories.items():
        if category.lower() == "uncategorized":
            continue
        for kw in keywords:
            if kw.lower() in task_lower:
                return category
    return "Uncategorized"


def categorize_tasks(tasks, categories):
    categorized = {cat: [] for cat in categories.keys()}
    if "Uncategorized" not in categorized:
        categorized["Uncategorized"] = []

    for task in tasks:
        cat = categorize_task(task, categories)
        categorized.setdefault(cat, []).append(task)

    return categorized


def print_categorized(categorized):
    for category, tasks in categorized.items():
        if not tasks:
            continue
        print(f"## {category}")
        for t in tasks:
            print(f"- {t}")
        print()


def save_categorized_markdown(categorized, output_file="categorized_tasks.md"):
    path = Path(output_file)
    lines = []
    for category, tasks in categorized.items():
        if not tasks:
            continue
        lines.append(f"## {category}\n")
        for t in tasks:
            lines.append(f"- {t}")
        lines.append("")  # blank line between categories

    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Saved categorized tasks to {output_file}")


def main():
    categories = load_categories()
    tasks = load_tasks()

    if not tasks:
        print("No tasks found in tasks.txt")
        return

    categorized = categorize_tasks(tasks, categories)

    print("=== Categorized Tasks (Console Output) ===\n")
    print_categorized(categorized)

    save_categorized_markdown(categorized)


if __name__ == "__main__":
    main()
