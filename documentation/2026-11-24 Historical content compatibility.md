# Historical content compatibility, 24 November 2026

The baseline used HOI4 1.20.0.0.8873, Runeterra, Quarior and local Azir with the Icathian 990 save. It includes cold startup and an in-session database reload. Counts below are occurrences in that log.

## Source verification

The 357 consumer files listed by the focus errors contain no executable checks for the historical focus IDs named against them. The 9,568 original missing-focus errors each had a matching validation failure. The overrides keep historical conditions false in their original scopes, including negated conditions. They retain the other definitions in each file.

HOI4 loads these as whole files. When upgrading HOI4, DLC, Runeterra or Quarior, compare the installed source against the SHA-256 below and carry the scoped edits onto the updated source. The French scripted localization file accounts for about 20 MB of the overrides.

Additional repairs cover the infantry mesh and weapon dependencies, portrait pools, two GUI sprites, one font, manufacturer traits, two nonrandom leader ideologies and inherited flag fallbacks. The active mod’s empty uppercase tank folder was renamed locally.

## Native check

With HOI4 closed, run `pwsh -File tools/launch-hoi4.ps1 -Mode Save -Country VOI -Save VOI_990_01_01_12.hoi4`. Resume Icathia and open its focus tree. Compare the new error.log against the signatures above. Inspect mod-specific errors and any new errors separately. The original log includes warnings from the save as well as database reloads.

## Inherited script overrides

The source digest identifies the installed input used for future comparisons. The last column counts the original invalid-focus messages associated with that path. Other repairs can share a file.

