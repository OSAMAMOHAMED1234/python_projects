from os_pack import web_app
from waitress import serve


if __name__ == '__main__':
  serve(
    web_app,
    host='127.0.0.1',
    port=5000,
    threads=2,
    # listen='127.0.0.1:5000',
  )