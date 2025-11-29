# Installing Matomo MCP Server on Windows

This guide will help you install the Matomo MCP Server on Windows 10 or Windows 11, even if you've never used Python before.

## Prerequisites

- Windows 10 or Windows 11
- Administrator access to your computer
- Internet connection

## Step 1: Install Python

Windows does not come with Python installed by default, so we need to install it first.

### Download Python

1. Open your web browser (Edge, Chrome, Firefox, etc.)
2. Go to: **https://www.python.org/downloads/**
3. You'll see a yellow button that says **"Download Python 3.x.x"** (the x's will be version numbers)
4. Click this button to download the installer
5. Wait for the download to complete (the file will be named something like `python-3.12.0-amd64.exe`)

### Install Python

1. **Find the downloaded file** (usually in your Downloads folder)
2. **Double-click** the installer to run it
3. **IMPORTANT**: On the first screen, you'll see two checkboxes at the bottom:
   - ✅ **CHECK the box** that says **"Add python.exe to PATH"**
   - This is crucial! If you forget this, Python won't work from the command line
4. Click **"Install Now"** (you may need to click "Yes" when Windows asks for permission)
5. Wait for the installation to complete (this takes 1-2 minutes)
6. When you see "Setup was successful", click **"Close"**

### Verify Python Installation

1. Press **Windows Key + R** on your keyboard
2. Type: `cmd` and press **Enter**
3. A black window (Command Prompt) will open
4. Type: `python --version` and press **Enter**
5. You should see something like: `Python 3.12.0`
6. If you see this, Python is installed correctly! ✅

**If you see an error** like "python is not recognized":
- You forgot to check "Add python.exe to PATH" during installation
- Uninstall Python (Windows Settings → Apps → Python → Uninstall)
- Reinstall and make sure to check the "Add python.exe to PATH" box

## Step 2: Install Matomo MCP Server

Now that Python is installed, we can install the Matomo MCP Server.

### Install the Package

1. **Open Command Prompt** (if you closed it):
   - Press **Windows Key + R**
   - Type: `cmd`
   - Press **Enter**

2. **Install matomo-mcp** by typing this command and pressing **Enter**:
   ```
   pip install --pre matomo-mcp
   ```

3. You'll see some text scrolling by as it downloads and installs. This is normal!

4. When it's done, you should see a message like:
   ```
   Successfully installed matomo-mcp-1.0.0a1 ...
   ```

5. **Verify the installation** by typing:
   ```
   python -m matomo_mcp --help
   ```

   If you see an error message about missing MATOMO_URL, that's actually good - it means the package is installed! ✅

## Step 3: Get Your Matomo API Token

You need an API token from your Matomo account to access your analytics data.

1. **Log into your Matomo account** in your web browser
2. Click your **username** in the top-right corner
3. Select **"Personal"** → **"Security"**
4. Scroll down to **"Auth tokens"**
5. Click **"Create new token"**
6. Give it a description like "Claude Desktop MCP"
7. Click **"Create new token"**
8. **Copy the token** - it will look like a long string of random letters and numbers
   - ⚠️ **Important**: Save this somewhere safe - you can only see it once!

## Step 4: Configure Claude Desktop

Now we need to tell Claude Desktop how to use the Matomo MCP Server.

### Find the Configuration File

1. Press **Windows Key + R**
2. Type: `%APPDATA%\Claude`
3. Press **Enter**
4. This opens the Claude configuration folder

### Create or Edit the Configuration File

1. Look for a file called `claude_desktop_config.json`
2. **If the file doesn't exist**:
   - Right-click in the empty space
   - Select **New** → **Text Document**
   - Name it: `claude_desktop_config.json`
   - Make sure to delete the `.txt` extension if Windows adds it
3. **Open the file** with Notepad (right-click → Open with → Notepad)

### Add the Matomo Configuration

1. **Copy this template** and paste it into the file:

```json
{
  "mcpServers": {
    "matomo": {
      "command": "python",
      "args": ["-m", "matomo_mcp"],
      "env": {
        "MATOMO_URL": "https://your-matomo-site.com",
        "MATOMO_TOKEN": "your_api_token_here"
      }
    }
  }
}
```

2. **Replace the placeholder values**:
   - Replace `https://your-matomo-site.com` with your actual Matomo URL
     - Example: `https://analytics.mycompany.com`
   - Replace `your_api_token_here` with the API token you copied in Step 3

3. **Save the file**:
   - Click **File** → **Save**
   - Close Notepad

### Example Configuration

Here's what a completed configuration looks like:

```json
{
  "mcpServers": {
    "matomo": {
      "command": "python",
      "args": ["-m", "matomo_mcp"],
      "env": {
        "MATOMO_URL": "https://analytics.example.com",
        "MATOMO_TOKEN": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
      }
    }
  }
}
```

## Step 5: Restart Claude Desktop

1. **Close Claude Desktop** completely (right-click the Claude icon in the system tray and select "Quit")
2. **Open Claude Desktop** again from the Start menu
3. The Matomo MCP Server should now be available!

## Testing the Installation

To verify everything is working:

1. Open Claude Desktop
2. Start a new conversation
3. Try asking Claude something like:
   - "Can you get information about site ID 1 from Matomo?"
   - "Show me the visit summary for the last 30 days"

If Claude can access your Matomo data, congratulations! 🎉 You've successfully installed the Matomo MCP Server.

## Troubleshooting

### "python is not recognized as an internal or external command"

**Problem**: Python is not in your PATH.

**Solution**:
1. Uninstall Python (Windows Settings → Apps → Python → Uninstall)
2. Reinstall Python and make sure to check "Add python.exe to PATH"

### "pip is not recognized as an internal or external command"

**Problem**: Pip is not installed or not in your PATH.

**Solution**:
1. Try using: `python -m pip install --pre matomo-mcp`
2. If that doesn't work, reinstall Python

### Claude Desktop doesn't show Matomo tools

**Problem**: The configuration file might have errors.

**Solution**:
1. Check that `claude_desktop_config.json` has valid JSON syntax
2. Make sure there are no extra commas or missing brackets
3. Verify the file is saved in `%APPDATA%\Claude\`
4. Restart Claude Desktop completely

### "Missing required environment variable: MATOMO_URL"

**Problem**: The configuration file doesn't have the correct settings.

**Solution**:
1. Double-check that you added the `env` section with `MATOMO_URL` and `MATOMO_TOKEN`
2. Make sure you replaced the placeholder values with your actual Matomo URL and token
3. Restart Claude Desktop

## Updating to a New Version

When a new version of matomo-mcp is released:

1. Open Command Prompt
2. Type: `pip install --pre --upgrade matomo-mcp`
3. Press Enter
4. Restart Claude Desktop

## Uninstalling

If you want to remove the Matomo MCP Server:

1. Open Command Prompt
2. Type: `pip uninstall matomo-mcp`
3. Press Enter
4. Type `y` when asked to confirm
5. Remove the "matomo" section from `claude_desktop_config.json`

## Getting Help

If you encounter issues:

- Check the troubleshooting section above
- Report issues at: https://github.com/kitconcept/matomo-mcp/issues
- Make sure you're using Python 3.10 or newer: `python --version`

---

**Note**: This guide is for the alpha version (1.0.0a1) of matomo-mcp. Some features may change in future releases.
