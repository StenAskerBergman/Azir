# Runeterra 990 candidate playtest

## RC13 · Shurima's political advisers

Use a fresh 990 campaign for this history change. Select only **Runeterra - Shurima and Targon Sprint RC13** in a separate playset. From Azir, preview `pwsh -File tools/launch-hoi4.ps1 -Mode Fresh -Country SHU -GameDebug -CandidateDirectory 'E:/Local Repo/Runeterra-sprint-candidates/2026-11-24-RC13' -Preview`. After the preview identifies RC13 alone and prints `-debug -start_tag=SHU`, remove `-Preview` to launch.

1. At the opening, inspect the political adviser slot. Both **Imperial Engineers** and **Provincial Delegates** should be unavailable to hire. Save before choosing **Imperial State** or **Republican Future**.
2. On the imperial route, move the balance strictly above +50% toward the court. With 100 PP and an open adviser slot, hire the Engineers. Enact the **Crown Levy**, then use **Repeal the Levy and Reassign the Engineers** once eligible. The balance should move to −65%, the Engineers should leave office, and the Delegates should be eligible for 100 PP.
3. Reload the branch save. On the provincial route, move strictly below −50%, hire the Delegates and enact **Local Muster**. **Renegotiate the Provincial Charters** should move the balance to +65%, remove the Delegates from office and enable hiring the Engineers. Save and reload after each switch. Check the new error log for recruitment warnings mentioning either adviser. Earlier saves can be checked separately for roster compatibility. [Release acceptance card](https://trello.com/c/qzr2g78W)

## RC12 · Icathian speeches

Start fresh as **VOI** in debug mode and finish `VOI_The_Voids_Influence` early. Save before choosing **Resist** or **Embrace**. Five days after the focus, look in Decisions for a 38-day speech mission. Note the speaker and date. A separate startup event can select a speaker between days 100 and 130 if the civil war has yet to begin.

1. On a control run, let the first mission expire. Expect a loss of 15 political power and 5 percentage points of stability, plus 5 points of support for mages (Zilean) or desolation (Malzahar), subject to caps. Check which mission appears next.
2. Reload for **Resist**. While Malzahar is present and you have 25 political power, use **We must Silence Malzahar!** Check that the decision can be paid for only once. Reload for **Embrace** and repeat with Zilean. Record what happens to the active mission, whether another 38-day timer starts and whether the prohibited speaker returns.
3. If a mission is active when the startup selector fires, record both speaker names and remaining days. At civil-war outbreak check that both timers clear. A single random selection cannot establish the outcome for both speakers. [Speech card](https://trello.com/c/ZrGxM9iD)

## RC12 · Startup comparison

When ready for the RC12 test, select **Runeterra - Shurima and Targon Sprint RC12** alone in a separate launcher playset. From Azir run `pwsh -File tools/launch-hoi4.ps1 -Mode Fresh -Country TAR -GameDebug -Preview -CandidateDirectory 'E:/Local Repo/Runeterra-sprint-candidates/2026-11-24-RC12'`. The preview must identify RC12 alone and print `-debug -start_tag=TAR`. Remove `-Preview` for the user-run launch. Record the checksum and whether TAR reaches 1 January 990.

If startup fails, retain the timestamped crash folder and its own `dlc_load.json`, `meta.yml` and `exception.txt`. On this machine the live Azir and PT-003 descriptors share a display name. The filenames in each crash folder identify which loadout actually ran. [Release acceptance card](https://trello.com/c/qzr2g78W)

## RC12 · Interrupted Moonstone petition

As SHU, save immediately before sending the petition from **Restore the Moonstone Accord**. In a control run, send it, leave TAR and Diana in place and let TAR answer. The petition is scheduled two days after dispatch. Either answer schedules a reply to SHU one day after the choice.

Reload the pre-petition save for a disposable debug run. Send the petition, pause before the next day and use `annex TAR` as SHU to remove the recipient. Advance four days. Check `get_country_flag SHU_awaiting_moonstone_answer`, then inspect Decisions for the exile search. Record whether waiting persists and the search is hidden, as predicted by RC12's scripts. Reload the original save after the experiment. In multiplayer, also check that a TAR player who receives the petition can leave it open and still answer once. [Moonstone card](https://trello.com/c/ZGUJkU36)

## RC12 · Fate of Targon from Shurima

Start as **SHU**. Use a save with **Recover Our Sand**, **Nomadic Library**, or **Shakkal Lecture** complete. Any one opens **The Neighbours**. Finish **The Neighbours** to set the expansion policy, then check that **Fate of Targon** becomes selectable. Complete it and check for the **+100 political power** reward and `get_country_flag SHU_targon_policy_chosen`. Save here with TAR still on the map.

| From that save | What to check |
| --- | --- |
| **The Tidecaller Ashore** | SHU starts with Nami. If she is still present and Shurima has yet to pledge aid, the focus opens her first event. Acknowledge it to unlock **Restore the Moonstone Accord** while the Moonstone remains outstanding. |
| **Puppet or Ally Targon** | This should already be selectable before meeting Nami. It opens the diplomatic choice in SHU with TAR as the target. Submission dispatches an offer to TAR after 5–8 days. The alliance option has additional faction and war conditions. |
| **Demand Targon's Annexation** | Reload before selecting the diplomatic focus. The ultimatum appears in TAR. Acceptance and refusal each schedule a reply to SHU two hours later. Annexation and the diplomatic focus exclude one another. |

For the alternate entry, inspect the tree with **Fate of Crystal Scar** completed and **Fate of Targon** unfinished. Crystal Scar satisfies the annexation prerequisite on its own. **Puppet or Ally Targon** and **The Tidecaller Ashore** still require **Fate of Targon**. Keep focus-prerequisite and availability bypass cheats off for these checks. [Fate of Targon card](https://trello.com/c/U3im8CcW)

## Targon · Reform promises and the purge

Use a separate TAR save for this check after testing the defectors. These expectations apply to RC08 and RC12.

1. At **Our Origins**, take **Deny Lunari Past**. In the next event, **Allow the Lunari to remain** grants 5 percentage points of stability, up to the cap. Check `get_country_flag TAR_purge_failure` as TAR. A positive flag records this deliberate choice. The option starts no timer and dispatches no war-preparation event.
2. At **The Summit Decides**, choose Pantheon or Taric for the Reformer opening. The ensuing event offers **Support the reformers**, **Challenge the reformers** and **Maintain resistance to reform**. Continue through **One Sky, Two Lights**, **Rebuild Targon** and **Reconcile Sun and Moon**. The existing peaceful route can be played without a promise hearing.
3. To inspect the dormant hearing, make a disposable save and use `event targon.12 TAR`. Reload that save before each choice. Promising the Solari or Lunari gives the matching spirit, 10 political power and 5 percentage points of immediate stability. **Balance Both Sides** gives 10 percentage points of immediate stability. Check the chosen flag with `get_country_flag` and one of `TAR_promised_solari`, `TAR_promised_lunari` or `TAR_balanced_promises`. Reload the untouched campaign afterward. Record a console preview separately from any naturally occurring popup. [Crisis card](https://trello.com/c/GWbPBCMe)

## RC12 · Nazumah's entrenchment laws

Use an RC12-only playset. Preview fresh Nazumah from the Azir checkout with `pwsh -File tools/launch-hoi4.ps1 -Mode Fresh -Country NAZ -GameDebug -Preview -CandidateDirectory 'E:/Local Repo/Runeterra-sprint-candidates/2026-11-24-RC12'`. After the candidate check passes, remove `-Preview` to launch.

1. Save before committing to a defense charter. Keep Nazumah independent and in control of the oasis (133). On the guard route, complete **Train the Oasis Reserves** and spend 45 political power on **Enact the Oasis Defense Levy**. The national spirit should show **+15% entrenchment speed**, **+10% army defense** and **+10% supply consumption**.
2. From the earlier save, complete **Outfit the Expeditions** and spend 45 political power on **Enact the Contract Muster**. Check for **−15% entrenchment speed**, **+5% army speed** and **−10% supply consumption**.
3. Save and reload each law. With joint command inactive, use **Release the Levy Obligations** or **Buy Out the Companies** for 60 political power. The corresponding spirit and entrenchment modifier should disappear. Compare the fresh error log with RC08's two `Unknown modifier: entrenchment_speed` entries. [Release acceptance card](https://trello.com/c/qzr2g78W)

## RC11 · Xerath's armistice offers

Use an RC11-only playset and a copy of an Arcanum checkpoint. For a fresh debug run preview `pwsh -File tools/launch-hoi4.ps1 -Mode Fresh -Country XER -GameDebug -Preview -CandidateDirectory 'E:/Local Repo/Runeterra-sprint-candidates/2026-11-24-RC11'`. After selecting RC11 alone, remove `-Preview` to start.

1. Acknowledge the Shurima war opening, complete **Negotiate Frontier Charters**, provision and garrison the frontier, then take **Install Frontier Mandates**. Save while XER and SHU are independent, fighting only each other, and SHU still controls the Sun Disc (144).
2. Spend 25 political power on **Offer Shurima an Armistice**. With a second player as SHU, accept once, then reload the pre-offer save and refuse. Acceptance should end the bilateral war. Refusal should keep the war active and prevent a new offer for 90 days. A third country joining either side or SHU losing control of state 144 should block the offer.
3. From a separate bilateral XER–NAZ war checkpoint, leave Nazumah in control of its capital (133) and try **Offer Nazumah an Armistice**. Acceptance should end only this war. Refusal should impose a 120-day cooldown. Record the recipient event, answer, war status after the reply, date and any matching native parser errors. [Release acceptance card](https://trello.com/c/qzr2g78W)

## RC10 · Shurima's restored imperial administration

Use a separate RC10-only playset after finishing the current Targon test. From the Azir checkout, preview a fresh SHU debug game with `pwsh -File tools/launch-hoi4.ps1 -Mode Fresh -Country SHU -GameDebug -Preview -CandidateDirectory 'E:/Local Repo/Runeterra-sprint-candidates/2026-11-24-RC10'`. Once the preview identifies RC10 alone, run the same command without `-Preview`.

1. From an imperial-route checkpoint, finish **Codify the Imperial Restoration**. SHU must own and control the Sun Disc (144) and Vekaura (141), keep the Sun Disc militarized, end the Xerath contest, complete the royal administration and supply road, and have imperial balance above 50%. Check for **Restored Imperial Administration** in the national spirits, then save.
2. On a copy of the save, lose control of Vekaura while keeping the balance above 50%. By the next weekly update the spirit should disappear. Retake Vekaura and advance through another weekly update. The spirit should return if the other conditions still hold.
3. Reload the checkpoint and keep the supply route intact. Reduce the imperial balance to 50% or lower. The spirit should disappear on the next update and return once balance rises above 50%. Check the fresh error log for the former `Unknown trigger-type: NAND` in `common/scripted_effects/SHU_regional_effects.txt`. Record the date and actual result on the [release acceptance card](https://trello.com/c/qzr2g78W).

## RC09 · Eclipse council retest after RC08

Use RC08 for the two defector verdicts. Its native 990 startup log reported parser errors in the later Eclipse council. RC09 repairs those war options. After finishing the RC08 test, use a separate RC09-only playset and a copy of a TAR save from after the verdict and before rebuilding. Alternatively, start fresh with the RC08 steps below and substitute RC09 for the candidate number in the PowerShell commands.

1. Open **The Eclipse Decision**, take the field with Diana, and confirm TAR keeps Diana, the other government has Rahvun, and the two sides are at war. Record the two capitals, troops and leader names.
2. Reload the pre-council save and choose Rahvun. TAR should keep Rahvun and the opposing government should receive Diana. Repeat with the optional 30-day Rakkor rally to check the split. A separate reload can test adjourning and peaceful rebuilding.
3. Keep the fresh `error.log` after the RC09 session. Look for `TAR_eclipse.txt`, `Targon_events.txt` and the previous `Invalid effect 'HOME_IDEOLOGY'` and `Invalid effect 'LEADER'` diagnostics. Save during the war and verify the victory notice and rebuilding once a side wins. [Eclipse council card](https://trello.com/c/DoXMiFc3)

## RC08 · Play Targon in debug mode

Finish your RC07 session first. In the Paradox launcher, create a playset called **RC08 Targon debug** and enable only **Runeterra - Shurima and Targon Sprint RC08**. Use English and single-player with Ironman off. With HOI4 closed, double-click [Start Targon Debug.cmd](<E:/Local Repo/Runeterra-sprint-candidates/2026-11-24-RC08/Start Targon Debug.cmd>) in the RC08 folder to start as Targon.

To preview the launch yourself, run these PowerShell commands from the Azir checkout, one at a time. Continue when the preview prints both `-debug -start_tag=TAR` and `Saved playset selects 2026-11-24-RC08 only`. If it reports another selection, check the launcher playset before starting.

```powershell
$rc08 = 'E:/Local Repo/Runeterra-sprint-candidates/2026-11-24-RC08'
pwsh -File tools/launch-hoi4.ps1 -Preview -Mode Fresh -Country TAR -GameDebug -CandidateDirectory $rc08
pwsh -File tools/launch-hoi4.ps1 -Mode Fresh -Country TAR -GameDebug -CandidateDirectory $rc08
```

### Get to the defectors

1. Complete **Our Past** and **Our Origins**. Save as `TAR_RC08_Summit` before taking **The Summit Decides**. This is your return point for the other governments.
2. Choose **Diana**, take **Return of the Lunari**, then save as `TAR_RC08_Remember` before **Remember Us**. Finish the focus to meet Aphelios and Alune in **In the Shadow of the Sun** (`targon.16`). Acknowledge it and advance one day for **Diana's Call** (`targon.17`). Acknowledge that and advance one more day for **The Defectors at the Door** (`targon.18`).
3. Give the soldiers shelter and check for **+5 Army Experience**. Reload `TAR_RC08_Remember` and try exile for **+2 percentage points of stability**, up to the cap. Make a separate save after each verdict. Reload it and check that the hearing stays resolved and its reward is paid once. The verdict also has a flag you can inspect below.
4. Save as `TAR_RC08_Council` before **Rebuild Targon**. Open **The Eclipse Decision** while independent, at peace, with Diana and Rahvun present and in control of the capital and another owned core. Use separate runs to side with Diana, side with Rahvun, rally the Rakkor for 30 days, or adjourn and rebuild peacefully. On a war run check who commands each side, save during the war, then finish it and inspect the victory notice and settlements. The council is `TAR_eclipse.1` and the victory notice is `TAR_eclipse.2`.

### Try the other governments and border decisions

| Start from | What to try | What to look for |
| --- | --- | --- |
| `TAR_RC08_Summit` | Choose Rahvun. Follow **The Unclouded Sun → Remember the Summit → Rebuild Targon**. Try the Solari mandate vote. | The Sunward Charter needs the balance of power strictly below −65%. Its law is **Levy the Temple Forges** and its border decision is **Offer Pilgrim Escorts**. |
| `TAR_RC08_Summit` | Choose Leona, then the reform policy. Follow **One Sky, Two Lights** and **Aid the Moon's Faithful**. Rebuild Targon and try the Rakkor mandate vote. | **The Oath of the Ranges** needs the balance strictly between −10% and +10%. Try **Muster the Pass Companies** and **Offer Joint Pass Drills**. **Rally Rakkor Tenacity** can already be inspected after **Our Past**. |
| Diana after the verdict | Rebuild peacefully or win the Eclipse War for the Lunari. Try the sanctuary mandate vote. | **The Moonlit Compact** needs the balance strictly above +65%. Try **Fund the Hidden Observatories** and **Offer Night Shelters**. |

Each charter law lasts 180 days. While it is active, an eligible neighboring SHU, NAZ or XER at peace with TAR can receive the matching offer for 35 political power. Save before sending it and check that the same campaign cannot send a second overture. On a separate save, **Reopen the Mountain Charter** while a law is active. The law should end and the mandate votes should stay locked for 90 days.

For a 990 border test with the original frontiers, pick **Nazumah (NAZ)** or **Xerath (XER)**. Both share a land border with TAR. Shurima (SHU) can qualify after a border change. On the Rakkor route, record both countries' army experience and Targon's manpower before **Offer Joint Pass Drills**. Acceptance grants the neighbor 8 Army Experience and gives TAR 15 Army Experience at a cost of 100 manpower. Refusal spends the offer and leaves those rewards unpaid. Reload the pre-offer save for the other answer.

### Console shortcuts for a disposable test save

Open the in-game console with the key below Esc (`§` on many Swedish layouts, backtick on US layouts). Pause first. These commands are documented in the [installed game's console reference](<E:/SteamLibrary/steamapps/common/Hearts of Iron IV/documentation/console_commands_documentation.md>).

| Enter in the console | Use it for |
| --- | --- |
| `Focus.AutoComplete 1` then `Focus.AutoComplete 0` | With the game paused, turn instant completion on, select an **eligible** focus, then turn it off before advancing time. Keep normal prerequisites and checks enabled so you can spot a blocked route. Advance time normally for queued events. |
| `get_country_flag TAR_solari_defectors_sheltered` and `get_country_flag TAR_solari_defectors_exiled` | As TAR, read both flags after the hearing and after reloading. Exactly the chosen verdict should be set. |
| `tdebug` | Toggle map tooltip IDs. Hover both capitals during the Eclipse War to identify the states and countries involved. |
| `pp 100` | Add 100 political power on a test copy if you want to inspect a decision before you can afford it naturally. |
| `help event` and `event targon.18 TAR` | Inspect the command, then preview the hearing on a **throwaway copy while the prologue is underway**. Choosing an option applies its real effects. Reload before continuing. Test the actual dispatch and timing through **Remember Us**. |

If something goes wrong, keep the save just before it happened. Record **RC08**, the in-game date, focus or event ID, option, and what happened after the next day tick. Copy the current [error.log](<C:/Users/stena/Documents/Paradox Interactive/Hearts of Iron IV/logs/error.log>) before the next launch and include the relevant lines. [Remember Us playtest card](https://trello.com/c/21GIMFLp)

## Start the RC06 candidate

The registered sprint entry now selects **RC06**. For its event repair, start fresh TAR, then fresh SHU in a separate run, and advance each campaign for at least 30 days. Neither country should receive **In the Shadow of the Sun**. As TAR, choose Diana at **The Summit Decides**, then verify **Return of the Lunari** still leads to **Remember Us**. Record the build, checksum, dates and any popup on the [event repair card](https://trello.com/c/aXkbbphs).

1. In the Paradox launcher, make a separate playset containing only **Runeterra - Shurima and Targon Sprint**. Its standalone package contains the Runeterra base, Quarior integration and Azir gameplay. Keep the development playset for the original layers. For multiplayer, both players use the same candidate files, game patch and DLC selection.
2. Start at the main menu once. Record the version, displayed **modded checksum** and whether the 990 bookmark opens. The installed base checksum is 0c4f. The build manifest digest identifies the files and is a different value from HOI4's checksum.
3. For a fresh debug run, use the command below from the Azir checkout after selecting the candidate-only playset. The previews resolved TAR, SHU, XER and VOI to the corresponding starting tag. The default helper resumes an existing VOI save, so specify the country and fresh mode for each opening test.

```powershell
pwsh -File tools/launch-hoi4.ps1 -Mode Fresh -Country TAR -GameDebug
```

## First playable acceptance pass

### Remember Us in RC07

After finishing the RC06 run, select a separate playset containing only **Runeterra - Shurima and Targon Sprint RC07**. Use English for this story test. Keep a separate save slot for each build.

From the Azir checkout, preview the country and check which files the saved launcher playset selects. For RC06, substitute `2026-11-24-RC06` in the path.

```powershell
pwsh -File tools/launch-hoi4.ps1 -Preview -Mode Fresh -Country TAR -GameDebug -CandidateDirectory 'E:/Local Repo/Runeterra-sprint-candidates/2026-11-24-RC07'
```

For RC07 the preview should print `-debug -start_tag=TAR` and `Saved playset selects 2026-11-24-RC07 only`. A mismatch reports the saved selection. Once the preview passes and your previous session is closed, the same command without `-Preview` starts the test. Record the checksum from the actual game for multiplayer comparison.

1. Start fresh as TAR and complete **Our Past**, **Our Origins** and **The Summit Decides**. Choose Diana, then complete **Return of the Lunari**. Save before completing **Remember Us**.
2. Finishing **Remember Us** opens **In the Shadow of the Sun**. Acknowledge the gathering with Aphelios and Alune. Advance one day for **Diana's Call**, acknowledge Pantheon's account, then advance one more day for **The Defectors at the Door**. Neither the Eclipse council nor rebuilding should be available while the witnesses are being heard.
3. At the defector hearing, note army experience and stability. Giving shelter grants **5 army experience**. Use the earlier save to try sending the soldiers away for **2 percentage points of stability**, subject to the usual cap. Check that the leader and character roster persist through both choices.
4. Save to a new slot after the verdict and reload. The hearing should stay resolved with the chosen reward applied once. Open **The Eclipse Decision** if its usual conditions are met, or take **Rebuild Targon** to stay on the peaceful route.
5. To continue an RC06 TAR checkpoint that already completed **Remember Us**, open **Hear the Witnesses of Remember Us** in Decisions before starting rebuilding or the Eclipse War. Close any open council first and finish any active 30-day rally. The same three events should follow. A different country or political branch should receive none.

Record the route, verdict, date and modded checksum on the [Remember Us card](https://trello.com/c/21GIMFLp).

### Shared candidate checks

| Test | In-game steps | Expected result |
| --- | --- | --- |
| Targon opening | Fresh TAR. Complete **Our Past**, **Our Origins** and **The Summit Decides**. Save before choosing the leader. Test Rahvun, Leona's reform option and Diana in separate runs. | The leader portrait and politics change correctly. **The Unclouded Sun**, **One Sky, Two Lights** and **Return of the Lunari** open on their respective routes. Rakkor Tenacity follows Our Past. Story campaigns unlock at their authored focus. |
| Eclipse War | Choose Diana, finish **Return of the Lunari** and **Remember Us**. Save before **Rebuild Targon**. In Decisions open **The Eclipse Decision**. First take the field with Diana. Reload and stand with Rahvun. | The chosen faction stays under player control. The opposing government has its leader, a valid capital and troops. The sides are at war. Rebuild Targon waits for peace and the decision cannot start a second war. |
| Rakkor or peaceful branch | Reload before the council. Give the Rakkor time to answer, wait 30 days, then open the decision. Try a separate save in which you adjourn and rebuild. | The rally shifts the targeted Lunari split from 35% toward 50%. The engine may round units and states. No second rally is offered. The peaceful route still reaches rebuilding. |
| Settlement and reload | Save during an active Eclipse War. Reload, finish it, then inspect **Rebuild Targon** and the postwar focuses from each winning side. | One victory notice. A Lunari winner can choose **Reconcile Sun and Moon** or **Let the Moon Govern**. A Solari winner can pursue reconciliation or its Solari settlement. |
| Shurima and Xerath | Start fresh SHU and XER separately. Inspect diplomacy, capitals, control and troops before advancing. As SHU complete **We Remember Shurima**. | SHU and XER begin at war. The SHU domestic package resolves before the separate Southern Oasis decision on Nazumah. The latter affects Shurima's opinion of Nazumah. |
| Tribe Unity | As SHU complete **Tribal Respect → Unity of the Tribes** while NAZ exists. Note the focus completion date and save before day 100. Try declining in SHU. Reload, choose **Pursue closer ties**, then save again before the next day. As NAZ, try each response from that save. | Both countries receive **Tribal family** at focus completion. SHU receives the invitation on day 100 and gains **Seeking Closer Tribal Ties** only if it sends the offer. NAZ receives the offer on day 101. A NAZ refusal leaves that spirit on SHU and ends the exchange. Acceptance removes it and sends confirmation to SHU on day 102. Acknowledge the confirmation for +10 percentage points each of stability and war support in both surviving countries, subject to caps. |
| Moonstone | As SHU with Nami, progress through **Fate of Targon**, **The Tidecaller Ashore** and **Restore the Moonstone Accord**. Petition a peaceful TAR with Diana. Check each answer using two players or a suitable checkpoint. | Acceptance gives TAR the +40 cooperation opinion toward SHU and SHU its blessing. Refusal gives TAR the −25 modifier and allows SHU to spend 50 PP seeking the hidden Lunari; after 30 days the exile route grants the Moonstone. Inspect both event windows and the fresh error log. |
| Icathia | Fresh VOI. Save before the Resistance/Embrace decision. Run each side. On the Resistance route check **Contact Zilean**, **Open University** and **Restoration of Icathia**. | Both rebel reservations survive campaign creation. An eligible living Zilean transfers from an extinct holder; a dead Zilean stays unavailable. Restoration transfers extinct ICA's claims, cores and characters. A surviving ICA retains its holdings. |
| Multiplayer | From the same candidate-only setup, compare the main-menu checksums. Play SHU/NAZ through the invitation and response, or SHU/TAR through the Moonstone petition. Save after dispatch, reload together, and advance through delivery. | Both players see the right event and relationship once. Record date reached, any out-of-sync warning, and whether both clients can continue after reload. |

Record the candidate name, modded checksum, start country, route, date and observed result on the [release acceptance card](https://trello.com/c/qzr2g78W). For a failure, keep the pre-event save and the fresh `Documents/Paradox Interactive/Hearts of Iron IV/logs/error.log` before another launch replaces it.
