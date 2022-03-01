from ..config import settings

if settings.environment == 'prod':
    from .deta import *
else:
    from .dict import *
