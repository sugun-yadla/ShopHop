from django.apps import AppConfig

class ShopHopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shophop'

    def ready(self):
        # Import your function here
        from shophop.utils import get_cheapest_from_web_scrape_data
        # Call your function
        get_cheapest_from_web_scrape_data()
