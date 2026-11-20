#!/usr/bin/env python3
"""news-image-20261120 entry (@huaminyo): copy the rendered front page to
/output/entry.png. Standard library only; deterministic (same bytes every run).
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")

os.makedirs(OUT, exist_ok=True)
# A plain copy: the bytes in the repository are the bytes the judge sees.
shutil.copyfile(SRC, os.path.join(OUT, "entry.png"))
