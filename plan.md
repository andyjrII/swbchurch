To Deploy your site:

1. Install white noise
   pip install whitenoise

2. Add whitenoise to the middleware section in Django settings:
   "whitenoise.middleware.WhiteNoiseMiddleware"

3. Install gunicorn
   pip install gunicorn

4. Downgrade Django version to 3
   pip install django==3.2.1

5. Find a compatible django filter version
   pip install django-filter==2.3

   ###########################
   Admin login
   ###########################

username: andyjames
email: ajsly87@gmail.com
password: SlyF0x@87

###########################
Virtual Environment
###########################

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\nerdEnv\Scripts\activate
deactivate
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Default
