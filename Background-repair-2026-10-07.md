# Six screenshot background repairs

Changed the live Documents checkout, not the asset-free Codex worktree. No commit or publication. Originals, sources, pixel/hash receipt and preview are outside the package at `C:/Users/stena/Documents/Codex/Azir-background-repair-20261007`.

| Screenshot | Custom wallpaper | Installed alias | Source |
| --- | --- | --- | --- |
| 1 | EtaSuperbLoadingScreen | load_nsb2 | Existing Gangplank/Nautilus source JPG, 1920x1080 |
| 2 | NuMustLoadingScreen | none | https://images7.alphacoders.com/859/859992.jpg, 1920x1200; restores vertical content missing from local 1080 crop |
| 3 | IotaAmazingLoadingScreen | load_6 | https://dd.b.pvp.net/latest/set2/en_us/img/cards/02IO006T1-full.png, 2048x1024 |
| 4 | DeltaAmazingLoadingScreen | load_1 | Existing Targon source JPG, 1920x972 |
| 5 | ZetaSuperbLoadingScreen | load_nsb | Existing Irelia/Sion source JPG, 1920x1080 |
| 6 | EtaMustLoadingScreen | none | https://dd.b.pvp.net/latest/set1/en_us/img/cards/01IO032-full.png, 2048x1024 |

All ten full textures use a 3440x1440 canvas matching current game settings, uniform contain scaling and plain slate borders. All ten corresponding thumbnails use the same composition. BGRA8 DDS stores pixels without block compression; decoded payloads exactly match export pixels. This avoids adding compression blocks but does not remove artifacts already embedded in source JPGs or create higher-resolution detail. Some art is interpolated to the canvas height.

`interface/frontendmainview.gui` copies the installed game definition and changes only `frontend_background` size/bounds: a 3440x1440 reference and screen-limited maximum bounds replace the old 1920x1440 cover bounds. The existing aspect-preservation flag remains enabled. This global menu container also affects other selectable wallpapers; their appearance and the engine's interpretation of these bounds need native verification. Loading artwork is controlled by the engine outside this menu container; the exported canvas corrects proportions at 3440x1440, but other loading resolutions remain unverified and may require another canvas export.

Validation: exact pixel readback, write/hash checks, GUI round-trip comparison proving only the intended bounds changed, and `python -B tools/validate_hoi4_mod.py` passed. No native reload, game restart or resolution changes were performed; the existing game process belongs to the user. No claim of universal screen-size acceptance or removal of all source artifacts.
