from django.apps import AppConfig


class SellConfig(AppConfig):
    name = 'pos.sell'

    def ready(self):
        import pos.sell.signals


