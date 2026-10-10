"""Один различающий локальный эксперимент; subject.py не изменяется."""
import hashlib
import platform
from pathlib import Path

from subject import cancel_edit

saved = {"value": "saved"}
draft = {"value": "draft"}
saved_before = saved.copy()
draft_before = draft.copy()
result = cancel_edit(saved, draft)

print("Python:", platform.python_version())
print("subject.py SHA256:", hashlib.sha256(Path("subject.py").read_bytes()).hexdigest())
print("saved:", repr(saved))
print("draft:", repr(draft))
print("result:", repr(result))
print("result is saved:", result is saved)
print("result == saved:", result == saved)
print("result == draft:", result == draft)
print("saved unchanged:", saved == saved_before)
print("draft unchanged:", draft == draft_before)
print("verdict:", "PASS" if result is saved and saved == saved_before else "FAIL")
