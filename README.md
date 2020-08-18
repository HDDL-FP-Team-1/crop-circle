# Crop Circle

We are an app that will allow local consumers to locate fresh local produce from local framers.

## Credit

Crop Circle was built using:

[MapBox](https://www.mapbox.com/) for displaying location information.

[MapBox.Places API](https://docs.mapbox.com/api/search/#mapboxplaces) for forward geolocating street addresses into latitude and longitude.

[django-registration-redux](https://django-registration-redux.readthedocs.io/en/latest/) for allowing a customizable registration process to allow a new farmer to to get a web page set up in minutes.  This will also allow in future models to extend the registration process for additional types of user.  

[star-rating](https://django-star-ratings.readthedocs.io/en/latest/?badge=latest/) to create a star rating system that allows consumers to rate farms they have visited.

[AWS Webservice](https://docs.aws.amazon.com/s3/index.html)

[PostgreSQL](https://www.postgresql.org) for database structure.

[Heroku](https://www.heroku.com) for web hosting the Crop Circle live site.

## ToDos

Incorporating additional users into the app, allowing consumers to: 
    - Be able to register accounts 
    - Interaction with farm web pages
        - Rating farms
        - Favoriting farms
        - Sharing pictures of produce or farm
    - Social Aspects
        - Sharing pictures
        - List of favorited farms