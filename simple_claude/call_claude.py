#!/usr/bin/env python3
"""
Simple script to call Claude AI using the Anthropic API.
"""

import os
import sys
from anthropic import Anthropic

model = "claude-haiku-4-5-20251001"

def call_claude(prompt: str, model: str = model, max_tokens: int = 1024) -> str:
    """
    Call Claude AI with a given prompt.
    
    Args:
        prompt: The user's prompt/question
        model: The Claude model to use (default: claude-haiku-4-5-20251001)
        max_tokens: Maximum tokens in the response (default: 1024)
    
    Returns:
        The response text from Claude
    
    Raises:
        ValueError: If API key is not set
        Exception: For API errors
    """
    # Get API key from environment variable
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "ANTHROPIC_API_KEY environment variable is not set. "
            "Please set it with: export ANTHROPIC_API_KEY='your-api-key'"
        )
    
    # Initialize the Anthropic client
    client = Anthropic(api_key=api_key)
    
    try:
        # Make the API call
        message = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract and return the response text
        return message.content[0].text
    
    except Exception as e:
        raise Exception(f"Error calling Claude API: {str(e)}")


def main():
    """Main function to run the script."""
    if len(sys.argv) < 2:
        print("Usage: python call_claude.py '<your prompt>'")
        print("\nExample:")
        print("  python call_claude.py 'What is the capital of France?'")
        print("\nNote: Make sure ANTHROPIC_API_KEY environment variable is set.")
        sys.exit(1)
    
    prompt = sys.argv[1]
    
    try:
        response = call_claude(prompt)
        print("\nClaude's response:")
        print("-" * 50)
        print(response)
        print("-" * 50)
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

