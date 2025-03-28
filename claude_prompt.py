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
You are an AI assistant specializing in summarizing workflows into concise and informative manual titles.

<input_data>
{json.dumps(input_data, indent=2, ensure_ascii=False)}
</input_data>

### Instructions:
- Identify the main goal of the user from the provided steps.
- Generate a clear and concise title summarizing the workflow.
- Follow these formatting rules:
  - Under 10 words.
  - Start with an imperative verb ("How to", "Guide to", "Learn to").
  - Include a domain name if relevant (e.g., "on {domain}").
  - Avoid redundant or vague words.

Return the result as a JSON object within <response> tags:

<response>
{{"title": "Generated title here"}}
</response>
"""
    return prompt
