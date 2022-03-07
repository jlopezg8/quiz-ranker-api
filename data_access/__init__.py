from config import settings

if settings.environment == 'prod':
    from data_access.deta import Users
else:
    from data_access.dict import Users
