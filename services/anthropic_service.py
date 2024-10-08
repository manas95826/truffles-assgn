# services/anthropic_service.py
import anthropic

class AnthropicService:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key="YOUR_ANTHROPIC_API_KEY")

    def extract_bank_statements(self, documents: str, extracted_data: str, user_query: str) -> str:
        response = self.client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=4096,
            messages=[
                {
                    "role": "user",
                    "content": f"This is the complete bank statement {documents} and the user's query is more specific to the extracted part: {extracted_data}. User query is {user_query}.",
                },
            ],
        )
        return response.content
