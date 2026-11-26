# Twin Cities asset accounting

**18 of the 20 milestone art slots remain in the development checkout.** Two installed scenes cover the other slots, and Caitlyn’s separate portrait export is complete locally. The original full 990 plan budgets 546 graphical deliverables, including those two scenes. The development balance is 544 under that scope, with 88 for the existing-content finish and 456 for the proposed roster and route expansion.

The 24 November baseline used the shared Azir checkout at `d821677` with working-tree changes, Quarior `3297129305`, Runeterra `3032467701` and the installed base game. The 26 November reconciliation updates the three completed development rows. The **64 installed city files** in that scoped inventory include exports and material maps and count physical files. Native rendering, asset provenance and release rights remain open wherever the source record does not establish them. See the [graphical binding inventory](Twin%20Cities%20Graphical%20Binding%20Inventory.md) and [existing route designs](Twin%20Cities%20Institutions%20and%20Bramble%20Crawler.md).

## What the current build needs

| Surface | Source evidence | Remaining work |
| --- | --- | --- |
| Focus tree | 18 focuses per city. Bramble Crawler and Sumpworks Recovery have custom art. The other 34 use generic goals. | Six institutional capstone icons are the first differentiated set. Use the other 28 in a fully bespoke pass. Four currently use `GFX_goal_generic_construction2`, which has competing loose bindings. Check the effective icon in-game. |
| Events and quests | The baseline covered 66 event blocks with 57 explicit picture uses. `GFX_PIL_tikras_jungle` now resolves locally for five events and `GFX_ZAU_excavator_works` resolves for one. | Both scenes are covered in development. The frozen RC13 package omits their event script, sprite registrations and images. Inspect event blocks using default presentation before budgeting additional artwork. |
| Leaders and advisors | The Council and Vander use inherited large art. Renata has a local leader portrait. Quarior defines and recruits Caitlyn as a corps commander. Both large and small portrait sizes resolve in development. Four domestic delegations use generic small portraits. | Supply the existing small export when packaging Caitlyn. Frozen RC13 includes the binding and large portrait, with the small texture absent. Four office portraits remain in the milestone. |
| Unique units and equipment | Four local types. Piltover has the Warden Caliver company and Bramble Crawler battalion. Zaun has Sump Raiders and the Sumpworks Recovery company. The two vehicles have local meshes, material companions, sprites and trial scenes. Existing map counters reuse native art. | Two infantry-team visual packages and four counter masters. The two infantry equipment families use native equipment artwork. Budget four bespoke plates for their two versions each. Static vehicle entities show no named bespoke animation states. |
| Technology and special projects | The two vehicle researches use their equipment images. Two facility projects per city share that city's category art. | Four project icons for Caliver, cube-battery upgrade, carbine and reusable filters. Preserve the two vehicle research/equipment plates as reuse. |
| Companies and industry | Institution advisors, contracts and trial factories exist. No city-owned military industrial organization definition was found in the inspected Azir and installed dependency directories. A Shuriman definition references PLT as a foreign tag. | Existing policy art belongs to the finish pass. Company logos, panels, trait trees, availability and ownership belong to a separately designed industry expansion. |
| Interface and motion | Two focus backgrounds, shared BoP panorama, domestic banners and national flags have loose files. Unit meshes, generic focus shine and animated character portraits are different systems. | Keep the established panels and backgrounds. Prove an optional animated-portrait view on one role before scaling it. Budget bespoke motion separately from static portraits and engine bindings. |

Four convention-based Caliver and Carbine sprite IDs remain unresolved in the inventory. Their archetypes have explicit generic pictures, so those four count as upgrades. The construction icon conflict is a binding review outside the illustration count. See [live event source](../events/PIL_tikras.txt), [technology](../common/special_projects/projects/azir_twin_cities.txt), and [equipment fallbacks](../common/units/equipment/azir_twin_cities_equipment.txt).

## Production count

An illustration, icon master, model with its material set, 2D loop, or 3D clip is one deliverable. A master can feed several UI crops, still fallbacks, and output resolutions. Character files, company definitions, dialogue, focus and quest scripting, numerical balance, exports, rights clearance and native QA are tracked separately. Caitlyn's small portrait counts as a completed development export. The future export count depends on which roles each character actually receives.

