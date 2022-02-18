from main import app

def test_hello():
    response = app.test_client().get('/') # Creates a test client for this application.

    assert response.status_code == 200 # assert the stutus code of the page('/') is 200
    assert response.data == b'Welcome to my Flask App' # assert the return statement ton the page