'''

https://www.pixelite.co.nz/article/validate-and-clean-user-submitted-address-data-pygeocoder/

Create new API Key
https://developers.google.com/maps/documentation/geocoding/get-api-key

Enable the API for GeoCoding
https://console.cloud.google.com/project/_/billing/enable


'''

from pygeocoder import Geocoder

gcoder = Geocoder("AIzaSyDpphQYnr1XxmPhsvGYh3AdPAy3EgE0sd4")

print(gcoder)
addr = gcoder.geocode("1 Rugby Street, Newtown, Wellington 6021, New Zealand")
# print(addr.values())

