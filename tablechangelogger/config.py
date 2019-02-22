from django.conf import settings

TABLE_CHANGE_LOG_CONFIG = getattr(settings, 'TABLE_CHANGE_LOG_CONFIG')
TABLE_CHANGE_LOG_ENABLED = TABLE_CHANGE_LOG_CONFIG.get(
    'TABLE_CHANGE_LOG_ENABLED', True)

LOGGABLE_MODELS = []

if TABLE_CHANGE_LOG_ENABLED:
    for _, table_config in TABLE_CHANGE_LOG_CONFIG.items():
        LOGGABLE_MODELS.append(table_config)