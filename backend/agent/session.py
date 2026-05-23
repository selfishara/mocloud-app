from fastapi import WebSocket
from .claude_client import stream_response


class AgentSession:
    def __init__(self, session_id: str, websocket: WebSocket):
        self.session_id = session_id
        self.websocket = websocket
        self.history: list[dict] = []

    async def handle_message(self, data: dict):
        user_message = data.get("content", "")
        self.history.append({"role": "user", "content": user_message})

        async for event in stream_response(self.history):
            await self.websocket.send_json(event)

        self.history.append({"role": "assistant", "content": "[streamed]"})
