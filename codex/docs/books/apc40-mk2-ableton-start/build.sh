#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
exec "$HOME/src/firstpair/publishing/scripts/build-library-book.sh" \
  --repo-root "$repo_root" \
  "$@"
