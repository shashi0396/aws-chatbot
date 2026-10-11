
import os

APP_TITLE = "Cloud Assistant"
APP_ICON = "🤖"

APP_MODE = os.getenv("APP_MODE", "mock")

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

BEDROCK_MODEL_ID = os.getenv(
    "BEDROCK_MODEL_ID",
    "amazon.nova-micro-v1:0",
)