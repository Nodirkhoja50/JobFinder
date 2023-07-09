'''from geopy.geocoders import GoogleV3

geoLoc = GoogleV3(api_key="GetLoc")

localname= geoLoc.reverse("41.400219,","70.060115")
print(localname.address)'''


'''from geopy.geocoders import GoogleV3
geolocator = GoogleV3()
location = geolocator.reverse("52.509669, 13.376294")
print(location.address)'''


from geopy.geocoders import Nominatim



# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

# Latitude & Longitude input
coordinates = "41.306211, 69.273168"


location = geolocator.reverse(coordinates)

address = location.raw['address']

# Traverse the data
city = address.get('city', '')
county = address.get("county",'')
state = address.get('state', '')
country = address.get('country', '')

