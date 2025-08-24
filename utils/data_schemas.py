# utils/data_schemas.py

"""
This module defines the Pydantic models for data validation.

These schemas ensure that the data returned by the Large Language Models (LLMs)
conforms to a predefined structure, which is crucial for maintaining data
integrity throughout the benchmarking pipeline.
"""

from pydantic import BaseModel, Field
from typing import Literal

class LLMOutput(BaseModel):
    """
    A Pydantic model to validate the JSON structure of the LLM's output.

    This class serves as a "template" for the expected response, ensuring that
    each field exists and has the correct data type. The `Field(alias=...)`
    allows the Python attribute (e.g., `maintenance_type`) to be different
    from the JSON key (e.g., "Maintenance Type"), which is useful for
    adhering to Python's snake_case naming conventions.
    """
    maintenance_type: str = Field(
        ...,
        alias="Maintenance Type",
        description="The classified maintenance type for the log entry."
    )
    issue_category: str = Field(
        ...,
        alias="Issue Category",
        description="The classified issue category for the log entry."
    )
    specific_problem: str | None = Field(
        None,
        alias="Specific Problem",
        description="A more granular, inferred problem description, if available."
    )
    certainty_level: Literal['High', 'Medium', 'Low', 'Unknown'] = Field(
        ...,
        alias="Certainty Level",
        description="The model's self-assessed confidence in its classification."
    )

    class Config:
        """
        Pydantic configuration options.
        `populate_by_name = True` allows using either the field name or alias for population.
        """
        populate_by_name = True

class ClientResponse(BaseModel):
    """
    A standardised data structure for the response from any LLM client.
    This ensures the main processing loop receives a consistent object.
    """
    content: str | None = None
    prompt_tokens: int = 0
    completion_tokens: int = 0
    error: str | None = None
    sleep_duration: float = 0.0