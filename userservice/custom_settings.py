import os
KONG_ADMIN_URL = os.environ['KONG_ADMIN_URL'] if os.environ.get('KONG_ADMIN_URL') else "http://kong:8001"
