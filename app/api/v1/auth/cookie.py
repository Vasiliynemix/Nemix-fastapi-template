from fastapi_users.authentication import CookieTransport

cookie_transport = CookieTransport(cookie_name='cookie', cookie_max_age=3600)
