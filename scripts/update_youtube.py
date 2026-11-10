#!/usr/bin/env python3
"""Fetch public AVQN YouTube uploads into videos.json using YouTube Data API v3."""
import json, os, urllib.parse, urllib.request
from pathlib import Path
KEY=os.environ.get("YOUTUBE_API_KEY","")
HANDLE=os.environ.get("YOUTUBE_HANDLE","@AletheiaVoxQuantumNetwork")
if not KEY:
    raise SystemExit("Missing YOUTUBE_API_KEY GitHub Actions secret")
def api(resource, **params):
    params["key"]=KEY
    url="https://www.googleapis.com/youtube/v3/"+resource+"?"+urllib.parse.urlencode(params)
    with urllib.request.urlopen(url,timeout=30) as response:
        return json.load(response)
channel=api("channels",part="contentDetails",forHandle=HANDLE)
items=channel.get("items",[])
if not items:
    raise SystemExit("YouTube channel not found; existing archive unchanged")
playlist=items[0]["contentDetails"]["relatedPlaylists"]["uploads"]
videos=[];page=None
while True:
    kwargs={"part":"snippet,contentDetails","playlistId":playlist,"maxResults":50}
    if page:kwargs["pageToken"]=page
    data=api("playlistItems",**kwargs)
    for item in data.get("items",[]):
        snippet=item.get("snippet",{})
        video_id=item.get("contentDetails",{}).get("videoId")
        if video_id and len(video_id)==11 and snippet.get("title") not in ("Private video","Deleted video"):
            videos.append({"id":video_id,"title":snippet.get("title","AVQN video"),"publishedAt":snippet.get("publishedAt","")})
    page=data.get("nextPageToken")
    if not page:break
Path("videos.json").write_text(json.dumps(videos,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("Updated",len(videos),"public video entries")
