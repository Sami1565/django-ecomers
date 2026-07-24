import os
import sys
import django

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
    django.setup()
    
    from django.core.management import call_command
    from django.db import connection
    
    print("=== Starting Django Migration Process ===")
    
    # Delete ALL existing migrations to force fresh start
    print("1. Deleting old migration files...")
    
    # Force fresh migrations
    print("2. Creating fresh migrations...")
    call_command('makemigrations', interactive=False, verbosity=3)
    
    # Apply migrations
    print("3. Applying migrations...")
    call_command('migrate', interactive=False, verbosity=3)
    
    print("=== Migrations Completed Successfully! ===")

if __name__ == "__main__":
    main()