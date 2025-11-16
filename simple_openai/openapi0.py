#!/usr/bin/env python3
"""
Simple Anthropic API call script with configurable system and user prompts.
"""

from openai import OpenAI
import os

# Initialize OpenAI client configured for Anthropic endpoint
client = OpenAI(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    base_url="https://api.anthropic.com/v1"
)

# Configurable prompts
SYSTEM_PROMPT = "You are a helpful assistant that provides clear and concise answers."
USER_PROMPT = "What is the capital of France?"

def main():
    """Make a single call to Anthropic API via OpenAI SDK."""
    try:
        response = client.chat.completions.create(
            model="claude-haiku-4-5-20251001",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT}
            ],
            temperature=0.7,
            max_tokens=500
        )

        # Extract and print the response
        answer = response.choices[0].message.content
        print(f"User: {USER_PROMPT}")
        print(f"\nAssistant: {answer}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