| Existing content finish | Count | Derivation |
| --- | ---: | --- |
| Focus icons | 34 | Six reviewed capstones and 28 remaining generic focuses |
| Event scenes | 2 | Tikras expedition and excavator works, both covered in development |
| Advisor portrait masters | 4 | Academy, Ferros, ward engineers, Glasc purchasing |
| Equipment plates | 4 | Two Caliver and two carbine loadouts |
| Special project icons | 4 | One for each facility project |
| Unit counter masters | 4 | One per existing battalion or company |
| Infantry-team model packages | 2 | Warden Caliver team and Sump Raider team |
| Unit animation clips | 12 | Three clips for each of the four existing unit types, using the two current vehicle models |
| Policy and industry symbols | 12 | Two symbols per implemented institution across six routes |
| Quest and decision icons | 8 | Four per city for signatures such as research permits, contracts, service and recovery |
| 2D milestone loops | 4 | Two per city across major choices or outcomes |
| **Subtotal** | **90** | 72 stills, 2 model packages, 12 unit clips, 4 loops |

**First milestone remaining.** Six capstone icons, four advisor portraits, four equipment plates and four special-project icons, for **18 remaining**. The two scenes count as covered and Caitlyn’s separate export sits outside the twenty slots.

### Milestone progress, 24 November 2026

The live checkout now has both event scenes installed through the existing `interface/PIL_tikras.gfx` bindings. The 210 × 176 Tikras image serves `PIL_tikras.1` through `.5`. The separate Zaun works image serves `PIL_tikras.6`. Both DDS files decoded and were visually inspected. These cover two of the twenty visual slots.

The local `gfx/characters/PLT/portrait_PLT_caitlyn_small.dds` is a 65 × 67 DXT5 export cropped from the currently bound Quarior large portrait. It resolves the existing small sprite for both military and civilian slots. Native display and distribution rights are pending. The export is under Git-ignored `gfx/`. Verify its presence in the emitted package manifest.

### Package readback, 26 November 2026

The registered standalone **Shurima and Targon Sprint RC13** package and its SHA-256 manifest omit all three DDS paths. RC13 includes Caitlyn's small sprite registration and both character slots using it, so its missing small texture is a packaging gap. The two Tikras scenes also have no packaged event script or sprite registration in RC13. The locally downloaded Workshop Azir copy also lacks the three DDS files.

The current candidate builder inventories physical `gfx/` files, including ignored DDS files, and its input filter admits all three local textures. A Git-only export would omit Caitlyn's crop. In a future package that includes these features, verify the portrait path and its hash in the emitted manifest. Include the two event textures with their matching scripts and bindings only if the candidate includes the Tikras feature. This was a package readback and builder-input check. [Builder](../tools/build_sprint_candidate.py) · [RC13 receipt](<E:/Local Repo/Runeterra-sprint-candidates/2026-11-24-RC13/build-receipt.json>)

`PIL_public_warrant_council` is the first capstone under review. The proposed composition is a brass-bound public warrant, a single blue seal and one folded engineering drawing. The approved gameplay reference is the civilian study unlocked by completion, with licensing and a working research network required. Focus rendering and installation await exact-icon approval.

| Full roster and route expansion | Count | Derivation |
| --- | ---: | --- |
| Base portrait masters | 64 | 68 identities less Council, Vander, Renata and Caitlyn with existing large art |
| Alternate portrait masters | 8 | Warwick, Viktor as Herald, Powder, Vi as Enforcer, Caitlyn under martial mandate, Orianna’s changed form, awakened Mel, and an alternate Ekko |
| Animated portrait loops | 76 | One for each base identity and each alternate form, with static fallbacks |
| Character event illustrations | 68 | One anchor scene per identity. Lesser figures can enter through a shared civic chain |
| Counterfactual event illustrations | 24 | Eight branches with one opening, one turning point and one terminal scene each |
| Shared special event, diplomacy and news art | 12 | Six interactions with two outcome scenes apiece |
| Counterfactual focus icons | 32 | Four focuses per new branch |
| Research and special-project icons | 24 | Twelve per city for industrial, civic and military research |
| Equipment artwork | 24 | Two visual marks for each of 12 new equipment families |
| Unit counter masters | 16 | Twelve new formations and four reusable generic role counters |
| Industry company insignia | 12 | Six organizations per city |
| Industry company and facility panels | 12 | One per organization |
| Quest icons | 16 | Two per new branch |
| Generic decision and policy symbols | 12 | Six reusable interaction families per city |
| Unit model packages | 12 | Six per city, each including material maps |
| Unit animation clips | 36 | Three native-compatible clips per new visual family |
| Animated event beats | 8 | One per new branch |
| **Subtotal** | **456** | 324 stills, 12 model packages, 36 unit clips, 84 loops |

