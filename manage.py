#!/usr/bin/env pythone:\mohamad\project_5\Mysite\fffffffff\models.py e:\mohamad\project_5\Mysite\fffffffff\views.py e:\mohamad\project_5\Mysite\fffffffff\migrations e:\mohamad\project_5\Mysite\fffffffff\admin.py
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_5.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
