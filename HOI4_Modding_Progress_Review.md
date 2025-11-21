# Hearts of Iron IV: Runeterra Mod - Progress Review Document

**Mod Name:** Azir (Runeterra - Shurima)  
**Document Date:** Current Progress Review  
**Purpose:** Comprehensive review of all HOI4 modding work completed to date

---

## Executive Summary

This document consolidates all major HOI4-related material from past work, including focus trees, lore logic, design rules, GFX setup, and faction-specific mechanics. The mod represents a substantial conversion of League of Legends' Runeterra universe into Hearts of Iron IV, with particular focus on the Shuriman region and its complex political dynamics.

**Note:** This document serves as the primary reference for all HOI4 modding work. For official HOI4 scripting documentation, refer to the `documentation` folder in the Hearts of Iron IV installation directory.

---

## 0. Official HOI4 Modding Documentation Reference

### 0.1 Documentation Location

The official Hearts of Iron IV modding documentation is located in the **`documentation`** folder at the root of the Hearts of Iron IV installation directory.

### 0.2 Available Documentation Files

All documentation files are available in both **Markdown (.md)** and **HTML (.html)** formats:

1. **`script_concept_documentation.md/html`** - Script concepts:
   - Bindable localization
   - Collections
   - Contextual localization
   - Formatted localization
   - Script constants

2. **`effects_documentation.md/html`** - Effects reference:
   - Effects for different scopes (CHARACTER, COUNTRY, STATE, etc.)
   - How to modify game state through scripts
   - 8,500+ lines of documentation

3. **`triggers_documentation.md/html`** - Triggers reference:
   - Triggers for different scopes
   - Conditions you can check in scripts
   - 7,400+ lines of documentation

4. **`modifiers_documentation.md/html`** - Modifiers reference:
   - All available modifiers by scope
   - How to apply stat changes
   - 5,000+ lines of documentation

5. **`console_commands_documentation.md/html`** - Console commands

6. **`dynamic_variables_documentation.md/html`** - Dynamic variables

7. **`loc_formatter_documentation.md/html`** - Localization formatters

8. **`loc_objects_documentation.md/html`** - Localization objects

9. **`script_collection_input.md/html`** - Collection input operations

10. **`script_collection_operator.md/html`** - Collection operators

**These are the official modding references for Hearts of Iron IV and should be consulted for all scripting questions.**

---

## 1. Focus Tree Content

### 1.1 Nazumah Focus Tree (`nazumah_focus.txt`)

**Status:** Substantially Complete  
**File Location:** `common/national_focus/nazumah_focus.txt`  
**Total Focuses:** 100+ focuses across multiple branches

#### Core Themes:
- **National Identity & Pride:** Focuses on hunter culture, warrior traditions, and national pride
- **Military Development:** Warrior guild improvements, armed forces foundation, hunter-based militarization
- **Economic Infrastructure:** Capital development, banking, regional development funds, industrial expansion
- **Diplomatic Paths:** Friend/Foe system with Shurima, alliance options with Azir/Sivir, or independence path
- **"We Are the Hunters Now":** Predatory readiness and confrontation with demi-gods (Azir, Nasus, Renekton)

#### General Unscripted Events (Happenings):

**Our Path! or Theirs Path?**
- Picking out a place for Nazumah's future
- Decision point for national direction

**Together or On Our Own?**
- Picking allies or foes for Nazumah's future
- Determines diplomatic alignment

#### Path Options:

**Various Independent Options:**
- Full independence paths
- Territorial expansion
- National pride and self-determination

**Obedience/Puppet Options:**
- Subject nation paths (akin to Manchuria)
- Integration with overlord's systems
- Conditional focuses based on subject status

#### Key Branches:

**Economic Development Path:**
- `NAZ_develop_capitalstate` → State Bank → Regional Development → Industrial Fund
- Infrastructure: Roads, railways, harbors, airports
- Resource exploitation and local crafts promotion

**Military Path:**
- `NAZ_basic_armed_forces` → `NAZ_warrior_tradition` → Specialization branches
- Hunter Warriors division templates
- Options: Strengthen Hunters vs Universal Conscription
- Military cooperation and doctrine development