| Override | Source | Source SHA-256 | Focus messages |
| --- | --- | --- | ---: |
| [common/abilities/CHI_abilities.txt](<../common/abilities/CHI_abilities.txt>) | HOI4 | `528011a9799420a2c754f4ce46c4659336999c0e4ed2ff9f374e7563b599a976` | 5 |
| [common/abilities/JAP_abilities.txt](<../common/abilities/JAP_abilities.txt>) | HOI4 | `fa59783fc6f6d86f211765506a70f8d8d1d62e3e16c091569ec47c0bbcca0fcc` | 5 |
| [common/abilities/PHI_abilities.txt](<../common/abilities/PHI_abilities.txt>) | HOI4 | `c12b282b110b2e0189a79d2ab5a6e5835b8c5ef47c236a13aad5f76fb0649f27` | 1 |
| [common/abilities/SWE_abilities.txt](<../common/abilities/SWE_abilities.txt>) | HOI4 | `990834c2cc0f86afa331a9ea8cccdac02ab54f0ac7b367f02bebb1e43419e560` | 1 |
| [common/abilities/generic_leader_abilities.txt](<../common/abilities/generic_leader_abilities.txt>) | HOI4 | `7da51338083808ee1a84d4b1e57c1929470bdbf583003bd085e99a0a2b0e9028` | 12 |
| [common/achievements.txt](<../common/achievements.txt>) | HOI4 | `a8a9155db011ff2a7f9cb7ae98d4aed12b01b4e5307c5f0d3751692425cf9a34` | 57 |
| [common/ai_equipment/FRA_tank.txt](<../common/ai_equipment/FRA_tank.txt>) | HOI4 | `ebfd9db73fd3ac9a3ff57c2881660628ffefb62bd7b59f16766452e39c25ed9f` | 1 |
| [common/ai_templates/generic.txt](<../common/ai_templates/generic.txt>) | HOI4 | `bb40be1918b9a8e595593b98816e384beaeb58843b8784d468fb2dae8e606253` | 1 |
| [common/ai_templates/templates_GER.txt](<../common/ai_templates/templates_GER.txt>) | HOI4 | `4e77e58d517266db77b436f3c6a7188105f1a887ea9901c2f8b1a1b51a06cfb0` | 1 |
| [common/ai_templates/templates_ITA.txt](<../common/ai_templates/templates_ITA.txt>) | HOI4 | `333ff392718e0a81a11df2cb730a54560749d7b9e0a64f515e0d97c49397d255` | 1 |
| [common/autonomous_states/colony.txt](<../common/autonomous_states/colony.txt>) | Quarior | `81dbe406f9bee9ee6a53b144754d4c76a9b7b4981b9d4310e0359b06143ff26c` | 1 |
| [common/autonomous_states/dominion.txt](<../common/autonomous_states/dominion.txt>) | HOI4 | `e55f4033c1bbd536538fb95be6ac0a4f3da12e78c74094a2e1b355e8fd1192e3` | 25 |
| [common/autonomous_states/integrated_puppet.txt](<../common/autonomous_states/integrated_puppet.txt>) | Quarior | `347f508c4d8529125fffd12276a5b9822991498b668c8de9b38eb6d35b264e66` | 2 |
| [common/autonomous_states/reichskommissariat.txt](<../common/autonomous_states/reichskommissariat.txt>) | Quarior | `a61d2464229d87fe2d26fa92b9e07d1e08cdfe423625289b05acfca98eae15ca` | 1 |
| [common/autonomous_states/satellite.txt](<../common/autonomous_states/satellite.txt>) | HOI4 | `58241f60a38e331ec6df666001fc9b5dee2dad49105d69d6f718e61936e71cd8` | 3 |
| [common/autonomous_states/taog_associated_dominion_puppet.txt](<../common/autonomous_states/taog_associated_dominion_puppet.txt>) | HOI4 | `edf3103b77414c425a07c0da3fc372183e887ab032876f821fbecfffdea9d25b` | 2 |
| [common/autonomous_states/wtt_imperial_associate.txt](<../common/autonomous_states/wtt_imperial_associate.txt>) | Quarior | `80e69bfea6647cecf58e4f6ef3d213b18ff8d623467fab7fd02b08efb5bb6d04` | 3 |
| [common/autonomous_states/wtt_imperial_protectorate.txt](<../common/autonomous_states/wtt_imperial_protectorate.txt>) | Quarior | `472bb0f2a2537a94a4830dacd1cef93aaf9adafad70263ab3ab6311a78d614ff` | 2 |
| [common/autonomous_states/wtt_imperial_subject.txt](<../common/autonomous_states/wtt_imperial_subject.txt>) | HOI4 | `07e92e74b0c93555fb6661f50550cdb9f7e206e0779e2c97c087e924a946c942` | 2 |
| [common/autonomous_states/wuw_austro_hungarian_subject.txt](<../common/autonomous_states/wuw_austro_hungarian_subject.txt>) | HOI4 | `c9476290decd8b38acf923d93f475a550e893d63a6ee856961c10f197b118012` | 3 |
| [common/autonomous_states/wuw_european_union_puppet.txt](<../common/autonomous_states/wuw_european_union_puppet.txt>) | HOI4 | `5cc07a65e38bea1cdb5e330e6540c8370955e572f3becbc4fe35561f5c3934e7` | 4 |
| [common/autonomous_states/wuw_volkskommissariat.txt](<../common/autonomous_states/wuw_volkskommissariat.txt>) | Quarior | `d085377ee26d67614e45fcdff8311d3471aa5482e1e6e335475396c15cb08334` | 1 |
| [common/bop/ITA.txt](<../common/bop/ITA.txt>) | HOI4 | `a9ac9ceaa37f6d26d1b4ff0e439c676a1681d6d104a98160ee690b55a1179234` | 7 |
| [common/characters/AFG.txt](<../common/characters/AFG.txt>) | HOI4 | `06cedeec7e712ef8c5a75709dd5edf68b41c5e2a05c73109b65727fe929cb054` | 40 |
| [common/characters/ARG.txt](<../common/characters/ARG.txt>) | HOI4 | `21a8a61768c8578f97bcf51448ae87619f708960e0de0b6baf0794f0be42574f` | 5 |
| [common/characters/AST.txt](<../common/characters/AST.txt>) | HOI4 | `b13a3885de962f198cff728f9e5f7f16c960936841f6949c6b243c8cda8f0346` | 50 |
| [common/characters/AUS.txt](<../common/characters/AUS.txt>) | HOI4 | `de46a87db9ec25196a80c1d20175ea3fcdaeb2086dc0d17bd8be900ac26aa19f` | 67 |
| [common/characters/BEL.txt](<../common/characters/BEL.txt>) | HOI4 | `ecbda6cd204d0a9227c2cfc83b64b078760247ef7585aec394a98eb825ba5867` | 15 |
| [common/characters/BRA.txt](<../common/characters/BRA.txt>) | HOI4 | `b4712f7917f38138f3b5ccf38042b5f5074a8109594ad55f6b325fa1f5079cf8` | 14 |
| [common/characters/BUL.txt](<../common/characters/BUL.txt>) | HOI4 | `d35126665e1d080783751e8fd98f98c4ccfdbd7b53c404922f9b7cd0fc82cc6f` | 20 |
| [common/characters/CAN.txt](<../common/characters/CAN.txt>) | HOI4 | `eb0608da9f6cf2ca604f0707031ca0466686a75ce098d3a0b80a274fcd256593` | 6 |
| [common/characters/CHI.txt](<../common/characters/CHI.txt>) | HOI4 | `24ea9d91e5e93b6a6b93aad542ea9bc21c9e9bb86a54960e8537b3625a0283f5` | 79 |
| [common/characters/CHL.txt](<../common/characters/CHL.txt>) | HOI4 | `45ca3a5eb275d47bb2da42f237d4b9fd23aecc8f495624d5a33c17290a15fccc` | 260 |
| [common/characters/COG.txt](<../common/characters/COG.txt>) | HOI4 | `eeaf348c147fa74d8ce979863136f247459541a67c6024f792b0d5d35a99099f` | 24 |
| [common/characters/CZE.txt](<../common/characters/CZE.txt>) | HOI4 | `ed666a42deda337946b708d30cdb692730504f40c3b06c885a983d7ef6568054` | 115 |
| [common/characters/DEN.txt](<../common/characters/DEN.txt>) | HOI4 | `05c38982e32191de43061fdab419583bcc68b017fd5d1ccb05ff0ac8332f7b5e` | 23 |
| [common/characters/ENG.txt](<../common/characters/ENG.txt>) | HOI4 | `01de51f84d9c584a25a178ecf0cf4e6fbb423f3d85e28aeb4d2f7506fed38680` | 18 |
| [common/characters/EST.txt](<../common/characters/EST.txt>) | HOI4 | `41af7f98e2a68cb2f67d6cd96be2972ad23377ebea30baa866794639b17de7b7` | 9 |
| [common/characters/ETH.txt](<../common/characters/ETH.txt>) | HOI4 | `56c498a3bba419f9e4f0e0bb70703e3df014e3779d40347a257cb3b671178156` | 12 |
| [common/characters/FIN.txt](<../common/characters/FIN.txt>) | HOI4 | `e67ea70a25955727f729eddefa393859d971b52ec93b42109bfe108567661606` | 73 |
| [common/characters/FRA.txt](<../common/characters/FRA.txt>) | HOI4 | `3ecc16f7be10209ecf82a76fb1c3674dd234741bdbd49efdccf42a54226e34fc` | 15 |
| [common/characters/GER.txt](<../common/characters/GER.txt>) | HOI4 | `c0c860d5fcd6deefa47ad3b5e6188b49ece86357f4729d75a2635e2bd93c399f` | 144 |
| [common/characters/GRE.txt](<../common/characters/GRE.txt>) | HOI4 | `d3b50b9cccb9144deceb4b963f0aa67c870e9b26d78f401a35f8b1286a54b376` | 2 |
| [common/characters/HOL.txt](<../common/characters/HOL.txt>) | HOI4 | `b740293cfbafe14f89e96f70212bd6dd5f1b687b164e90cce9b69f1f7f1f5d86` | 8 |
| [common/characters/HUN.txt](<../common/characters/HUN.txt>) | HOI4 | `9f842621cb1276bf5f8e2fc41e24cb51f84ec5032414e8c6dd83e75d41789c99` | 98 |
| [common/characters/IA.txt](<../common/characters/IA.txt>) | HOI4 | `db3ffb930ca86bd1f959bfc536ddd567bbea705509829a1f8decb78ab683d85c` | 5 |
| [common/characters/ICE.txt](<../common/characters/ICE.txt>) | HOI4 | `d370204b55427d467a60c0782428fb10a3176e36c5e865059c31f3953fe8d229` | 9 |
| [common/characters/INS.txt](<../common/characters/INS.txt>) | HOI4 | `9585305a14132419808272011d50d8dbb68f8134c1ddfcaa33a0e26437c8b4cc` | 71 |
| [common/characters/IRQ.txt](<../common/characters/IRQ.txt>) | HOI4 | `3931908c6f38e7c4090d2f4117698e38883c3f1059da68fc95a14f9d65825448` | 34 |
| [common/characters/ITA.txt](<../common/characters/ITA.txt>) | HOI4 | `7c19962b2e3ca43f8a536c04c8cf6078b38b1dc8b630f729ea44950412ce16be` | 76 |
| [common/characters/JAP.txt](<../common/characters/JAP.txt>) | HOI4 | `b71b053f6b755d4e49ba2ae8b557cac409b81260f56797cb0bb2f42ee3f94b4a` | 202 |
| [common/characters/LAT.txt](<../common/characters/LAT.txt>) | HOI4 | `f3e43ea756c14c443349617dd3bc2201f7a664bf515ebaf522b671bbf142210d` | 10 |
| [common/characters/LIT.txt](<../common/characters/LIT.txt>) | HOI4 | `cd2fc8b34b637a19b5aa49b630dad84eaf5a081361fe805ad08ce1703d20f078` | 13 |
| [common/characters/MAN.txt](<../common/characters/MAN.txt>) | HOI4 | `435414ba9dd8cc24011d3b5aaada05b37a7f56434b0f06e7742faffd659959e5` | 9 |
| [common/characters/MEX.txt](<../common/characters/MEX.txt>) | HOI4 | `e057ebbc6803a31abca373d4355299ab2311050aa0c4b15c24cfcd68894a4fa6` | 13 |
| [common/characters/NOR.txt](<../common/characters/NOR.txt>) | HOI4 | `5af53bb9fa31ecb3e50240973cb7e53c85bace62311f1d5663d1598e793bd279` | 22 |
| [common/characters/NZL.txt](<../common/characters/NZL.txt>) | HOI4 | `e308b1166c4adac6100c789d4a5a9fde0bbc8c1147be00d54008e3f2f7b5ab43` | 1 |
| [common/characters/PAR.txt](<../common/characters/PAR.txt>) | HOI4 | `2677c6a295df05dc441db90e8884c6295c25e3406a7c323785d00fa689fdd9c5` | 2 |
| [common/characters/PER.txt](<../common/characters/PER.txt>) | HOI4 | `d9e37f48dd14cec7df2eed7fa8f2c2a3cc68abbfcaf7a88f37f8eab999cb5312` | 20 |
| [common/characters/PHI.txt](<../common/characters/PHI.txt>) | HOI4 | `ab46dc0311d634ca0658c12faa63a703800ff587bacc08b65d442229ac9a2943` | 33 |
| [common/characters/POL.txt](<../common/characters/POL.txt>) | HOI4 | `c3638879f55ae726f7a89f17032c64555141412f61abc492661cde37ab634cf0` | 35 |
| [common/characters/POR.txt](<../common/characters/POR.txt>) | HOI4 | `601e3e3213eb4b4a5aa6d122f06f41a196686e1fbdb28a12a8173f4b46d4f560` | 20 |
| [common/characters/PRC.txt](<../common/characters/PRC.txt>) | HOI4 | `efd2b15d3e4f10815638ae2f9aca4f32232e29acd5c53845540cef4a437b3b5a` | 30 |
| [common/characters/RAJ.txt](<../common/characters/RAJ.txt>) | HOI4 | `45a752e2d0e353a35fc14fa10aedf5c65beea5fa21346054706a014c9f223edc` | 107 |
| [common/characters/ROM.txt](<../common/characters/ROM.txt>) | HOI4 | `add162a2eb8b537ade680bf3990d68b2a3513c3b2db909766a27e4d03161529f` | 47 |
| [common/characters/SAF.txt](<../common/characters/SAF.txt>) | HOI4 | `715b7f97c8c07cbeffabad5dbf88c5e8e4b234debdad7797d8b95d89f773b944` | 3 |
| [common/characters/SIA.txt](<../common/characters/SIA.txt>) | HOI4 | `b7c184e68a2523ee121579e4dedd73adcd090d13e6f270b1d61807ad7ad81287` | 38 |
| [common/characters/SOV.txt](<../common/characters/SOV.txt>) | HOI4 | `28c16c68170784d6ff22223cc577a637bdcf8c851cbaba9ebfa10f012ad30098` | 71 |
| [common/characters/SPR.txt](<../common/characters/SPR.txt>) | HOI4 | `8734cbed277ca8369d646720618530eedc2e4c06c5c866725e6744944606c6e5` | 182 |
| [common/characters/SWE.txt](<../common/characters/SWE.txt>) | HOI4 | `2b7f917b5026a3793b9d587da4ccc6b9a5291d6a0a5a8e327521c6f3e3aebae3` | 16 |
| [common/characters/SWI.txt](<../common/characters/SWI.txt>) | HOI4 | `0e4ef0ce9653a8fca21bec31e78aab29f33959a31f3c303020dd05d191921042` | 17 |
| [common/characters/TUR.txt](<../common/characters/TUR.txt>) | HOI4 | `7122e350464501f31d3c1d5a06f5fa2557bcd4f34e088ca2a7e9325ad293d8fb` | 39 |
| [common/characters/URG.txt](<../common/characters/URG.txt>) | HOI4 | `ad809efa1bc1afe2a67c0deb0e6427a17350a1b4ca10cc5bbc51fcbe4bd24944` | 2 |
| [common/characters/USA.txt](<../common/characters/USA.txt>) | HOI4 | `42c7429ddb2500955233e3b340d8d53fe83b6b6d1971044fa94d0782fcefa2cd` | 14 |
| [common/characters/Warlords_China.txt](<../common/characters/Warlords_China.txt>) | HOI4 | `6c51398627393d447ad39a69cc18ad564841d9cf778f0458ee1b161d3653510b` | 2 |
| [common/continuous_focus/generic.txt](<../common/continuous_focus/generic.txt>) | HOI4 | `3c9660831933bf8b1ae9a0624fd0b38d0769f683abf40788c8a2c8bdb8894184` | 6 |
| [common/country_leader/00_traits.txt](<../common/country_leader/00_traits.txt>) | Quarior | `dda4e5075746e8f1da4da95966ec3ec3acf63813b93fc4fe2e5c02c317041e3d` | 3 |
| [common/decisions/categories/00_decision_categories.txt](<../common/decisions/categories/00_decision_categories.txt>) | HOI4 | `fc017a803e9ebaaeeda6d604c1006427ceeb9559fdf7c12d1ba0fa532d92995e` | 2 |
| [common/decisions/categories/AFG_decision_categories.txt](<../common/decisions/categories/AFG_decision_categories.txt>) | HOI4 | `23c260202b090a45a02f0f83ed1bbed1f547c4c2db93bf8774ee08b672e51567` | 2 |
| [common/decisions/categories/AST_decision_categories.txt](<../common/decisions/categories/AST_decision_categories.txt>) | HOI4 | `308117f0a7b6bac81a2d09c53e7e27ec8b3a63b2903e5ae553bdb69a421536b2` | 22 |
| [common/decisions/categories/AUS_decision_categories.txt](<../common/decisions/categories/AUS_decision_categories.txt>) | HOI4 | `a98451649437b3ad5d533909c0d093e89e6af338bba0a21455301cb4c3ee2ccf` | 16 |
| [common/decisions/categories/BALTIC_decision_categories.txt](<../common/decisions/categories/BALTIC_decision_categories.txt>) | HOI4 | `ee86b15f8e92718f7e65d44e87517cebc233f906c135ec83e8f32dd73ad4346a` | 44 |
| [common/decisions/categories/BEL_decision_categories.txt](<../common/decisions/categories/BEL_decision_categories.txt>) | HOI4 | `b1e13954f261702b9bd60df81789b624d9e63a0eed66fc090503b3dc71d1ad03` | 18 |
| [common/decisions/categories/BRA_decision_categories.txt](<../common/decisions/categories/BRA_decision_categories.txt>) | HOI4 | `dd1361b9f1f3d45cf34256173d79217ee43fb1998b0d92dc72ce2f2031960a1d` | 4 |
| [common/decisions/categories/BUL_decision_categories.txt](<../common/decisions/categories/BUL_decision_categories.txt>) | HOI4 | `d53a6a42a8158e6f5a67b1cfeb3575550edaa5983643cd154a67b076e6664848` | 10 |
| [common/decisions/categories/CHI_decision_categories.txt](<../common/decisions/categories/CHI_decision_categories.txt>) | HOI4 | `bb8ebd9ebf3e41c90e1e4773e6f70eca067c776f73824bb5c07175db4d28c599` | 70 |
| [common/decisions/categories/CHL_decision_categories.txt](<../common/decisions/categories/CHL_decision_categories.txt>) | HOI4 | `b144ef3b754f28b0aff1adbd5e3c03c6f8ed7eaadce81e40d683ce8b5030c04e` | 4 |
| [common/decisions/categories/COG_decision_categories.txt](<../common/decisions/categories/COG_decision_categories.txt>) | HOI4 | `e383802064feb61ef9ad9df6cc356bed6df09d0bc9b77f793389cff6bc975c10` | 6 |
| [common/decisions/categories/CZE_decision_categories.txt](<../common/decisions/categories/CZE_decision_categories.txt>) | HOI4 | `b125024e394272695fb1b3e96620882184d8d9d49dfe600b09a6d7f0d71858ca` | 14 |
| [common/decisions/categories/DEN_decision_categories.txt](<../common/decisions/categories/DEN_decision_categories.txt>) | HOI4 | `ffb0eb88ff971941c707ca353dbd3e1dd738b11c71439a292d9dcede3d7fa5eb` | 48 |
| [common/decisions/categories/ENG_decision_categories.txt](<../common/decisions/categories/ENG_decision_categories.txt>) | HOI4 | `7f80d354486fa0e82514bab6dc3bdf7dd24dc75e52bbd207abc5819269f4d0ea` | 8 |
| [common/decisions/categories/ETH_decision_categories.txt](<../common/decisions/categories/ETH_decision_categories.txt>) | HOI4 | `b595dfdf83fa9105507d3df848df804d4d2e45a1e00f91ecf3904c9dcc77b503` | 20 |
| [common/decisions/categories/FIN_decision_categories.txt](<../common/decisions/categories/FIN_decision_categories.txt>) | HOI4 | `438a210c0c8340a2765204616a9df0e7542c97787d17776c533d83405276d2d5` | 22 |
| [common/decisions/categories/FRA_decision_categories.txt](<../common/decisions/categories/FRA_decision_categories.txt>) | HOI4 | `b20c050b6b7721d48a8abd1bab0a1a239263101d5e91a11f84895f6b36d394b4` | 6 |
| [common/decisions/categories/GER_decision_categories.txt](<../common/decisions/categories/GER_decision_categories.txt>) | HOI4 | `56bd48059e9b1f217e0186069bc230be7de55cd898b480e1b18d22e1b80e8bd1` | 78 |
| [common/decisions/categories/GUAY_decision_categories.txt](<../common/decisions/categories/GUAY_decision_categories.txt>) | HOI4 | `d76fe7df995a835678160ce9a6fc934191e35276d477cc30c6aa30896b300a84` | 4 |
| [common/decisions/categories/HOL_decision_categories.txt](<../common/decisions/categories/HOL_decision_categories.txt>) | HOI4 | `7f146f6b245eb22ccdcc0ec04b1894028947ed91d451220e29d1eb22918ae47b` | 32 |
| [common/decisions/categories/HUN_decision_categories.txt](<../common/decisions/categories/HUN_decision_categories.txt>) | HOI4 | `8d7c8974d89e1b303486841e766953a0bc852f9bf6ebed80c6fb8de04dd31d9c` | 4 |
| [common/decisions/categories/ICE_decision_categories.txt](<../common/decisions/categories/ICE_decision_categories.txt>) | HOI4 | `efcefa427d4c1c97f2a1125a581b44413a45856ad56de5b3e83297a840cef52a` | 4 |
| [common/decisions/categories/INS_decision_categories.txt](<../common/decisions/categories/INS_decision_categories.txt>) | HOI4 | `57b686f4cdb1f8f83a5b1861050989d28405fe507db5b01caf7b7aaefc3d56e1` | 30 |
| [common/decisions/categories/IRQ_decision_categories.txt](<../common/decisions/categories/IRQ_decision_categories.txt>) | HOI4 | `847b97dedf787bc6edc4871ceb666590ef1603d5871c4d946aed7de4fa7ed18d` | 2 |
| [common/decisions/categories/ITA_decision_categories.txt](<../common/decisions/categories/ITA_decision_categories.txt>) | HOI4 | `b4691b11ec8941380046cbc9d7c34afde5a27e5a8e73d6e81b4be66dc6607df9` | 12 |
| [common/decisions/categories/JAP_decision_categories.txt](<../common/decisions/categories/JAP_decision_categories.txt>) | HOI4 | `3c508d52301dbe38daa56be67df6903d03453ce6a19efad720286ec7fe159f0b` | 28 |
| [common/decisions/categories/MAN_decision_categories.txt](<../common/decisions/categories/MAN_decision_categories.txt>) | HOI4 | `43a871efaa8200c402dc9efa180ee0c46ebf480a543a5e061f156b7d932af016` | 22 |
| [common/decisions/categories/NOR_decision_categories.txt](<../common/decisions/categories/NOR_decision_categories.txt>) | HOI4 | `51c1520686a38e97e67cedad0f752f14304a7edc441da848945a66db1eca899e` | 26 |
| [common/decisions/categories/PER_decision_categories.txt](<../common/decisions/categories/PER_decision_categories.txt>) | HOI4 | `b21b5a21651b47b751c8fc5cc356805aff6463c555e71cefa572aa1d0238fe02` | 2 |
| [common/decisions/categories/PHI_decision_categories.txt](<../common/decisions/categories/PHI_decision_categories.txt>) | HOI4 | `49a982016a91db07a4dcb575f6f86b1ac0bbcac79149d4e58c568a5d288ae8f6` | 12 |
| [common/decisions/categories/POL_decision_categories.txt](<../common/decisions/categories/POL_decision_categories.txt>) | HOI4 | `54b58b6ad34da19d7da8451db2732b6fb467ec680de213252310c10620857701` | 32 |
| [common/decisions/categories/POR_decision_categories.txt](<../common/decisions/categories/POR_decision_categories.txt>) | HOI4 | `650e80fa0ce4ff7fbfbc982a80752ea1a54a7e73c72dfb9fdd80434fbe1a3ab7` | 16 |
| [common/decisions/categories/PRC_decision_categories.txt](<../common/decisions/categories/PRC_decision_categories.txt>) | HOI4 | `03690a95e30defc09d1c293fa76d7ff28e84c0a23914c4af8488f641c980848b` | 28 |
| [common/decisions/categories/RAJ_GOE_decision_categories.txt](<../common/decisions/categories/RAJ_GOE_decision_categories.txt>) | HOI4 | `eb0b35e3bc1ba967ba6f89b37a030d835815eb6b1524d37e297d6a148daa9cb5` | 38 |
| [common/decisions/categories/RAJ_decision_categories.txt](<../common/decisions/categories/RAJ_decision_categories.txt>) | HOI4 | `9886b53ab8f19bdaf81a21261db38a04b9b678265d329d027c533d73c93dc105` | 4 |
| [common/decisions/categories/ROM_decision_categories.txt](<../common/decisions/categories/ROM_decision_categories.txt>) | HOI4 | `26993adf94f252aa87ada16625fcd7e7d3fc74fece6bf5e0c92a180c6ca882f3` | 28 |
| [common/decisions/categories/SIA_decision_categories.txt](<../common/decisions/categories/SIA_decision_categories.txt>) | HOI4 | `8926049c089fe33e2a7948c11cb72d9f70ea5b8c2cd24e445f35a56e8efd5c2d` | 28 |
| [common/decisions/categories/SOV_decision_categories.txt](<../common/decisions/categories/SOV_decision_categories.txt>) | HOI4 | `24ee57427f28bfa437a604dfe36f32849232732f482501a391c38eb7c69b6d50` | 34 |
| [common/decisions/categories/SS_decision_categories.txt](<../common/decisions/categories/SS_decision_categories.txt>) | HOI4 | `9fd8166cf7cb9bc35fb7cba6b4b2d9719d711ccf259dacc8afa2672e6641557b` | 2 |
| [common/decisions/categories/SWE_decision_categories.txt](<../common/decisions/categories/SWE_decision_categories.txt>) | HOI4 | `81859c8e5848f172d87c4bb7b43b5663496a0fe2146deb54080b319e16ac265f` | 24 |
| [common/decisions/categories/SWI_decision_categories.txt](<../common/decisions/categories/SWI_decision_categories.txt>) | HOI4 | `0e396973cbb028158f3c8976e8626de04a69d3926f04a52a32b1668ce0574f49` | 20 |
| [common/decisions/categories/USA_decision_categories.txt](<../common/decisions/categories/USA_decision_categories.txt>) | HOI4 | `9a45bde14096873a96424dbf19097dbec55b48e5e7c85f46e2caca491582e79f` | 14 |
| [common/decisions/categories/YUG_decision_categories.txt](<../common/decisions/categories/YUG_decision_categories.txt>) | HOI4 | `48362c431538ec83774ca2ffde193947daa0d1c6a90c25bf9a0f25c575d10d50` | 8 |
| [common/decisions/categories/infiltration_decision_categories.txt](<../common/decisions/categories/infiltration_decision_categories.txt>) | HOI4 | `255beea6601b68474b6afbc64bf8ef5cc12fe393450d1fd5defa03dab3bc5684` | 2 |
| [common/decisions/runeterra-foreign_politics_decisions.txt](<../common/decisions/runeterra-foreign_politics_decisions.txt>) | Quarior | `e3c11e3034c8adf4e2b07df733cf68f00847f2d898ef1f35871855cfb90356fa` | 8 |
| [common/decisions/runeterra-political_actions_decisions.txt](<../common/decisions/runeterra-political_actions_decisions.txt>) | Quarior | `3c4039f5656887518900f2e60630b90611761c62fb49494b528ac3c4c675a50c` | 10 |
| [common/decisions/runeterra-propaganda_efforts_decisions.txt](<../common/decisions/runeterra-propaganda_efforts_decisions.txt>) | Quarior | `516d1380acc6130b0ce7029ae5be8aab08d76778acc73b2ec82c4491f4615d25` | 2 |
| [common/doctrines/subdoctrines/land/infantry_subdoctrines.txt](<../common/doctrines/subdoctrines/land/infantry_subdoctrines.txt>) | HOI4 | `3bd676cd553a7cfd5da8ccb48fd0f13372b60f264977a95292f91d60c0e06475` | 1 |
| [common/dynamic_modifiers/SEA_dynamic_modifiers.txt](<../common/dynamic_modifiers/SEA_dynamic_modifiers.txt>) | HOI4 | `ca416318bb2731a3bda7f4c407318fd29d113b2613c64184f4f932acc91eb026` | 1 |
| [common/dynamic_modifiers/bba_dynamic_modifiers.txt](<../common/dynamic_modifiers/bba_dynamic_modifiers.txt>) | Runeterra | `52413a428ef331b3c002002e5a536e33d9c8c815081d8bdb39d467af21c4c799` | 2 |
| [common/dynamic_modifiers/wuw_dynamic_modifiers.txt](<../common/dynamic_modifiers/wuw_dynamic_modifiers.txt>) | HOI4 | `bd0d7bdfe7ca255f8d7c5c78124675fe3bbc1f78b9e0b120e396941364b4d7b0` | 6 |
| [common/focus_inlay_windows/ast_right_vs_left_campaign_empty_inlay_window.txt](<../common/focus_inlay_windows/ast_right_vs_left_campaign_empty_inlay_window.txt>) | HOI4 | `0021c7eb94bbda7a2d3812743bddbc4d037f41178a6803dd63ad2d4fc31c048f` | 3 |
| [common/focus_inlay_windows/ast_right_vs_left_campaign_inlay_window.txt](<../common/focus_inlay_windows/ast_right_vs_left_campaign_inlay_window.txt>) | HOI4 | `7f47b647acf014dd4dc48853d8b823c4d4ac81d7585f6cb3cd0d7b915322f1ae` | 3 |
| [common/focus_inlay_windows/ger_inner_circle_inlay_window.txt](<../common/focus_inlay_windows/ger_inner_circle_inlay_window.txt>) | HOI4 | `4d9fc09017946a0b4cacba49f368adbc7c913e5fb16a313ac83454e597fa8954` | 2 |
| [common/focus_inlay_windows/jap_imperial_influence_inlay_window.txt](<../common/focus_inlay_windows/jap_imperial_influence_inlay_window.txt>) | HOI4 | `3be6a4d02ef03a08e7b1ca63366d23bc01b3b0bde33d8ee7e0e50d0684107c16` | 2 |
| [common/focus_inlay_windows/sia_khana_ratsadon_inlay_window.txt](<../common/focus_inlay_windows/sia_khana_ratsadon_inlay_window.txt>) | HOI4 | `54a3ff4d30aae27974295a412b6e215124b0e09861cdda50f6c83b32cdadc1e0` | 1 |
| [common/ideas/GER.txt](<../common/ideas/GER.txt>) | HOI4 | `0e8c80be2f65757ae2c53564cc9b780a309fe8601135eecd1571959c51a8d726` | 134 |
| [common/ideas/SOV.txt](<../common/ideas/SOV.txt>) | HOI4 | `0dfd23aca2f9429e94ed146fccf151a5f187f8fe4a446c60103e18aa5c1aa236` | 28 |
| [common/ideas/_economic.txt](<../common/ideas/_economic.txt>) | Quarior | `07385d4f6dfcc34681dbe0e6134d66570799c8e0c5c77881965492f9edef2c06` | 17 |
| [common/ideas/_manpower.txt](<../common/ideas/_manpower.txt>) | Quarior | `6dd75a9c3e004583be645c2bd56d1e40a49d3a42a72815cd32a499c2c3504159` | 38 |
| [common/ideas/afghanistan.txt](<../common/ideas/afghanistan.txt>) | HOI4 | `6552a3a0f024e52b941426e5b02cc2aec3129306139ccf31b6d75f7697cf6d30` | 10 |
| [common/ideas/argentina.txt](<../common/ideas/argentina.txt>) | HOI4 | `9a9cb75012d8169b6dc7bc1b7a956e4df51dcadb7b6b0e3956c7473d8fa8d548` | 16 |
| [common/ideas/army_spirits.txt](<../common/ideas/army_spirits.txt>) | HOI4 | `932c983b6ff7cf3a221bb4b7399ff1f1ff9fdf3f4ca52e83e13ed47fd64fb512` | 16 |
| [common/ideas/australia.txt](<../common/ideas/australia.txt>) | HOI4 | `57f5057f205de6e108d6c579240713e4f42214bdbb7d99faa7a70cdc5cf97efc` | 48 |
| [common/ideas/austria.txt](<../common/ideas/austria.txt>) | HOI4 | `720f1fd1f1b604b38ca9a8e65e2ac3329fbd575950ca087abb53b553f18037c0` | 66 |
| [common/ideas/baltic_shared.txt](<../common/ideas/baltic_shared.txt>) | HOI4 | `642f4afeb4b403d3126208a33a12d16e7dbd0fe0e46f32617c3cdd943e5b7239` | 8 |
| [common/ideas/belgium.txt](<../common/ideas/belgium.txt>) | HOI4 | `2193cc5dd4d157294730ef1602b71777a789ab1759cc7245dc3b04a80714d060` | 26 |
| [common/ideas/brazil.txt](<../common/ideas/brazil.txt>) | HOI4 | `3cf85f8a2b8e06be738a9b6c64a85f01c7156d00bb3faedaedcc73434a9c79c6` | 26 |
| [common/ideas/british_raj_goe.txt](<../common/ideas/british_raj_goe.txt>) | HOI4 | `8e97c74d1ec7274170e5bbaf505daa26b06a961444b4503707ecc47492e29f2a` | 30 |
| [common/ideas/bulgaria.txt](<../common/ideas/bulgaria.txt>) | HOI4 | `0ace14ba8a3f21b2bc8ab5a1f7d42409317c9e75d0c9b0516ea889c9b147bda2` | 174 |
| [common/ideas/canada.txt](<../common/ideas/canada.txt>) | HOI4 | `2b3ebfde7b637d69c850c2fe49f1c184bc6903a42d7d94a0e278803e23774f51` | 6 |
| [common/ideas/chile.txt](<../common/ideas/chile.txt>) | HOI4 | `253d3545bce175622d75c13290fb832d87903d3fa9aa32c71cca1d66ea963e46` | 32 |
| [common/ideas/china.txt](<../common/ideas/china.txt>) | HOI4 | `29ce35190153145adb6315a5020f3922a1f058812012691ec6fc488ce575b2a1` | 8 |
| [common/ideas/china_shared.txt](<../common/ideas/china_shared.txt>) | HOI4 | `4adf32fb08fd730ee70489c2ca29e48c03e8da854e954293108c463bb609e858` | 16 |
| [common/ideas/comchina.txt](<../common/ideas/comchina.txt>) | HOI4 | `51ed8c87d8351b8b5ae70ca6766b081884eb97feabacecc557915bd044ce3de7` | 16 |
| [common/ideas/congo.txt](<../common/ideas/congo.txt>) | HOI4 | `05213e8483e310e85f5dc2ca977cf3b559181507dc6b1afc1baa9aa8446a62cc` | 16 |
| [common/ideas/czechoslovakia.txt](<../common/ideas/czechoslovakia.txt>) | HOI4 | `9decc5b967cb1d181458a71071a6d76c82f91197caca5ac9c68ac036ee3c0aed` | 144 |
| [common/ideas/denmark.txt](<../common/ideas/denmark.txt>) | HOI4 | `2705da1d3cdc6d9a1593d51ef54dc30eb7881014af16399c1d78c6b0f0890e38` | 6 |
| [common/ideas/ethiopia.txt](<../common/ideas/ethiopia.txt>) | HOI4 | `d0a58d968bd7680eb5c6cca63964c88ed35037f56dbd6bb875122a4d068140b7` | 66 |
| [common/ideas/finland.txt](<../common/ideas/finland.txt>) | HOI4 | `9e9cc6599d73c77aefb80417c84137397cc7577fc37758c5c64679eba367d184` | 30 |
| [common/ideas/france.txt](<../common/ideas/france.txt>) | HOI4 | `2ebe3cad775942f68b66732cde7bc4456bd9b7ab89aa159e792a042f2153c67e` | 14 |
| [common/ideas/greece.txt](<../common/ideas/greece.txt>) | HOI4 | `6fc6fc09e67c8d09d69439bbce64e01754ae6075b6960d27630c12f4859546ba` | 22 |
| [common/ideas/hungary.txt](<../common/ideas/hungary.txt>) | HOI4 | `040d892b34ec4ec5d9df11a4d9029611c9e358fb1decbedbc34ff4666d5e42b9` | 32 |
| [common/ideas/iceland.txt](<../common/ideas/iceland.txt>) | HOI4 | `a6caabadc06130ce108ed80137bd64006dfbe34f66489f3a8b253945734513fa` | 12 |
| [common/ideas/indonesia.txt](<../common/ideas/indonesia.txt>) | HOI4 | `4d76e8a146920d90d63a6f05dc98f9c9883fe7a16fb0e403b5bb9a29081b7cd1` | 6 |
| [common/ideas/iraq.txt](<../common/ideas/iraq.txt>) | HOI4 | `3229fb5b7483b3b0d49c8a180717285b541badef3ec1764c3c624911af3364ec` | 8 |
| [common/ideas/italy.txt](<../common/ideas/italy.txt>) | HOI4 | `d4562b13651fdeb30d50484677eb7aac03767af31b79c4b7f6f7899c5848b720` | 282 |
| [common/ideas/japan.txt](<../common/ideas/japan.txt>) | HOI4 | `9c5edbc6fc5f860ae7c921fb109f889353d422e38aaaaf667d5474867494dd18` | 64 |
| [common/ideas/manchukou.txt](<../common/ideas/manchukou.txt>) | HOI4 | `1dcf6411cc34bb7792fd729c2eb711aec176b8ae9cb8274a863ddcae99cf1195` | 52 |
| [common/ideas/mexico.txt](<../common/ideas/mexico.txt>) | HOI4 | `1e07342d3711eef7ae67e3c052ca089dc9e96147fa0cbecf6a713a2d1e4de372` | 16 |
| [common/ideas/netherlands.txt](<../common/ideas/netherlands.txt>) | HOI4 | `98ce4a03b53fe6dd37f8469bdd2bf5d4528fca912f035fb7de7f57eb3aa2de51` | 18 |
| [common/ideas/new_zealand.txt](<../common/ideas/new_zealand.txt>) | HOI4 | `4d0a0482ae7258f43cacd6d468fcf97a3c68c39f5aa1a4343f2614dcd08a52df` | 4 |
| [common/ideas/norway.txt](<../common/ideas/norway.txt>) | HOI4 | `ed98c333284a22fca5ff4bd62a1060b6df2081ae2cc4f41b3816506dcf93cec9` | 4 |
| [common/ideas/paraguay.txt](<../common/ideas/paraguay.txt>) | HOI4 | `347294005a0824a5f2e12f95efcb23899e32322e87e74d6c55e908f19e7e3bd1` | 2 |
| [common/ideas/persia.txt](<../common/ideas/persia.txt>) | HOI4 | `2e1b23ea425e93f90f79533e0c4666689dedf24ee293174d2d3ee034d6fc6ac9` | 18 |
| [common/ideas/philippines.txt](<../common/ideas/philippines.txt>) | HOI4 | `1a258b80a3ea4623241c28a1b79228d74ced0e78d90dd8ca2e8c56910bdaf0ef` | 14 |
| [common/ideas/poland.txt](<../common/ideas/poland.txt>) | HOI4 | `cd64091734151e5c122c2fc4c8213d9772142de780615473cd45aa947c4b215d` | 12 |
| [common/ideas/portugal.txt](<../common/ideas/portugal.txt>) | HOI4 | `3701f33a49146dc3f682c16d5a04d10b5de199d23a39f890afb73f360c635ad3` | 6 |
| [common/ideas/romania.txt](<../common/ideas/romania.txt>) | HOI4 | `12b04f965581dd90da27f7aa38948237ff6cce64ee3a9cd5f7a6858a649a100c` | 36 |
| [common/ideas/siam.txt](<../common/ideas/siam.txt>) | HOI4 | `1ac8fff3811e24588ff34619b7aec9f1f8f0c5f041548ac2d6a742c3dd8036a4` | 18 |
| [common/ideas/south_africa.txt](<../common/ideas/south_africa.txt>) | HOI4 | `10414ef3976c6081846849024b0c880bcac13ff8b7818ba2dbe215ced6069d15` | 2 |
| [common/ideas/sweden.txt](<../common/ideas/sweden.txt>) | HOI4 | `ef04207fc37935c7b1c80cb75ad81b1974fe1123da636045795b409d644ab07d` | 2 |
| [common/ideas/switzerland.txt](<../common/ideas/switzerland.txt>) | HOI4 | `c7def6003291eaf8b40d2be5ac2287f8c391d9ead57e8e533683787b20fe64c0` | 8 |
| [common/ideas/turkey.txt](<../common/ideas/turkey.txt>) | HOI4 | `791df482d4b4469a94d61244d7e72d2c4ee30fed26da0cbd285adac0b8b255ca` | 4 |
| [common/ideas/uruguay.txt](<../common/ideas/uruguay.txt>) | HOI4 | `56210ad7dfc0570fa31dbdefed55f8b317b44484110845fea388ffc13cbad04f` | 6 |
| [common/ideas/usa.txt](<../common/ideas/usa.txt>) | HOI4 | `e7686a9ed58f8a7ca492467bfaba4b36768934629049c0aa289c243e53d680af` | 56 |
| [common/ideas/yugoslavia.txt](<../common/ideas/yugoslavia.txt>) | HOI4 | `f5c46cf15f9fef207760a796fe62370ad947b01becfb8f39c7e9ffcb0d765263` | 6 |
| [common/intelligence_agencies/00_intelligence_agencies.txt](<../common/intelligence_agencies/00_intelligence_agencies.txt>) | HOI4 | `3a69775e9b5332e8ff75572f126fde38383c2922513f47d888dc45126b9d0d05` | 11 |
| [common/military_industrial_organization/organizations/AFG_organization.txt](<../common/military_industrial_organization/organizations/AFG_organization.txt>) | HOI4 | `a7d3e7b85ebfe05b25560f99ed8cdebb1a7699096e6a01da25f3f539abc6a6d3` | 3 |
| [common/military_industrial_organization/organizations/AST_organization.txt](<../common/military_industrial_organization/organizations/AST_organization.txt>) | HOI4 | `62bd4704a9b74ba72b95fd27a85332d26648320ee1029848cc87aa43e83b6d29` | 19 |
| [common/military_industrial_organization/organizations/AUS_organization.txt](<../common/military_industrial_organization/organizations/AUS_organization.txt>) | HOI4 | `be30804f2018cf47c24aa7f3ce619d75875bba139de1ec2fde7d71e6badee3a0` | 11 |
| [common/military_industrial_organization/organizations/BEL_organization.txt](<../common/military_industrial_organization/organizations/BEL_organization.txt>) | HOI4 | `62c428ad6838244004104059927a1fc355bba15375ee525ac906d2cc3f21e505` | 11 |
| [common/military_industrial_organization/organizations/BRA_organization.txt](<../common/military_industrial_organization/organizations/BRA_organization.txt>) | HOI4 | `c2329420de361bd05fcb4ee657c4f406da0148558191aeca5afb4f5cdbc686a2` | 5 |
| [common/military_industrial_organization/organizations/BUL_organization.txt](<../common/military_industrial_organization/organizations/BUL_organization.txt>) | HOI4 | `ed254b7f97d2e2f1dcaf5844bf4f27570f93565a4c9f31dab4c0cf19a6a56843` | 10 |
| [common/military_industrial_organization/organizations/CAN_organization.txt](<../common/military_industrial_organization/organizations/CAN_organization.txt>) | HOI4 | `e63b3db16d3f45096d9f3f5e94b0b0c8bcbf87dbc5def24ae5ca8b798ea7272a` | 2 |
| [common/military_industrial_organization/organizations/CHI_organization.txt](<../common/military_industrial_organization/organizations/CHI_organization.txt>) | HOI4 | `ee0c4f9e5abf61c8652becaa50a59798399af73d545323d11be8158892ec8ec1` | 18 |
| [common/military_industrial_organization/organizations/COG_organization.txt](<../common/military_industrial_organization/organizations/COG_organization.txt>) | HOI4 | `f4646454d02a8d12649dde9cbd8ff32649d19579811e2c4473291b5afe96ab80` | 3 |
| [common/military_industrial_organization/organizations/CZE_organization.txt](<../common/military_industrial_organization/organizations/CZE_organization.txt>) | HOI4 | `d89b34d9bec22db271ea36a229c7e000f224b4bc2c882add283b0b80765d2910` | 65 |
| [common/military_industrial_organization/organizations/DEN_organization.txt](<../common/military_industrial_organization/organizations/DEN_organization.txt>) | HOI4 | `a20e25b8db13ccdc2a93b0cf221c1ebef67f472df32d16dec607356595b85a95` | 13 |
| [common/military_industrial_organization/organizations/ENG_organization.txt](<../common/military_industrial_organization/organizations/ENG_organization.txt>) | HOI4 | `bc8f883e2b38b1ce2e6875f85689ad36529bc7e373392baf577eab0e1419df50` | 21 |
| [common/military_industrial_organization/organizations/ETH_organization.txt](<../common/military_industrial_organization/organizations/ETH_organization.txt>) | HOI4 | `3d34aa0b3a96365971030eeece568a8945049ad12f0edfe5e6151be3d8afdda6` | 2 |
| [common/military_industrial_organization/organizations/FIN_organization.txt](<../common/military_industrial_organization/organizations/FIN_organization.txt>) | HOI4 | `ac1701b0ea2518e3f287c28a1cbfe0356ffda637908a715fb1ba140678dc4c4f` | 21 |
| [common/military_industrial_organization/organizations/FRA_organization.txt](<../common/military_industrial_organization/organizations/FRA_organization.txt>) | HOI4 | `1017c29349e648e6cf2d13baced0e77c26ceb05aa969ff23b68518f22f5f0324` | 7 |
| [common/military_industrial_organization/organizations/GER_organization.txt](<../common/military_industrial_organization/organizations/GER_organization.txt>) | HOI4 | `3d2dd208cffc420e88a6b943b8e31aa621e0113b433650b6851e28768400d394` | 42 |
| [common/military_industrial_organization/organizations/GRE_organization.txt](<../common/military_industrial_organization/organizations/GRE_organization.txt>) | HOI4 | `4950e486cbf25356d0d714d5b8cbb847f4620a6868abb29eb8ce20bd1b415581` | 3 |
| [common/military_industrial_organization/organizations/HOL_organization.txt](<../common/military_industrial_organization/organizations/HOL_organization.txt>) | HOI4 | `5797670114b3a07f5809b8e3887451a4fda721d1ea78c7e6054ce05dfe64db75` | 1 |
| [common/military_industrial_organization/organizations/HUN_organization.txt](<../common/military_industrial_organization/organizations/HUN_organization.txt>) | HOI4 | `f58ab571fb60c4954da1490718f03a1988a35a67bb7b80a6f274ff0a51c07ad5` | 15 |
| [common/military_industrial_organization/organizations/IRQ_organization.txt](<../common/military_industrial_organization/organizations/IRQ_organization.txt>) | HOI4 | `b77122aaf60b5773082b5e8cd6059c1d7bc2ff1953d7ba9183b64db7f7557b24` | 6 |
| [common/military_industrial_organization/organizations/ITA_organization.txt](<../common/military_industrial_organization/organizations/ITA_organization.txt>) | HOI4 | `1b1b625df5ab94a5a6ccc4651d7abca95697e9a29a05fb95b12af8e22d8a0534` | 47 |
| [common/military_industrial_organization/organizations/JAP_organization.txt](<../common/military_industrial_organization/organizations/JAP_organization.txt>) | HOI4 | `3c05efef674e6bd3a1ace673b20d3b404096a5a43d3e14056bf73b36264c2ff0` | 44 |
| [common/military_industrial_organization/organizations/MAN_organization.txt](<../common/military_industrial_organization/organizations/MAN_organization.txt>) | HOI4 | `ad1f61353b731000d209bde7332ad564d85ee8ccd4620aebdbaf406acba82a93` | 6 |
| [common/military_industrial_organization/organizations/MEX_organization.txt](<../common/military_industrial_organization/organizations/MEX_organization.txt>) | HOI4 | `2721eecfd356fd74c9b8a8eb92ffa88c9fa2f580a3d5028b70e973e3c0ba8098` | 4 |
| [common/military_industrial_organization/organizations/NOR_organization.txt](<../common/military_industrial_organization/organizations/NOR_organization.txt>) | HOI4 | `63f6e9e5a9e1ed91e5beb89bfb2c48bb5b60e38e8dc5c753ef1d462fc9679c23` | 4 |
| [common/military_industrial_organization/organizations/PER_organization.txt](<../common/military_industrial_organization/organizations/PER_organization.txt>) | HOI4 | `5e85b9ad2ef170a1c753d42d26a20d3b49c94b650f1eb47ac6482a99ac86c11b` | 2 |
| [common/military_industrial_organization/organizations/PHI_organization.txt](<../common/military_industrial_organization/organizations/PHI_organization.txt>) | HOI4 | `090b1e28c1d3168413a48bc20de28a75650777b8250cc28b02b60811c8fd093b` | 1 |
| [common/military_industrial_organization/organizations/POL_organization.txt](<../common/military_industrial_organization/organizations/POL_organization.txt>) | HOI4 | `58669341b54b5e6e84b1d3555c14f42b831542390268aff37ba4e0425adbadab` | 2 |
| [common/military_industrial_organization/organizations/POR_organization.txt](<../common/military_industrial_organization/organizations/POR_organization.txt>) | HOI4 | `1dc3627ee41010b475a1d1c42a35770ae9b4b9a9b1e719aab391533b5ca48a13` | 3 |
| [common/military_industrial_organization/organizations/PRC_organization.txt](<../common/military_industrial_organization/organizations/PRC_organization.txt>) | HOI4 | `aecde927cbcfd26446fd69fe2674920f783c8be14b83ca3206268fba221074a2` | 7 |
| [common/military_industrial_organization/organizations/RAJ_GOE_organization .txt](<../common/military_industrial_organization/organizations/RAJ_GOE_organization .txt>) | HOI4 | `b2c37a66e31c852eb07ff1e9b5700684405871d37d11c372ef42b8b5c2a0fad2` | 8 |
| [common/military_industrial_organization/organizations/ROM_organization.txt](<../common/military_industrial_organization/organizations/ROM_organization.txt>) | HOI4 | `848a6fbad32bd457d0518305b7ed88e2e04f6551da6ac3d6a0b8440ff66d2ba2` | 14 |
| [common/military_industrial_organization/organizations/SIA_organization.txt](<../common/military_industrial_organization/organizations/SIA_organization.txt>) | HOI4 | `e75e7e3ce72ac3106c5fc8f192e8dd1c59b1cf335330b09449c9c9aaee311593` | 3 |
| [common/military_industrial_organization/organizations/SOV_organization.txt](<../common/military_industrial_organization/organizations/SOV_organization.txt>) | HOI4 | `26f7b1c2c71c3fefd04e47e5144782835db67adad7448fe6c94659c865b7939e` | 85 |
| [common/military_industrial_organization/organizations/SWE_organization.txt](<../common/military_industrial_organization/organizations/SWE_organization.txt>) | HOI4 | `0fa516a001e2e6078e96c2afb8f16015a3a5a12c9259920f0381bb499bca2810` | 14 |
| [common/military_industrial_organization/organizations/SWI_organization.txt](<../common/military_industrial_organization/organizations/SWI_organization.txt>) | HOI4 | `9775f1b3d26bdd4dc96476d057dc20b7658ea567e90ca786ef966321c6509834` | 1 |
| [common/military_industrial_organization/organizations/USA_organization.txt](<../common/military_industrial_organization/organizations/USA_organization.txt>) | HOI4 | `00129226b714c3d9a92c551e04d937d00336c970ca5e67c004b8d2acc8e801a3` | 38 |
| [common/military_industrial_organization/organizations/YUG_organization.txt](<../common/military_industrial_organization/organizations/YUG_organization.txt>) | HOI4 | `df3c893be8a760c86d5e806f9c14c034b3ba53acf4b1853258d5b55f4830c556` | 3 |
| [common/military_industrial_organization/organizations/baltic_organization.txt](<../common/military_industrial_organization/organizations/baltic_organization.txt>) | HOI4 | `7eed99564ce65a398367f35676dc113aa06bc08d8b2e4d02945374cbb3d81680` | 1 |
| [common/military_industrial_organization/policies/_general_policies.txt](<../common/military_industrial_organization/policies/_general_policies.txt>) | HOI4 | `993f7f1b2e22f13a39fc727e7625364ba2aac1dde2586ca4cf4c1f9e209b766a` | 2 |
| [common/occupation_laws/occupation_laws.txt](<../common/occupation_laws/occupation_laws.txt>) | HOI4 | `28bb360531006f01cc8c5692ce76bfc4077a6fabdb0772a4fa7ed85eb49c58e0` | 14 |
| [common/on_actions/01_tfv_on_actions.txt](<../common/on_actions/01_tfv_on_actions.txt>) | HOI4 | `3b49674d30d32065e286fd2edc70cbdddf65b5c975374011d717deb53b5ad983` | 2 |
| [common/on_actions/03_wtt_on_actions.txt](<../common/on_actions/03_wtt_on_actions.txt>) | HOI4 | `56f210e5fa36ff9ff547e2ed2d2d12ce1378584974363ced1d41a1411369cecf` | 4 |
| [common/on_actions/04_mtg_on_actions.txt](<../common/on_actions/04_mtg_on_actions.txt>) | HOI4 | `8e5d2413b53f3b07421dd38bac4572bc24c7e62887bc04fd1518b6d21f91072a` | 16 |
| [common/on_actions/05_lar_on_actions.txt](<../common/on_actions/05_lar_on_actions.txt>) | HOI4 | `77dc977ecd340429906d6a5f4f2561ba3a6d23fae97dd61e031465c752acaf56` | 52 |
| [common/on_actions/06_bftb_on_actions.txt](<../common/on_actions/06_bftb_on_actions.txt>) | HOI4 | `2a95aee6dcf9e31d8bf449be9ae51bafa339be4c05e8fc9c1f3c15065953532c` | 38 |
| [common/on_actions/07_nsb_on_actions.txt](<../common/on_actions/07_nsb_on_actions.txt>) | HOI4 | `37b7be23883b126ed63710b7d25d081ed0c467dccab2ba48e2fdcdc7280609d4` | 54 |
| [common/on_actions/08_bba_on_actions.txt](<../common/on_actions/08_bba_on_actions.txt>) | HOI4 | `954a3d91a4a3e6d52c35585bdd934ea4fdd7ade9d1bf16018215212654fd7f62` | 34 |
| [common/on_actions/09_aat_on_actions.txt](<../common/on_actions/09_aat_on_actions.txt>) | HOI4 | `952af62c98db4bd58f70f672557ac269084992bf19833eba69f1346508ee205e` | 82 |
| [common/on_actions/10_toa_on_actions.txt](<../common/on_actions/10_toa_on_actions.txt>) | HOI4 | `5eb38ab67b46c0063b58178519637a679d2876e569fc6614f127dcd0039b57ca` | 12 |
| [common/on_actions/12_wuw_on_actions.txt](<../common/on_actions/12_wuw_on_actions.txt>) | HOI4 | `e21f5cafd0f342e00210ee0c65a2402e8c3b8eaaa62692d42861d7287683d3f8` | 104 |
| [common/on_actions/13_goe_on_actions.txt](<../common/on_actions/13_goe_on_actions.txt>) | HOI4 | `ba0070af7a13143e1e1e380631249b422d366723892b5bd11064d2603a463f74` | 34 |
| [common/on_actions/14_sea_on_actions.txt](<../common/on_actions/14_sea_on_actions.txt>) | HOI4 | `691781ffe5f1ff438e381ea795af185dee159a2a0c6ea61fa5ae410865798624` | 88 |
| [common/on_actions/15_mun_on_actions.txt](<../common/on_actions/15_mun_on_actions.txt>) | HOI4 | `4007e3d23c4d532bb03b435bd27e63fffd1bf75b0d32a97dd35b13f505dcda1f` | 10 |
| [common/on_actions/16_taog_on_actions.txt](<../common/on_actions/16_taog_on_actions.txt>) | HOI4 | `56edaee825b4d49164b5011a46680bcac2dc774e13923ec8d11545be4b30ee0d` | 120 |
| [common/on_actions/17_ttbe_on_actions.txt](<../common/on_actions/17_ttbe_on_actions.txt>) | HOI4 | `5f14188f0308fcfe1efd3c091ddc5daa02319c5e8031863d07b8d2fec7e66b16` | 36 |
| [common/operations/00_operations.txt](<../common/operations/00_operations.txt>) | HOI4 | `e9d91ac1af23868d96a91a8ddf0463b769480525407e04bc02ec6edb4b7a273e` | 3 |
| [common/operations/LaR_FRA_operations.txt](<../common/operations/LaR_FRA_operations.txt>) | HOI4 | `3d9da1875c4934e5c5f4207049f4e46953b2eca5cffcf9f5e489c7e7c0bdf9f7` | 7 |
| [common/operations/NSB_historical_operations.txt](<../common/operations/NSB_historical_operations.txt>) | HOI4 | `3e2a7e0a94ef951dda6a1ae5f96092c755925538cb1d0d8ab0eaaf4198900c90` | 3 |
| [common/operations/POL_historical_operations.txt](<../common/operations/POL_historical_operations.txt>) | HOI4 | `7476b311c06a946b41f525901aec507a7ea9c2c7354402fee2543c097d738bd7` | 2 |
| [common/operations/SIA_operations.txt](<../common/operations/SIA_operations.txt>) | HOI4 | `06a2d89512dd7dfbb4a47109c2bed1eaa064255b939c94688e9b8bd7a5763bf5` | 1 |
| [common/peace_conference/ai_peace/CZE.txt](<../common/peace_conference/ai_peace/CZE.txt>) | HOI4 | `925e2f5c18bd80f4433a999995f96449c4ac10b314809628dd6f0a5d5da3abb7` | 2 |
| [common/peace_conference/ai_peace/GRE.txt](<../common/peace_conference/ai_peace/GRE.txt>) | HOI4 | `39f5471896e3dfb7e9246acebc560bce2684ce9a32ed8512e9d678c694d20190` | 2 |
| [common/peace_conference/cost_modifiers/AST_peace.txt](<../common/peace_conference/cost_modifiers/AST_peace.txt>) | HOI4 | `0812a95edc4198039ec69d9c4f724508505e8ad5ce569caa04e3ecba264da2d5` | 2 |
| [common/peace_conference/cost_modifiers/DEN_peace.txt](<../common/peace_conference/cost_modifiers/DEN_peace.txt>) | HOI4 | `7a5b3207222495bc249b7667b8a4a60f44fbd8e8ee760bc5bf6c818fc5ceb955` | 4 |
| [common/peace_conference/cost_modifiers/FIN_peace.txt](<../common/peace_conference/cost_modifiers/FIN_peace.txt>) | HOI4 | `075a16aae823fe2e5ba7dbef21e46e2eae9b8b47261ceec7c7984aaa27e9f49f` | 1 |
| [common/peace_conference/cost_modifiers/GER_peace.txt](<../common/peace_conference/cost_modifiers/GER_peace.txt>) | HOI4 | `01b4e5d83916780cc984ce133a9d39cccf5745a9ec10b7568c704a3c9d39c441` | 6 |
| [common/peace_conference/cost_modifiers/ITA_peace.txt](<../common/peace_conference/cost_modifiers/ITA_peace.txt>) | HOI4 | `c2d45aacdedd8f73393ade462cc90f06fbfbdc81cc2d5782f30c9a5dc83016b0` | 2 |
| [common/peace_conference/cost_modifiers/JAP_peace.txt](<../common/peace_conference/cost_modifiers/JAP_peace.txt>) | HOI4 | `c1e8563bfc6ecb8ea520fcf6e6b5c79bd1a2ef4cd82f36bf46af160727bdf9dd` | 6 |
| [common/peace_conference/cost_modifiers/RK_peace.txt](<../common/peace_conference/cost_modifiers/RK_peace.txt>) | HOI4 | `ee557224e5bf3e2b2d6a8ae2f1593b1a4b8b30f7185b07859019f5e081d27f4b` | 24 |
| [common/raids/naval_commando_raids.txt](<../common/raids/naval_commando_raids.txt>) | HOI4 | `f13ba44200e12d6539d2368243760dc3c1f81c8279481bdb1182336f19c184cc` | 2 |
| [common/resistance_compliance_modifiers/resistance_modifiers.txt](<../common/resistance_compliance_modifiers/resistance_modifiers.txt>) | HOI4 | `d2cb16e2dfbff0c916a5f17f804f6781bc10810cbcccb5877f394f30cc7653f7` | 1 |
| [common/scripted_effects/AST_scripted_effects.txt](<../common/scripted_effects/AST_scripted_effects.txt>) | HOI4 | `6c105d1e7e78c556db5b5bb36e148bf76cda055f3c3bc0ecbf95f009cbef3938` | 56 |
| [common/scripted_effects/BLT_scripted_effects.txt](<../common/scripted_effects/BLT_scripted_effects.txt>) | HOI4 | `ef3504d3fc2dd0cd8c9c8157bbd8e501decb9bb28ef3e0ce5b350c846660ded4` | 0 |
| [common/scripted_effects/CHI_scripted_effects.txt](<../common/scripted_effects/CHI_scripted_effects.txt>) | HOI4 | `e28835d04e1bcede4d7f1a92674d81099ffb311708f585f405bf0956fc9ebbec` | 16 |
| [common/scripted_effects/CZE_scripted_effects.txt](<../common/scripted_effects/CZE_scripted_effects.txt>) | HOI4 | `cb5ee5136b5759efe4caaaace23189964fce57af18558d0ac535336ea93319c6` | 4 |
| [common/scripted_effects/DEN_scripted_effects.txt](<../common/scripted_effects/DEN_scripted_effects.txt>) | HOI4 | `17eaedd7b12a5f1a1640c203599e584207d89022cd7aa1e461939bf97b12dace` | 16 |
| [common/scripted_effects/ENG_scripted_effects.txt](<../common/scripted_effects/ENG_scripted_effects.txt>) | HOI4 | `fade6a7c2034d8cd7833942d21dc6af9d4129bd786a47be524598f755c54f97a` | 20 |
| [common/scripted_effects/GER_scripted_effects.txt](<../common/scripted_effects/GER_scripted_effects.txt>) | HOI4 | `1d6b5cc8e00d685aa3c95cecab41cfeb2da590e90490de5dcce05e8e8e2beeb3` | 140 |
| [common/scripted_effects/INS_scripted_effects.txt](<../common/scripted_effects/INS_scripted_effects.txt>) | HOI4 | `65e82419ff1ad085a3393bada9dd2344997d4c28737e3dd5ab7fa067fe9186f3` | 8 |
| [common/scripted_effects/IRQ_scripted_effects.txt](<../common/scripted_effects/IRQ_scripted_effects.txt>) | HOI4 | `5eb65761eaf14200fc2f15a220c78177c89d8ddf4ec8a88f063c3d811f4a754c` | 12 |
| [common/scripted_effects/ITA_scripted_effects.txt](<../common/scripted_effects/ITA_scripted_effects.txt>) | HOI4 | `18b2fb010f48bed7e4b7f59354fcc8f3c1dc511325bb83311686ebf975d3f132` | 164 |
| [common/scripted_effects/JAP_scripted_effects.txt](<../common/scripted_effects/JAP_scripted_effects.txt>) | HOI4 | `29d244e5d375e73df7500509c61fbebb1f90d3e0c1e843d0a11fc666e627f17d` | 180 |
| [common/scripted_effects/NORDIC_scripted_effects.txt](<../common/scripted_effects/NORDIC_scripted_effects.txt>) | HOI4 | `dabbc05c1d76c7469e3431582f83a5c2d054678c3b2ec19209b21c4af9682707` | 4 |
| [common/scripted_effects/NOR_scripted_effects.txt](<../common/scripted_effects/NOR_scripted_effects.txt>) | HOI4 | `97b420cacc1628f6aca85b6608d8f98accba2b22eaa5a0a5cbccd354d321a57a` | 24 |
| [common/scripted_effects/POL_scripted_effects.txt](<../common/scripted_effects/POL_scripted_effects.txt>) | HOI4 | `55fc2b345a04076852bdfbdddd76b8ad857c1bebbfde554ce1ebe62a50d2edd3` | 0 |
| [common/scripted_effects/PRC_scripted_effects.txt](<../common/scripted_effects/PRC_scripted_effects.txt>) | HOI4 | `794a71b62c01567a3cae1fb102df59e85de0faab12eb165a9f4e01af40851909` | 4 |
| [common/scripted_effects/RAJ_GOE_scripted_effects.txt](<../common/scripted_effects/RAJ_GOE_scripted_effects.txt>) | HOI4 | `4fa9feaa108aed39cab27d1bb47a711e9ccc2c2698f7c65cae15504ada141dfb` | 12 |
| [common/scripted_effects/ROM_scripted_effects.txt](<../common/scripted_effects/ROM_scripted_effects.txt>) | HOI4 | `7360daca09359aee256a95536248241e748cf6442c4d764798dc33cfe9e39ffb` | 48 |
| [common/scripted_effects/SIA_scripted_effects.txt](<../common/scripted_effects/SIA_scripted_effects.txt>) | HOI4 | `46d0ca0329c483fecef7edec089cb7f5e5314dc3303e0aa99c8f237bef5c043f` | 16 |
| [common/scripted_effects/SOV_scripted_effects.txt](<../common/scripted_effects/SOV_scripted_effects.txt>) | HOI4 | `7fac0bf8bbd77bdd68b2c215c15756529138b21fc78c1e1f49fdb11831f4617a` | 68 |
| [common/scripted_effects/SPR_scripted_effects.txt](<../common/scripted_effects/SPR_scripted_effects.txt>) | HOI4 | `c4cc3910549d6a993921c78caa9454344494f66762cbc470f71c97b22a50c003` | 96 |
| [common/scripted_effects/SP_scripted_effects.txt](<../common/scripted_effects/SP_scripted_effects.txt>) | HOI4 | `4bc05e35ff893f6d5e2a54321a546416d8ba45777b7404a59a9c40b9083a510e` | 8 |
| [common/scripted_effects/SWE_scripted_effects.txt](<../common/scripted_effects/SWE_scripted_effects.txt>) | HOI4 | `229750634a47cc5b1e0791a91f6527b75295cc86c0e4e3d5fb81348eb12d8f16` | 4 |
| [common/scripted_effects/SWI_scripted_effects.txt](<../common/scripted_effects/SWI_scripted_effects.txt>) | HOI4 | `216d0c50bb0bae4e294b2f583770b32b323abeb92a9e0562a4e97f395c19188e` | 0 |
| [common/scripted_effects/TOA_scripted_effects.txt](<../common/scripted_effects/TOA_scripted_effects.txt>) | HOI4 | `7c5c9a47976e5d58bd875079b9140f0db6da37152ce16bbd60020fd790ad961d` | 24 |
| [common/scripted_effects/WTT_warlord_scripted_effects.txt](<../common/scripted_effects/WTT_warlord_scripted_effects.txt>) | HOI4 | `a6c0aacb49734f83c3c6a0c917297a322792b62adbad9d62c54b77e9641846f8` | 16 |
| [common/scripted_effects/YUG_scripted_effects.txt](<../common/scripted_effects/YUG_scripted_effects.txt>) | HOI4 | `1ff0436b9a3d41015f03f230d90036701419d8a5e86bc8dc9986d39381b3969f` | 12 |
| [common/scripted_localisation/00_scripted_localisation.txt](<../common/scripted_localisation/00_scripted_localisation.txt>) | HOI4 | `c879180d572781f852218a2cf781504550ea1300bf3cb0d109886392fb9c5c18` | 19 |
| [common/scripted_localisation/00_scripted_localisation_DE_loc.txt](<../common/scripted_localisation/00_scripted_localisation_DE_loc.txt>) | HOI4 | `13ae7c352def2128f97ffa1e77df3f1c134bce8b7e8ee7e45d3d41d36090f2a0` | 1 |
| [common/scripted_localisation/00_scripted_localisation_SPR_loc.txt](<../common/scripted_localisation/00_scripted_localisation_SPR_loc.txt>) | HOI4 | `0997ce02f60303f6d23278da44aa3c6f52e420458a11b3f6fa566099a2f742f9` | 2 |
| [common/scripted_localisation/AAT_Nordics_scripted_loc.txt](<../common/scripted_localisation/AAT_Nordics_scripted_loc.txt>) | HOI4 | `c038ae66df0d4e6fd491689e51355584a61e7c0f3444655d9f1677f182321363` | 3 |
| [common/scripted_localisation/AAT_Norway_scripted_loc.txt](<../common/scripted_localisation/AAT_Norway_scripted_loc.txt>) | HOI4 | `ae415334c6c3f11ef26a91f016f1cdeaffd516bc81ea7807fb04bd4a3bb35fc0` | 6 |
| [common/scripted_localisation/AAT_finland_scripted_loc.txt](<../common/scripted_localisation/AAT_finland_scripted_loc.txt>) | HOI4 | `2c1a7331360d77b7b22bd10d15f6638e58e408a34d5132564d66a0343a00c733` | 23 |
| [common/scripted_localisation/BBA_Switzerland_scripted_loc.txt](<../common/scripted_localisation/BBA_Switzerland_scripted_loc.txt>) | HOI4 | `b20949aec537badbdd9b10726b63b91ea5c8d67e16b3612487de6666a576e471` | 3 |
| [common/scripted_localisation/BBA_ethiopia_scripted_loc.txt](<../common/scripted_localisation/BBA_ethiopia_scripted_loc.txt>) | HOI4 | `88bd3af1d38758c54fdb8b2f5ff18e345eac526a0bdcbfeb2c224dec4d9c91ee` | 3 |
| [common/scripted_localisation/BBA_italy_scripted_loc.txt](<../common/scripted_localisation/BBA_italy_scripted_loc.txt>) | HOI4 | `0451bead730cf414ad62cfb9c08ca55812a8a0404e1e6142dfaf4fbe43ffab16` | 31 |
| [common/scripted_localisation/FR_SCRIPTING_FULL_AUTOMATED.txt](<../common/scripted_localisation/FR_SCRIPTING_FULL_AUTOMATED.txt>) | HOI4 | `9578906731e2b769bb1be16106eb3a91976999a962ee5655d2fcabef88321622` | 1333 |
| [common/scripted_localisation/GOE_IRQ_scripted_loc.txt](<../common/scripted_localisation/GOE_IRQ_scripted_loc.txt>) | HOI4 | `2fe11fe3cbaf2df06230b55c936bbfbd38697ab1460d6bbdaabf7be97c271b5b` | 2 |
| [common/scripted_localisation/MUN_scripted_localisation.txt](<../common/scripted_localisation/MUN_scripted_localisation.txt>) | HOI4 | `23f8c553f81db18cea2284aadf1fe798c5c58c50e82a2ae4c5dfda835442f7c8` | 2 |
| [common/scripted_localisation/NSB_baltic_scripted_loc.txt](<../common/scripted_localisation/NSB_baltic_scripted_loc.txt>) | HOI4 | `fca7180df4fd60fd2d6f96c88db7229c4f62e2317e1b807ed26f99b89ca7185a` | 2 |
| [common/scripted_localisation/NSB_poland_scripted_loc.txt](<../common/scripted_localisation/NSB_poland_scripted_loc.txt>) | HOI4 | `c3272af9a0cb0e41360e8632a6d748ebe28b858e53a5a5d023fcc9c58258aa6e` | 8 |
| [common/scripted_localisation/NSB_soviet_scripted_loc.txt](<../common/scripted_localisation/NSB_soviet_scripted_loc.txt>) | HOI4 | `771b937231ed14229978f7b8d3856ff97cfe59fbae1d5f2b6850d4ad53354a8d` | 26 |
| [common/scripted_localisation/SEA_CHI_scripted_loc.txt](<../common/scripted_localisation/SEA_CHI_scripted_loc.txt>) | HOI4 | `57f22b596357864f361174faf5ba5eb43c1d215fe47895a2a97393e2ba1d5118` | 13 |
| [common/scripted_localisation/SEA_JAP_scripted_loc.txt](<../common/scripted_localisation/SEA_JAP_scripted_loc.txt>) | HOI4 | `eb9c4fcbc88aae1eede0b650fb9cfe18c9c34d7b2fe94baf506dc5b7f86ba290` | 3 |
| [common/scripted_localisation/SEA_PHI_scripted_loc.txt](<../common/scripted_localisation/SEA_PHI_scripted_loc.txt>) | HOI4 | `9bb4bd7b604119117b0ba6197e368845e3c7b0377c2c08e486ace133ca952d43` | 7 |
| [common/scripted_localisation/SEA_PRC_scripted_loc.txt](<../common/scripted_localisation/SEA_PRC_scripted_loc.txt>) | HOI4 | `387cced4840ef6988e3ba6af4a72b99dc0ba71e82201cfcacd2f875fe5d64a0e` | 5 |
| [common/scripted_localisation/TAOG_INS_scripted_loc.txt](<../common/scripted_localisation/TAOG_INS_scripted_loc.txt>) | HOI4 | `49255cd6ce659f907ea9d7419530ba5b2a2fe53b86ee1dfffdb82b9395138b2a` | 2 |
| [common/scripted_localisation/TAOG_SIA_scripted_loc.txt](<../common/scripted_localisation/TAOG_SIA_scripted_loc.txt>) | HOI4 | `a661cf53a2dc84204ac65050cdb9672490d2b5a075e465c68988c112dc58621a` | 2 |
| [common/scripted_localisation/TOA_Brazil_scripted_loc.txt](<../common/scripted_localisation/TOA_Brazil_scripted_loc.txt>) | HOI4 | `84a5b4984a1cbb769c6396c021392b9844760fa558748f0e57d396baf609eaf4` | 4 |
| [common/scripted_localisation/TOA_Chile_scripted_loc.txt](<../common/scripted_localisation/TOA_Chile_scripted_loc.txt>) | HOI4 | `2085e1569d2de75a7a454008c674ff8c23a46e0fd632d9242a1391022563fccf` | 8 |
| [common/scripted_localisation/TTBE_scripted_localisation.txt](<../common/scripted_localisation/TTBE_scripted_localisation.txt>) | HOI4 | `aadcc1447507b788f1cd114a1ef3a97ea01169a29afeda7d17ab1b98d9f1872a` | 16 |
| [common/scripted_localisation/WUW_AUS_scripted_loc.txt](<../common/scripted_localisation/WUW_AUS_scripted_loc.txt>) | HOI4 | `ed5530b695b0c9a386b8d3db3facd90d3ad0681b9409ff7ce3c6a550deb1ccec` | 17 |
| [common/scripted_localisation/WUW_GER_scripted_loc.txt](<../common/scripted_localisation/WUW_GER_scripted_loc.txt>) | HOI4 | `82233d7bb8362d933182c7da345606089a67b92adedb764c37a942e1e2f67683` | 7 |
| [common/scripted_localisation/bftb_scripted_localisation.txt](<../common/scripted_localisation/bftb_scripted_localisation.txt>) | HOI4 | `8f191cd2b85638aae3a7de66cbe25a057bcc4f23ca3e8fc1920370a496b5e996` | 12 |
| [common/scripted_triggers/00_scripted_triggers.txt](<../common/scripted_triggers/00_scripted_triggers.txt>) | HOI4 | `3a82d8306dc15d8c6e62a05271158917217b5e5a0d63c8a0060044e316d93520` | 1 |
| [common/scripted_triggers/00_scripted_triggers_FR_loc.txt](<../common/scripted_triggers/00_scripted_triggers_FR_loc.txt>) | HOI4 | `cad64349fe2af5a1412e4ab3f1f4cd56820779d7b86f0b8b0c76a31b682b207f` | 92 |
| [common/scripted_triggers/AFG_scripted_triggers.txt](<../common/scripted_triggers/AFG_scripted_triggers.txt>) | HOI4 | `76d65562a6d5c6858eb251f323c2a87b4ff34161391cd65e7e321b77907b59db` | 0 |
| [common/scripted_triggers/AST_scripted_triggers.txt](<../common/scripted_triggers/AST_scripted_triggers.txt>) | HOI4 | `6982c6f087ab45c16b4ad226df338a8bc26b000b2eeacc4a1692ca8e8ecd1cce` | 0 |
| [common/scripted_triggers/AUS_scripted_triggers.txt](<../common/scripted_triggers/AUS_scripted_triggers.txt>) | HOI4 | `4b435e9ab20334afca5a2dd7c23d83e5126bb0591414b579c6b01564ebc23cf3` | 15 |
| [common/scripted_triggers/BEL_scripted_triggers.txt](<../common/scripted_triggers/BEL_scripted_triggers.txt>) | HOI4 | `cb9451d7b83e17d67f9e8f6a870baf3524b9f6482149a0199f21d86cdb95d9a2` | 0 |
| [common/scripted_triggers/BUL_scripted_triggers.txt](<../common/scripted_triggers/BUL_scripted_triggers.txt>) | HOI4 | `52da1cf28ecdebf34fd73f3ff9e1ea601e4a037d27c796dae6b224296c3bc08d` | 3 |
| [common/scripted_triggers/CHL_scripted_triggers.txt](<../common/scripted_triggers/CHL_scripted_triggers.txt>) | HOI4 | `65c64b3e1f5dedeb5e2bc437ef0e4d035ef28ca1851ea9a3a6392db04147682b` | 1 |
| [common/scripted_triggers/DEN_scripted_triggers.txt](<../common/scripted_triggers/DEN_scripted_triggers.txt>) | HOI4 | `394ef4e81d7a9faef313d36c5b3840edf452dbe952ab2cb37865cf8db7fc9538` | 1 |
| [common/scripted_triggers/ETH_scripted_triggers.txt](<../common/scripted_triggers/ETH_scripted_triggers.txt>) | HOI4 | `69d4f09616d7dc6a67bb7d45695f1b9008548174ef27573bc8e3868b3c0bd30b` | 5 |
| [common/scripted_triggers/FIN_scripted_triggers.txt](<../common/scripted_triggers/FIN_scripted_triggers.txt>) | HOI4 | `3b804448b068b34cb3bacc7b9313ac03a480399be39cf2ef6cbd6a2f35452efa` | 0 |
| [common/scripted_triggers/FRA_scripted_triggers.txt](<../common/scripted_triggers/FRA_scripted_triggers.txt>) | HOI4 | `a15831322f451f635897425c9529db4fbb67dedf11743d467f05fe5dd6b8abc7` | 2 |
| [common/scripted_triggers/GER_scripted_triggers.txt](<../common/scripted_triggers/GER_scripted_triggers.txt>) | HOI4 | `1c9ceda7a5a278b42b26fe8e7ea88bff70b7ab162050eb16ea2c77a50407f761` | 4 |
| [common/scripted_triggers/GRE_scripted_triggers.txt](<../common/scripted_triggers/GRE_scripted_triggers.txt>) | HOI4 | `632322cac12787e48ae625789fb905743445fec355defa535c8a9dee636ed368` | 0 |
| [common/scripted_triggers/HUN_scripted_triggers.txt](<../common/scripted_triggers/HUN_scripted_triggers.txt>) | HOI4 | `cd1126f064711d94049ad90b46971115cdc38d27148b2ebdfc0e7819ea086eb0` | 3 |
| [common/scripted_triggers/ICE_scripted_triggers.txt](<../common/scripted_triggers/ICE_scripted_triggers.txt>) | HOI4 | `22b44dad8f729464b0ebd86506c96a46b2c7e97c7c5466cec752ba90ecd795f3` | 0 |
| [common/scripted_triggers/INS_scripted_triggers.txt](<../common/scripted_triggers/INS_scripted_triggers.txt>) | HOI4 | `b4b89baef93fde568b7cb2a80d60cc8bb6f8d768e3cea02fcb080c234e936d30` | 18 |
| [common/scripted_triggers/ITA_scripted_triggers.txt](<../common/scripted_triggers/ITA_scripted_triggers.txt>) | HOI4 | `a3c08f3b474059333d5915eae7d2486223017482e71845e00e77e6199f960cda` | 17 |
| [common/scripted_triggers/NORDIC_scripted_triggers.txt](<../common/scripted_triggers/NORDIC_scripted_triggers.txt>) | HOI4 | `5a9c1a8199628323da9134acdcacd35d9c69d3ccc5b14995402b06b378095f4b` | 25 |
| [common/scripted_triggers/NOR_scripted_triggers.txt](<../common/scripted_triggers/NOR_scripted_triggers.txt>) | HOI4 | `01d64409b6692628e6e4b0fa91a31e5b9d934b833e36947bfb0aedebbe6aec0b` | 4 |
| [common/scripted_triggers/PHI_scripted_triggers.txt](<../common/scripted_triggers/PHI_scripted_triggers.txt>) | HOI4 | `3275e8dc85d5a62c35d655ea238f3b16df30d601aa20e98b0d47d8b55387a813` | 3 |
| [common/scripted_triggers/POL_scripted_triggers.txt](<../common/scripted_triggers/POL_scripted_triggers.txt>) | HOI4 | `4c91bf6c2682f9f34c5ace92c7273dd79fcc940c4404837716dc6aa62318f704` | 16 |
| [common/scripted_triggers/PRC_scripted_triggers.txt](<../common/scripted_triggers/PRC_scripted_triggers.txt>) | HOI4 | `c1c433a2aea228ea1c1c56d242040a9878af1cf4d9499f5c1a7ba108e74c45aa` | 0 |
| [common/scripted_triggers/RAJ_GOE_scripted_triggers.txt](<../common/scripted_triggers/RAJ_GOE_scripted_triggers.txt>) | HOI4 | `2d4ede4a724d1c6b99314969f5a942786cc788f62efa8d4693fa30be6c94da62` | 8 |
| [common/scripted_triggers/SIA_scripted_triggers.txt](<../common/scripted_triggers/SIA_scripted_triggers.txt>) | HOI4 | `cc332a838c0b7b16c1381658d64f33504b0ec198ceb0859ca359543938a1ea94` | 1 |
| [common/scripted_triggers/SOV_scripted_triggers.txt](<../common/scripted_triggers/SOV_scripted_triggers.txt>) | HOI4 | `ba5b80f54c97e0180a4b2c02d53bf9438ddada0590f08fc3b3331be0b2110f5a` | 21 |
| [common/scripted_triggers/SWE_scripted_triggers.txt](<../common/scripted_triggers/SWE_scripted_triggers.txt>) | HOI4 | `d7f4f6a4ac73597b4c4155dfedf83a3023590500a33373fe13f34a6ecc883e93` | 2 |
| [common/scripted_triggers/SWI_scripted_triggers.txt](<../common/scripted_triggers/SWI_scripted_triggers.txt>) | HOI4 | `7fbfb746ab2b599304eb55f13c6854bc4ccc4d292e4ba6c2cf31c8d2e76a77a2` | 0 |
| [common/scripted_triggers/TUR_scripted_triggers.txt](<../common/scripted_triggers/TUR_scripted_triggers.txt>) | HOI4 | `a7e0eb81074b70201d586436a0fe06da778537f8d6931cb29c33e1e1cacaa19f` | 2 |
| [common/scripted_triggers/diplomacy_scripted_triggers.txt](<../common/scripted_triggers/diplomacy_scripted_triggers.txt>) | HOI4 | `f9de7d3d4f773ddc4664a2f125a03d38796b3b6b9f3c89da7e97f7b94e456c5a` | 45 |
| [common/scripted_triggers/laws_war_support.txt](<../common/scripted_triggers/laws_war_support.txt>) | HOI4 | `056216177298704571617f64be5194b289d0bdc4488fc04d9c855f81a655c278` | 4 |
| [common/special_projects/projects/land_projects.txt](<../common/special_projects/projects/land_projects.txt>) | HOI4 | `eea9c3722209aec2eaff25e37090903458726b91ea147bf484b9082eef0db8ef` | 1 |
| [common/technologies/NSB_armor.txt](<../common/technologies/NSB_armor.txt>) | Quarior | `b485461ca6bd698ccbf56cc6b66a8e47b26a21f3c45371cfa20d0d2b8fb0df82` | 21 |
| [common/technologies/electronic_mechanical_engineering.txt](<../common/technologies/electronic_mechanical_engineering.txt>) | Quarior | `c27b99d80a114479fdd9deb0213e4038f954f31dd22b6277f266bb7685e3f7cf` | 1 |
| [common/technologies/industry.txt](<../common/technologies/industry.txt>) | Quarior | `03111d018ec8dcdefcfa7d18dc1c6232d2617c6bfb495be678b0e52591b269a4` | 1 |
| [common/technologies/infantry.txt](<../common/technologies/infantry.txt>) | Quarior | `65195699dc233a2db835dd2b2d0f8ac75df225d83968971fce58acae48682bec` | 1 |
| [common/technologies/support.txt](<../common/technologies/support.txt>) | Quarior | `af3753184d02ed8861398fd06536d68297255eff9128b96b43d7837884ee6553` | 3 |
| [common/technology_sharing/01_dod_tech_sharing_groups.txt](<../common/technology_sharing/01_dod_tech_sharing_groups.txt>) | HOI4 | `53bff324b4fb2be7c021f1e51006011cfda8b02515c52b9f221576512d0002af` | 1 |
| [common/technology_sharing/12_wuw_tech_sharing_groups.txt](<../common/technology_sharing/12_wuw_tech_sharing_groups.txt>) | HOI4 | `3b6e3e1bab064dd4fed4eab1ebd900c80a2adcbfb6406a2b65d5df39cbaaf297` | 2 |
| [common/unit_leader/00_traits.txt](<../common/unit_leader/00_traits.txt>) | HOI4 | `1e37cb682a49ce55330c27b0184c3ac216b77de183a96de74fc10383253f67d4` | 13 |
| [common/unit_medals/00_default.txt](<../common/unit_medals/00_default.txt>) | HOI4 | `e5580ca87030cfb1aeda6fca1077aee73df56eefaffe80eebc71233ffaace582` | 20 |
| [common/units/names_divisions/AST_names_divisions.txt](<../common/units/names_divisions/AST_names_divisions.txt>) | HOI4 | `e7b6ca63b322507b4d59693b4ad8fd9d9e390fac1786e29a4ece034d7b166395` | 2 |
| [common/units/names_divisions/ENG_names_divisions.txt](<../common/units/names_divisions/ENG_names_divisions.txt>) | HOI4 | `68c439a905596be460d44e454e41eba30f3494411ebfc66e0d2b59d1c57f6e76` | 2 |
| [common/units/names_divisions/GER_names_divisions.txt](<../common/units/names_divisions/GER_names_divisions.txt>) | HOI4 | `b4a70695f57bf3407190e111aeeed89c66baf99021db4cbf10114f3bedd98c50` | 10 |
| [common/units/names_divisions/MEX_names_divisions.txt](<../common/units/names_divisions/MEX_names_divisions.txt>) | HOI4 | `cd06e92c0e10fd16f7e7741335081fc903e74bcd8a5ef6b8eb2c49795a3158d2` | 2 |
| [common/units/names_divisions/SOV_names_divisions.txt](<../common/units/names_divisions/SOV_names_divisions.txt>) | HOI4 | `84797ddd70e2efa68dacb112d695c4b5667e727680d993662eedd09e31140013` | 3 |
| [common/units/names_divisions/SPR_names_divisions.txt](<../common/units/names_divisions/SPR_names_divisions.txt>) | HOI4 | `c61c89f87e8e9c4c1c259a241bd7782e7a3ad372e7dc237e68e95d15bfb676fa` | 1 |
| [common/units/names_ships/GER_ship_name.txt](<../common/units/names_ships/GER_ship_name.txt>) | HOI4 | `582d66b9bd2e7511080b25224a7da555e9be3ddeea12b031da0b4cae2faa68f3` | 117 |
| [common/units/names_ships/SOV_ship_names.txt](<../common/units/names_ships/SOV_ship_names.txt>) | HOI4 | `c6bdf4764fd50735a58e72341cd8a7d0a096e120bb7f6b3bc2ee43a4e043618f` | 1 |
| [common/units/names_ships/USA_ship_names.txt](<../common/units/names_ships/USA_ship_names.txt>) | HOI4 | `b1b449c3441057bbf34e5e2d3ec4bfd71119fb09e72d448171b40a93b2640c55` | 7 |
| [events/Generic.txt](<../events/Generic.txt>) | Quarior | `53f9e279e9fa6242788dc7f96a1343480200ac4609c231b0bd3e9b8d7a9b022b` | 19 |
| [events/NewsEvents.txt](<../events/NewsEvents.txt>) | Quarior | `07c20ac662bda2e7a7334f805c45ce43b09e24c202c08b70b1b72f10bf9e4c11` | 6 |
| [events/PoliticalEvents.txt](<../events/PoliticalEvents.txt>) | Quarior | `adee4c15f1db9175c4f5487d1aa184ac033ae28be76f7c9389e6fdea4b55e4ef` | 12 |
| [events/WarJustification.txt](<../events/WarJustification.txt>) | Quarior | `17b0a335e7f6f42d3dc3252ab5d47fca6205b91192a5f572e646630867069bdc` | 1 |
| [events/stability_events.txt](<../events/stability_events.txt>) | Quarior | `bbdfcbb6b904a1959a73fd60dff12df706799664d9b2c1af1a3ad75f7f18e8f3` | 2 |
| [history/general/spain_shared_advisors.txt](<../history/general/spain_shared_advisors.txt>) | HOI4 | `5eb7ff8b9cc18ee30b2ef4e573e1ac2991bd267863062004ba3cb8052655e22a` | 180 |
| [music/lar_songs.txt](<../music/lar_songs.txt>) | HOI4 DLC | `0c7ffc3355c7376700b70db9c111ce7088b6d875d5143b9a6233e925dca10109` | 2 |
| [music/mtg_songs.txt](<../music/mtg_songs.txt>) | HOI4 DLC | `d44797153f6a7a7d6dfe6bb68b750f0eefbff33be225e94cec72666f7e676993` | 4 |

