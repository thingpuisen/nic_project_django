#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nic_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
     # If runsslserver is in the arguments, print a clean HTTPS URL
    if "runsslserver" in sys.argv:
        print("Your Django HTTPS server is running at: https://127.0.0.1:8000\n")

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
