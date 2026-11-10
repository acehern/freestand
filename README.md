**Free Stand**  
**Free Stand** is a free and open-source digital music stand for worship teams and musicians.  
View PDF chord charts full-screen, build setlists, attach audio and YouTube links, transpose charts, annotate pages, and keep everything **on your device**—no account required.  
**License:** [GNU GPLv3 or later  
   
 **Copyright (C)** 2026 Casey Dale Herron  
   
 ](LICENSE "LICENSE")  
**App file:** `freestand.html` (also served as `www/index.html` for GitHub Pages)  
  
---  
**Features**  
**Library**  
- **Add PDFs** — import one or many chord charts at once  
- **Search** — filter songs by name  
- **Edit song** — rename, manage charts, audio, and YouTube  
- **Multiple charts per song** — different keys or arrangements; labels follow the file name when possible  
- **Delete** songs with confirmation  
- **Local storage** — charts and data stay on the device (IndexedDB); works offline  
**Chord chart viewer**  
- Full-screen PDF viewing with page navigation (edge taps / swipe)  
- **Bluetooth page turner / foot pedal** — clickers and pedals that send standard keys (arrows, Page Up/Down, space)  
- **Pages per screen** — Auto, 1, or 2 (via **⋮** menu)  
- **Transpose (− / +)** — shift chord symbols when chords are detectable in the PDF text; tap **Key** to reset  
- **Chart switcher** — when a song has more than one PDF (**⋮** menu)  
- Auto-hiding top bar (shows on tap, hides after \~10 seconds)  
- **Pinch zoom**, double-tap zoom (100% ↔ 120%), pan when zoomed  
- Zoom level remembered per chart  
**Formatted chart view (Beta)**  
- Rebuilds text-based PDFs into a clean **chord-over-lyric** layout (two-column pages)  
- Toggle in the **⋮** menu  
- **Transpose** and **auto key match** work on the formatted layout  
- **Arrangement editor (Beta)** — drag sections (Intro, Verse, Chorus, Bridge, …) into a custom order; repeat or remove sections; reset to original; arrangement saved per chart. Original PDF is never modified.  
- Best for text-based charts; scanned image-only PDFs will not format well  
**Audio (MP3 / M4A)**  
- Attach **one or more** audio files per song  
- In-viewer player with track name and multi-track dropdown  
- **Minimize** while playing — thin bottom bar; expand to full player  
- **Key detection** from the audio (labels use **sharps**)  
- **Pitch shift ±1** without changing tempo (where the browser supports it)  
- **Auto key match** (☰ menu) — after the MP3 key is detected, transpose the chart to match, then keep chart and audio locked together when you shift  
**YouTube**  
- Save a YouTube link on a song  
- Play in an in-app popup  
**Setlists**  
- Create setlists and order songs for a service  
- Open songs in setlist context  
**Annotations**  
- Text notes, draw, highlight, and erase on **original PDF** pages  
- Saved per song/chart on the device  
- (Not available while Formatted chart view is on)  
**App experience**  
- Light / dark mode (☰ menu)  
- Splash / cover screen  
- Mobile-friendly layout; works as a web app or packaged Android (Capacitor) build  
- Optional PWA-style install when served over HTTPS  
  
---  
**Quick start (web)**  
1. Open `freestand.html` (or `www/index.html`) in a modern browser, **or**  
2. Serve the `www` folder over HTTPS for best mobile / PWA behavior.  
```  
cd www && python3 -m http.server 8080  
 # then open http://localhost:8080  
   
```  
**Publish on GitHub (GitHub Pages)**  
1. Create a new repository on GitHub (e.g. `freestand`), **without** adding a README if you will push this folder as-is.  
2. On your computer:  
```  
cd FreeStand-repo   # or wherever you unzipped this project  
 git init  
 git add .  
 git commit -m "Initial Free Stand release (GPL-3.0)"  
 git branch -M main  
 git remote add origin https://github.com/YOUR_USERNAME/freestand.git  
 git push -u origin main  
   
```  
1. On GitHub: **Settings → Pages → Build and deployment**  
  - Source: **Deploy from a branch**  
  - Branch: **main**, folder: **/www**  
2. After a minute, your app will be at  
   
 `https://YOUR_USERNAME.github.io/freestand/`  
3. Optional: add a **Release** and attach an Android APK for downloaders.  
**Android**  
This project can be wrapped with [Capacitor.  
   
 Prefer publishing APKs under GitHub **Releases** rather than committing large binaries to the repo.](https://capacitorjs.com/ "https://capacitorjs.com/")  
UI source of truth: `freestand.html` / `www/index.html`.  
  
---  
**License**  
Free Stand is free software under the **GNU General Public License v3.0 or later**.  
You may use, share, and modify it under the GPL. If you distribute it (including modified versions or an app store build), you must provide **Corresponding Source** and keep the same license freedoms for recipients. See [LICENSE.](LICENSE "LICENSE")  
There is **no warranty**; see the GPL for details.  
  
---  
**Credits**  
- PDF rendering: [PDF.js (Apache-2.0)](https://mozilla.github.io/pdf.js/ "https://mozilla.github.io/pdf.js/")  
- Built for churches and musicians who want a simple, local-first chart stand  
  
---  
**Contributing**  
Issues and pull requests are welcome. By contributing, you agree that your contributions are licensed under GPL-3.0-or-later.  
