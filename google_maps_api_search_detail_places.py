import requests
from urllib.parse import urlencode, urlparse, parse_qsl

api_key = ''
data_type = 'json'
endpoint = f'https://maps.googleapis.com/maps/api/geocode/{data_type}'
params = {
  'key': api_key,
  'address': '1600 Amphitheatre Parkway, Mountain View, CA',
}
url_params = urlencode(params)
url = f'{endpoint}?{url_params}'

def extract_lat_lng(address_or_postalcode, data_type='json'):
  endpoint = f'https://maps.googleapis.com/maps/api/geocode/{data_type}'
  params = {'address': address_or_postalcode, 'key': api_key}
  url_params = urlencode(params)
  url = f'{endpoint}?{url_params}'
  r = requests.get(url)
  if r.status_code not in range(200, 299): 
    return {}
  latlng = {}
  try:
    latlng = r.json()['results'][0]['geometry']['location']
  except:
    pass
  return latlng.get('lat'), latlng.get('lng')
extract_lat_lng('1600 Amphitheatre Parkway, Mountain View, CA')

to_parse = 'https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway%2C+Mountain+View%2C+CA&key=AIzaSyD8PCLxbKHRBrJWg6JYp-YXYz0ph4LKiQw'
parsed_url = urlparse(to_parse)
query_string = parsed_url.query
query_tuple = parse_qsl(query_string)
query_dict = dict(query_tuple)
endpoint = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"

# places api
lat, lng = 37.42230960000001, -122.0846244
base_endpoint_places = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/{data_type}'
params = {
  'key': api_key,
  'input': 'Mexican food',
  'inputtype': 'textquery',
  'fields': 'place_id,formatted_address,name,geometry,permanently_closed'
}
locationbias = f'point:{lat},{lng}'
use_circular = True
if use_circular:
  radius = 5000
  locationbias = f'circle:{radius}@{lat},{lng}'
params['locationbias'] = locationbias
params_encoded = urlencode(params)
places_endpoint = f'{base_endpoint_places}?{params_encoded}'
r = requests.get(places_endpoint)
r.json()

places_endpoint_2 = f'https://maps.googleapis.com/maps/api/place/nearbysearch/{data_type}'
params_2 = {
  'key': api_key,
  'location': f'{lat},{lng}',
  'radius': 1500,
  'keyword': 'Mexican food'
}
params_2_encoded = urlencode(params_2)
places_url = f'{places_endpoint_2}?{params_2_encoded}'
r2 = requests.get(places_url)
r2.json()

# place detail
place_id = 'ChIJlXOKcDC3j4ARzal-5j-p-FY'
detail_base_endpoint = f'https://maps.googleapis.com/maps/api/place/details/{data_type}'
detail_params = {
  'key': api_key,
  'place_id': f'{place_id}',
  'fields' : 'name,rating,formatted_phone_number,formatted_address',
}
detail_params_encoded = urlencode(detail_params)
detail_url = f'{detail_base_endpoint}?{detail_params_encoded}'
r = requests.get(detail_url)
r.json()



import requests
from urllib.parse import urlencode, urlparse, parse_qsl
GOOGLE_API_KEY = ''

class GoogleMapsClient(object):
  lat = None
  lng = None
  data_type = 'json'
  location_query = None
  api_key = None
    
  def __init__(self, api_key=None, address_or_postal_code=None, *args, **kwargs):
    super().__init__(*args, **kwargs)
    if api_key == None:
      raise Exception('API key is required')
    self.api_key = api_key
    self.location_query = address_or_postal_code
    if self.location_query != None:
      self.extract_lat_lng()
  
  def extract_lat_lng(self, location=None):
    loc_query = self.location_query
    if location != None:
      loc_query = location
    endpoint = f'https://maps.googleapis.com/maps/api/geocode/{self.data_type}'
    params = {'address': loc_query, 'key': self.api_key}
    url_params = urlencode(params)
    url = f'{endpoint}?{url_params}'
    r = requests.get(url)
    if r.status_code not in range(200, 299): 
      return {}
    latlng = {}
    try:
      latlng = r.json()['results'][0]['geometry']['location']
    except:
      pass
    lat,lng = latlng.get('lat'), latlng.get('lng')
    self.lat = lat
    self.lng = lng
    return lat, lng
  
  def search(self, keyword='Mexican food', radius=5000, location=None):
    lat, lng = self.lat, self.lng
    if location != None:
      lat, lng = self.extract_lat_lng(location=location)
    endpoint = f'https://maps.googleapis.com/maps/api/place/nearbysearch/{self.data_type}'
    params = {
      'key': self.api_key,
      'location': f'{lat},{lng}',
      'radius': radius,
      'keyword': keyword
    }
    params_encoded = urlencode(params)
    places_url = f'{endpoint}?{params_encoded}'
    r = requests.get(places_url)
    if r.status_code not in range(200, 299):
      return {}
    return r.json()
    
  def detail(self, place_id='ChIJlXOKcDC3j4ARzal-5j-p-FY', fields=['name', 'rating', 'formatted_phone_number', 'formatted_address']):
    detail_base_endpoint = f'https://maps.googleapis.com/maps/api/place/details/{self.data_type}'
    detail_params = {
      'place_id': f'{place_id}',
      'fields' : ','.join(fields),
      'key': self.api_key
    }
    detail_params_encoded = urlencode(detail_params)
    detail_url = f"{detail_base_endpoint}?{detail_params_encoded}"
    r = requests.get(detail_url)
    if r.status_code not in range(200, 299):
      return {}
    return r.json()
client = GoogleMapsClient(api_key=GOOGLE_API_KEY, address_or_postal_code='92660')
print(client.lat, client.lng)
client.search('Tacos', radius=5000)
client.detail(place_id='ChIJRfptTwEg3YARACDUpVSiRso')