**Diplomatic Path:**
- `NAZ_Friend_or_Foe` → Three paths:
  - **Friend of Shurima:** Recognize Azir's/Sivir's sovereignty → Imperial/Republican Alliance
  - **Foe of Shurima:** Declare Independence → Fortify Borders → National Pride → War Preparations
  - **Common Cause:** Economic Alliance path

**Expansion Paths:**
- `NAZ_that_which_is_rightfully_ours` → Multiple territorial claims
- Lowlands, Highlands, Shakkal regions
- `NAZ_crowning_of_the_hunter` → `NAZ_proclaim_Kingdom_of_Nazumah`

**Subject/Independent Paths:**
- Subject path: Royal Subject → Capital Railroad → Invite Foreign Settlers
- Independent path: Political Equals → Country Leader/Securing Future → Military Cooperation

#### Notable Features:
- Conditional paths based on subject status
- Mutually exclusive focus options for strategic choices
- Integration with Shurima's political system via opinion modifiers
- Big Game focus for anti-Shurima path (currently placeholder)
- Branch options emphasizing "we are the hunters now," predatory readiness, and confrontation with demi-gods like Azir, Nasus, Renekton
- Manchuria-style subject mechanics with conditional focuses

---

### 1.2 Xerath Focus Tree (`xerath_focus.txt`)

**Status:** Partially Complete - Structure Established  
**File Location:** `common/national_focus/xerath_focus.txt`  
**Total Focuses:** 30+ focuses with extensive branching planned

#### Core Themes:
- **Power Struggle:** Arrogance, magical ambition, strategic manipulation
- **Temporary Alliances:** Unstable cooperation with Renekton and Noxus
- **Conquest Paths:** Xerath's Conquest vs Renekton's Conquest (mutually exclusive)
- **Foreign Interference:** Noxian Coalition and colonial pacts
- **Story Emphasis:** Xerath seeks outside power to tilt balance against Azir

#### Key Branches:

**Opening Path:**
- `XER_temporary_alliance` → `XER_usurp_the_throne` → Branch split

**Power Play Branch:**
- `XER_power_play` → Two mutually exclusive conquest paths:
  - **Xerath's Conquest:** `XER_xerath_conquest` → Power Pact → Baccai Ritual → Remove the Savages
  - **Renekton's Conquest:** `XER_renekton_conquest` → Blood Pact → Brutal Dominance

**Path of Domination:**
- `XER_path_of_domination` → Loyal Legionaries → Brutal Slavery → Raider Relationship
- Suppress Rebellions → Ruthless Cruelty → Endless Rage

**Path of Ascension:**
- `XER_path_of_ascension` → Internal Support → Loyal Henchmen → Abolish Slavery
- Foreign Interference → Power Struggle → Collective Punishment

**Noxian Path:**
- `XER_colonial_pact` → Noxian Coalition → Colonial Investments
- Identity Fusion / Colonial Identity branches
- Noxian Suppression focus for betrayal scenarios

#### Notable Features:
- Extensive commented design notes for future implementation
- Multiple betrayal and alliance scenarios planned
- Integration with Renekton's path via mutually exclusive focuses
- Noxian coalition mechanics with potential for double-cross

#### Implementation Status:
- Basic structure complete
- Many focuses have placeholder completion rewards
- Event triggers planned but not fully implemented
- AI will_do factors set but may need balancing

---

### 1.3 Mount Targon Focus Tree (`targon_focus.txt`)

**Status:** Partially Complete - Foundation Established  
**File Location:** `common/national_focus/targon_focus.txt`  
**Total Focuses:** 20+ focuses with three major paths

#### Core Themes:
- **Rakkor Origins:** Historical foundation setting
- **Three Paths:** Reform, Purity (Solari), Rejectors (Lunari)
- **Leader Selection:** Pantheon, Leona, Rahvun, Diana, Kayle paths
- **Solari Order:** Solar militarization and order
- **Lunari Suppression vs Reconciliation:** Paths for handling Lunari
- **Pantheon's Warrior Resurgence:** Warrior-focused path
- **Cosmic Intervention:** Branches involving Bard or celestial intervention

#### Key Branches:

**Opening Sequence:**
- `TAR_our_past` → `TAR_our_origins` → `TAR_our_leader`
- Leader selection determines available paths

