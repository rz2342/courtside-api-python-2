from pydantic import BaseModel, Field
from datetime import datetime, date
from decimal import Decimal
from typing import Optional
from pydantic.alias_generators import to_camel


class GameResponse(BaseModel):
    id: int
    game_id: Optional[str] = Field(alias="gameId")
    home_team: str = Field(alias="homeTeam")
    away_team: str = Field(alias="awayTeam")

    # spread fields
    home_spread_odds: Optional[Decimal] = Field(alias="homeSpreadOdds")
    away_spread_odds: Optional[Decimal] = Field(alias="awaySpreadOdds")
    home_spread: Optional[Decimal] = Field(alias="homeSpread")
    opening_home_spread: Decimal = Field(alias="openingHomeSpread")
    home_moneyline: Optional[Decimal] = Field(alias="homeMoneyline")
    away_moneyline: Optional[Decimal] = Field(alias="awayMoneyline")

    # over/under fields
    opening_over_under: Decimal = Field(alias="openingOverUnder")
    over_under: Optional[Decimal] = Field(alias="overUnder")
    over_odds: Optional[Decimal] = Field(alias="overOdds")
    under_odds: Optional[Decimal] = Field(alias="underOdds")

    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    game_date: date = Field(alias="gameDate")
    has_ended: bool = Field(alias="hasEnded")

    class Config:
        orm_mode = True
        from_attributes = True
        populate_by_name = True  # This allows population using the field names


class GameIdUpdateRequest(BaseModel):
    home_team: str
    away_team: str
    game_date: date
    game_id: str

    class Config:
        # Allow both snake_case and camelCase when creating objects
        alias_generator = to_camel
        populate_by_name = True
        # Example for API documentation
        json_schema_extra = {
            "example": {
                "homeTeam": "New York Knicks",
                "awayTeam": "Brooklyn Nets",
                "gameDate": "2025-01-11",
                "gameId": "0112102",
            }
        }
