# In llm_clients/google_client.py

import time
import google.generativeai as genai
from llm_clients.base_client import BaseClient
from utils.data_schemas import ClientResponse
import logging

class GoogleClient(BaseClient):
    """Client for interacting with the Google Gemini API."""

    def __init__(self, model_config: dict, api_key: str):
        super().__init__(model_config, api_key)
        genai.configure(api_key=self.api_key)
        self.client = genai.GenerativeModel(self.model_name)
        self.requests_made = 0

        # Check if an RPM limit is specified in the config
        self.rpm = self.model_config.get("rpm") 
        if self.rpm:
            # If it is, calculate the delay
            self.delay_between_requests = (60.0 / self.rpm) + 1.0
            logging.info(f"RPM limit for {self.model_name} set to {self.rpm}. Delay between requests: {self.delay_between_requests:.1f}s.")
        else:
            # If not specified, set delay to zero
            self.delay_between_requests = 0

    def get_completion(self, prompt: str) -> ClientResponse:
        """
        Gets a completion from the Gemini API with rate limiting and retry logic.
        """
        sleep_slept = 0.0

        # Only sleep if a delay is configured and it's not the first request
        if self.requests_made > 0 and self.delay_between_requests > 0:
            logging.info(f"Waiting {self.delay_between_requests:.1f}s to respect Google API rate limit...")
            time.sleep(self.delay_between_requests)
            sleep_slept = self.delay_between_requests
        
        self.requests_made += 1

        retries = 3
        delay = 5

        for i in range(retries):
            try:
                generation_config = genai.types.GenerationConfig(
                    temperature=0.0,
                    response_mime_type="application/json",
                    max_output_tokens=2048
                )
                response = self.client.generate_content(
                    prompt,
                    generation_config=generation_config
                )
                prompt_tokens = response.usage_metadata.prompt_token_count
                completion_tokens = response.usage_metadata.candidates_token_count
                content = response.text

                return ClientResponse(
                    content=content,
                    prompt_tokens=prompt_tokens,
                    completion_tokens=completion_tokens,
                    sleep_duration=sleep_slept
                )
            except Exception as e:
                logging.error(f"Google API error: {e}. Attempt {i + 1} of {retries}.")
                if i < retries - 1:
                    time.sleep(delay * (i + 1))
                else:
                    return ClientResponse(error=f"Google API Error: {e}", sleep_duration=sleep_slept)

        return ClientResponse(error="Failed to get completion after all retries.", sleep_duration=sleep_slept)