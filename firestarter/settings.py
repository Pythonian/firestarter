import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ADMINS = (
    ('Test Admin', 'test@example.com'),
)

SECRET_KEY = '#)=h)_wc*k%f=wk+!$x0t%1wx7*_50$a1%*75s$og(8$27$ju1'

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'crowdfunding',
    'widget_tweaks',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'firestarter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(BASE_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'firestarter.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / 'static_root'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR, 'static',
)


# The name of your project or campaign.
PROJECT_NAME = 'Firestarter Funding Campaign'

# The address of the funding site.
PROJECT_ADDR = 'http://localhost:8000'

# The slogan to be displayed on the main page.
PROJECT_SLOGAN = 'Support our awesome project.'

# Goal amount (int) that you are trying to raise.
GOAL = 25000

# Date (datetime object) when the campaign will end
DATE = datetime.datetime.now() + datetime.timedelta(days=30)

# Disable new contributions when time runs out?
STOP = False

# The email address that notifications will come from.
# e.g. noreply@example.com
NOTIFY_SENDER = 'noreply@example.com'

# List of payment types that you will accept.
# Possible values (copy these entirely):
#   ('CC', 'Credit Card (VISA/MasterCard/AMEX)', 'icon-credit-card')
#   ('PP', 'PayPal Account', 'icon-dollar')
PAY_TYPES = (
    ('CC', 'Credit Card (VISA/MasterCard/AMEX)', 'icon-credit-card'),
)

SUCCESS_DISCLAIMER = ('If you claimed a reward in connection with your contribution, '
    'shipping will begin by next month. Stay tuned to one of our social '
    'media accounts to get updates as to what rewards are shipping when.')

# Stripe API key (if using Stripe for CC payments)
STRIPE_PUBLIC_KEY = ''
STRIPE_PRIVATE_KEY = ''
