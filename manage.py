import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scheduler.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError() from exc
    if "runserver" in sys.argv:
        sys.argv.append("--noreload")
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
