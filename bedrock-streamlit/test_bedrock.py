
import boto3
import os

region = os.getenv("AWS_REGION", "us-east-1")
model_id = os.getenv(
    "BEDROCK_MODEL_ID",
    "amazon.nova-micro-v1:0",
)

client = boto3.client("bedrock-runtime",region_name=region)

response = client.converse(
    modelId=model_id,
    messages=[
        {
            "role": "user",
            "content": [
                {"text": "Explain Amazon Bedrock in two sentences."}
            ],
        }
    ],
    inferenceConfig={
        "maxTokens": 150,
        "temperature": 0.3,
    },
)

print(response["output"]["message"]["content"][0]["text"])