**Reform Path:**
- `TAR_reform` → Victory Speech → Integrate Opposition
- Reconciliation between Solari and Lunari

**Purity Path (Solari):**
- `TAR_purity` → Remember Summit → Purge Opposition
- Requires PuristPathTrue flag and Rahvun/Leona leader
- Special forces cap bonuses

**Rejectors Path (Lunari):**
- `TAR_rejectors` → Remember Us → Help Our Allies
- Requires PuristPathFalse flag
- Lunari endurance ideas

#### Notable Features:
- Conditional path availability based on leader selection
- Flag-based path locking (PuristPathTrue/False)
- Event-driven leader promotion system
- Integration with Targon events (`targon.1`, `targon.3`, `targon.20`)

#### Implementation Status:
- Basic structure complete
- Some branches commented out (Solari Priests, Protectors of Humanity)
- Event integration partially complete
- Cosmic branches planned but not implemented

---

### 1.4 Shurima Focus Tree (`shurima_focus.txt`)

**Status:** Substantially Complete  
**File Location:** `common/national_focus/shurima_focus.txt`  
**Total Focuses:** 100+ focuses

#### Core Themes:
- **Imperial Restoration:** Azir's vision of reformed Shurima
- **Leadership Choice:** Emperor (Azir) vs Empress (Sivir) paths
- **Economic Revival:** Infrastructure and Sun Disc restoration
- **Diplomatic Expansion:** Relations with Nazumah, Targon, and other factions

#### Key Branches:

**Opening Path:**
- `SHU_sundisc_has_risen` → `SHU_our_leader` → Leader choice event

**Leadership Split:**
- `SHU_emperor` (Azir) vs `SHU_empress` (Sivir) - mutually exclusive
- Both lead to `SHU_imperial_courts`

**Economic Development:**
- `SHU_economic_revival` → `SHU_sun_disc_restorations`
- State building slots and infrastructure bonuses

**Imperial Administration:**
- `SHU_imperial_courts` → `SHU_imperial_law` → `SHU_public_order`
- Stability and governance improvements

#### Notable Features:
- Extensive focus tree with multiple parallel branches
- Integration with Nazumah diplomatic system
- Event-driven leader promotion
- Shared focuses with Xerath planned (`SHU_XER_shared.txt`)

---

### 1.5 Renekton Focus Tree

**Status:** Planned - Not Yet Implemented  
**Expected Location:** `common/national_focus/renekton_focus.txt` or integrated into Xerath tree

#### Core Themes:
- **Instability & Rage:** Rage-driven mobilization, reactive violence
- **Distrust:** Trauma-driven rejection of all authority
- **Unstable Alliances:** Possible temporary cooperation with Xerath or Noxian Coalition
- **Betrayal Scenarios:** May betray Xerath mid-war due to paranoia

#### Expected Mechanics:
- **Rage-Driven Mobilization:** Military bonuses at cost of stability
- **Reactive Warfare:** Decentralized carnage, brute force tactics
- **Distorted Heroism:** Branches representing betrayal and reactive warfare
- **Temporary Cooperation:**
  - Initial cooperation with Xerath against common enemies
  - Possible Noxian Coalition alliance
  - High risk of mid-war betrayal due to paranoia

#### Scenario Possibilities:
- Renekton initially cooperates with Xerath but turns unstable
- Attacks Xerath mid-war due to paranoia and distrust
- Forms temporary truce with Noxus if it serves immediate purpose
- Fragile alliances that break once immediate goals are achieved

**Note:** Renekton's path may be implemented as a separate focus tree or as integrated branches within the Xerath focus tree, given their interconnected storylines.

---

### 1.6 Other Focus Trees

**Aurma Focus Tree:** Maritime-focused nation with naval development paths  
**Shakkal Focus Tree:** Regional Shuriman power  
**Void Focus Tree:** Icathian/Void content  
**Raider Focus Tree:** Shared raider mechanics (`raider_focus_shared.txt`)

---

## 2. Localization & Trait Index

### 2.1 Nazumah Localization

**File Location:** `localisation/english/focus_NAZ_nazumah_l_english.yml`

