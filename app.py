#!/usr/bin/env python
from flask import Flask
import unittest

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Tarun"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()
