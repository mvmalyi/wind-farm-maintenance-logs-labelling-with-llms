# utils/config_loader.py

import os
import getpass # A secure way to ask for user input without showing it on screen

def get_api_key(key_name: str, config: dict) -> str:
    """
    Retrieves an API key using a 3-step check:
    1. Checks for an environment variable.
    2. Checks the provided config dictionary (from YAML).
    3. Prompts the user for input as a last resort.
    
    Args:
        key_name: The name of the key to retrieve (e.g., "openai_api_key").
        config: The api_settings dictionary loaded from config.yaml.

    Returns:
        The retrieved API key.
    """
    # 1. Check for environment variable (e.g., OPENAI_API_KEY)
    env_var = key_name.upper() # (the convention is to use uppercase for env variables)
    api_key = os.getenv(env_var)
    if api_key:
        print(f"INFO: Found API key in environment variable '{env_var}'.")
        return api_key

    # 2. Check the config file dictionary
    api_key = config.get(key_name)
    # Check if the key exists and is not the placeholder
    if api_key and "YOUR_" not in api_key:
        print(f"INFO: Found API key in config.yaml.")
        return api_key

    # 3. Prompt the user
    print(f"WARNING: API key for '{key_name}' not found in environment variables or in the used configurations YAML file.")
    api_key = getpass.getpass(f"Please paste your {key_name} manually: ")
    return api_key