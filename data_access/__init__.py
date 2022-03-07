from config import settings

if settings.environment == 'prod':
    from data_access.deta import Test, Users
else:
    from data_access.dict import Test, Users
