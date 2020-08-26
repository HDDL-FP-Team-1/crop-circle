# Crop Circle

We are an app that will allow local consumers to locate fresh local produce from their local farmers. It gives the ability for farmers to advertise their current merchandise as well as multiple locations that they are using to distribute from.  The goal of Crop Circle is to allow local farmers to reach the consumer market without spending too much time at a computer.

## User Experience
- Farmer: 

- Consumer:

## Credit

Crop Circle was built using:

[Materialize](https://materializecss.com/) for UI/UX. Created and designed by Google, Material Design is a design language that combines the classic principles of successful design along with innovation and technology.

[MapBox](https://www.mapbox.com/) an open source mapping platform we integrated for users to search and display location information.

[MapBox.Places API](https://docs.mapbox.com/api/search/#mapboxplaces) for forward geocoding street addresses into latitude and longitude by making a request to Mapbox's api when our forms are submitted.  

[django-registration-redux](https://django-registration-redux.readthedocs.io/en/latest/) for allowing a customizable registration process to allow a new farmer to get a web page set up in minutes.  This will also allow in future models to extend the registration process for additional types of user.  

[star-rating](https://django-star-ratings.readthedocs.io/en/latest/?badge=latest/) to create a star rating system that allows consumers to rate farms they have visited.

[AWS Webservice](https://docs.aws.amazon.com/s3/index.html)

[PostgreSQL](https://www.postgresql.org) for database structure.

[Heroku](https://www.heroku.com) for web hosting the Crop Circle live site.

## ToDos

### Incorporating additional users into the app, allowing consumers to: 
..- Register accounts 
...* Interact with farm web pages including,
...* Rating farms
...* Favoriting farms
...* Sharing pictures of produce or farm
..- Social Aspects
...* Sharing pictures
...* List of favorited farms

## Demo

![Crop Circle Demo]()

## License

[HDDL]()