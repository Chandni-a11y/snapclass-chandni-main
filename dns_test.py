import httpx

try:
    r = httpx.get("https://uefuxjfwhflyitgqkprm.supabase.co")
    print("Status:", r.status_code)
except Exception as e:
    print("Error:", e)
