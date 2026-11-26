# Hextech Excavator Works and Tikras

The Hextech Excavator Works use the existing Bramble Crawler line battalion. Each battalion needs 12 rigs. The research focus and River Pilt trials remain the route into Piltover production.

Riot's *Fit to Rule* supplies the skirmish, captured rig, Mara's prefecture, Qiyana leaving the path exposed, and the reprisal. The commander can follow that sequence or change its outcome. Kumungu stands in for Tikras when applying infrastructure damage. The chain keeps Ixtal's existing roster and government. [Fit to Rule](https://therune.lol/lore/stories/qiyana-color-story/)

## Owner playtest

1. Start fresh as PLT. Complete **Design the Bramble Crawler**, then research **Bramble Crawler Engineering** under Support Research. Produce twelve rigs or complete the River Pilt trials.
2. At peace, with both Kumungu states under Ixtal's control, open **Decisions → Hextech Excavator Works → Send the Bramble Crawlers into Kumungu**. The dispatch uses 20 PP and one rig. Reload at the tree line to compare reprisal with withdrawal. Check that the original illustration displays, the reprisal damages infrastructure, and Ixtal gets a response.
3. At war, take Kumungu or Kumungu Coast with a crawler division above 75% strength present. Check the automatic report. On a separate save, bring in a crawler after taking the state with ordinary infantry and use **Hear the Kumungu Field Report**. Try both states separately. The party takes two days to reach the path and one more to reach the tree line. Save during the wait and pull the crawler out or lose control of the operation's state. The later scene should allow withdrawal only. The bypass awards five Army XP. The reprisal damages infrastructure in the state where the operation began.
4. As ZAU, secure the researched designs and take ownership and control of the Academy (51). Choose **Reopen the Captured Excavator Works**. Check the production line, the green **River Pilt Reclamation Column** and Zaun-specific dispatches. Repeat before the design exists to check that the transfer stays unavailable.
5. With 3D units enabled, check both liveries, facing and scale, chassis motion, exhaust and track dust. In combat, look for the head to dip and rise and the toothed drum to spin with wood splinters coming off the front. Stop the formation and check that the drum, treads and emitters stop. Check a manually designed template in each country as well as the supplied template. Repeat the war and transfer checks through save and reload and in multiplayer.

## Verification

The wartime entry checks for a crawler battalion in the template, presence of that division and overall strength above 75%. The engine trigger measures divisional strength. It cannot report how many individual crawlers are running. The redrawn meshes use a closed armored cockpit, twin sloping housings, exposed hydraulic rams and a rotary drum with seven staggered rows of teeth. Piltover has bronze armor and blue glazing. Zaun has green armor, jade glazing, a copper return hose and a riveted patch above the left track. Each 35-joint rig has chassis, cutter head and drum joints and 32 paired tread joints. The drum spins during the clearance animation. The treads stop in idle. Native motion and map scale remain owner verification.

## Runtime assets

The checkout ignores the gfx directory. Package the bound files below with the corresponding gameplay and interface scripts. The local campaign uses the supplied Riot illustration.

- Mesh and entity registrations — **gfx/entities/PIL_bramble_crawler.gfx**, **PIL_bramble_crawler.asset**, and **PIL_bramble_particles.gfx**.
- Meshes, finishes and clips — **gfx/models/units/pil_bramble_crawler/**. The registrations point to **bramble_crawler_animated.mesh** and **bramble_crawler_zaun.mesh**, their **finish** textures, their shared normal and specular maps, and the **idle**, **move** and **work** clips and animation registration. **tools/animate_bramble_crawler.py** builds the meshes, finishes and clips.
- Blade particles — **gfx/particles/azir_crawler_blade.asset** and **azir_crawler_wood_chip.dds**. Track dust and exhaust reference base-game particle files.
- HUD and event sprites — **gfx/interface/decisions/PIL_hextech_excavator.dds**, **gfx/interface/equipmentdesigner/PIL_hextech_excavator.dds**, and **gfx/event_pictures/PIL_ZAU/PIL_tikras_jungle.dds** and **ZAU_excavator_works.dds**. Include the existing crawler focus, unit and trials sprites in **interface/PIL_bramble_crawler.gfx**.
