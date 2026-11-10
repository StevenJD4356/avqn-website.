# Aletheia Vox Quantum Network

Official AVQN website source for GitHub Pages.

## Publish
In **Settings → Pages**, choose **Deploy from a branch**, branch **main**, folder **/(root)**, and save. GitHub Pages requires a public repository on GitHub Free.

## Automatic YouTube archive
The homepage reads `videos.json`. A daily GitHub Actions workflow fetches the public uploads playlist, including videos and Shorts, via the official YouTube Data API v3.

1. Create a Google Cloud project and enable **YouTube Data API v3**.
2. Create an API key with YouTube Data API restrictions.
3. In repository **Settings → Secrets and variables → Actions**, add a repository secret named **YOUTUBE_API_KEY**.
4. Open **Actions → Refresh YouTube Archive → Run workflow** to import existing uploads. Future refreshes run daily.

Until configured, the site provides links to the YouTube channel and displays an archive setup message. The key is used by GitHub Actions and never placed in public HTML.

No videos are fabricated. Only public accessible uploads are imported.
