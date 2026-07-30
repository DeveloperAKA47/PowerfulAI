from openai import OpenAI
from pathlib import Path
import uvicorn
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi.staticfiles import StaticFiles

baseDir = Path(__file__).resolve().parent
STATIC_DIR = baseDir / "static"
load_dotenv()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", include_in_schema=False)
def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/chat")
def chat(quesetion: str):
    api_key = os.getenv("ALIYUN_KEY")
    base_url = os.getenv("ALIYUN_BASE_URL")

    if not api_key or not base_url:
        raise HTTPException(
            status_code=500,
            detail=" ALIYUN_KEY 和 ALIYUN_BASE_URL wrong",
        )

    try:
        aliyun_client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            timeout=60.0,
        )

        ali_res = aliyun_client.chat.completions.create(
            model="qwen3.7-plus",
            messages=[
                {
                    "role": "user",
                    "content": (
                        "你是智能导购，请根据用户需求推荐合适的产品，"
                        f"\n\n用户问题：{quesetion}"
                    ),
                }
            ],
            stream=False,
        )

        message = ali_res.choices[0].message.content

        return {"message": message or "AI 没有返回有效内容"}

    except Exception as e:
        print("aliyun_client error:", e)
        raise HTTPException(
            status_code=500,
            detail="调用 AI 服务失败",
        )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
