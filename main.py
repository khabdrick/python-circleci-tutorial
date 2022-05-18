from flask import Flask

app = Flask(__name__) #create an instance of the Flask class you just imported

@app.route('/')
def main():
    # display a string in the home page
    return "Welcome to my Flask App"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)