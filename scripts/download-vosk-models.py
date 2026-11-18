#!/usr/bin/env python3
"""Download and validate Vosk offline models. Does not silently substitute languages."""
import argparse
import pathlib
import urllib.request
import zipfile

MODELS = {
    "en": "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip",
    "hi": "https://alphacephei.com/vosk/models/vosk-model-small-hi-0.22.zip",
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="offline-models")
    parser.add_argument("--telugu-url", help="Verified Vosk-compatible Telugu model ZIP URL")
    args = parser.parse_args()
    output = pathlib.Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    urls = dict(MODELS)
    if args.telugu_url:
        if not args.telugu_url.startswith("https://"):
            parser.error("--telugu-url must be HTTPS")
        urls["te"] = args.telugu_url
    for lang, url in urls.items():
        target = output / (lang + ".zip")
        print(f"Downloading {lang}: {url}", flush=True)
        urllib.request.urlretrieve(url, target)
        with zipfile.ZipFile(target) as archive:
            bad = archive.testzip()
            if bad:
                raise ValueError(f"{lang} archive corrupt: {bad}")
            files = archive.namelist()
            if not any(name.endswith("/conf/model.conf") for name in files):
                raise ValueError(f"{lang} archive lacks Vosk model config")
        print(f"Verified {target} ({target.stat().st_size} bytes)", flush=True)
    if "te" not in urls:
        print("Telugu not downloaded: verified Telugu Vosk model URL is still required.")

if __name__ == "__main__":
    main()
