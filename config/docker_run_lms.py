# -*- coding: utf-8 -*-


# FUN_BASE_ROOT should be added to Python PATH before importing this file
import sys
from path import path
BASE_ROOT = path('/app/')
FUN_BASE_ROOT = BASE_ROOT / "fun-apps"
sys.path.append(FUN_BASE_ROOT)



from fun.envs.lms.common_wb import *


PLATFORM_NAME = u'FUN Campus, la plateforme'
ENVIRONMENT = 'campus'
LMS_BASE = 'lmscampus.preprod.fmb.objectif-libre.com'
CMS_BASE = 'cmscampus.preprod.fmb.objectif-libre.com'
SITE_NAME = LMS_BASE
EMAIL_DOMAIN = 'fun-campus.fr'
GOOGLE_ANALYTICS_ACCOUNT = 'demo'

LMS_ROOT_URL = "https://{}".format(LMS_BASE)
SITE_VARIANT = 'lms'
GOOGLE_ANALYTICS_ACCOUNT = ''
SERVER_EMAIL = '%s-%s@%s' % (ENVIRONMENT, SITE_VARIANT, EMAIL_DOMAIN)
#FAVICON_PATH = "/static/starter-theme/images/favicon.ico"


DEFAULT_FROM_EMAIL = "no-reply@fun-campus.fr"
DEFAULT_FEEDBACK_EMAIL = "feedback@fun-campus.fr"
DEFAULT_BULK_FROM_EMAIL = "no-reply@fun-campus.fr"
TECH_SUPPORT_EMAIL = "technical@fun-campus.fr"
CONTACT_EMAIL = "info@fun-campus.fr"
BUGS_EMAIL = "bugs@fun-campus.fr"
PAYMENT_SUPPORT_EMAIL = "billing@fun-campus.fr"
PAYMENT_ADMIN = "demo"
# STATS emails are used by fun/management/commands/enrollment_statistics.py
STATS_EMAIL = "demo"
FAVICON_PATH = "images/favicon.ico"

BULK_EMAIL_DEFAULT_FROM_EMAIL = "no-reply@fun-campus.fr"


ADMINS = [['funteam', 'richard@openfun.fr']]


RAVEN_CONFIG = {
    'dsn': '',
}

update_logging_config(LOGGING)

def configure_raven(sentry_dsn, raven_config, logging_config):
    logging_config['handlers']['sentry']['dsn'] = sentry_dsn
    raven_config['dsn'] = sentry_dsn

configure_raven("https://9f7147a6f22c461db73188c7345f58e0:5a58060e3a9e452686359187b47db2c2@sentry.fun-mooc.fr/17",
                RAVEN_CONFIG, LOGGING)

BULK_SMTP_SERVER = '192.168.10.254'
TRANSACTIONAL_SMTP_SERVER = '192.168.10.254'
EMAIL_BACKEND = 'fun.smtp.backend.MultipleSMTPEmailBackend'
EMAIL_HOST = {
    'bulk': {'host': BULK_SMTP_SERVER, 'port': 12016 },
    'transactional': {'host': TRANSACTIONAL_SMTP_SERVER, 'port': 12015 }
    }

ELASTIC_SEARCH_CONFIG = [{'host': 'elasticsearch', 'port': 9200}]
HAYSTACK_CONNECTIONS = configure_haystack(ELASTIC_SEARCH_CONFIG)

VIDEOFRONT_ADMIN_TOKEN = "a454b283a7a783b02f0d07aaf4a661b558b1c327"

REGISTRATION_EXTRA_FIELDS = {u'city': u'hidden', u'gender': u'optional', u'year_of_birth': u'optional', u'level_of_education': u'optional', u'goals': u'optional', u'honor_code': u'required', u'terms_of_service': u'required', u'country': u'hidden', u'mailing_address': u'optional'}

MKTG_URL_LINK_MAP = {u'ABOUT': u'about', u'GIP': u'gip', u'TOS': u'charte',
                     u'LEGAL': u'legal', u'COURSES': u'courses', u'CONTACT':
                     u'contact', u'CHARTE': u'charte', u'ROOT': u'root',
                     u'HONOR': u'legal', 'MOOC': 'mooc', 'CREATE': 'create'}

# those settings make links in navigation.html work (fun logo and courses)
FEATURES['COURSES_ARE_BROWSABLE'] = True
MKTG_URLS = {
        'ROOT': '/',
        'COURSES': 'courses'
}

CACHES = {'celery': {'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'KEY_FUNCTION': 'util.memcache.safe_key',
            'KEY_PREFIX': 'integration_celery',
            'LOCATION': ['memcached:11211']},
 'default': {'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
             'KEY_FUNCTION': 'util.memcache.safe_key',
             'KEY_PREFIX': 'sandbox_default',
             'LOCATION': ['memcached:11211']},
 'general': {'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
             'KEY_FUNCTION': 'util.memcache.safe_key',
             'KEY_PREFIX': 'sandbox_general',
             'LOCATION': ['memcached:11211']},
 'mongo_metadata_inheritance': {'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
                                'KEY_FUNCTION': 'util.memcache.safe_key',
                                'KEY_PREFIX': 'integration_mongo_metadata_inheritance',
                                'LOCATION': ['memcached:11211']},
 'openassessment_submissions': {'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
                                'KEY_FUNCTION': 'util.memcache.safe_key',
                                'KEY_PREFIX': 'openassessment_submissions',
                                'LOCATION': '/data/shared/openassessment_submissions_cache'},
 'staticfiles': {'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
                 'KEY_FUNCTION': 'util.memcache.safe_key',
                 'KEY_PREFIX': 'integration_static_files',
                 'LOCATION': ['memcached:11211']},
 'video_subtitles': {'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
                     'KEY_FUNCTION': 'util.memcache.safe_key',
                     'KEY_PREFIX': 'video_subtitles',
                     'LOCATION': '/data/shared/video_subtitles_cache'}}


SVG_CONVERTER_SERVER = 'http://haproxy:85'
SVG_CONVERTER_SERVER_TOKEN = 'NONE'

MKTG_URL_LINK_MAP= {
    'GIP': u'gip',
    'ABOUT': u'about',
    'LEGAL': u'legal',
    'CHARTE': u'charte',
    'CONTACT': u'contact',
    'CONDITIONS': u'conditions',
    'POLITIQUE': u'politique',
    'ROOT': u'root',
    'COURSES': u'courses',
    'HONOR': u'charte',
    'TOS': u'conditions',
 }
FEATURES['AUTOMATIC_AUTH_FOR_TESTING'] = True

# Sampaccoud hack to make it work
SHARED_ROOT = '/data/shared'
ORA2_FILEUPLOAD_ROOT = os.path.join(SHARED_ROOT, "openassessment_submissions")
ORA2_FILEUPLOAD_CACHE_ROOT = os.path.join(SHARED_ROOT, "openassessment_submissions_cache")

STATIC_ROOT = '/data/static/lms'
MEDIA_ROOT = '/data/media'

STATIC_URL = '/static/'

LOGGING['handlers'].update(
    local={'class': 'logging.NullHandler'},
    tracking={'class': 'logging.NullHandler'},
)

sys.path.append('/app/edx-platform/common/djangoapps')
