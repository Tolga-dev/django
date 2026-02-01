from django.core.management.base import BaseCommand
import helpers
from django.conf import settings


VENDOR_STATICFILES = {
    "flowbite.min.js" : "https://cdn.jsdelivr.net/npm/flowbite@4.0.1/dist/flowbite.min.js",
    "flowbite.min.css" :"https://cdn.jsdelivr.net/npm/flowbite@4.0.1/dist/flowbite.min.css"
}

STATICFILES_VENDOR_DIRS = getattr(settings, 'STATICFILES_VENDOR_DIRS')

class Command(BaseCommand):
    help = 'Prints Hello, World! to the console'

    def handle(self, *args, **kwargs):
        self.stdout.write('Downloading vendor static files...')
        
        for filename, url in VENDOR_STATICFILES.items():
            output_path = STATICFILES_VENDOR_DIRS / filename
            dl_success = helpers.download_to_local(url, output_path)
            print(f"Downloading {filename} from {url}... {output_path}")
            if dl_success:
                self.stdout.write(self.style.SUCCESS(f'Successfully downloaded {filename}'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed to download {filename}'))
            
            
