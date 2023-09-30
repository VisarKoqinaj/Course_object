from flask import Flask

app=Flask("my app", )


@app.route("/home")
def hello():
    return "Hello World"

#run
if __name__ == "__main__":
    app.run(debug=True)



