#!/usr/bin/python3
"""Start Bibliome's connector for Claude.

Runs mcp_server.py, the script that ships inside Bibliome.app, with the two
locations it needs: Bibliome's library folder and the socket the running app
listens on. Both are inside Bibliome's own sandbox container in the user's home
folder, which is found here so the plugin config can name every path literally.
"""
import os
import sys
from pathlib import Path

PYTHON = "/usr/bin/python3"
SERVER = "/Applications/Bibliome.app/Contents/Resources/pdf_organizer/mcp_server.py"
APP_STORE = "https://apps.apple.com/us/app/bibliome-library/id6786826590"

if not os.path.isfile(SERVER):
    sys.stderr.write(f"Bibliome is not installed in /Applications. It is on the Mac App Store: {APP_STORE}\n")
    sys.exit(1)

container = Path.home() / "Library" / "Containers" / "com.langberg.mypdflibrarian" / "Data"
env = dict(os.environ)
env["PDF_DATA_DIR"] = str(container / "Library" / "Application Support" / "PDFOrganizer")
env["BIBLIOME_MCP_SOCKET"] = str(container / "bibliome-mcp.sock")
os.execve(PYTHON, [PYTHON, SERVER], env)
