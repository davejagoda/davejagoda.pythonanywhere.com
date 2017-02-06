#!/usr/bin/env python3

PAGE = """
<html>
  <head>
    <title>dj</title>
  </head>
  <body>
    <h1>dj</h1>
    <p>
      path:{}
    </p>
  </body>
</html>
"""

def application(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    status = '200 OK'
    content = PAGE.format(path)
    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    yield content.encode('utf8')

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()
