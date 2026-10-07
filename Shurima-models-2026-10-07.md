# Shurima models - 7 October 2026

Installed SHU_infantry_entity in gfx/entities/shurima_sand_soldier.asset, with its unique mesh bindings in shurima_sand_soldier.gfx. Runtime mesh, DDS texture, six animation files and their registrations are in gfx/models/units/shurima_sand_soldier. No rules or unit statistics were changed. All unrelated changes and previous assets were preserved.

Source: E:/Downloads/League Universe/Loose Files from Downloads/azir.glb. Despite its filename this is a SOLDIER, with embedded animations. The supplied single-idle GLB and Moonlight Azir.blend also contain soldiers. No source documents were treated as user instructions.

Idle/alternate idle, run, death and spawn were exported using Blender 4.5.1 and the existing downloaded io_pdx_mesh addon. Combat uses azirsoldier_dash_exit provisionally; this is not a verified spear attack. Spawn is available but unbound. Entity scale 0.025 remains provisional until native inspection.

Binary readback passed: 1828 vertices, 32 bones, matching bone order in all six 24-fps clips. Installed mesh, DDS and idle animation reimported successfully and rendered outside HOI4. All mesh/animation paths resolve. Existing focus/localization validator passed; it does not test model behavior. Native model selection, scale, orientation, appearance and animation remain unverified. The running user game was not restarted or controlled.

Azir himself and his tower were not located as separate downloaded models. Their intended use needs clarification before choosing a special unit, fort replacement or landmark. Online source investigated: https://modelviewer.lol/model-viewer?id=268000 . Local League archive E:/Riot Games/League of Legends/Game/DATA/FINAL/Champions/Azir.wad.client exists but was not extracted.

Scripts, source export dumps, receipts and soldier-readback.png are outside the release folder in E:/Downloads/Azir-HOI4-conversion. Runtime gfx files are Git-ignored and require separate packaging. No commit or publication performed.


## Khada continuation

Source verified: https://modelviewer.lol/model-viewer?id=268000 and https://docs.modelviewer.lol/extractor . Downloaded the asset referenced by that viewer, decoded meshopt geometry and KTX2 textures into an editable GLB outside the mod. This is Azir himself, with 46 source animations. Seven clips (idle, alternate idle, run, death, respawn, two attacks) have been converted to PDX files under E:/Downloads/Azir-HOI4-conversion/azir-runtime. They are preparation assets, not installed game content.

The installed shader gfx/FX/pdxmesh.shader declares matBones[50]. Azir originally exported 93 bones; unused helpers plus detailed finger/feather chains were removed and their vertex weights merged into retained ancestors, producing 48 bones. This intentionally simplifies finger and feather motion. Binary readback confirmed all seven animations use the matching 48-bone order. Native behavior and visual acceptance remain unverified; placement as a special army model is still awaiting the user choice.

Soldier material repair is installed: explicit neutral normal and conservative specular textures were added because the native shader samples both. Diffuse DDS was rebuilt as BC3 with ten mip levels; auxiliary maps have three. Binary comparison proved geometry, skeleton and animation files unchanged. The previous runtime folder is backed up outside the mod at E:/Downloads/Azir-HOI4-conversion/backup-materials-20261007-031832. This fixes an incomplete material contract and absent mipmaps; it does not establish that the user's speckled-render symptom is solved. In-game comparison is still needed.

Khada's Extras turret index was inspected for the separate tower. Metadata for variants 0-24 did not identify Azir's tower; later requests returned HTTP 429 and the search stopped. The tower remains unidentified and uninstalled. No game restart, publication, commit or other shared changes were performed. All new runtime art remains Git-ignored.


Azir visual conversion follow-up: the first animated readback failed despite matching skeleton names. Khada stores a reflected 0.0085 armature scale and a KHR_texture_transform. Removing the reflected object scale before exporting (retaining source bone units), baking the glTF UV transform into UV coordinates, and correcting the temporary exporter's initial-pose world-space calculation produced a coherent textured idle readback. Render: E:/Downloads/Azir-HOI4-conversion/azir-readback.png. Exporter changes are confined to the task-local addon copy, not the user's Blender installation. Seven animation files retain a matching 48-bone skeleton; only an idle frame has been visually inspected. Other motion cycles, native HOI4 appearance and game placement remain unverified.


## Soldier material/UV defect - screenshot follow-up

The user's second native screenshot still shows dark speckled soldiers. Exporter author guidance checked: https://github.com/ross-g/io_pdx_mesh/wiki/FAQ recommends tracing an existing native asset. Material workflow guidance inspected: https://steamcommunity.com/sharedfiles/filedetails/?id=3004523941 (PDX material, DDS slots and UV editing). The actual installed vanilla western_european_infantry.mesh uses PdxMeshAdvanced with diffuse/normal/specular maps and UVs near 0-1.

Concrete defect found in our soldier: u0 was 0-4095. The original GLB material contains KHR_texture_transform with scale [0.000240657391, 0.000240497437] and offset [0.00554900011, 0.00308901072]. The first conversion copied the image but omitted that transform. This makes the sampler repeat the texture thousands of times and is a strong explanation for the speckled appearance. The earlier material-map repair did not address this defect.

Applied that exact source transform to runtime mesh u0, giving a combined range 0.0030890107-0.9910410047. All other mesh attributes and every animation file were verified unchanged. Backup: E:/Downloads/Azir-HOI4-conversion/backup-uv-20261007-033523. Export script was corrected to bake the same transform into Blender UVs for future conversions. Normal/specular maps and shader were left unchanged in this batch to isolate the UV fix.

The corrected installed mesh was reimported and rendered. A texture-focused emissive preview (soldier-uv-preview.png outside the mod) shows coherent gold artwork; this bypasses native lighting and is not native rendering proof. The ordinary lit Blender render remains quite dark, so shader/normal/light behavior must not be declared solved. HOI4 was not running during this check; no game was launched. A fresh native comparison remains required. No commit or publication performed.
