try:
    from settings.deve_settings import *
except ImportError as exc:
    raise ImportError(
        "Couldn't import development settings from settings_module."
    ) from exc
