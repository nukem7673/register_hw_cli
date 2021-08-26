import requests
import argparse

# Create parser
parser = argparse.ArgumentParser(description="Registers a new *ion* with local Earthscape servers. The default registration api endpoint is on stage servers, but this can be changed by setting the flag '-production' to true")

parser.add_argument('--code', metavar='code', type=str, help='The code given on Earthscape for registration.')
parser.add_argument('--serial', metavar='serial', type=str, help='The name of the device (listed on Earthscape)')
parser.add_argument('--production', metavar='production', type=str, nargs='?', default='True', help='If set to "true", the hardware will attempt to register to a production server site.')
parser.add_argument('--custom_url', metavar='custom_url', type=str, default="", help='Allows the user to set the url for the registration manually.')

args = parser.parse_args()

print(vars(args))
url = "http://stage.earthscape.com/api/v1/hardware/ars" if args.production == 'False' else "http://www.earthscape.com/api/v1/hardware/ars"

if args.custom_url is not "":
    url = args.custom_url

PARAMS = {
    "code": args.code,
    "serial": args.serial
}

r = requests.post(url, json=PARAMS) # Use "json"  . . .  NOT "data"
print(r)
print(r.json())

