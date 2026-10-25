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

- A Mac with the app installed in /Applications from the Mac App Store. Without it, the plugin stops with a message saying so.
- bibliome: Bibliome open while you use it. Its connector runs on the Python that comes with macOS, which needs Apple's command line tools once (`xcode-select --install`).

## Without the plugin

Each app also gives you its connector setup to paste into Claude Desktop, Claude Code or another MCP client.
