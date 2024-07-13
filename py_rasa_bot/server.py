from sanic import Sanic
from sanic.response import json
from rasa_sdk.executor import CollectingDispatcher, ActionExecutor
from rasa_sdk.interfaces import Tracker

app = Sanic("server")
action_executor = ActionExecutor()

@app.route("/webhook", methods=["POST"])
async def webhook(request):
    action_call = request.json
    tracker = Tracker.from_dict(action_call.get("tracker"))
    domain = action_call.get("domain")
    response = await action_executor.run(
        action_call=action_call,
        tracker=tracker,
        domain=domain,
    )
    return json(response)

@app.route("/favicon.ico", methods=["GET"])
async def favicon(request):
    return json({"status": "not found"}, status=404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
