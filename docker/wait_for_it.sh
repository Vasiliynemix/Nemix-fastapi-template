#!/bin/bash
# wait-for-it.sh

host="$1"
port="$2"
shift 2
cmd="$@"

until nc -z "$host" "$port"; do
  echo "Сервис $host:$port недоступен, ожидание..."
  sleep 1
done

exec "$cmd"