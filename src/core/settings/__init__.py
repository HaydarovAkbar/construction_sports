from decouple import config

ENV_NAME = config('ENV_NAME', default='prod', cast=str)

if ENV_NAME == 'dev':
    from .dev import *
else:
    from .prod import *
