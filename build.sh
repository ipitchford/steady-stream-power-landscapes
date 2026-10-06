#!/bin/sh
set -eu
cd "$(dirname "$0")"
for item in manuscript:paper companion:companion; do
    directory=${item%:*}
    stem=${item#*:}
    (
        cd "$directory"
        pdflatex -interaction=nonstopmode -halt-on-error "$stem.tex"
        pdflatex -interaction=nonstopmode -halt-on-error "$stem.tex"
    )
done
