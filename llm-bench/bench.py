import os, json, time, datetime, urllib.request
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TASK = "一句话摘要：vci-vinf 08-30 值守发现注册表404，根因=迁移码不随，根修=改指公面正本。"
def call(url, key, model):
    t0 = time.time()
    try:
        body = json.dumps({"model": model, "messages": [{"role": "user", "content": TASK}], "max_tokens": 120}).encode()
        req = urllib.request.Request(url, data=body, headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            j = json.loads(r.read())
        return {"ok": True, "sec": round(time.time()-t0, 1), "out_head": j["choices"][0]["message"]["content"][:80]}
    except Exception as e:
        return {"ok": False, "sec": round(time.time()-t0, 1), "err": type(e).__name__ + ":" + str(e)[:60]}
res = {"ts": now, "round": "R3-armB", "task": "duty-summary", "rows": []}
if os.environ.get("DS"):
    res["rows"].append({"provider": "deepseek", "model": "deepseek-chat", **call("https://api.deepseek.com/v1/chat/completions", os.environ["DS"], "deepseek-chat")})
if os.environ.get("KM"):
    res["rows"].append({"provider": "kimi", "model": "moonshot-v1-8k", **call("https://api.moonshot.cn/v1/chat/completions", os.environ["KM"], "moonshot-v1-8k")})
res["rows"].append({"provider": "longcat", "ok": None, "note": "endpoint未定(候root)——honest pending，key已置"})
os.makedirs("llm-bench", exist_ok=True)
fn = "llm-bench/r3-%s.json" % now.replace(":", "").replace("-", "")
json.dump(res, open(fn, "w"), ensure_ascii=False, indent=1)
json.dump({"ts": now, "status": "ran", "file": fn}, open("llm-bench/status.json", "w"), ensure_ascii=False)
print(json.dumps(res, ensure_ascii=False)[:400])
