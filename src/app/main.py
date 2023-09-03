from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db import get_session
from app.models import Movie, MovieCreateIn

app = FastAPI()


@app.get('/movies', response_model=list[Movie])
async def get_movies(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Movie))
    return result.scalars().all()


@app.post('/movies')
async def add_movie(movie: MovieCreateIn, session: AsyncSession = Depends(get_session)):
    movie = Movie(name=movie.name)
    session.add(movie)
    await session.commit()
    await session.refresh(movie)
    return movie
