#!/usr/bin/env bash
set -euo pipefail
book_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
firstpair_root="${FIRSTPAIR_ROOT:-$HOME/src/firstpair}"
case "${1:-book}" in
  book)
    shift || true
    exec "$firstpair_root/publishing/scripts/build-library-book.sh" --repo-root "$book_root" "$@"
    ;;
  prepare-vault)
    exec python3 "$book_root/scripts/prepare-vault-source.py"
    ;;
  plan-vault)
    exec "$firstpair_root/publishing/scripts/firstpair-vault" plan "$book_root/vault.build.json" --product desktop
    ;;
  vault)
    exec "$firstpair_root/publishing/scripts/firstpair-vault" build "$book_root/vault.build.json" --product desktop
    ;;
  check-vault)
    exec "$firstpair_root/publishing/scripts/firstpair-vault" validate --vault "$book_root/dist-obsidian/Professional Podcat Audio"
    ;;
  *)
    echo 'Usage: ./build.sh [book|prepare-vault|plan-vault|vault|check-vault]' >&2
    exit 2
    ;;
esac
