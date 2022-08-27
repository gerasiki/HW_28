# Avito

## Run database (docker)
docker run --name hunting_db -e POSTGRES_PASSWORD=q1w2e3R$ -e POSTGRES_USER=user -e POSTGRES_DB=hunting -p 5432:5432 -d postgres:13.0-alpine

## Run postgres
docker run --name skypro-postgres -e POSTGRES_PASSWORD=postgres -d postgres
