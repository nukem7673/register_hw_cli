import requests
import argparse

# Create parser
parser = argparse.ArgumentParser(description="Registers a new *ion* with Earthscape servers. The default registration api endpoint is on stage servers, but this can be changed by setting the flag '-production' to true")

parser.add_argument('Code', metavar='code', type=str, help='The code given on Earthscape for registration.')
parser.add_argument('Serial', metavar='serial', type=str, help='The name of the device (listed on Earthscape)')
parser.add_argument('Production', metavar='production', type=str, nargs='?', default='True', help='If set to "true", the hardware will attempt to register to a production server site.')

args = parser.parse_args()

print(vars(args))
url = "http://stage.earthscape.com/api/v1/hardware/ars" if args.Production == 'False' else "http://www.earthscape.com/api/v1/hardware/ars"

PARAMS = {
    "code": args.Code,
    "serial": args.Serial
}

r = requests.post(url, json=PARAMS) # Use "json"  . . .  NOT "data"
print(r.json())

