#!/bin/sh
set -eu
cd "$(dirname "$0")"
exec python3 -m http.server "${1:-8873}" --bind 127.0.0.1
