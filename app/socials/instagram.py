import subprocess

def getInstagram(search_param):
  location = search_param

  # Create subprocess to login then search for locations
  p = subprocess.Popen(["instagram-scraper", "-u", "exesiospb", "-p", "ExesiosPB1", "--search-location", location], stdout=subprocess.PIPE)
  output, err = p.communicate()

  if output != "":
    # Bytes => Strings, then split by spaces
    output = output.decode()
    output = output.split("\n")
    # Currently looks like location-id: 34324, title: Stoke-On-Trent, ...
    # So format
    current = output[0]
    output = current.split(", ")
    # We take location-id: .... then get the actual id
    locationId = output[0].split(": ")[1]

    # Now we want to scrape all the images from this location id
    p = subprocess.Popen(["instagram-scraper", "-u", "exesiospb", "-p", "ExesiosPB1", "--location", locationId, "--media_metadata"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    
    if output != "":
      json = {error: '', done: 'true'}
      return json
    else:
      json = {error: err, done: 'false'}
      return json      
  
  else:
    json = {error: err, done: 'false'}
    return json