**Full total by deliverable type:** 396 stills, 14 model packages, 48 unit clips and 88 2D loops. Each additional standard figure adds three deliverables under this specification: a portrait master, a loop and a character scene. Each added visual form adds two if its story already has a scene. Each added unit visual family adds one model package, three clips, and a counter before equipment art. Each extra four-focus route adds ten directly attributable deliverables: four focus icons, three scenes, two quest icons and one animated beat. Research, companies and formations can be shared across routes.


## How the additional routes give players choices

The current three institutions per city give six starting points for expansion. Keep institution, ruler, military command and foreign posture as separate choices with their own gates. Choosing an industrial regime should leave the player free to pursue mutual defense, commercial neutrality or conflict. Give each ruler a distinct offer or dilemma where their history matters, and give the office a successor path so normal gameplay survives a change in personnel.

| Proposed 990 branch | Who can sponsor it | Turning point and cost | Foreign options |
| --- | --- | --- | --- |
| PLT Civic Reconciliation Council | Mel, Seraphine, or a civic coalition | Give Zaun representation in a shared service board or retain separate municipal budgets. Representation requires continued ward consent. | Shared clinics and transit, neutral mediation, or unilateral services after a veto. |
| PLT Hexgate Trusteeship | Jayce, Heimerdinger or the Academy | Decide who audits a dangerous pilot and who owns the research. Public oversight slows commissioning. Industrial sponsors demand purchasing power. | Open standards with secure Ixtali access, bilateral research, export controls or an independent research program. |
| PLT Temporary Protectorate | Caitlyn, Grayson or a civilian-appointed command | Authorize limited emergency command. Decide whether to submit to review and hand power back, or face an institutional split. | Border defense, reciprocal ceasefire terms, conditional foreign assistance or resistance to external control. |
| PLT Freeport League | A merchant coalition, with Ferros or an independent delegation | Pool shipping guarantees or protect competing carriers. Tariff and credit policy determine who carries the losses. | Trade guarantees, Bilgewater escort or anti-smuggling talks, neutral port access, or embargo and counter-embargo. |
| ZAU Lanes Sovereignty Pact | Silco or a separate Lanes coalition | Negotiate recognition from a position of leverage. Decide how far to rely on a single industrial patron. | Conditional recognition, separate transit rights, boycott, or ward-backed negotiated settlement. |
| ZAU Labor Congress | Sevika, Zeri or elected union delegates | Resolve essential-service strikes and decide whether centralized procurement is accountable to the shops. | Joint labor standards, relief arrangements, union embargo or domestic substitution. |
| ZAU Voluntary Repair Commune | Viktor with affected communities and an elected oversight body | Accept supervised medical work, restrict access, or break with the Herald after a breach of consent. | Joint relief, technology exchange under inspections, research quarantine or return to local workshops. |
| ZAU Chem-Baron Congress | Rival barons or a neutral administrator | Balance industrial output with enforcement of local limits. A broken cartel can produce reform, a withdrawal or an Urgot challenge with its own arrival gate. | Competing freight concessions, conditional trade, export controls or industrial independence from Piltover. |

