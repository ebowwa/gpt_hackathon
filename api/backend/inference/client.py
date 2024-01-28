from openai import OpenAI

class OpenAIClient:
    def __init__(self, api_key, base_url):
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

    def get_chat_response(self, message):
        response = self.client.chat.completions.create(model="ollama/mistral", messages=[
            {
                "role": "user",
                "content": message
            }
        ])
        return response

if __name__ == "__main__":
    # Example usage
    client = OpenAIClient(api_key="null", base_url="https://dev-hub.agentartificial.com")
    response = client.get_chat_response("this is a test request, write a short poem about ducks wearing fedoras.")
    print(response)