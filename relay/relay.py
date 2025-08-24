from fastapi import FastAPI, Request
import httpx, os

app = FastAPI()
SNOW_INSTANCE = os.getenv("SNOW_INSTANCE")   # e.g. devXXXXX.service-now.com
SNOW_USER = os.getenv("SNOW_USER")
SNOW_PASS = os.getenv("SNOW_PASS")

@app.post("/alert")
async def alert(req: Request):
    payload = await req.json()
    for alert in payload.get("alerts", []):
        short = alert["annotations"].get("summary", "Prometheus Alert")
        desc = alert["annotations"].get("description", "")
        await create_incident(short, desc)
    return {"status": "ok"}

async def create_incident(short, desc):
    url = f"https://{SNOW_INSTANCE}/api/now/table/incident"
    data = {"short_description": short, "description": desc, "urgency": "2", "impact": "2"}
    async with httpx.AsyncClient(auth=(SNOW_USER, SNOW_PASS)) as c:
        await c.post(url, json=data)
