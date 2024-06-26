import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
else:
    # Fill the Values
    API_ID = 1623073
    API_HASH = "a6f2f0a7b2022f8ca7717d9101c5ff5c"
    BOT_TOKEN = "7450280328:AAHdx_qn1-imOcirYLiqmgDalepvb_EyDYQ"
    DATABASE_URL = "postgresql://whisperbot_iv:ivarmone009@localhost:5432/whisper_ivbot"
