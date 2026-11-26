# Research in Runeterra Prime, 990 AN

**Author decision, 26 November 2026.** Use the existing research lines for the first replacements. Keep the equipment families, stocks and production paths they feed. Reshape individual branches later where the current line cannot express a consequential difference in play. The shared core, faction-specific access, meaningful gaps and plausible inventions remain the design direction.

| Read | Question answered |
| --- | --- |
| [World coverage](World%20Coverage.md) | Which polities exist or can emerge, and what evidence do we have in each of the eight areas? |
| [Shared research](Shared%20Research.md) and [source-node inventory](Current%20technology%20nodes.csv) | Which existing functions, unlocks, layouts and consumers would each replacement inherit? |
| [Shurima](Shurima.md) | How do the opening war, ordinary arms, the Lion Rider muster and the first research slot interact? |
| [Piltover](Piltover.md) | When does workshop knowledge become stock, field strength or a transferable capability? Which arcane outcomes already have an owner? |

## First in-place replacement

The English generic infantry arms line now uses the following names. Keep the main sequence intact. The four equipment nodes advance existing production models. The three intervening or final drill nodes improve eligible formations. All four models draw from or contribute to the existing infantry equipment family. A surplus of old arms can still equip a formation. The opening grant of 1,500 pieces to Shurima retains its value.

| Year | Existing technology | New English title | Result in the current script |
| --- | --- | --- | --- |
| 972 | `infantry_weapons` | Common Infantry Arms | Basic equipment, infantry and inherited vehicle weapon modules. The shared name key also labels the research category. |
| 990 | `infantry_weapons1` | Muster Arms | Equipment model 1. This and the previous model are already known to Shurima at the start. |
| 992 | `infantry_weapons2` | Close-Order Arms Drill | +5% soft attack for the three listed light, cavalry and vehicle-infantry categories. |
| 993 | `improved_infantry_weapons` | Standardized Infantry Arms | Equipment model 2. The existing anti-armor branch also departs here. |
| 994 | `improved_infantry_weapons_2` | Coordinated Assault Drill | +5% soft attack for the same categories. |
| 996 | `advanced_infantry_weapons` | Masterwork Infantry Arms | Equipment model 3. |
| 998 | `advanced_infantry_weapons2` | Combined Assault Drill | +5% soft attack for light infantry and cavalry, +10% for vehicle infantry. |

The replacement covers generic English titles, descriptions and equipment short names. It proposes no national weapon silhouette. Country-specific equipment names, inherited sprites and the module side effects need separate review before changing them. The date of each node is the research timing of this build. [English replacements](../../localisation/english/replace/zz_azir_infantry_arms_l_english.yml) · [Research effects and paths](../../common/technologies/infantry.txt)

## Four campaign encounters to evaluate against the map

| Case | What the player can do | Acceptance check for a later playable build |
| --- | --- | --- |
| Industrial replacements against elite troops | Compare Shurima's existing replacements and Lion Rider specialist demand against Xerath's available formation mix. Keep the first-pass armory family. | Use the same terrain, frontage, experience, supply, equipment fill and combat duration. Record combat losses, organization, available reserves, replacement time and sustained field strength. Compare soft/hard attack weighting separately from the armor/piercing bonus. A cheaper line must be able to replace losses faster if that advantage is promised. |
| A land power faces a maritime or aerial opponent | Shurima starts with zero convoys in country history. Its harbor and fleet focuses depend on coastal control. Bilgewater's country history specifies 250 convoys. Eight dockyard levels are distributed across Quarior states 11–20, with ports at the bays and Slaughter Docks. The inherited Bilgewater army order contains land divisions. Convoys and yards establish merchant lift and capacity to build or repair. An operational escort fleet requires a hull design, available yards, crews and deployed ships. Riot describes the skilled crews who sustain the port. [Bilgewater](https://universe.leagueoflegends.com/en_US/region/bilgewater/) · [Coastal focuses](../../common/national_focus/shurima_focus.txt) | Model one disrupted sea route. Observe convoys lost, access to a port, dockyard allocation to repairs versus replacements, and deliveries reaching the front. For air, compare ground warning/AA with actual interception by a based and supplied wing. A country without such a wing keeps the resulting vulnerability. Hold coast and airbase ownership fixed. |
| Buying stock versus taking the excavator works | A one-off delivery can fill a template. Zaun can separately gain the Crawler design and register a column by taking the works. This specific equipment blocks lend-lease and licensing. | Check the inventory and production list before and after each scripted transfer. An annexation alone must not distribute the project to third parties. Verify production after stock depletion and after reload. [Piltover trace](Piltover.md) |
| Magic becomes industrial | The approved Twin Cities direction progresses from ordinary research to industrial use and a later milestone. A unique equipped defender, a commissioned commercial gate, a weapon prototype and a factory product each have distinct owners. | On the approved route, count one unlock per outcome. With and without the facility DLC, check visible choices, tooltips and later access. A unique artifact grants no automatic replacement flow. Preserve the Portal reveal. [Author decision](../Twin%20Cities%20Signature%20Research.md) |

## Compatibility and release

For each next replacement, use its existing technology and category IDs to trace starting history, research bonuses, hidden decision grants, AI strategies, equipment archetypes, template needs, stocks and production orders. Follow country-specific localization and generic fallback. Verify classic equipment and designer layouts independently. Treat doctrine mastery, facility breakthroughs, prototype completion, unit training and diplomatic access as separate sources of progression.

Only a demonstrated mismatch needs a structural proposal. For example, the current foot-weapon node also grants vehicle modules. Before splitting those unlocks, identify which designs use the modules, which countries can currently make them and what happens to those designs on reload. Route any new national art through review of that country's means, institutions and fielded formations.

Native acceptance for the first English replacement is the same seven existing nodes in their current positions, the new generic names on relevant research and production screens, and uninterrupted stockpile and reinforcement behavior in an existing save. Check the category label on a research bonus and the three drill tooltips. For future mechanical changes add one campaign check of AI production, deployment and replenishment, then a two-player check on identical builds covering research completion, transfer and reload. Evidence in these documents is static unless a specific run is cited.
