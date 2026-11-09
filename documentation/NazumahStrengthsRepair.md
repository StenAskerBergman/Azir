# Nazumah Utilize Our Strengths repair

Date: 7 October 2026

## Production path traced

`common/national_focus/nazumah_focus.txt` defines `NAZ_utilize_our_strengths`. Its two prerequisites, `NAZ_strengthen_the_hunters` and `NAZ_universal_conscription`, are mutually exclusive sibling focuses following `NAZ_warrior_tradition`. Requiring both made the focus unreachable. The completion reward selected inherited benefits by `original_tag`; its fighting branch listed AFA, TIG and SID but omitted NAZ. `common/ideas/nazumah_ideas.txt` defines `NAZ_our_strength_fighting_idea` as allowed for original tag NAZ and gives `army_attack_factor = 0.1` and `army_defence_factor = 0.05`.

## Repair

Changed only the `NAZ_utilize_our_strengths` block in `common/national_focus/nazumah_focus.txt`:

- Combined the two recruitment prerequisites into a single `OR` prerequisite, allowing either route.
- Added `original_tag = NAZ` to the existing fighting-idea branch. Existing AFA/TIG/SID fighting, ORO/GBA/BEG production, and HAR/QEM research conditions and rewards remain intact.

Focus ID, icon, layout, cost, and all other focus definitions were preserved. No localization, idea definition, or shared planner/lore-writer files were edited by this repair.

## Verification

- `python -B tools/validate_hoi4_mod.py`: PASS (`focus rewards, layout references, and English localization are consistent`).
- `git diff --check`: PASS.
- Focused assertions: PASS. Confirmed the OR alternative, NAZ fighting-idea grant, the inherited reward branches and their original tags, and the existing NAZ idea modifiers/eligibility.
- Reviewed the source diff: only the owned focus block changed in the focus file. Other pre-existing dirty/staged lore work was preserved.

## Evidence limits

These are source/static checks. No native HOI4 parser/startup, focus progression, reward execution, gameplay, or multiplayer test was performed; those remain unverified.

## Ownership release

The bounded `NAZ_utilize_our_strengths` source repair and receipt are complete. Exclusive edit ownership of that focus block is released. No shared Planner, localization, coverage file, staging, commit, push, or publication action was taken.
