"""
Vercel Build Migration Script
This script runs migrations during Vercel deployment
"""

import os
import sys
import django

def main():
    """
    Main function to run migrations on Vercel
    """
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
    
    # Setup Django
    django.setup()
    
    from django.core.management import call_command
    from django.db import connection
    
    print("=" * 50)
    print("🚀 Starting Django Migration Process on Vercel")
    print("=" * 50)
    
    try:
        # Step 1: Create migrations
        print("\n📝 Step 1: Creating migrations...")
        call_command('makemigrations', interactive=False, verbosity=3)
        print("✅ Migrations created successfully!")
        
        # Step 2: Apply migrations
        print("\n📝 Step 2: Applying migrations...")
        call_command('migrate', interactive=False, verbosity=3)
        print("✅ Migrations applied successfully!")
        
        # Step 3: Verify database schema
        print("\n📝 Step 3: Verifying database schema...")
        with connection.cursor() as cursor:
            # Check if store_product table exists
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='store_product';")
            table_exists = cursor.fetchone()
            
            if table_exists:
                # Get column names
                cursor.execute("PRAGMA table_info(store_product);")
                columns = cursor.fetchall()
                column_names = [col[1] for col in columns]
                print(f"   ✅ Columns in store_product: {', '.join(column_names)}")
                
                # Check for 'available' field
                if 'available' in column_names:
                    print("   ✅ 'available' field found!")
                else:
                    print("   ⚠️ 'available' field not found - re-running migrations...")
                    call_command('migrate', interactive=False, verbosity=3)
            else:
                print("   ℹ️ store_product table not found yet - migrations will create it")
        
        print("\n" + "=" * 50)
        print("✅ Migrations Completed Successfully!")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n❌ Error during migration: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()