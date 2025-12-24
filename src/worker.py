"""
Cloudflare Worker entry point for OpenMedCalc API
This module adapts the FastAPI application to run on Cloudflare Workers
"""

from js import Response
import sys
import os

# Add parent directory to path to import main app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

async def on_fetch(request):
    """
    Cloudflare Workers entry point for handling requests

    This function receives requests from Cloudflare Workers and passes them
    to the FastAPI application using the ASGI interface.
    """
    import asgi

    return await asgi.fetch(app, request)
