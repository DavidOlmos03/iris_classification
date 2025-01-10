from pydantic import BaseModel, model_validator

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    @model_validator(mode="before")
    def validate_fields(cls, values: dict[str, float]) -> dict[str, float]:
        for field in ["sepal_length", "sepal_width", "petal_length", "petal_width"]:
            value = values.get(field)
            if value is None or value == "":
                raise ValueError(f"{field} cannot be empty.")
            if not isinstance(value, (float, int)):
                raise TypeError(f"All data in {field} must be float or integer.")
            if value <= 0:
                raise ValueError(f"All data in {field} must be positive.")
        return values