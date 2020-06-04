from sanic import Sanic
from sanic.response import json

app = Sanic("hello_example")

@app.route("/")
async def test(request):
  return json({"hello": "world", "version": 2})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)