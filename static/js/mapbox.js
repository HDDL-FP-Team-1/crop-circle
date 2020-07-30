
 document.addEventListener("submit", function (event) {
   console.log('test')
       event.preventDefault();
         let street = document.querySelector("#id_street_address").value;
         let street2 = document.querySelector("#id_street_address_line_2").value;
         let city = document.querySelector("#id_city").value;
         let state = document.querySelector("#id_state").value;
         let zip = document.querySelector("#id_zip_code").value;
         let address = (`${street} ${street2} ${city} ${state} ${zip}`);
         let mappy = address.trim().replace(/\s/g, '%20')
         let splitMappy = mappy.split('.').join('')
         var ACCESS_TOKEN = 'pk.eyJ1IjoiaGRkbCIsImEiOiJja2NtMGY1ZDgwcTZ5MnN0OGY3ajJjbW4yIn0.qHA8T449zRKiEj4SS9jnuQ';
        
        forwardGeocoding(splitMappy, ACCESS_TOKEN) 
         
 
     });
     
 
 function forwardGeocoding(splitAddress, ACCESS_TOKEN) {
  
   base_url = new URL("https://api.mapbox.com/geocoding/v5/mapbox.places/" + splitAddress + '.json'),
   params = {access_token:ACCESS_TOKEN, limit:1, country:'US'}
   Object.keys(params).forEach(key => base_url.searchParams.append(key, params[key]))
   fetch(base_url)
     .then(response => response.json())
     
     .then(data => getLatLong(data))
     
     ;
 } 
 
 function getLatLong (data) {
   var longitude = data.features[0].center[0];
   document.querySelector('#id_longitude').value=longitude 
   let longVar = document.querySelector('#id_longitude').value
   console.log(longVar)
   var latitude = data.features[0].center[1];
   console.log(latitude)
   document.querySelector('#id_latitude').value=latitude;
   document.getElementById("farmAdd").submit()
 }
 
 function postData (data) {
   fetch('')
 }
