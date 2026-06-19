import os
import sys
import re

LANG_MAP = {
    "cpp": "cpp",
    "go": "go",
    "java": "java",
    "javascript": "js",
    "python3": "py",
    "typescript": "ts"
}

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    leetcode_dir = os.path.dirname(script_dir)
    problems_dir = os.path.join(leetcode_dir, "problems")

    if not os.path.exists(problems_dir):
        print(f"Error: The 'problems' directory was not found at: {problems_dir}")
        sys.exit(1)

    title = input("Enter the problem title (e.g., '1768. Merge Strings Alternately'): ").strip()
    if not title:
        print("Error: Problem title cannot be empty.")
        sys.exit(1)

    title = re.sub(r'[\\/*?:"<>|]', "", title)
    if not title:
        print("Error: Problem title became empty after removing invalid characters.")
        sys.exit(1)

    available_langs = sorted(list(LANG_MAP.keys()))
    print(f"\nAvailable languages: {', '.join(available_langs)}")
    langs_input = input("Enter languages (comma-separated, or 'all'): ").strip().lower()

    if not langs_input:
        print("Error: No languages specified.")
        sys.exit(1)

    selected_langs = []
    if langs_input == "all":
        selected_langs = available_langs
    else:
        parts = [p.strip() for p in langs_input.split(",")]
        for p in parts:
            if p in LANG_MAP:
                selected_langs.append(p)
            else:
                print(f"Warning: Unsupported language '{p}' skipped.")

    if not selected_langs:
        print("Error: No valid languages selected.")
        sys.exit(1)

    print("\nCreating files...")
    for lang in selected_langs:
        lang_dir = os.path.join(problems_dir, lang)
        problem_dir_path = os.path.join(lang_dir, title)

        if os.path.exists(problem_dir_path):
            print(f"Warning: Path already exists: {problem_dir_path}. Skipping.")
            continue

        if not os.path.exists(lang_dir):
            os.makedirs(lang_dir, exist_ok=True)
            print(f"Created language directory: {lang_dir}")

        os.makedirs(problem_dir_path, exist_ok=True)

        ext = LANG_MAP[lang]
        solve_file_path = os.path.join(problem_dir_path, f"solve.{ext}")

        with open(solve_file_path, "w", encoding="utf-8") as f:
            f.write("")
        print(f"Created: {solve_file_path}")

    print("\nDone!")

if __name__ == "__main__":
    main()