#### Traits:
- **Great Hunter:** Elite warrior tradition
- **Father of the Empire:** Leadership trait
- **Pride of Nazumah:** National identity trait

#### Ideas:
- **Improved Warrior Guild:** Enhanced warrior organization
- **Foundation of Armed Forces:** Military establishment

#### Localization Themes:
- Cultural identity and survival
- Elite warrior tradition
- Hunter culture and national pride

#### Ideas:
- `NAZ_improved_warrior_tradition_idea`
- `NAZ_foundation_of_armed_forces`
- `NAZ_state_bank_idea`
- `NAZ_improved_irregulars_idea`
- `NAZ_our_finest_idea`
- `NAZ_our_strength_fighting_idea` / `NAZ_our_strength_production_idea` / `NAZ_our_strength_research_idea`
- `NAZ_rallying_the_people_idea`
- `NAZ_jagged_alliance_idea`
- `NAZ_volunteers_idea`
- `NAZ_rightfully_ours_idea`
- `NAZ_education_idea`

### 2.2 Shurima Localization

**File Locations:**
- `localisation/english/focus_SHU_shurima_l_english.yml`
- `localisation/english/SHU_countries_l_english.yml`
- `localisation/english/SHU_parties_l_english.yml`

#### Key Localization:
- **Fate of the Crystal Scar:** Major narrative focus
- Supporting localization lines for SHU-specific focuses and events
- Additional narrative ties to Shurima's rise and ancient memory
- Extensive country name variations by ideology
- Party system with multiple subfactions:
  - Solari, Lunari, Noxian Trifarix, Chem Barons, Ascended Council, Hunters, Raiders, etc.
- Dynamic faction naming system

### 2.3 Shared Localization

**File Location:** `localisation/english/focus_SHU_XER_l_english.yml`

Shared focuses between Shurima and Xerath paths.

---

## 3. Icon & GFX Definitions

### 3.1 Standard SpriteType Pattern

**Location:** `interface/focus-*_customicons.gfx` files

#### Standard Icon Definition:
```hoi4
SpriteType = { 
    name = "GFX_focus_[FACTION]_[FOCUS_NAME]"
    texturefile = "gfx/interface/goals/[FACTION]/[ICON_FILE].dds"
}
```

#### Shine Variant Pattern:
```hoi4
SpriteType = {
    name = "GFX_focus_[FACTION]_[FOCUS_NAME]_shine"
    texturefile = "gfx/interface/goals/[FACTION]/[ICON_FILE].dds"
    effectFile = "gfx/FX/buttonstate.lua"
    animation = {
        animationmaskfile = "gfx/interface/goals/[FACTION]/[ICON_FILE].dds"
        animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
        animationrotation = -90.0
        animationlooping = no
        animationtime = 0.75
        animationdelay = 0
        animationblendmode = "add"
        animationtype = "scrolling"
        animationrotationoffset = { x = 0.0 y = 0.0 }
        animationtexturescale = { x = 1.0 y = 1.0 }
    }
    # Second animation with rotation = 90.0
    legacy_lazy_load = no
}
```

### 3.2 Icon Files by Faction

**Nazumah Icons:** `interface/focus-NAZ_customicons.gfx`
- `GFX_focus_NAZ_Big_Game`
- `GFX_focus_NAZ_national_pride`
- `GFX_focus_NAZ_tribal_traditions`
- `GFX_focus_NAZ_invite_nearby_settlers`
- `GFX_focus_NAZ_City_On_Water`
- `NAZ_Big_Game_Big_Guns`

**Shurima Icons:** `interface/focus-SHU_customicons.gfx`
- `GFX_focus_SHU_we_remember_shurima`
- `GFX_focus_deep_pockets` (with shine variant)
- Multiple generic and custom icons

**Xerath Icons:** `interface/focus-XER_customicons.gfx`
- Custom Xerath-specific focus icons

**Targon Icons:** `interface/focus-TAR_customicons.gfx`
- Targon-specific focus icons

**Aurma Icons:** `interface/focus-AUR_customicons.gfx`
- Maritime and naval-themed icons

**Generic Icons:** `interface/focus-generic_customicons.gfx`
- Reusable generic focus icons
- `interface/focus-generic_customicons_with_shine.gfx` for shine variants

