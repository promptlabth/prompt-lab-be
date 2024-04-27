from typing import Optional, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint

if TYPE_CHECKING:
    from app.model.features.features_model import Features
    from app.model.models.models_model import Models
    from app.model.languages.languages_model import Languages

class InputPrompts(SQLModel, table=True):
    __tablename__ = "input_prompts"
    __table_args__ = (
        UniqueConstraint("feature_id", "model_id", "language_id", name="unique input prompts"),
    )
    id: Optional[int] = Field(default=None, primary_key=True)
    prompt_input: str

    # Relationship

    # 1 input prompt have 1 tone
    feature_id: Optional[int] = Field(default=None, foreign_key="features.id")
    feature: Optional["Features"] = Relationship(back_populates="input_prompts")

    # 1 input prompt have 1 model
    model_id: Optional[int] = Field(default=None, foreign_key="models.id")
    model: Optional["Models"] = Relationship(back_populates="inputPrompts")

    # 1 input prompt have 1 language
    language_id: Optional[int] = Field(default=None, foreign_key="languages.id")
    language: Optional["Languages"] = Relationship(back_populates="input_prompts")