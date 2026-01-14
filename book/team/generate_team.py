import os
import yaml

INPUT_DIR = "book/team/team_info"     # folder containing individual md files
TEMPLATE_FILE = "book/team/template.md"    # template for individual team cards
OUTPUT_FILE = "book/team/topics_people.md"     # existing overview file
PLACEHOLDER = "{{TEAM_CARDS}}"        # placeholder in team.md


def read_person(filepath):
    """Read an individual .md file and extract frontmatter + body."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if content.startswith("---"):
        _, frontmatter, body = content.split("---", 2)
        data = yaml.safe_load(frontmatter)
        data["body"] = body.strip()
        return data
    return None


def generate_card(person):
    """Generate HTML for a neat horizontal person card."""
    return f"""<div class="team-card">
<img src="https://github.com/TUDelft-MUDE/source-files/raw/main/file/{person['photo']}" alt="{person['name']}" class="dark-light resized">
<div class="team-info">
<h3>{person['name']}</h3>
<p><em>{person['role']}</em></p>
<p>{person['body']}</p>
<a href="mailto:{person['email']}">Email</a>
</div>
</div>"""


def generate_all_cards(people):
    """Generate the full HTML for all team cards, grouped by role in custom order."""
    grouped = {}
    for p in people:
        grouped.setdefault(p["role"], []).append(p)

    # Define the desired role order
    role_order = ["MUDE guide", "Instructor", "Teaching Assistant"]

    # Sort grouped roles according to role_order
    grouped_sorted = {role: grouped[role] for role in role_order if role in grouped}

    # Include any roles not in role_order at the end (alphabetically)
    remaining_roles = sorted(set(grouped.keys()) - set(grouped_sorted.keys()))
    for role in remaining_roles:
        grouped_sorted[role] = grouped[role]

    cards_html = ""

    # Add CSS at the top
    cards_html += """<style>
.team-container {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin: 0;
  padding: 0;
}
.team-card {
  flex: 1 1 calc(33.333% - 15px);
  box-sizing: border-box;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 2px 2px 6px rgba(0,0,0,0.1);
  margin: 0;
}
.team-card img {
  width: 60px;
  height: 60px;
  object-fit: cover;
  border-radius: 8px;
}
.team-info {
  text-align: left;
  font-size: 0.9em;
}
.team-info h3 {
  margin: 0;
  font-size: 1.05em;
}
.team-info p {
  margin: 2px 0;
}
.resized {
  max-width: 100px;
  max-height: 100px;
  width: auto;
  height: auto;
}

/* Responsive: 2 per row on tablets, 1 per row on mobile */
@media (max-width: 900px) {
  .team-card { flex: 1 1 calc(50% - 15px); }
}
@media (max-width: 600px) {
  .team-card { flex: 1 1 100%; }
}
</style>\n\n"""

    cards_html += "# Our Team\n\n"

    for role, members in grouped_sorted.items():
        cards_html += f"## {role}\n\n<div class='team-container'>"
        for m in members:
            cards_html += generate_card(m)
        cards_html += "</div>\n\n---\n\n"

    return cards_html


def main():
    # Read all people
    people = []
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".md"):
            person = read_person(os.path.join(INPUT_DIR, filename))
            if person:
                people.append(person)

    if not people:
        print("⚠️ No people found in INPUT_DIR")
        return

    # Generate cards HTML
    cards_html = generate_all_cards(people)

    # Read existing file
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace placeholder
    if PLACEHOLDER not in content:
        print(f"⚠️ Placeholder {PLACEHOLDER} not found in {TEMPLATE_FILE}")
        return

    content = content.replace(PLACEHOLDER, cards_html)

    # Write back to same file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Updated {OUTPUT_FILE} with team cards")


if __name__ == "__main__":
    main()
