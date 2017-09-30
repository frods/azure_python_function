import os
import json

get_arg_prefix = "REQ_QUERY_"
get_args = {}

for var in os.environ:
    if var.startswith(get_arg_prefix):
        get_args[var[len(get_arg_prefix):].lower()] = os.environ[var]

print "Get Args", get_args


returnData = {
    #HTTP Status Code:
    "status": 200,
    
    #Response Body:
    "body": "<h1>Azure Works :) {}</h1>".format(get_args.get("name", ""),
    
    # Send any number of HTTP headers
    "headers": {
        "Content-Type": "text/html",
        "X-Awesome-Header": "YesItIs"
    }
}

output = open(os.environ['res'], 'w')
output.write(json.dumps(returnData))