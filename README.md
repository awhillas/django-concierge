# django-concierge

django-concierge is a Django app to gather web analytics data from users
and provide an admin interface to view the data.

Detailed documentation is in the "docs" directory.

## Quick start

1. Add "concierge" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "django_concierge",
    ]

2. Include the concierge URLconf in your project urls.py like this::

    path("concierge/", include("django_concierge.urls")),

3. Add the following in you base HTML template(s) which will include the JavaScript
    needed to gather the analytics data:

    {% include "concierge/concierge_js_header.html" %}

4. Run `python manage.py migrate` to create the models.

5. Start the development server and visit the admin to view the analytics dashboard.

6. You will need to add a JavaScript snippet to your base template(s) which will gather
    the analytics data and send it to the server via AJaX.

## TODOs

- [ ] Admin dashboard
- [ ] Lookup location of IP address
- [ ] Cookies for tracking sessions
- [ ] Deermine bounce rate