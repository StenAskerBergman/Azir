# Hextech and Shimmer research in 990

## Author direction, 25 November 2026

Piltover can build its defense around Hextech. Zaun can pursue Shimmer. Each player chooses how much research and focus time to invest in their city's specialty. Ordinary research should advance the program. A player who pursues the breakthrough earns late-game defenders. The Portal belongs to Piltover's Hexcore route.

| Tier | When the player can pursue it | What the player earns |
| --- | --- | --- |
| 1. Foundations | Available to research at the 990 start, at low cost. | Basic bombs and progress from ordinary research. Jayce's hammer, Vi's gauntlets and Viktor's staff belong later. |
| 2. Industrial use | Complete Tier 1. | A practical industrial application of Hextech or Shimmer. The specific production benefit for each city is open. |
| 3. Core | Complete Tier 2, meet research goals and earn a national focus or event milestone. | Piltover builds the Hexcore and unlocks late-game defensive character capabilities. It can now start the separate Hexcore Portal project. Zaun earns its own Shimmer milestone and defenders. |
| 4. Beyond the prototype | Building the Hexcore can reveal the tier. Research requires both the Core and the completed Portal. | Expand what the Portal can carry beyond its first limited allied goods shipments. The exact cargo and the Zaun counterpart are open. |

An unexplained tier marker is acceptable before the reveal. Keep the project name, reward, prerequisites that reveal the reward, and character equipment out of early tooltips. Cross-map teleportation is a possible final mission. Its payload, destinations and implementation remain open.

## How the HOI4 project would work

The proposed split puts foundations and industrial use in research slots. Relevant technologies use `special_project_specialization` to contribute breakthrough progress. The Core can use a facility project that checks specific research and a focus or event flag in `available`. Breakthrough points alone cannot identify which research goals the player met. The completion hook for a project is `project_output.country_effects`. It can grant a hidden technology and fire a country event. A regular technology instead uses `on_research_complete`.

Use the Core project as the Portal's `special_project_parent` if both are facility projects. Use `visible` to control the reveal and `available` to enforce requirements for starting a project. A later ordinary technology can check `is_special_project_completed` in its research conditions. Treat a visible mystery marker as separate presentation work. Inspect the locked tooltip and tree connections in-game before promising a surprise.

The installed game's Radar project demonstrates the whole sequence. It checks an Engineering technology, costs one Air breakthrough, runs prototype iterations, grants a technology to its owner and places a radar station in the facility state. Further ordinary research checks project completion. In Azir, the existing Caliver and Hex Carbine projects use the Land facility, restrict eligibility by original country and DLC, and have their own follow-ups. Reusing the facility does not require rewriting those projects. [Engineering follow-up](../common/technologies/electronic_mechanical_engineering.txt) · [Existing city projects](../common/special_projects/projects/azir_twin_cities.txt) · [Paradox developer diary](https://store.steampowered.com/news/posts/?appids=394360&enddate=1728910871&feed=steam_community_announcements)

## Campaign decisions still open

- **Piltover's existing Hexgate.** The charter and commissioning events already send a scheduled consignment to another terminal. Timetable and port-ledger focuses depend on the opening. The proposed distinction is between the existing commercial schedule and the Core-powered facility that lets the player dispatch limited stockpiled goods to a chosen ally. This also preserves the canal's established role carrying heavy freight. [Commissioning event](../events/PIL_events.txt) · [Freight account](../localisation/english/PIL_events_l_english.yml)
- **The defenders.** Jayce already participates in civic licensing, so the proposed unlock is his hammer-equipped defensive role. Vi's gauntlets link a Piltover defense role to a Zaun-born character. Viktor helped develop Hextech with Jayce and has his own reasons to support or oppose its use. Decide whether Viktor's staff-equipped role belongs to Piltover at Tier 3 or whether his wartime allegiance depends on earlier player choices. Choose Zaun's Shimmer defenders separately. [Existing city roles](Twin%20Cities%20Institutions%20and%20Bramble%20Crawler.md) · [Jayce](https://www.leagueoflegends.com/en-us/champions/jayce/) · [Arcane season one](https://www.netflix.com/tudum/articles/arcane-season-1-recap)
- **The first shipment.** A limited transfer of existing equipment to a selected ally fits the country-level `send_equipment` effect. Shipment size, eligible goods and destinations are balance decisions. The possible final teleportation mission needs its own scope. The documented `teleport_armies` effect operates from an origin state and filters by army owner.
- **Zaun's later tiers.** Shimmer gets the same depth of investment. Its industrial application, breakthrough, defenders and final project need Zaun-specific outcomes. Zaun already lets the player fund Singed's work on filtering materials and audit the grant. A later event could put a distinct Shimmer proposal before the player. Accepting the earlier grant would establish a working relationship while leaving the Shimmer decision open. [Laboratory grant](../events/ZAU_events.txt)

This entry records the design discussion and checked script patterns. The four tiers, reveal, defenders and Portal shipment have no new gameplay implementation from this discussion.
