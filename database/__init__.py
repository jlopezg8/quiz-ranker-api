from config import settings

if settings.environment == 'prod':
    from database.deta import *
else:
    from database.dict import *
