import os
import sys
import django

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
    django.setup()
    
    from django.core.management import call_command
    
    print("=== Starting Django on Vercel ===")
    
    try:
        # Create migrations
        print("Creating migrations...")
        call_command('makemigrations', interactive=False)
        
        # Apply migrations
        print("Applying migrations...")
        call_command('migrate', interactive=False)
        
        # Collect static files
        print("Collecting static files...")
        call_command('collectstatic', interactive=False)
        
        print("=== Deployment successful! ===")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()