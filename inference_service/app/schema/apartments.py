"""Schema for Apartment."""

from pydantic import BaseModel


class Apartment(BaseModel):
    """
    Apartment Schema.

    area - Apartment area
    constraction_year - Apartment construction year
    bedrooms - Count of Apartment bedrooms
    garden_area - Apartment garden area
    balcony_present - Apartment balcony presence
    parking_present - Apartment parking preents

    """
    area: int
    bedrooms: int
    garden: int
    constraction_year: int
    balcony_yes: int
    storage_yes: int
    parking_yes: int
    garage_yes: int
    furnished_yes: int
