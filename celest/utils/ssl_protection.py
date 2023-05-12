import http.client
import ssl

class SSL_Protection:
    
    def make_request(self, method, host, port, path, data=None, headers=None):
        context = ssl.create_default_context()
        conn = http.client.HTTPSConnection(host=host, port=port, context=context)
        headers = headers or {}
        headers.update({'Content-type': 'application/json'})
        conn.request(method=method, url=path, body=data or '', headers=headers)
        response = conn.getresponse()
        return response.read()

    
    def test(self, host):
        context = ssl.create_default_context()
        conn = http.client.HTTPSConnection(host=host, context=context)
        conn.request(method='GET', url='/')
        response = conn.getresponse()
        return response.status