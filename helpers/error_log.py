import os
import sys
import traceback
from datetime import datetime

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IMAGE_HINTS = {
    "refresh_button": {
        "path": "images/ui/refresh_button.PNG",
        "suggestion": (
            "Take a new screenshot of the refresh button and replace "
            "images/ui/refresh_button.PNG (keep the same filename)."
        ),
    },
    "covenant": {
        "path": "images/covenant/covenant.PNG",
        "suggestion": (
            "Take a new screenshot of the covenant summon and replace "
            "images/covenant/covenant.PNG (keep the same filename)."
        ),
    },
    "mystic": {
        "path": "images/mystic/mystic.PNG",
        "suggestion": (
            "Take a new screenshot of the mystic summon and replace "
            "images/mystic/mystic.PNG (keep the same filename)."
        ),
    },
    "buy_button": {
        "path": "images/ui/buy_button.png",
        "suggestion": (
            "Take a new screenshot of the buy confirmation button and replace "
            "images/ui/buy_button.png (keep the same filename)."
        ),
    },
    "confirm_button": {
        "path": "images/ui/confirm_button.PNG",
        "suggestion": (
            "Take a new screenshot of the refresh confirm button and replace "
            "images/ui/confirm_button.PNG (keep the same filename)."
        ),
    },
    "unknown": {
        "path": None,
        "suggestion": (
            "Verify Tesseract OCR is installed at "
            "C:\\Program Files\\Tesseract-OCR\\tesseract.exe and that the game "
            "shop is visible on screen."
        ),
    },
}


class AppError(Exception):
    def __init__(self, context, message):
        super().__init__(message)
        self.context = context


def resource_path(relative_path):
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS
    else:
        base = PROJECT_ROOT
    return os.path.join(base, relative_path)


def _log_directory():
    if getattr(sys, "frozen", False):
        base = os.path.dirname(sys.executable)
    else:
        base = PROJECT_ROOT
    return os.path.join(base, "log")


def _log_filename():
    now = datetime.now()
    stem = f"{now.day}-{now.strftime('%B')}-{now.hour}-{now.minute}"
    log_dir = _log_directory()
    os.makedirs(log_dir, exist_ok=True)
    candidate = os.path.join(log_dir, f"{stem}.log")
    if not os.path.exists(candidate):
        return candidate
    suffix = 2
    while True:
        candidate = os.path.join(log_dir, f"{stem}-{suffix}.log")
        if not os.path.exists(candidate):
            return candidate
        suffix += 1


def write_error_log(context, exc):
    hint = IMAGE_HINTS.get(context, IMAGE_HINTS["unknown"])
    lines = [
        f"Timestamp: {datetime.now().isoformat(timespec='seconds')}",
        f"Context: {context}",
        f"Error: {exc}",
    ]
    if hint["path"]:
        lines.append(f"Image: {hint['path']}")
    lines.append(f"Suggestion: {hint['suggestion']}")
    lines.append("")
    lines.append("Traceback:")
    if isinstance(exc, BaseException):
        lines.append("".join(traceback.format_exception(type(exc), exc, exc.__traceback__)))
    else:
        lines.append(str(exc))
    log_path = _log_filename()
    with open(log_path, "w", encoding="utf-8") as log_file:
        log_file.write("\n".join(lines))
