# In llm_clients/ollama_client.py

import ollama
import logging
from llm_clients.base_client import BaseClient, ModelNotFoundError
from utils.data_schemas import ClientResponse

class OllamaClient(BaseClient):
    """Client for interacting with a local Ollama server."""

    def __init__(self, model_config: dict, endpoint_url: str):
        """
        Initialises the Ollama client and performs a pre-flight check
        to ensure the requested model is available locally.
        """
        super().__init__(model_config)
        self.client = ollama.Client(host=endpoint_url)
        
        try:
            logging.info(f"Checking for local Ollama model: {self.model_name}...")
            
            available_models = [m['model'] for m in self.client.list()['models']]
            
            if self.model_name not in available_models:
                raise ModelNotFoundError(
                    f"Ollama model '{self.model_name}' not found. "
                    f"Please run `ollama pull {self.model_name}` or check the model name."
                )
            logging.info(f"Ollama model '{self.model_name}' found and is ready.")
            
        except Exception as e:
            raise ModelNotFoundError(f"Could not verify Ollama models. Is the Ollama server running? Error: {e}")

    def get_completion(self, prompt: str) -> ClientResponse:
        """
        Gets a completion from the local Ollama server.
        """
        try:
            response = self.client.chat(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                format="json",
                options={"temperature": 0.0}
            )

            content = response["message"]["content"]
            prompt_tokens = response.get("prompt_eval_count", 0)
            completion_tokens = response.get("eval_count", 0)

            return ClientResponse(
                content=content,
                prompt_tokens=prompt_tokens,
                completion_tokens=completion_tokens,
            )
        except Exception as e:
            error_message = f"Ollama Error: {e}"
            logging.error(f"ERROR: {error_message}")
            return ClientResponse(error=error_message)