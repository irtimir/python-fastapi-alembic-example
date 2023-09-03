from sqlmodel import SQLModel, Field


# Just pydantic data-only model
class MovieBase(SQLModel):
    name: str


# Adds the id to the model, this is a tabular model (table=True),
# so it is both a pydantic and SQLAlchemy model
class Movie(MovieBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


# Pydantic model, will be used to create the instances
class MovieCreateIn(MovieBase):
    pass
