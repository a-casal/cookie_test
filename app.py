from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<H1>Cookie test page</H1><p>Use /set-cookie to set persistent hasPersistentLogin cookie.</p>'
                             '<p>Use /read-cookie to read hasPersistentLogin value.</p>'
                             '<p>Use /delete-cookie to delete hasPersistentLogin cookie.</p>')
    return response


@app.route('/read-cookie')
def read_cookie():
    #Read cookie
    read_cookie = request.cookies.get('hasPersistentLogin')
    returned_string = '<p>The hasPersistentLogin value is: {}</p>'.format(read_cookie)
    
    response = make_response(returned_string)

    return response


@app.route('/set-cookie')
def set_cookie():
    #Set cookie
    returned_string = '<p>hasPersistentLogin cookie successfully set.</p>'
    
    response = make_response(returned_string)
    response.set_cookie('hasPersistentLogin', '*', max_age=30*24*60*60, httponly=False, secure=True, domain='cookie-test-vegj.onrender.com')

    return response


@app.route('/delete-cookie')
def delete_cookie():
    #Delete cookie
    returned_string = '<p>hasPersistentLogin successfully deleted.</p>'
    
    response = make_response(returned_string)
    response.set_cookie('hasPersistentLogin', '' , max_age=0, httponly=False, secure=True, domain='cookie-test-vegj.onrender.com')

    return response