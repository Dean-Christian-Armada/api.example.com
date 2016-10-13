from django.conf import settings

if not settings.DEBUG:
	print "--------"
	print "ON PRODUCTION"
	ALLOWED_HOSTS = ["example.com"]

	# Database
	# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
	DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'example_com',
        'USER': 'deanarmada',
        'PASSWORD': 'd3@narmada13',
        'HOST': 'localhost', # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        'PORT': '', 
    }
}