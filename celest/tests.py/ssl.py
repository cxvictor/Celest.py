from celest.utils.ssl_protection import SSL_Protection

ssl_prot = SSL_Protection()
host = 'www.google.com'
response = ssl_prot.make_request('GET', host=host, port=443, path='/')
print(response)