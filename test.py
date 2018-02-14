from bottle import route, run, template

@route('/test')
def index():
    print("Test running...")
    return "This string was returned..."

@route('/java', method='POST')
def doLogin():
    print("POST request from Java...")
    return "Response to POST request from Bottle..."

@route('/java', method='GET')
def doLogin():
    print("GET request from Java...")
    return "Response from Bottle..."


run(host='localhost', port=8081)
