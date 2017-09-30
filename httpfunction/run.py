import os
import json

get_args = None

for var in os.environ:
    if var.startswith("REQ_QUERY_"):
        get_args = os.environ[var]

print "Get Args", get_args


returnData = {
    #HTTP Status Code:
    "status": 200,
    
    #Response Body:
    "body": "<h1>Azure Works :)</h1>",
    
    # Send any number of HTTP headers
    "headers": {
        "Content-Type": "text/html",
        "X-Awesome-Header": "YesItIs"
    }
}

output = open(os.environ['res'], 'w')
output.write(json.dumps(returnData))