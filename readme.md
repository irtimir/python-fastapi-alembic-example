# FastAPI + Asyncpg + Alembic example

## Get started

```shell
docker compose up --build
```

## Migrations

### Create base structure
Alembic initialization with [asynchronous template](https://github.com/sqlalchemy/alembic/tree/rel_1_12_0/alembic/templates/async).
Creates structure in `project/migrations`

```shell
docker-compose exec web alembic init -t async migrations
```

### Create a new migration

```shell
docker-compose exec web alembic revision --autogenerate
```

### Applying Migration

```shell
docker-compose exec web alembic upgrade head
```
