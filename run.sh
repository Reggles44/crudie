#!/usr/bin/env bash

DATABASE_PORT=5432
DATABASE_URL=postgresql://postgres:crudie@localhost:$DATABASE_PORT

app::start() {
  app_dir=$1
  tag=$2
  docker build -f "$app_dir/Dockerfile" -t "$tag" "$app_dir"
  docker run --rm -d --name "$tag" -e DATABASE_URL=$DATABASE_URL --network=host -p 8888:8888 "$tag"
}

app::stop() {
  tag=$1
  docker logs "$tag"
  docker stop "$tag"
}

app::test() {
  python test.py
}

run() {
  for app in "$@"; do
    name=$(sed 's/\//-/g' <<<"$app")
    echo "Testing $name"

    app::start "$app" "$name"
    app::test "$name"
    app::stop "$name"

  done
}

run $1
