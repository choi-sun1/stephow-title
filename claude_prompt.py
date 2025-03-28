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
You are an AI assistant that generates concise manual titles based on user workflows.

<input_data>
{json.dumps(input_data, indent=2, ensure_ascii=False)}
</input_data>

### Instructions:
- Determine the **user’s goal** from the given steps.
- Generate a **concise and informative title** (under 10 words).
- Prefer to start with an imperative phrase such as "How to", "Guide to", or "Learn to".
- Include the **domain name** if relevant (e.g., "on {domain}").
- The title will be shown to users as the default and is only generated once, so make it **clear, helpful, and final**.
- Generate the title in the user's language: **{language.upper()}**.
- Avoid vague, repetitive, or redundant terms.
- If some steps are unclear (e.g., "Untitled"), use contextual clues such as domain or page title if available.

### Examples:
Input: ["Click 'Login'", "Enter credentials", "Submit form"]
→ Title: "How to Log In to Your Account"

Input: ["Open settings", "Change password"]
→ Title: "Guide to Updating Your Password"

Return the result as a JSON object within <response> tags:

<response>
{{"title": "Generated title here"}}
</response>
"""
    return prompt
