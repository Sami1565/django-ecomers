#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
    
    # Auto-migrate on Vercel
    if 'VERCEL' in os.environ:
        print("=== Vercel Deployment - Running Migrations ===")
        try:
            from django.core.management import call_command
            call_command('makemigrations', interactive=False)
            call_command('migrate', interactive=False)
            print("Migrations applied!")
        except Exception as e:
            print(f"Migration error: {e}")
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()