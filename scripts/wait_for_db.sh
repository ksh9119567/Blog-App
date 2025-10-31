#!/usr/bin/env bash
set -e

host="$1"
shift
cmd="$@"

echo "⏳ Waiting for PostgreSQL at $host to become available..."

# Wait for the PostgreSQL service
until pg_isready -h "$host" -U "$POSTGRES_USER" > /dev/null 2>&1; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "✅ Postgres is up - running migrations..."
alembic upgrade head

>&2 echo "🚀 Starting FastAPI server..."
exec $cmd
