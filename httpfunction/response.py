def makeResponse(get_args):
    return {
        #HTTP Status Code:
        "status": 200,
        
        #Response Body:
        "body": "<h1>Azure Works :) {}</h1>".format(get_args.get("name", "")),
        
        # Send any number of HTTP headers
        "headers": {
            "Content-Type": "text/html",
            "X-Awesome-Header": "YesItIs"
        }
    }
