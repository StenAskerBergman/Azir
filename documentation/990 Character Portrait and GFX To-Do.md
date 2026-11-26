# Shuriman generic pass for the 17 countries
Give ordinary recruits, cabinet appointments and common military graphics a regional identity throughout the 990 campaign. Build the shared assets once. Each country below has a casting brief and a short list of graphics that need a local treatment. The occupations and motifs are proposed art direction.

## Shared production list
- [ ] **Characters.** Build country-appropriate name pools for generated officers. Supply ordinary generals, field marshals and admirals where the country fields a navy. Cover the political adviser, military staff and high command slots used by the country. Use institutional titles where the office matters more than the individual.
- [ ] **Portraits.** Build reusable civilian, army and naval portrait pools with large and small crops for the slots that use them. Use a shared desert pool for compatible countries and distinct pools for cultures such as Marai and the Voidborn. Inventory suitable Azir artwork first. Treat Quarior artwork as temporary filler.
- [ ] **GFX.** Build a common icon set for industry, trade, research, recruitment, supply, defense and diplomacy. Make the standard infantry, reconnaissance, support and naval counters readable at map scale. Export the required sizes and selected, unavailable or shine states wherever the consuming interface uses them.
- [ ] **Integration.** Bind each country to its name and portrait pools. Check a newly generated officer, an appointed adviser, the common focus icons and a deployed division for each country. Include flags at all three sizes and check the fallback when a named champion is unavailable.

- [ ] **Jakkel tag migration.** Rename Jungle Path (current tag `JGL`, spelled Jakkal in the country files) to Jakkel (`JKL`). Update the tag registration, country and state histories, localization, map color, army and portrait references, and all three flag sizes together. Check the merged build for an inherited `JGL` registration and verify ownership and cores in a fresh 990 start.

## Officer corps and succession decisions — 25 November 2026

