"""
Cloudflare Worker entry point for OpenMedCalc API
This module adapts the FastAPI application to run on Cloudflare Workers
"""

from workers import WorkerEntrypoint


class Default(WorkerEntrypoint):
    async def on_fetch(self, request):
        # Lazy import to avoid startup cost
        from main import app
        import asgi

        return await asgi.fetch(app, request.js_object, self.env)
