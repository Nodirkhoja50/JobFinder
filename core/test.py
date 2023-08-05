'''from geopy.geocoders import GoogleV3

geoLoc = GoogleV3(api_key="GetLoc")

localname= geoLoc.reverse("41.400219,","70.060115")
print(localname.address)'''


'''from geopy.geocoders import GoogleV3
geolocator = GoogleV3()
location = geolocator.reverse("52.509669, 13.376294")
print(location.address)'''


from geopy.geocoders import Nominatim





# Latitude & Longitude input
coordinates = "66.011062,39.040001"








def check_current_location(coordinates):
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.reverse(coordinates)

    address = location.raw['address']
    print('hello')
    # Traverse the data
    city = address.get('city')
    county = address.get("county",'')
    state = address.get('state', '')
    country = address.get('country', '')
    return city,county

#print(check_current_location(coordinates)[0])
j,k = check_current_location(coordinates)
print(j)
print(k)