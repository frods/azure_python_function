import os
import json

import response

get_arg_prefix = "REQ_QUERY_"
get_args = {}

for var in os.environ:
    if var.startswith(get_arg_prefix):
        get_args[var[len(get_arg_prefix):].lower()] = os.environ[var]

print "Get Args", get_args

output = open(os.environ['res'], 'w')
output.write(json.dumps(response.makeResponse(get_args)))
