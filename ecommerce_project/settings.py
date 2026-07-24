# ===== VERCEL PRODUCTION SETTINGS =====
import os
import sys

# Force migrations on Vercel
if 'VERCEL' in os.environ:
    print("Running on Vercel - Applying migrations...")
    from django.core.management import call_command
    try:
        call_command('migrate', interactive=False, verbosity=3)
        print("Migrations applied successfully!")
    except Exception as e:
        print(f"Error applying migrations: {e}")