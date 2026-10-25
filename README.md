# psychosonic plugins

Claude plugins for three Mac apps. Each one connects Claude to an app on your Mac. The apps reach no network for this; what a tool returns goes to the Claude conversation that asked for it.

| Plugin | App | What Claude can do |
| --- | --- | --- |
| notesmith | [Notesmith](https://apps.apple.com/us/app/notesmith/id6802464646) | Search and read your notes. |
| bibliome | [Bibliome](https://apps.apple.com/us/app/bibliome-library/id6786826590) | Search your PDF library, answer from it and check claims against it, with links to the page. |
| agentscribe | [AgentScribe](https://apps.apple.com/us/app/agentscribe/id6813940342) | Keep a memory on your Mac that you can review. |

## Install in Claude Code

```text
/plugin marketplace add negativetime/psychosonic-plugins
/plugin install notesmith@psychosonic
/plugin install bibliome@psychosonic
/plugin install agentscribe@psychosonic
```

Install only the ones for apps you have.

## What each plugin needs

- A Mac with the app installed in /Applications from the Mac App Store. Without it, the plugin can't connect.
- bibliome: Bibliome open while you use it. Its connector runs on the Python that comes with macOS, which needs Apple's command line tools once (`xcode-select --install`).

These run in Claude Code and Cowork on your Mac. They don't run on claude.ai in a browser.

## What each plugin runs

Each plugin starts a program that ships inside its app. Nothing is downloaded and nothing runs from this repository.

### notesmith

Runs `/Applications/Notesmith.app/Contents/Helpers/agent-notes`, the connector inside Notesmith. It is the same program Notesmith's own connector setup gives to Claude.

It is sandboxed and has no network entitlement; its only other entitlement is an app group shared with Notesmith. It searches and reads your notes and returns the text to Claude. It cannot change your notes. If you turn on the Agent Inbox in Notesmith, Claude can also keep notes of its own there, apart from yours. If Bibliome is installed too, it can search your Bibliome library through the same app group.

To try it: install Notesmith, write a note or two, then ask Claude to search them.

### bibliome

Runs `/usr/bin/python3` with `mcp_server.py`, a script that ships inside Bibliome. It is the same script Bibliome's Settings > MCP gives to Claude. Two environment values point it at Bibliome's library folder and local socket, both inside Bibliome's own container.

It makes no network connections; its only socket is the local one to the running Bibliome app, which it asks for results. It opens the app's catalog read only and changes nothing in the library. Bibliome must be open, and `/usr/bin/python3` needs Apple's command line tools.

To try it: install Bibliome, add a few PDFs, leave it open, then ask Claude to search them.

### agentscribe

Runs `/Applications/AgentScribe.app/Contents/Helpers/agent-notes --agent claude`, the connector inside AgentScribe. It is the same program AgentScribe's own connect sheet gives to Claude. `--agent claude` only labels which app saved a memory.

It is sandboxed and has no network entitlement; its only other entitlement is an app group shared with AgentScribe. It stores and searches the memories Claude saves, on your Mac, and you review them in the app.

To try it: install AgentScribe, ask Claude to remember something, then open the app.

## Without the plugin

Each app also gives you its connector setup to paste into Claude Desktop, Claude Code or another MCP client.
