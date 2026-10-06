#!/usr/bin/env python3
"""Verify the package byte hashes before rebuilding or replaying."""
from __future__ import annotations
import hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def main()->None:
    count=0
    for line in (ROOT/'MANIFEST.sha256').read_text().splitlines():
        if not line.strip():
            continue
        expected,relative=line.split('  ',1)
        path=(ROOT/relative).resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError(f'Unsafe manifest path: {relative}')
        actual=hashlib.sha256(path.read_bytes()).hexdigest()
        if actual!=expected:
            raise SystemExit(f'HASH MISMATCH: {relative}')
        count+=1
    print(f'PASS: {count} package files match SHA-256 manifest.')
if __name__=='__main__':
    main()
