
# import logging
# import pprint
import http.client

# _logger = logging.getLogger(__name__)
def checkout(encencryptedText, url, access_code, env):
    # _logger.info("checkout encencryptedText:\n%s", pprint.pformat(encencryptedText))
    # _logger.info("checkout url:\n%s", pprint.pformat(url))
    # _logger.info("checkout access_code:\n%s", pprint.pformat(access_code))
    # _logger.info("checkout env:\n%s", pprint.pformat(env))
    if env == 'production':
        conn = http.client.HTTPSConnection(url.replace("https://", "").replace("http://", ""))
    else:
        conn = http.client.HTTPConnection(url.replace("https://", "").replace("http://", ""))
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--" % encencryptedText
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'accesscode': "%s" % access_code,
    }
    # conn.request("POST", "/api/checkout", payload, headers)
    conn.request("POST", "/checkout", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")