Character story choices should cross these eight branches. Vi can serve under either city with an allegiance gate. Jinx can aid, leave or oppose a regime without forced succession. An invited foreign figure keeps their home-country ownership until a documented transfer. Isha, youth characters and a figure such as Janna get civilian or narrative roles. The alternate forms are conditional 990 proposals and require a chronology check before work begins. Arcane's Vander/Warwick connection supplies a form change for the same identity. Riot's shared-canon update explains why older regional material needs a continuity check. [Riot canon update](https://www.leagueoflegends.com/en-us/news/dev/tl-dw-champs-lore-more-dev-update/) · [Arcane production account](https://www.netflix.com/tudum/features/arcane-season-two-behind-the-scenes)

### Shared systems that preserve replay choices

| Player choice | Generic option available across leaders | Unique presentation or character gate |
| --- | --- | --- |
| Deal with the other city | Propose a treaty, stay neutral, dispute a breach, or withdraw through a fallback network | A conditional rescue, joint oversight decision or rival succession changes terms and scene text. Preserve the four existing crossing outcomes. |
| Build a foreign alignment | Seek technical exchange, limited defense cooperation, neutral commerce or mediation. Use independent counterpart consent and allow parallel offers. | Ixtal controls worksite access, Crystal Scar retains custody, and a Noxian offer can be refused or restricted. Bilgewater trade and a Shuriman corridor are proposed and need independent partner design. |
| Contest a hostile neighbor | Protect industry, defend an approach, intercept disruption through game systems, or negotiate de-escalation | A named officer can sponsor a specific defense plan. A generic officer can run the standard version. |
| Build an economy | Select public procurement, direct municipal production, company contracts, or a domestic substitute | Institution affects costs and upkeep. Each city has several suppliers and retains a route when a foreign contract fails. |
| Change the government | Return emergency powers, replace an unavailable sponsor, or negotiate a coalition | Explicit consent and succession events where a named appointment matters. Other policy decisions refer to the office and current conditions. |
| Recover from failure | Repair after a breach, release a suspended order, change suppliers or accept a neutral recovery mission | One shared incident chain can vary stakes and text. Use unique art for a lasting branch consequence. |

Seven domestic institutions per city give **49 possible institutional pairings** before leader or posture variants. Validate routes with their normal sponsor and a valid alternate or generic officeholder. Cover absent, removed and defected sponsors, each existing crossing outcome, live and lost freight, concurrent offers, and withdrawal before and after fulfillment. Include a change of ruler in a save/reload run, then test the same reachable foreign decision sequence with two human players. Pairwise coverage plus focused tests of incompatible states is the planning assumption.

### Proposed manufacturing, research and command scope

| City | Six company or bureau packages | Six new unit visual packages |
| --- | --- | --- |
| Piltover | Academy instruments, Ferros precision works, Warden ordnance, River Pilt shipyards, aeronautics bureau, and independent works cooperative | Warden patrol, shield company, observer team, fast carrier, harbor patrol craft, survey aircraft |
| Zaun | Ward engineering guild, Glasc manufacturing, Sump pumpworks, salvage cooperative, chem filtration works, and Lower Landing transport works | Firelight scouts, ward engineers, chem-safety team, freight hauler, pump tender, salvage scout craft |

Plan two research tracks per domain per city across civil works, standards, communications, security, transport and industry. That yields 24 expansion research icons and does not count the four existing facility projects again. Keep company logos, project badges and manufacturing plates separate if each is visible at a distinct UI decision. Ensure each unit gets an in-game equipment and unlock path, lend-lease or export policy, diplomatic eligibility, designer and map presentation, and an explicit fallback when 3D models are disabled.

Proposed **field-marshal candidates** are Caitlyn, Grayson, Vi, Vander, Sevika and Scar, gated by experience, appointment and which city they serve. The ten proposed named **corps-command candidates** are those six plus Marcus, Steb, Loris and Zeri. Caitlyn already has the corps role in Quarior. These roles reuse the portrait masters in the roster. Give each side a recruitable generic commander and field-marshal route using existing generic portraits for campaigns where named figures stay civilian, die, or leave. Ambessa can act through a Noxian intervention only under its own availability conditions.

Track **68 identity and role specifications**, with explicit implementation rows for city ownership, availability, transfer, succession, removal, command and adviser slots. The inspected start carries legacy country-leader declarations for the Council and Vander, a dependency character record for Caitlyn, and a Zaun character record for Renata. Review those four before migrating any declaration. Political offices can share a file by city, and a foreign figure's record belongs with its owning tag. A source-file count depends on that layout.

## Delivery gates and evidence

1. **Visually confirm the installed files.** Check the two event scenes and Caitlyn's small portrait in a development playset that includes them, then check the construction icon in the native UI. Inspect a trial of each vehicle and the Sumpworks decision icon. Check all four crossing outcomes in the existing playtest paths.
2. **Prove each production workflow on one case.** Check portrait crops in the cabinet and army screens. Check one optional animated portrait with a static fallback. Confirm one custom focus state and one animated vehicle through movement and battle rendering. Confirm the company, tech and production bindings against the engine's native views.
3. **Expand in playable slices.** For each route, trace the opening, meaningful adverse branch, independent foreign response, payoff and recovery. For a character, track country of ownership, reachability, age or form, distinct gameplay contribution, portrait slots, event art, availability and fallback roles.
4. **Release evidence.** A loose file and a sprite registration are source evidence. Record native initialization, player-triggered display, asset source and distribution permission, performance, replay behavior and multiplayer separately. Keep unapproved images and unused reference art outside the release package.

The 68-identity roster is a production boundary for the estimate. It covers the 22 entries in Riot's two regional champion lists, plus local rulers, city-linked published figures, named supporting cast, several LoR figures, and a foreign sponsor. Warwick shares Vander's identity in this scenario. Older lore figures, dated variants and minor named characters beyond this ledger remain a discovery backlog. Review further named Arcane appearances, LoR followers and regional stories against a distinct gameplay role before adding them. Each qualifying addition grows the budget by the per-figure rates above. [Riot Piltover](https://universe.leagueoflegends.com/en_US/region/piltover/) · [Riot Zaun](https://universe.leagueoflegends.com/en_US/region/zaun/?mv=image-gallery) · [Riot LoR roster](https://playruneterra.com/en-us/news/game-updates/rotation-2024-full-list/) · [Riot older LoR roster](https://playruneterra.com/en-us/news/game-updates/rotated-cards-march-2023/) · [Arcane credits](https://media.netflix.com/en/only-on-netflix/81435684) · [Arcane cast index](https://wiki.leagueoflegends.com/en-us/Universe%3AArcane) · [Ekko biography](https://universe.leagueoflegends.com/en_US/story/champion/ekko/)

The next named-figure sweep should cover Elora, Kino, Amara, Lest, Rictus, Ran, Ren, Gert, and the Midenstokke and other named LoR follower lines. Check named figures against episode credits or Riot material, merge variant names, then decide which can drive a quest, appear in an existing scene, or remain a background reference. Keep foreign agents and incidental cameos in the discovery ledger until their 990 participation is defined.

## Character ledger


### Piltover and cross-city

| Identity | Basis | Proposed playable or story role |
| --- | --- | --- |
| The Council | Existing collective ruler | Starting government; can remain in office under compatible institutions |
| Caitlyn Kiramman | Existing recruited corps commander and audit participant | Inspectorate, civil oversight, or accountable emergency commander |
| Camille Ferros | City champion | Ferros security commissioner; conditional pressure on the Council |
| Ezreal | City champion | Expedition sponsor and artifact-permit quest |
| Heimerdinger | City champion | Academy director or constitutional steward; can advise the wards |
| Jayce Talis | City champion and existing story sponsor | Patent advocate, research director, or accountable First Councillor |
| Orianna | City champion | Prosthetics, engineering, and consent arc |
| Seraphine | City champion with Zaunite family | Mutual-aid and reconciliation missions |
| Vi | Zaun-born city champion | Cross-city officer or ward liaison; allegiance decided in play |
| Mel Medarda | City-linked champion | Diplomacy, Council leadership, and Noxian independence choice |
| Cassandra Kiramman | Arcane | Council continuity and ventilation records |
| Tobias Kiramman | Arcane | House liaison, family and succession event |
| Grayson | Arcane | Enforcer reform, ceasefire liaison, transferable command |
| Marcus | Arcane | Enforcer command or compromised treaty witness |
| Steb | Arcane | Wardens corps commander or rescue officer |
| Loris | Arcane | Wardens corps commander or protection detail |
| Maddie Nolen | Arcane | Security appointment and loyalty inquiry |
| Shoola | Arcane | Council vote and municipal oversight |
| Hoskel | Arcane | Council commerce vote |
| Irius Bolbok | Arcane | Council technology safeguards |
| Salo | Arcane | Council patronage and succession faction |
| Sky Young | Arcane | Laboratory researcher and consequences witness |
| Ximena Talis | Arcane | Family and public accountability event |
| Corina Veraza | Legends of Runeterra | Investigation antagonist with a conditional cooperation outcome |
| Albus Ferros | Legends of Runeterra | Industrial board and finance advisor |
| Jae Medarda | Legends of Runeterra | Exploration and recovery expedition contact |
| Chief Mechanist Zevi | Legends of Runeterra | Municipal production and standards advisor |
| Ambessa Medarda | External Noxian figure | Envoy, patron, or intervention antagonist; foreign character owner |

### Zaun and cross-city

| Identity | Basis | Proposed playable or story role |
| --- | --- | --- |
| Vander / Warwick | Existing starting ruler plus alternate form | Vander leads ward continuity; Warwick is a conditional rescue or containment form |
| Blitzcrank | City champion | Worker rescue and engineering, with an independent charter option |
| Dr. Mundo | City champion | Medical or containment story with civilian safety choices |
| Ekko | City champion and existing story sponsor | Firelights sponsor, optional elected coordinator, command under a mandate |
| Janna | City champion | Community protection events and civic affinity |
| Jinx / Powder | City champion and alternate identity | Workshop quest, underground ally or antagonist, reconciliation or departure |
| Renata Glasc | Existing recruitable leader | Directorate chief, contract diplomacy and succession |
| Singed | City champion and existing story sponsor | Research appointment, oversight, or dismissal |
| Twitch | City champion | Sump reconnaissance or containment event and optional specialist |
| Urgot | City champion | Conditional antagonist, insurrection, or exile after a demonstrated arrival |
| Viktor | City champion | Academy or ward scientist, voluntary medical commune, conditional Herald form |
| Zac | City champion | Rescue and civic protection quest |
| Ziggs | City champion | Demolition research and workshop regulation |
| Zeri | City champion | Neighborhood defense communications and local command |
| Silco | Arcane | Conditional independence faction, negotiation or rivalry with Vander |
| Sevika | Arcane | Labor coalition, negotiator, or civilian-authorized commander |
| Scar | Arcane | Firelight corps command and recovery liaison |
| Benzo | Arcane | Trade and neighborhood mediation |
| Mylo | Arcane | Youth or apprentice story |
| Claggor | Arcane | Youth or mechanical apprenticeship story |
| Felicia | Arcane | Family and Lanes history, with timeline gates |
| Isha | Arcane | Civilian shelter and Jinx story |
| Huck | Arcane | Relief, addiction recovery, or community testimony |
| Babette | Arcane | Local information and safe passage |
| Jericho | Arcane | Market supply story |
| Finn | Arcane | Chem-baron cartel rival |
| Smeech | Arcane | Salvage cartel dispute |
| Renni | Arcane | Foundry or cartel dispute |
| Margot | Arcane | Chem-baron arbitration |
| Chross | Arcane | Industrial patronage or cartel dispute |
| Deckard | Arcane | Shimmer trial consequences and containment |
| Thieram | Arcane | Last Drop civic contact |
| Inna | Riot Ekko biography | Clinic, workplace and family story |
| Wyeth | Riot Ekko biography | Workshop, safety and family story |
| Velveteen Lenare | Older Zaun regional material | Conditional golem industry sponsor |
| Wencher Spindlow | Older Zaun regional material | Conditional cartel rival |
| Saita Takeda | Older Zaun regional material | Conditional supplier and barter route |
| Petrok Grime | Older Zaun regional material | Conditional chem industry rival |
| Professor von Yipp | Legends of Runeterra | Cross-city automation scientist and conditional transfer of research |
| Maryam | Legends of Runeterra | Temple caretaker and relief liaison |
