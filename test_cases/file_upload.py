from flask import request

file = request.files["file"]

file.save(file.filename)