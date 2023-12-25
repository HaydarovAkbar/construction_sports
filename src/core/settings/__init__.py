from decouple import config

ENV_NAME = config('ENV_NAME', default='production', cast=str)

if ENV_NAME == 'dev':
    from .dev import *
elif ENV_NAME == 'test':
    from .test import *
else:
    from .prod import *