## Additional changed files

- [.gitignore](<../.gitignore>)
- [gfx/entities/infantry.gfx](<../gfx/entities/infantry.gfx>)
- [gfx/entities/units_infantry.asset](<../gfx/entities/units_infantry.asset>)
- [interface/azir_inherited_gui_sprites.gfx](<../interface/azir_inherited_gui_sprites.gfx>)
- [common/country_leader/azir_manufacturer_traits_compatibility.txt](<../common/country_leader/azir_manufacturer_traits_compatibility.txt>)
- [common/ideologies/00_ideologies.txt](<../common/ideologies/00_ideologies.txt>)
- [portraits/01_anniversary_portraits.txt](<../portraits/01_anniversary_portraits.txt>)
- [portraits/027_lar_portraits.txt](<../portraits/027_lar_portraits.txt>)
- [portraits/02_tiger_portraits.txt](<../portraits/02_tiger_portraits.txt>)
- [portraits/03_mtg_portraits.txt](<../portraits/03_mtg_portraits.txt>)

The local launcher descriptor `../Runeterra-Map.mod` uses forward slashes for the same installation path. The local empty tank directory now uses lowercase `tanks`. The following flag files match the installed nonaligned variant at each size. These assets are covered by the project’s Git ignore rule.

- `gfx/flags/` — `ANU.tga`, `ASY.tga`, `ATJ.tga`, `BAR.tga`, `BHR.tga`, `BIA.tga`, `BLC.tga`, `BOU.tga`, `BRN.tga`, `CBV.tga`, `CHM.tga`, `CHR.tga`, `CIP.tga`, `CPS.tga`, `EVE.tga`, `EZO.tga`, `FOR.tga`, `FSA.tga`, `GAL.tga`, `GAR.tga`, `GDC.tga`, `GOW.tga`, `GSM.tga`, `HBC.tga`, `HES.tga`, `HYD.tga`, `IAS.tga`, `IMO.tga`, `INC.tga`, `INU.tga`, `ITZ.tga`, `KAT.tga`, `KHL.tga`, `KHM.tga`, `KLT.tga`, `KOL.tga`, `MAY.tga`, `MIS.tga`, `MPU.tga`, `MYS.tga`, `NAH.tga`, `NWF.tga`, `NXM.tga`, `OKN.tga`, `PLU.tga`, `POK.tga`, `PSH.tga`, `PSR.tga`, `QUE.tga`, `RAP.tga`, `RHI.tga`, `RIG.tga`, `RJP.tga`, `RNG.tga`, `SAB.tga`, `SAR.tga`, `SIC.tga`, `SIN.tga`, `SKK.tga`, `SND.tga`, `SNG.tga`, `SOK.tga`, `SSI.tga`, `THU.tga`, `TML.tga`, `TNE.tga`, `UBD.tga`, `VAN.tga`, `WIS.tga`, `WPG.tga`, `XIC.tga`, `YUC.tga`

