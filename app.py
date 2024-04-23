from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<H1>Cookie test page</H1><p>Use /set-cookie to set persistent test_cookie.</p><p>Use /read-cookie to read test_cookie value.</p><p>Use /delete-cookie to delete test_cookie.</p>')
    return response


@app.route('/read-cookie')
def read_cookie():
    #Read cookie
    read_cookie = request.cookies.get('test_cookie')
    returned_string = '<p>The test_cookie value is: {}</p>'.format(read_cookie)
    
    response = make_response(returned_string)

    return response


@app.route('/set-cookie')
def set_cookie():
    #Set cookie
    returned_string = '<p>Test_cookie successfully set.</p>'
    
    response = make_response(returned_string)
    response.set_cookie('test_cookie', 'Cookie is present', max_age=30*24*60*60, httponly=True)

    return response


@app.route('/delete-cookie')
def delete_cookie():
    #Delete cookie
    returned_string = '<p>Test_cookie successfully deleted.</p>'
    
    response = make_response(returned_string)
    response.set_cookie('test_cookie', '' , max_age=0)

    return response