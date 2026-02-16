import json
import requests

API_URL = "http://127.0.0.1:8000"

with open("eval/eval_data.json") as f:
    data = json.load(f)

for item in data:
    response = requests.post(
        f"{API_URL}/rank",
        json={"job_description": item["job_description"]}
    )

    ranking = response.json()["ranking"]
    print("Expected Top Resume:", item["expected_top_resume"])
    print("Actual Top Resume:", ranking[0]["resume"])
