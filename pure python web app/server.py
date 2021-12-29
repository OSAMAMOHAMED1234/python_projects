def render_template(template_name='index.html', context={}):
  html_str = ''
  with open(template_name, 'r') as f:
    html_str = f.read()
    html_str = html_str.format(**context)
  return html_str

def home(environ):
  return render_template(template_name='index.html', context={'msg': 'Hello OSAMA'})

def contact_us(environ):
  return render_template(template_name='index.html', context={'msg': 'Contact Us'})

def app(environ, start_response):
  # for k,v in environ.items():
  #   print(k, v)
  # print('REMOTE_HOST : ', environ.get('REMOTE_HOST'))
  # print('SERVER_PORT : ', environ.get('SERVER_PORT'))
  # print('REQUEST_METHOD : ', environ.get('REQUEST_METHOD'))
  # print('QUERY_STRING : ', environ.get('QUERY_STRING'))
  path = environ.get('PATH_INFO')
  print('path', path)
  if path.endswith('/'):
    path = path[:-1]
  if path == '':
    data = home(environ)
  elif path == '/contact':
    data = contact_us(environ)
  else:
    data = render_template(template_name='404.html', context={'msg': '404 Page not found.', 'path': path})
  data = data.encode('utf-8')
  start_response(
    f'200 OK', [
      ('Content-Type', 'text/html'),
      ('Content-Length', str(len(data)))
    ]
  )
  return iter([data])

# hupper -m waitress --host=127.0.0.1 --port=8080 server:app