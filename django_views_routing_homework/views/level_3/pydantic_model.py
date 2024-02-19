from pydantic import BaseModel, EmailStr, field_validator


class UserData(BaseModel):
    full_name: str
    email: EmailStr
    registered_from: str
    age: int | None = None

    @field_validator('full_name')
    def full_name_is_valid(cls, v: str) -> bool:  # noqa: VNE001
        if 5 <= len(v) <= 256:
            return True
        raise ValueError("Name must be between 5 and 256 characters")

    @field_validator('registered_from')
    def registered_from_is_valid(cls, v: str) -> bool:  # noqa: VNE001
        if v == 'website' or v == 'mobile_app':
            return True
        raise ValueError("Registered from must be 'website' or 'mobile_app'")

    @field_validator('age')
    def age_is_valid(cls, v: int) -> bool:  # noqa: VNE001
        if 0 <= v <= 120:
            return True
        raise ValueError("Age must be between 0 and 120")
