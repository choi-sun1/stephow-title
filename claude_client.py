import boto3
import json

MODEL_ID = "anthropic.claude-3-sonnet-20240229-v1:0"

def call_claude(prompt):
    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1024,
        "temperature": 0.5
    }

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json"
    )

    result = json.loads(response["body"].read())
    return result["content"][0]["text"]