### 3.3 Icon Organization

Icons are organized by faction in:
- `gfx/interface/goals/[FACTION]/` directories
- Standardized naming: `GFX_focus_[FACTION]_[NAME].dds`
- Shine variants use same texturefile with animation overlay

### 3.4 Example Icons

**Notable Icon References:**
- `SHU_fate_of_crystal_scar` - Major Shurima narrative focus icon
- `NAZ_pact_of_shurima` - Generic reference icon (reusable across contexts)

---

## 4. Lore Logic & Faction Differences

### 4.1 Shurima Politics

#### Core Tensions:
1. **Slavery:** 
   - Azir: Reformed vision, opposes slavery
   - Xerath: Pragmatic tool, uses when useful
   - Renekton: Doesn't care, focused on warfare

2. **Divine Authority:**
   - Azir: Legitimate imperial order, structured state
   - Xerath: Power for its own sake, manipulation
   - Renekton: Rejects all authority, trauma-driven

3. **Supply Chains:**
   - Azir: Organized imperial supply systems
   - Xerath: Arcane-powered logistics
   - Renekton: Decentralized, survival-based

4. **Ancient Hierarchy:**
   - Azir: Restores and respects ancient order
   - Xerath: Subverts for personal power
   - Renekton: Destroys hierarchy through violence

### 4.2 Warfare Philosophies

**Azir:**
- Organized imperial armies
- Structured military doctrine
- Emphasis on discipline and order

**Xerath:**
- Arcane devastation
- Shock warfare with magical weapons
- Cunning over brute force

**Renekton:**
- Brute force and rage
- Decentralized carnage
- Reactive, trauma-driven tactics
- Reactive violence driven by trauma
- Distrust of all authority
- Instability and rage-driven mobilization

### 4.3 Noxus Relations

**Noxian Philosophy:**
- Accepts slavery if useful; rejects if inefficient
- Values strength, conquest, useful alliances
- Might ally with Xerath for opportunity but watches closely
- Tolerates raiders as long as they serve state goals
- Incorporates raiders into legions if they prove strength

**Noxian-Xerath Dynamics:**
- Temporary alliance possible
- Xerath plans eventual betrayal
- Noxus aware of Xerath's untrustworthiness
- Colonial investments and pacts

**Noxian-Raider Relations:**
- Integration vs suppression options
- Raiders can become regular army units
- Strength-based meritocracy

---

## 5. Scenario Possibilities

### 5.1 Xerath-Noxus Alliance

**Setup:**
- Xerath forms temporary alliance with Noxus
- Gains leverage against Azir
- Plans eventual betrayal

**Mechanics:**
- `XER_foreign_interference` → `XER_noxian_coalition` → `XER_colonial_investments`
- `XER_noxian_suppression` for betrayal scenario
- Colonial identity vs Shuriman identity conflict

### 5.2 Renekton-Xerath Cooperation

**Setup:**
- Initial cooperation against common enemies (defeating Nasus, reclaiming Shurima)
- Unstable alliance with constant power struggles
- Renekton may betray mid-war due to paranoia
- Possible temporary cooperation with Noxian Coalition

**Mechanics:**
- `XER_temporary_alliance` → `XER_power_play`
- Mutually exclusive conquest paths
- Blood Pact vs Power Pact branches
- Betrayal events planned
- Mid-war betrayal scenario: Renekton turns on Xerath due to paranoia

**Renekton's Perspective:**
- Rage-driven mobilization
- Unstable alliances that serve immediate purpose
- Fragile truces that break once goals are achieved
- Reactive warfare and distorted heroism

### 5.3 Nazumah Third Power

**Setup:**
- Nazumah rises as independent power
- Exploits chaos between Shurima factions
- Can align with Azir, oppose Shurima, or remain neutral

**Mechanics:**
- `NAZ_Friend_or_Foe` decision point
- Multiple alliance paths
- Independence declaration option
- Territorial expansion focuses

### 5.4 Targon Intervention

**Setup:**
- Solari or Lunari disputes
- Pantheon's warrior resurgence
- Cosmic branches involving Bard or celestial intervention

**Mechanics:**
- `TAR_our_leader` determines intervention type
- Reform path for reconciliation
- Purity path for Solari dominance
- Rejectors path for Lunari return

