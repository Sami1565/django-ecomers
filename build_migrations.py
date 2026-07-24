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
        
        # Verify the 'available' field exists
        print("3. Verifying schema...")
        with connection.cursor() as cursor:
            cursor.execute("PRAGMA table_info(store_product);")
            columns = cursor.fetchall()
            column_names = [col[1] for col in columns]
            print(f"Columns in store_product: {column_names}")
            
            if 'available' in column_names:
                print("✅ 'available' field found!")
            else:
                print("❌ 'available' field NOT found - re-running migrations...")
                call_command('migrate', interactive=False, verbosity=3)
        
        print("=== Migrations Completed Successfully! ===")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()