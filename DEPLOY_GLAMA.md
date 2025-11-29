# Deploying Matomo MCP Server to Glama

This guide explains how to deploy the Matomo MCP Server to [Glama](https://glama.ai), a managed MCP hosting platform.

## Why Glama?

- ✅ **Zero installation** for end users - No Python, no local setup
- ✅ **Works everywhere** - Windows, Mac, Linux
- ✅ **Production-ready** - Isolated VMs, monitoring, logging
- ✅ **Simple configuration** - Users just add a URL to Claude Desktop
- ✅ **Free tier available** - Start with 1 MCP server for free

## Prerequisites

1. **Glama account** - Sign up at https://glama.ai
2. **GitHub repository** - Your matomo-mcp code should be on GitHub
3. **Docker** (for local testing) - Optional but recommended

## Deployment Steps

### Step 1: Create a Glama Account

1. Go to https://glama.ai
2. Click "Sign Up" or "Get Started"
3. Choose your plan:
   - **Starter (Free)**: 1 MCP server - Perfect for testing
   - **Pro ($26/month)**: 5 MCP servers - For production use
   - **Business ($80/month)**: 10 MCP servers - For teams

### Step 2: Prepare Your Repository

Your repository should have:

- ✅ `Dockerfile` (provided in this repo)
- ✅ `.dockerignore` (provided in this repo)
- ✅ `pyproject.toml` with dependencies
- ✅ Source code in `matomo_mcp/` directory
- ✅ `README.md` with usage instructions

All of these are already included in the matomo-mcp repository!

### Step 3: Test Docker Build Locally (Optional but Recommended)

Before deploying to Glama, test that your Docker image builds correctly:

```bash
# Build the Docker image
docker build -t matomo-mcp:test .

# Test running it
docker run -it --rm \
  -e MATOMO_URL=https://your-matomo.com \
  -e MATOMO_TOKEN=your_token_here \
  matomo-mcp:test
```

If you see the MCP server start without errors, you're ready to deploy!

### Step 4: Deploy to Glama

**Note:** As of writing, Glama's custom server deployment interface may require contacting their team or using their admin dashboard. Here are the expected steps:

#### Option A: Through Glama Dashboard (Expected Flow)

1. **Log into Glama** at https://glama.ai
2. **Navigate to "Deploy Server"** or "Admin" section
3. **Configure your deployment**:
   - **Name**: `matomo-mcp`
   - **Repository**: `https://github.com/kitconcept/matomo-mcp`
   - **Dockerfile path**: `Dockerfile` (root of repo)
   - **Branch**: `main`
   - **Transport**: SSE or stdio (choose SSE for remote hosting)

4. **Set environment variables** (per-user configuration):
   - Users will configure their own `MATOMO_URL` and `MATOMO_TOKEN`
   - Or, you can make this a multi-tenant service (see below)

5. **Click "Deploy"**

6. **Wait for build** - Glama will:
   - Pull your GitHub repository
   - Build the Docker image
   - Deploy to isolated VM
   - Provide you with a URL

#### Option B: Contact Glama Support

If custom deployment isn't available in the UI:

1. Email Glama support: Check https://glama.ai for support contact
2. Provide:
   - Repository URL: `https://github.com/kitconcept/matomo-mcp`
   - Request to deploy as hosted MCP server
   - Mention you have a Dockerfile ready

### Step 5: Get Your Server URL

Once deployed, Glama will provide:
- **Server URL**: Something like `https://matomo-mcp.glama.ai` or `https://mcp.glama.ai/matomo`
- **Access token format**: May use Glama's auth or your own

### Step 6: Share with Users

Users can now configure Claude Desktop without installing anything:

```json
{
  "mcpServers": {
    "matomo": {
      "url": "https://your-server-url.glama.ai",
      "transport": "sse",
      "headers": {
        "Authorization": "Bearer GLAMA_TOKEN_HERE"
      },
      "env": {
        "MATOMO_URL": "https://their-matomo-instance.com",
        "MATOMO_TOKEN": "their_matomo_token"
      }
    }
  }
}
```

## Architecture Options

### Option 1: Simple Hosted Server (Easiest)

Each user deploys their own instance:
- User signs up for Glama
- User deploys matomo-mcp with their own credentials
- User configures Claude Desktop with their Glama URL

**Pros:** Simple, no multi-tenancy needed
**Cons:** Each user needs Glama account

### Option 2: Multi-Tenant Service (Advanced)

You host one instance for all users:
- You deploy matomo-mcp to Glama
- You add authentication layer
- Users get API keys from you
- Your server proxies to their Matomo instances

**Pros:** Users don't need Glama accounts
**Cons:** Requires building auth system (see `cloud-server/` directory)

## Monitoring & Logs

Glama provides:
- **OS-level logs** - See all server output
- **Application traces** - Debug MCP protocol issues
- **Performance metrics** - CPU, memory usage
- **Request logging** - Track API calls

Access these through the Glama dashboard.

## Updating Your Server

To deploy updates:

1. **Push changes to GitHub** (main branch)
2. **Trigger rebuild** in Glama dashboard
3. **Or** Glama may auto-redeploy on git push (depending on configuration)

## Pricing Considerations

**For Individual Users:**
- Free tier: 1 server (perfect for personal use)
- Pro tier: $26/month for 5 servers

**For Hosting as a Service:**
- Business tier: $80/month for 10 servers + $3/server after
- With 50 users: $80 + (40 × $3) = $200/month
- Charge users: $5-10/month = $250-500/month revenue

## Troubleshooting

### Build Fails

**Check:**
- Dockerfile syntax
- All dependencies in pyproject.toml
- Files listed in .dockerignore aren't needed

**Solution:** Test locally with `docker build .`

### Server Starts But Doesn't Respond

**Check:**
- Environment variables are set (MATOMO_URL, MATOMO_TOKEN)
- Matomo URL is accessible from Glama's network
- API token is valid

**Solution:** Check Glama logs for error messages

### Claude Desktop Can't Connect

**Check:**
- URL is correct in claude_desktop_config.json
- Transport type matches (sse vs stdio)
- Authorization headers if required

**Solution:** Test the URL with curl or Postman first

## Alternative: Self-Publishing to Glama Directory

If you want your server in Glama's public directory:

1. **Make repo public** on GitHub
2. **Add package.json** (if needed for npm)
3. **Follow MCP server conventions**
4. **Submit to Glama** - They may have a submission process

Benefits:
- Users can find your server in directory
- One-click deployment for users
- More visibility

## Next Steps

After deploying to Glama:

1. **Update README.md** - Add Glama deployment option
2. **Create user guide** - How to use your hosted server
3. **Set up monitoring** - Watch for errors and usage
4. **Gather feedback** - Improve based on user needs

## Resources

- [Glama Homepage](https://glama.ai)
- [Glama MCP Server Hosting Blog](https://glama.ai/blog/2025-09-10-glama-mcp-server-hosting)
- [Glama Pricing](https://glama.ai/pricing)
- [MCP Specification](https://github.com/modelcontextprotocol/specification)

## Support

- **Glama Support**: Check https://glama.ai for contact info
- **Matomo MCP Issues**: https://github.com/kitconcept/matomo-mcp/issues

---

**Note:** Glama is actively developing their platform. Some steps may change. Check their latest documentation at https://glama.ai for the most up-to-date deployment process.