### 5.5 Multi-Faction Dynamic

**League-Style Conflict:**
- Azir rebuilds Shurima with reformed vision
- Xerath schemes for power, seeks outside leverage
- Renekton destabilizes through reactive violence and rage
- Noxus opportunistically invades, watches for opportunities
- Nazumah rises as third power exploiting chaos
- Targon intervenes in Shurima's crisis via Solari or Lunari disputes

**Complex Interactions:**
- Multiple temporary alliances
- Betrayal scenarios (Xerath-Noxus, Renekton-Xerath)
- Power struggles between all factions
- Regional conflicts with shifting allegiances
- Renekton's instability causing mid-war betrayals
- Nazumah's diplomatic navigation between major powers

---

## 6. Export & Technical Notes

### 6.1 3D Asset Export Workflow

**Location:** `NOTES and USEFUL CODE LINES.txt`

#### Azir Soldier Export Process:
1. **Blender Import:**
   - Import `.glb` file
   - Material assignment before PDX Mesh export
   - Quaternion view mode required before export

2. **Material Workflow:**
   - Using SUVA material workflow
   - Material assignment critical before export

3. **File Structure:**
```
/gfx/entities/
  - [TAG].gfx
  - [TAG].asset

/gfx/models/units/
  - [TAG]_infantry.mesh
  - [TAG]_infantry_diffuse.dds
  - [TAG]_infantry_normal.dds
  - [TAG]_infantry_spec.dds
```

### 6.2 Code Patterns

**Multi-Nation Triggers:**
```hoi4
every_country = {
    limit = {
        # CONDITIONS
        has_war = yes
        is_subject = no
        OR = {
            tag = GER
            tag = HUN
            tag = ROM
        }
    }
    # EFFECTS
    country_event = XXX
}
```

---

## 7. Speeches & Flavor Text

### 7.1 Shurima Rise Speeches

**Content:**
- Japanese versions calling for unity against invaders
- English poetic versions spoken as Azir
- Lines include calls for Rammus
- Declarations against false prophets
- Shouts for reclaiming Shurima's destiny
- Unity against external threats
- Imperial restoration themes

**Themes:**
- Imperial restoration
- Ancient memory
- Unity against external threats
- Reclaiming Shurima's glory

### 7.2 Flavor Text Integration

- Event descriptions
- Focus descriptions
- Trait tooltips
- Decision descriptions
- Localization for all major factions

---

## 8. Implementation Status Summary

### 8.1 Complete Systems

✅ **Nazumah Focus Tree:** Substantially complete with 100+ focuses  
✅ **Shurima Focus Tree:** Complete with extensive branching  
✅ **GFX Icon System:** Standardized pattern established  
✅ **Localization Framework:** Extensive coverage for major factions  
✅ **Lore Foundation:** Comprehensive political and military logic documented  

### 8.2 Partially Complete

⚠️ **Xerath Focus Tree:** Structure complete, many focuses need completion rewards  
⚠️ **Targon Focus Tree:** Foundation established, some branches commented out  
⚠️ **Event Integration:** Events planned but not fully implemented  
⚠️ **Shared Focuses:** `SHU_XER_shared.txt` exists but needs expansion  

### 8.3 Planned/Incomplete

❌ **Renekton Focus Tree:** Designed but not yet implemented (may be integrated into Xerath tree)  
❌ **Cosmic/Celestial Branches:** Planned for Targon (Bard, celestial intervention) but not implemented  
❌ **Betrayal Event Chains:** Designed but not scripted (Renekton-Xerath, Xerath-Noxus)  
❌ **Noxian Focus Tree:** Referenced but not created  
❌ **Full Event Integration:** Many focuses reference events that need creation  
❌ **General Unscripted Events:** Nazumah "Happenings" (Our Path/Theirs Path, Together/On Our Own) need implementation  
❌ **Pantheon Warrior Path:** Mentioned for Targon but not fully implemented  
❌ **Kayle Path:** Referenced for Targon but not implemented  

---

## 9. Technical Architecture

### 9.1 File Organization

**Focus Trees:**
- `common/national_focus/[faction]_focus.txt`