- `gfx/flags/medium/` — `ANU.tga`, `ASY.tga`, `BAR.tga`, `BHR.tga`, `BIA.tga`, `BLC.tga`, `BRN.tga`, `CBV.tga`, `CHM.tga`, `CHR.tga`, `CIP.tga`, `CPS.tga`, `EVE.tga`, `EZO.tga`, `FOR.tga`, `FSA.tga`, `GAL.tga`, `GAR.tga`, `HBC.tga`, `HES.tga`, `HYD.tga`, `IAS.tga`, `IMO.tga`, `INC.tga`, `INU.tga`, `ITZ.tga`, `KAT.tga`, `KHL.tga`, `KLT.tga`, `KOL.tga`, `MAY.tga`, `MIS.tga`, `MPU.tga`, `MYS.tga`, `NAH.tga`, `NWF.tga`, `OKN.tga`, `PLU.tga`, `PSH.tga`, `PSR.tga`, `QUE.tga`, `RAP.tga`, `RHI.tga`, `RIG.tga`, `RJP.tga`, `RNG.tga`, `SAB.tga`, `SAR.tga`, `SIN.tga`, `SKK.tga`, `SNG.tga`, `SOK.tga`, `THU.tga`, `TML.tga`, `UBD.tga`, `VAN.tga`, `WIS.tga`, `WPG.tga`, `YUC.tga`

