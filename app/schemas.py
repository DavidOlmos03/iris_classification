"""
    This module contains the IrisFeatures class, which is used to validate the input data.
"""

from pydantic import BaseModel, model_validator

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    @model_validator(mode="before")
    def validate_fields(cls, values: dict[str, float]) -> dict[str, float]:
        """
        Validates the fields of the IrisFeatures class.

        This validator checks that all fields are not empty, are floats or integers, 
        and are positive.
        If any of these conditions are not met, it raises a ValueError.

        Args:
            values (dict[str, float]): A dictionary containing the values of the IrisFeatures class.

        Returns:
            dict[str, float]: The validated dictionary.

        Raises:
            ValueError: If any of the fields are empty, not floats or integers, or not positive.
            TypeError: If any of the fields are not floats or integers.
        """

        for field in ["sepal_length", "sepal_width", "petal_length", "petal_width"]:
            value = values.get(field)
            if value is None or value == "":
                raise ValueError(f"{field} cannot be empty.")
            if not isinstance(value, (float, int)):
                raise TypeError(f"All data in {field} must be float or integer.")
            if value <= 0:
                raise ValueError(f"All data in {field} must be positive.")
        return values
