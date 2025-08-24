# llm_clients/base_client.py

from abc import ABC, abstractmethod
from utils.data_schemas import ClientResponse

class ModelNotFoundError(Exception):
    """Custom exception raised when an LLM model is not found."""
    pass

class BaseClient(ABC):
    """
    Abstract Base Class for all LLM API clients.

    It enforces a common interface for making API calls and retrieving
    structured responses, ensuring interchangeability in the main script.
    """
    def __init__(self, model_config: dict, api_key: str | None = None):
        """
        Initialises the client with model-specific configuration.

        Args:
            model_config: A dictionary containing model details from config.yaml.
            api_key: The API key for the service, if required.
        """
        self.model_config = model_config
        self.model_name = model_config.get("model_name")
        self.api_key = api_key

    @abstractmethod
    def get_completion(self, prompt: str) -> ClientResponse:
        """
        The core method to get a completion from the LLM.
        This must be implemented by all subclasses.

        Args:
            prompt: The formatted prompt string to send to the model.

        Returns:
            A ClientResponse object containing the model's output and metadata.
        """
        pass