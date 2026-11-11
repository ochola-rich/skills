#!/usr/bin/env python3
"""
Apple Human Interface Guidelines (HIG) Crawler & Extractor

Fetches official HIG Markdown documentation directly from Apple Developer endpoints
and stores them in data/raw/ for offline indexing and skill generation.
"""

import os
import sys
import time
import json
import urllib.request
import urllib.error
from pathlib import Path

BASE_URL = "https://developer.apple.com/design/Human-Interface-Guidelines"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleHIGCrawler/1.0"

# Target key sections to extract
TARGET_SLUGS = [
    # Design Principles & Fundamentals
    "design-principles",
    "getting-started",
    
    # Foundations
    "accessibility",
    "app-icons",
    "color",
    "dark-mode",
    "layout",
    "materials",
    "motion",
    "typography",
    "spatial-layout",
    "sf-symbols",
    
    # Patterns
    "entering-data",
    "feedback",
    "loading",
    "modality",
    "onboarding",
    "searching",
    "settings",
    "undo-and-redo",
    
    # Components
    "buttons",
    "toolbars",
    "tab-bars",
    "sidebars",
    "search-fields",
    "menus",
    "activity-views",
    
    # Inputs
    "gestures",
    "pointing-devices",
    "keyboards",
]

def fetch_markdown(slug: str) -> str:
    url = f"{BASE_URL}/{slug}.md"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "text/markdown, text/plain"}
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode("utf-8")

def main():
    repo_root = Path(__file__).resolve().parent.parent
    raw_dir = repo_root / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    
    manifest = {
        "source": BASE_URL,
        "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "articles": []
    }
    
    print(f"Starting Apple HIG crawl for {len(TARGET_SLUGS)} target topics...")
    success_count = 0
    
    for i, slug in enumerate(TARGET_SLUGS, start=1):
        output_file = raw_dir / f"{slug}.md"
        print(f"[{i}/{len(TARGET_SLUGS)}] Fetching {slug}...", end=" ", flush=True)
        try:
            content = fetch_markdown(slug)
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(content)
            print("OK")
            manifest["articles"].append({
                "slug": slug,
                "file": f"data/raw/{slug}.md",
                "bytes": len(content),
                "status": "success"
            })
            success_count += 1
        except urllib.error.HTTPError as e:
            print(f"HTTP Error {e.code}")
            manifest["articles"].append({"slug": slug, "status": f"HTTP {e.code}"})
        except Exception as e:
            print(f"Error: {e}")
            manifest["articles"].append({"slug": slug, "status": str(e)})
        
        time.sleep(0.3)  # Respectful rate limiting
        
    manifest_file = repo_root / "data" / "manifest.json"
    with open(manifest_file, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
        
    print(f"\nCrawl complete! Successfully fetched {success_count}/{len(TARGET_SLUGS)} topics.")
    print(f"Raw data saved to: {raw_dir}")
    print(f"Manifest written to: {manifest_file}")

if __name__ == "__main__":
    main()
