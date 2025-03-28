import json

def build_prompt_from_steps(steps, domain="stephow.com", language="ko"):
    input_data = {
        "steps": [],
        "domain": domain,
        "language": language
    }

    for step in steps:
        title = step.get("step_title") or step.get("step_name") or "Untitled"
        desc = step.get("step_description") or ""
        text = title.strip()
        if desc:
            text += f" - {desc.strip()}"
        input_data["steps"].append(text)

    prompt = f"""
You are an AI assistant that generates concise, clear, and action-oriented manual titles based on user workflows.

<input_data>
{json.dumps(input_data, indent=2, ensure_ascii=False)}
</input_data>

### Instructions:
- Determine the **main user goal** from the given steps.
- Generate **a single, concise, and informative title** (no more than **10 words**).
- The title must be **action-oriented**, starting with:
  - "How to ..."
  - "Guide to ..."
  - "Learn to ..."
- If relevant, include the **domain name** (e.g., "on {domain}").
- Generate the title in **{language.upper()}**.
- Avoid:
  - Generic or vague business terms (e.g., "workflow", "task", "process")
  - Redundant words
  - Passive voice
- This title will be shown to users as the **default**, so ensure it's **clear, final, and requires no further edits**.

### Examples:
Input: ["Click 'Login'", "Enter credentials", "Submit form"]
→ Title: "How to Log In to Your Account on stephow.com"

Input: ["Open settings", "Change password"]
→ Title: "Guide to Updating Your Password"

Return the result as a JSON object inside <response> tags:

<response>
{{"title": "Generated title here"}}
</response>
"""
    return prompt
