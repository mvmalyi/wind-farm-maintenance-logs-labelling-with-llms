# llm_clients/openai_client.py

import time
from openai import OpenAI, APIError
from llm_clients.base_client import BaseClient
from utils.data_schemas import ClientResponse

class OpenAIClient(BaseClient):
    """Client for interacting with the OpenAI API."""

    def __init__(self, model_config: dict, api_key: str):
        super().__init__(model_config, api_key)
        self.client = OpenAI(api_key=self.api_key)

    def get_completion(self, prompt: str) -> ClientResponse:
        """
        Gets a completion from the OpenAI API with retry logic.

        Args:
            prompt: The formatted prompt string.

        Returns:
            A ClientResponse object.
        """
        retries = 3
        delay = 5  # seconds

        for i in range(retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[{"role": "user", "content": prompt}],
                    #temperature=0.0, # Intended for reproducibility but seems like it doesn't work with the latest GPT versions
                    response_format={"type": "json_object"},
                )
                
                content = response.choices[0].message.content
                prompt_tokens = response.usage.prompt_tokens
                completion_tokens = response.usage.completion_tokens
                
                return ClientResponse(
                    content=content,
                    prompt_tokens=prompt_tokens,
                    completion_tokens=completion_tokens
                )

            except APIError as e:
                print(f"ERROR: OpenAI API error: {e}. Attempt {i + 1} of {retries}.")
                if i < retries - 1:
                    time.sleep(delay * (i + 1)) # Exponential backoff
                else:
                    return ClientResponse(error=f"OpenAI API Error: {e}")
            except Exception as e:
                return ClientResponse(error=f"An unexpected error occurred: {e}")
        
        return ClientResponse(error="Failed to get completion after all retries.")