- `gfx/flags/small/` — `ANU.tga`, `ASY.tga`, `BAR.tga`, `BHR.tga`, `BIA.tga`, `BLC.tga`, `BOU.tga`, `BRN.tga`, `CBV.tga`, `CHM.tga`, `CHR.tga`, `CIP.tga`, `EVE.tga`, `EZO.tga`, `FOR.tga`, `FSA.tga`, `GAL.tga`, `GAR.tga`, `HBC.tga`, `HES.tga`, `HYD.tga`, `IAS.tga`, `IMO.tga`, `INC.tga`, `INU.tga`, `ITZ.tga`, `KAT.tga`, `KHL.tga`, `KLT.tga`, `KOL.tga`, `MAY.tga`, `MIS.tga`, `MPU.tga`, `MYS.tga`, `NAH.tga`, `NWF.tga`, `OKN.tga`, `PLU.tga`, `PSH.tga`, `QUE.tga`, `RAP.tga`, `RHI.tga`, `RIG.tga`, `RJP.tga`, `SAB.tga`, `SAR.tga`, `SIN.tga`, `SKK.tga`, `SNG.tga`, `SOK.tga`, `THU.tga`, `TML.tga`, `UBD.tga`, `WIS.tga`, `WPG.tga`, `YUC.tga`

