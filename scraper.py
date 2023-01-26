# Importing libraries
import time
import hashlib
from urllib.request import urlopen, Request
 
# setting the URL you want to monitor
url = Request('https://portal.permit.pcta.org/availability/mexican-border.php',
              headers={'User-Agent': 'Mozilla/5.0'})

# to perform a GET request and load the
# content of the website and store it in a var

def getData():
    response = urlopen(url).read()
    resp = str(response)
    resp = resp.split("data = {\"limit\":35,\"calendar\":")
    resp = resp[0].split(";var canadaStart = false")

    return bytes(resp[0], 'utf-8')

# to create the initial hash
currentHash = hashlib.sha224(getData()).hexdigest()
print("running")
time.sleep(10)
while True:
    try:
        # create a hash
        currentHash = hashlib.sha224(getData()).hexdigest()
         
        # wait for 30 seconds
        time.sleep(30)
         
        # create a new hash
        newHash = hashlib.sha224(getData()).hexdigest()
 
        # check if new hash is same as the previous hash
        if newHash == currentHash:
            continue
 
        # if something changed in the hashes
        else:
            # notify
            print("something changed")

            # create a hash
            currentHash = hashlib.sha224(getData()).hexdigest()
 
            # wait for 30 seconds
            time.sleep(30)
            continue
             
    # To handle exceptions
    except Exception as e:
        print("error")