import os
from typing import AsyncGenerator
import anthropic
from dotenv import load_dotenv

load_dotenv()

_client = anthropic.AsyncAnthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))

SYSTEM_PROMPT = """You are MoCloud, a mobile AI agent. You help users automate tasks, write and execute code, and build workflows from their phone. Be concise and practical."""


async def stream_response(history: list[dict]) -> AsyncGenerator[dict, None]:
    async with _client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=history,
    ) as stream:
        async for text in stream.text_stream:
            yield {"type": "token", "text": text}
    yield {"type": "session_end"}