## Remaining diagnostics

Runeterra and Azir diagnostics include 152 research grid entries, 228 invalid AI doctrine trigger calls, 19 missing custom textures, authored mission references, and old-save warnings. The launcher also reads two disabled Workshop descriptors, Coring Button and Toolpack+, whose publishers specify malformed version wildcards. Their metadata is independent of the active playset.

## Icathia save test PT-011

The 12:16 debug launch reached single-player on 1 January 990. The archived error log contained zero Belgian asset IDs, missing-mesh messages, duplicate tank textures, missing flags or invalid historical focus predicates. It still reported two Finnish texture errors, 26 missing infantry clone parents and 54 failed infantry attachments.

After the launch, the restored infantry definitions were placed after their parents inside the effective units_infantry.asset. Both Finnish mesh material bindings now use the shape in the installed model. Other follow-up changes removed the 30 Earth-only AI theater templates, retired the three Japanese landmark tooltip branches, and repaired inherited event, decision, tag and idea registrations. The old Icathia save now has a compatibility definition for its serialized Malaxa organization.

Only the local launcher descriptors for Coring Button and Toolpack+ were normalized from broad, invalid version wildcards to 1.20.* for this installation. The Workshop copies can regenerate those descriptors. Neither disabled mod was tested. Changes made after PT-011 have static verification only.
