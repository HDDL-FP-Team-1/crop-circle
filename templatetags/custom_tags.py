from django import template
register = template.Library()

from ..models import YourModel

@register.simple_tag
def any_function():
  	return YourModel.objects.count()

@register.inclusion_tag('path_to_your_html_file.html')
def any_function():
      variable = YourModel.objects.order_by('-publish')[:5]
      return {'variable': variable}

@register.assignment_tag
def any_function(count=5):
      return *some database query*

@register.mapbox
function buildLocationList(data) {
  data.features.forEach(function(store, i){
    # /**
    #  * Create a shortcut for `store.properties`,
    #  * which will be used several times below.
    # **/
    var prop = store.properties;

    # /* Add a new listing section to the sidebar. */
    var listings = document.getElementById('listings');
    var listing = listings.appendChild(document.createElement('div'));
    /* Assign a unique `id` to the listing. */
    listing.id = "listing-" + prop.id;
    /* Assign the `item` class to each listing for styling. */
    listing.className = 'item';

    /* Add the link to the individual listing created above. */
    var link = listing.appendChild(document.createElement('a'));
    link.href = '#';
    link.className = 'title';
    link.id = "link-" + prop.id;
    link.innerHTML = prop.address;

    /* Add details to the individual listing. */
    var details = listing.appendChild(document.createElement('div'));
    details.innerHTML = prop.city;
    if (prop.phone) {
      details.innerHTML += ' · ' + prop.phoneFormatted;
    }
  });
}