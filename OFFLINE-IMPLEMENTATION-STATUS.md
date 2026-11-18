# PicSecure Svara — offline recognition status

The application source has **not yet been committed** to this repository. The source ZIP must be unpacked and committed before the Android build workflow can succeed.

## Supported offline model archives
- English: `vosk-model-small-en-us-0.15`
- Hindi: `vosk-model-small-hi-0.22`
- Telugu: **not verified**; do not label an unrelated language model as Telugu.

Run **Actions → Download validated offline speech archives → Run workflow**. This downloads English and Hindi ZIPs into a temporary Actions artifact. Supply an independently verified Telugu Vosk model URL only when one is available.

Downloading an artifact is not equivalent to installing models into the Android application. The Kotlin `SvaraOfflineSpeechPlugin` expects extracted models in app-private `files/vosk-models/{en,hi,te}`, with Vosk `am` and `conf` directories. Installation, language switching and physical-device tests remain release gates.

## Build verification
`Android source validation` intentionally fails with an explicit missing-source error until application source and a dependency lockfile are committed. No passing APK build is claimed.
