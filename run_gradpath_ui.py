"""Local launcher for the GradPath web UI."""

from __future__ import annotations

import sys
import threading
import time
import webbrowser
from pathlib import Path

# The repo folder is named `Gradpath` (capital G) but agents import from
# `gradpath` (lowercase). Python's import system is case-sensitive even on
# macOS. We add the parent to sys.path, import the package under its real
# name, then register it under the lowercase alias so all agent imports resolve.
_parent = Path(__file__).resolve().parent.parent
if str(_parent) not in sys.path:
    sys.path.insert(0, str(_parent))

import importlib as _importlib
_pkg = _importlib.import_module("Gradpath")
sys.modules.setdefault("gradpath", _pkg)

import uvicorn


def _open_browser() -> None:
    time.sleep(1.2)
    webbrowser.open("http://127.0.0.1:8000")


if __name__ == "__main__":
    threading.Thread(target=_open_browser, daemon=True).start()
    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=False)
