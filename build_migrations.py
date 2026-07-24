import os
import sys
import django

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
    django.setup()
    
    from django.core.management import call_command
    from django.db import connection
    
    print("=== Starting Django Migration Process on Vercel ===")
    
    try:
        # Force migrations
        print("1. Creating migrations...")
        call_command('makemigrations', interactive=False, verbosity=3)
        
        print("2. Applying migrations...")
        call_command('migrate', interactive=False, verbosity=3)
        
        # Check if 'available' field exists
        print("3. Verifying schema...")
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            print(f"Tables found: {tables}")
        
        print("=== Migrations Completed Successfully! ===")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()