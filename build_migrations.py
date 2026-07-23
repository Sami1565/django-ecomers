import os
import sys
import django

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
    django.setup()
    
    from django.core.management import call_command
    call_command('makemigrations')
    call_command('migrate')
    print("Migrations applied successfully!")

if __name__ == "__main__":
    main()