**Localization:**
- `localisation/english/focus_[TAG]_[faction]_l_english.yml`
- `localisation/english/events_[TAG]_[faction]_l_english.yml`
- `localisation/english/SHU_countries_l_english.yml`
- `localisation/english/SHU_parties_l_english.yml`

**GFX Icons:**
- `interface/focus-[TAG]_customicons.gfx`
- `gfx/interface/goals/[TAG]/[icon].dds`

**Events:**
- `events/[Faction]_events.txt`

**Ideas:**
- `common/ideas/[faction]_ideas.txt`

**Characters:**
- `common/characters/[TAG]_characters.txt`

**Traits:**
- `common/country_leader/[Faction]_Traits.txt`

### 9.2 Code Standards

**Focus Naming:**
- `[TAG]_[focus_name]` (e.g., `NAZ_national_pride`)

**Icon Naming:**
- `GFX_focus_[TAG]_[focus_name]` or `GFX_[TAG]_[focus_name]`

**Event Naming:**
- `[faction].[number]` (e.g., `shurima.1`, `xerath.2`)

**Idea Naming:**
- `[TAG]_[idea_name]_idea`

---

## 10. Recommendations for Next Steps

### 10.1 Priority 1: Complete Core Systems

1. **Complete Xerath Focus Tree:**
   - Fill in placeholder completion rewards
   - Implement event triggers
   - Balance AI will_do factors

2. **Implement Event Chains:**
   - Create events referenced in focuses
   - Betrayal scenarios
   - Alliance formation events

3. **Renekton Focus Tree:**
   - Create separate focus tree or integrate into Xerath tree
   - Implement rage-driven mechanics
   - Betrayal scenarios

### 10.2 Priority 2: Expand Content

1. **Shared Focuses:**
   - Expand `SHU_XER_shared.txt`
   - Create shared focuses for other faction pairs

2. **Targon Branches:**
   - Implement commented-out branches
   - Cosmic intervention paths
   - Pantheon warrior path

3. **Noxian Content:**
   - Create Noxian focus tree
   - Implement raider integration mechanics
   - Colonial management system

### 10.3 Priority 3: Polish & Balance

1. **Localization:**
   - Complete all focus descriptions
   - Add flavor text for events
   - Tooltip descriptions

2. **GFX:**
   - Create missing icons
   - Add shine variants where appropriate
   - Ensure consistency

3. **Balance:**
   - Test focus tree paths
   - Balance AI decision-making
   - Balance rewards

---

## 11. Summary of Entire Content

This unified document covers:

- ✅ **All major focus-tree material:** Nazumah, Xerath, Renekton (planned), Targon
- ✅ **All known localization and traits:** Nazumah, Shurima, and shared localization
- ✅ **All SpriteType/GFX formatting standards:** Standard patterns with shine variants
- ✅ **All lore foundations:** Political, military, and narrative design for Shurima's conflicts
- ✅ **All scenario logic:** Multi-faction dynamics, betrayals, alliances
- ✅ **All asset-export technical notes:** 3D model workflow and code patterns
- ✅ **All Shurima Rise speeches and flavor writing:** Japanese and English versions

**Everything relevant to HOI4 Runeterra modding is contained in this document.**

---

## 12. Conclusion

This mod represents a substantial conversion of League of Legends' Runeterra universe into Hearts of Iron IV, with particular depth in the Shuriman region. The work demonstrates:

- **Comprehensive Focus Tree Design:** Multiple factions with extensive branching paths
- **Rich Lore Integration:** Political, military, and cultural differences well-documented
- **Technical Competence:** Proper GFX setup, localization framework, code organization
- **Ambitious Scope:** Complex multi-faction dynamics with betrayal and alliance scenarios

**Current State:** The mod has a solid foundation with Nazumah and Shurima focus trees substantially complete. Xerath and Targon trees have good structure but need completion. The lore foundation is excellent and provides clear direction for future implementation.

**Next Phase:** Focus on completing Xerath tree, implementing event chains, creating Renekton content, and adding general unscripted events (Nazumah "Happenings") to realize the full vision of Shurima's complex political landscape.

**Document Status:** This document serves as the primary reference for all HOI4 modding work. It consolidates all major material and should be updated as new content is implemented.

---

**Document End**