- [ ] **Research before production.** For each country, check the author's 990 discussions, Runeterra lore and concept art for ordinary people in the relevant occupation. Record the visual reference and any unresolved casting choice before making portraits. Jakkel's country history establishes Ira and mage rule. The appearance of its ordinary officers is still open.
- [ ] **Portrait standard.** Use League of Legends character illustration, regional cultural references and the individual champion concept and splash art to establish appearance at the chosen stage of the story. Attach the visual references when generating. Use Hearts of Iron IV for bust framing, rank readability and the large and small crops. Keep recurring officers recognizable through promotion and changes of allegiance. Give officers affected by succession a stable identity alongside the generated recruit pool.
- [ ] **Targon.** Start with a Rakkor officer baseline. Give senior figures the marshal portraits. A few celestial beings among the lieutenant portraits remain an option. Distinguish temple service, clan affiliation and rank through clothing and insignia. A village captain who joins Diana after the clan rally and civilian subjects for Remember Us are proposals. [Targon scope](https://chatgpt.com/c/6b04d587-ffd4-83eb-8e7e-4179d93b299a) · [Eclipse paths](https://chatgpt.com/c/66fbe2e4-eb84-8000-85ac-89cf6308b36b)
- [ ] **Shurima.** Use the Royal Trade Guild, work unions and merchant fleet as references for ordinary appointments. A guild factor, labor representative and shipmaster are proposed portrait subjects.
- [ ] **Icathia and Voidborn.** Trace the ordinary officer corps on both sides of the split. Record the author's intended loyalties and consequences before casting route-specific officers.

### Icathia and Void generic portraits

Current direction: start with ordinary people before contact with the Void. A pre-contact Malzahar portrait is an exploratory first step for a possible character journey. The concept shows him as a Shuriman seer. His face and clothing are proposed art direction, pending review. [Riot biography](https://www.leagueoflegends.com/en-us/champions/malzahar/)

25 November 2026: The author rejected the generated three-officer concept sheet. Its casting, uniforms and palette have no approval. The generator received only a text description. Use The Fall of Icathia painting itself as the reference input and show direct crops of the relevant figures alongside any proposed armor interpretation. The resulting spear-bearer study awaits review.

On 25 November 2026 the author accepted the existing portraits shown for Jax, Zilean, Kassadin, Kai’Sa, Bel’Veth, Rek’Sai, Cho’Gath and Kha’Zix. These eight named characters have dedicated faces. Their large and small crops are closed.

- [ ] Inventory portraits actually assigned to generated Icathian and Void officers. Identify the appearance of an ordinary recruit on each side using existing world art and the authored 990 setting.
- [ ] Show examples of unnamed officers or supported visual references for them. Check the allegiance of the soldiers in *The Fall of Icathia* before borrowing their clothing or equipment.

#### Icathian character decisions, 25 November 2026

| Subject | Decided | Still open |
| --- | --- | --- |
| Levy captain | Selected as a pre-Void levy subject with boiled leather and a wicker shield. Portrait rejected on 25 November 2026. Production stopped. | No approved appearance or roster placement. |
| Kohari archer | Selected as the second subject. Axamuk’s red-lacquered bow and blue raptor fletching are source references. Portrait rejected on 25 November 2026. Production stopped. | No approved appearance or roster placement. |
| Plumed veteran | Helmet study identified as a reference. | Casting, historical role and whether to produce the portrait. |
| Pre-contact Malzahar | Shuriman seer established as the premise for an exploratory look. | Final visual design and journey stages. |
| Eight named champions | Existing portraits accepted. Both Zaun Kai’Sa sizes frozen. | In-game verification of Kai’Sa recruitment and commission. |
| Resistance and Voidborn generics | Begin with ordinary pre-contact officers. | Who stays, leaves or changes allegiance, and which slots use cultists or creatures. |

### Kai’Sa’s foreign recruitment and Zaun quest

**Recruitment order, updated 25 November 2026.** Two decisions can open the same foreign offer chain. On Embrace, Kai’Sa leaves to protect civilians. On the human Resistance route, she stays eligible for Kassadin’s reunion until the player explicitly refuses her in the return event (`azir_kaisa.1.c`). Accepting her on Resistance or recruiting her automatically on the hybrid route closes foreign recruitment.

- [x] Offer field command to Shurima first, then Nazumah if Shurima refuses, then Zaun if Nazumah refuses. Run the chain once. Any acceptance ends further offers. If Zaun declines too, Kai’Sa continues independently.
- [x] Shurima and Nazumah each pay **125 PP** when hiring after human Resistance rejects Kai’Sa. If VOI chose Embrace, the invasion has begun and the same appointment costs **250 PP**. Record the triggering route when the chain opens. Refusal is free.
- [x] Both countries start with a **−10 percentage point stability modifier** on hiring. On each anniversary of hiring, reduce the remaining penalty by one percentage point. It reaches zero on the tenth anniversary. Track the backlash separately from changes to national stability from other causes.
- [x] Zaun takes Kai’Sa on provisionally with her ordinary portrait and the full −10-point modifier. Her quest substitutes for the sponsorship PP charge. Completing it removes the entire recruitment penalty at once and upgrades the same character to the Husk portrait and full field command.

**Implemented Zaun quest — The Missing Shift**

1. **Reopen the pump station.** A maintenance shift has missed its return from the lower sumps. Assign one civilian factory for 14 days to restart the pumps and give Kai’Sa and the search crew access. The report identifies the gallery where the workers took shelter.
2. **Bring the shift home.** Choose an extraction. Spend 25 support equipment to send respirators and winches down the service shaft for immediate rescue, or keep the factory assigned for seven more days to drain the longer exit. Both recover the workers. The second route keeps the quest accessible to a Zaun without spare equipment.
3. **Give her a permanent crew.** After the survivors return, take the decision to commission Kai’Sa to lead future sump rescues. Their testimony explains why the city accepts her, and her crew supplies the Husk mantle and equipment. On commissioning, remove the −10-point modifier and unlock the upgraded portrait and command together, once. Until then she keeps her ordinary portrait and provisional status.

Local script checks cover both entry points, both price thresholds, ten annual recovery steps and both extractions. Only the final commission changes her portraits and lifts Zaun’s backlash. In-game verification is pending.

| Story moment | Portrait sheet | What to carry into the artwork |
| --- | --- | --- |
| Childhood and first contact | [Kai’Sa 9](<file:///E:/Downloads/Runeterra%20Art%20References/Concept%20Art%20Kai'Sa/Kaisa_concept_9.webp>) | Use the progression of carapace coverage. In the childhood scene, show her father’s knife and the first patch of living skin clinging to her arm. The figures on the sheet are adult proportion studies. |
| Returning to the surface as a hunter | [Kai’Sa 6](<file:///E:/Downloads/Runeterra%20Art%20References/Concept%20Art%20Kai'Sa/Kaisa_concept_6.webp>) | Pair a closed helmet from the lower row with the face above it so a patrol can recognize the person inside. |
| Shurima and Nazumah recruitment offers | [Kai’Sa 7](<file:///E:/Downloads/Runeterra%20Art%20References/Concept%20Art%20Kai'Sa/Kaisa_concept_7.webp>) | Use the exposed profile and cheek marking as the reference for both encounters. Each government meets the same protector. |
| Zaun completes her rescue quest | [Husk 2](<file:///E:/Downloads/Runeterra%20Art%20References/Concept%20Art%20Kai'Sa/Husk/Husk_Concept_2.webp>) | Borrow the mantle and green-lit equipment for the alternate portrait. Husk’s cancelled Zaunite mercenary concept supplies the visual reference for this mod route. |

Approved and frozen on 25 November 2026 after review at native size: the 156 × 210 Zaun command portrait with the green-edged Husk mantle and the 65 × 67 advisor portrait with the tighter face-and-collar crop.

Kai’Sa’s protection of Shuriman survivors and Malzahar’s willingness to sacrifice them explain her break with Icathia on Embrace. [Kai’Sa on the League Wiki](https://wiki.leagueoflegends.com/en-us/Universe:Kai%27Sa) · [Malzahar](https://wiki.leagueoflegends.com/en-us/Universe:Malzahar#Prophet_) · [Husk](https://wiki.leagueoflegends.com/en-us/Husk)

### Xerath's Arcane Order

Begin with one shared army containing Baccai commanders, Baccai mages and Xerath's acolytes. For each recurring general, record starting command, personal allegiance, portrait and fate under each settlement.

| Route | Officer corps outcome |
| --- | --- |
| Renekton kills Xerath and takes control | Purge the designated Xerath loyalists. Reward Renekton's supporters with identifiable commands or promotions. |
| Xerath prevails | Purge the designated Renekton loyalists and reward Xerath's supporters. Settle each affected officer's fate. |
| Shared command | Keep officers from both camps available in the same army. Preserve their identities and portraits. |
| Noxian alignment | Add a recognizable Noxian contribution. A named foreign general with field command and a possible recall is a proposal. The sponsor, terms and recall trigger are open. |

Alexander von Falkenhausen supplies the HOI4 reference for the proposed foreign appointment. The installed Chinese focus can unlock a corps commander and army-chief appointment, and a German event can recall him. Track the foreign appointment separately from domestic succession. Check which generals remain in field command and which advisers remain available after each outcome and after reload.

- [ ] **Sun Discs.** Give Nerimazeth's earlier fallen disc and the imperial capital's later disc distinct visual references. Atreus places the first Ascended at Nerimazeth. The imperial disc is associated with Azir's interrupted Ascension and the restored capital. Opposing Baccai reactions to Xerath's project are a proposed motive for individual loyalties. [Ezreal's field notes](https://wiki.leagueoflegends.com/en-us/Universe%3AEzreal%27s_Field_Notes) · [Atreus's account](https://wiki.leagueoflegends.com/en-us/Universe%3AFor_Those_Who_Have_Fallen) · [Bloodline](https://universe.leagueoflegends.com/en_US/story/rg-shurima-story/)

## Country checklist

For the active-playset inventory, see [country audit and first production gaps](Shuriman%20generic%20pass%20-%20active%20playset%20audit.md). The checklist below describes intended coverage. The audit identifies which assets already supply it.

| Country | Characters to supply | Generic portraits to supply | GFX to produce or adapt |
| --- | --- | --- | --- |
| Shurima | Imperial officers, provincial administrators, irrigation and works advisers | Imperial officer and provincial civilian sets | Sun Disc state seal, canal works, grain and imperial levies |
| Xerath Arcane Order | Shared Baccai commanders, Baccai mages and acolytes with the succession outcomes above | Order functionary and arcane commander sets | Arcane authority, conduit works and siege formations |
| Icathia | Resistance officers, wardens, scholars and quartermasters | Survivor civilian and warden officer sets | Restored civic seal, containment works and defensive infantry |
| Voidborn | Define which generic slots take brood commanders or mortal cult servants and how they are named | Separate creature silhouettes and cultist portraits for the corresponding slots | Brood muster, adaptation and swarm counters |
| Nazumah | Council delegates, craftspeople, hunt captains and defense staff | Council civilian, artisan and hunter-officer sets | Council seal, workshops, expedition supply and hunters |
| Targon | Rakkor officers and civic advisers, plus Solari and Lunari officeholders where allegiance matters | Rakkor officer baseline, temple office variants and senior marshal portraits | Mountain supply, pilgrimage and distinct faction emblems |
| Crystal Scar | Local stewards, custodians and defenders consistent with the chosen Scar population | Establish the custodians’ appearance before producing the pool | Custody, extraction, reclamation and territorial defense |
| Marai | Reef stewards, tide scouts and coastal commanders | Marai civilian and military pools with readable aquatic silhouettes | Reef settlements, Moonstone custody, marine units and coastal supply |
| Great West Sai | Caravan organizers, route guards and desert commanders | Shared Sai base with a western insignia or dress detail | Caravan trade, wells, escort units and West Sai flag |
| Great East Sai | Settlement representatives, scouts and patrol commanders | Shared Sai base with an eastern insignia or dress detail | Settlement supply, patrols, scouts and East Sai flag |
| Shakkal | Camp organizers, raider captains and gang representatives | Camp civilian and raider base with gang-specific details | Gang emblems, camp supply, raiding and irregular infantry |
| Ixtal | Court officials, elemental specialists and territorial commanders | Ixtali court, specialist and field-officer sets | Elemental disciplines, jungle defense, worksite access and scouts |
| Jakkel (JKL) | Guides, local envoys, supply organizers and patrol leaders | Trail guide and patrol sets once the local population is established | Trail access, jungle supply, guides and light patrols |
| Northern Noxus Colonies | Colonial administrators, garrison officers and locally recruited intermediaries | Noxian service dress and local civilian or auxiliary sets | Colonial administration, garrison, auxiliary troops and colonial flag |
| Aurma | Port officials, merchant representatives, naval captains and coastal staff | Port civilian and maritime officer sets | Harbor works, convoy trade, shipbuilding and coastal forces |
| Piltover | Civic officials, Academy engineers, Warden officers and port staff | Piltovan civic, technical and uniformed service sets | Civic warrants, precision industry, river freight and Warden counters |
| Zaun | Ward representatives, industrial specialists, crew bosses and defense organizers | Ward civilian, industrial worker and local officer sets | Ward services, filtration, salvage, sump transport and militia counters |

---
A country row is ready when its ordinary characters can be generated or appointed with appropriate names and portraits, its shared icons resolve, and its distinctive graphics appear in the relevant views. Named champion and story-route work belongs to the individual country plans.


