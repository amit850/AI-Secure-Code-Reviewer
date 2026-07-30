from flask import redirect, request

url = request.args.get("next")

return redirect(url)