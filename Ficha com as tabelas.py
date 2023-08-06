import os
txt='''{
    "schema_version": 2,
    "oldId": "-MKMNILZ9jPt84VX2ExT",
    "name": "Tabelas",
    "avatar": "",
    "bio": "",
    "gmnotes": "",
    "defaulttoken": "",
    "tags": "[]",
    "controlledby": "all",
    "inplayerjournals": "",
    "attribs": [
        {
            "name": "Untitled",
            "current": "@{whispertoggle}",
            "max": "",
            "id": "-MKMNINUa41MsnAMe9HW"
        },
        {
            "name": "Untitled",
            "current": "@{whispertoggle}",
            "max": "",
            "id": "-MKMNINW7i7Nuy9ha6T1"
        },
        {
            "name": "ac",
            "current": 10,
            "max": "",
            "id": "-MKMNINW7i7Nuy9ha6T0"
        },
        {
            "name": "acrobatics_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINPCxgSfRd6OUtr"
        },
        {
            "name": "animal_handling_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINRivsRNvs6M8F9"
        },
        {
            "name": "appliedUpdates",
            "current": "upgrade_to_2_9,upgrade_to_4_2_1,fix_npc_missing_attack_display_flag_attribute,fix_npc_version_number,fix_npcs_in_modules_saves_and_ability_mods,fix_spell_attacks,fix_npc_actions_to_support_translation,fix_npc_attacks,fix_npc_attacks_with_auto_damage_roll,fix_npc_actions_with_damage,fix_spell_school_ouput",
            "max": "",
            "id": "-MKMNINXlMgZ16dfdLF_"
        },
        {
            "name": "arcana_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINQxMNA-z18lr5i"
        },
        {
            "name": "armorwarningflag",
            "current": "hide",
            "max": "",
            "id": "-MKMNINW7i7Nuy9ha6Sz"
        },
        {
            "name": "athletics_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINPCxgSfRd6OUtq"
        },
        {
            "name": "caster_level",
            "current": 0,
            "max": "",
            "id": "-MKMNINHM_Qfs05PMtQe"
        },
        {
            "name": "charisma_mod",
            "current": 0,
            "max": "",
            "id": "-MKMNINZEApKGiyKGp1L"
        },
        {
            "name": "charisma_save_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINPCxgSfRd6OUto"
        },
        {
            "name": "class_display",
            "current": " 1",
            "max": "",
            "id": "-MKMNINIHI2RKSZ2tAaZ"
        },
        {
            "name": "constitution_mod",
            "current": 0,
            "max": "",
            "id": "-MKMNINYEb2NdkGwZW8W"
        },
        {
            "name": "constitution_save_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINOtDjSC1w7ydWD"
        },
        {
            "name": "customacwarningflag",
            "current": "hide",
            "max": "",
            "id": "-MKMNINW7i7Nuy9ha6T-"
        },
        {
            "name": "death_save_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINPCxgSfRd6OUtp"
        },
        {
            "name": "deception_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINT0vad1mkQeYPB"
        },
        {
            "name": "dexterity_mod",
            "current": 0,
            "max": "",
            "id": "-MKMNINYEb2NdkGwZW8V"
        },
        {
            "name": "dexterity_save_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINOtDjSC1w7ydWC"
        },
        {
            "name": "global_attack_mod",
            "current": "",
            "max": "",
            "id": "-MKMNINVfqK60eQykT-q"
        },
        {
            "name": "global_damage_mod_crit",
            "current": "",
            "max": "",
            "id": "-MKMNINVfqK60eQykT-s"
        },
        {
            "name": "global_damage_mod_roll",
            "current": "",
            "max": "",
            "id": "-MKMNINVfqK60eQykT-r"
        },
        {
            "name": "global_damage_mod_type",
            "current": "",
            "max": "",
            "id": "-MKMNINVfqK60eQykT-t"
        },
        {
            "name": "global_save_mod",
            "current": "",
            "max": "",
            "id": "-MKMNINUa41MsnAMe9HY"
        },
        {
            "name": "global_skill_mod",
            "current": "",
            "max": "",
            "id": "-MKMNINUa41MsnAMe9HX"
        },
        {
            "name": "history_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINQxMNA-z18lr5j"
        },
        {
            "name": "hit_dice",
            "current": "",
            "max": 1,
            "id": "-MKMNINIHI2RKSZ2tAa_"
        },
        {
            "name": "hitdie_final",
            "current": "@{hitdietype}",
            "max": "",
            "id": "-MKMNINHM_Qfs05PMtQc"
        },
        {
            "name": "initiative_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINN7yWQYazoQBQv"
        },
        {
            "name": "insight_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINRivsRNvs6M8FA"
        },
        {
            "name": "intelligence_mod",
            "current": 0,
            "max": "",
            "id": "-MKMNINYEb2NdkGwZW8X"
        },
        {
            "name": "intelligence_save_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINOtDjSC1w7ydWE"
        },
        {
            "name": "intimidation_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINT0vad1mkQeYPC"
        },
        {
            "name": "invalidXP",
            "current": 0,
            "max": "",
            "id": "-MKMNINXlMgZ16dfdLFZ"
        },
        {
            "name": "investigation_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINQxMNA-z18lr5k"
        },
        {
            "name": "jack",
            "current": 1,
            "max": "",
            "id": "-MKMNINL6skEANqA0wCP"
        },
        {
            "name": "jack_attr",
            "current": "",
            "max": "",
            "id": "-MKMNINN7yWQYazoQBQu"
        },
        {
            "name": "jack_bonus",
            "current": "",
            "max": "",
            "id": "-MKMNINN7yWQYazoQBQt"
        },
        {
            "name": "l1mancer_status",
            "current": "completed",
            "max": "",
            "id": "-MKMNING1yqnLFZbhOqY"
        },
        {
            "name": "level",
            "current": 1,
            "max": "",
            "id": "-MKMNINHM_Qfs05PMtQd"
        },
        {
            "name": "lvl1_slots_total",
            "current": 0,
            "max": "",
            "id": "-MKMNINIHI2RKSZ2tAab"
        },
        {
            "name": "lvl2_slots_total",
            "current": 0,
            "max": "",
            "id": "-MKMNINJRu8L_oGHZ_78"
        },
        {
            "name": "lvl3_slots_total",
            "current": 0,
            "max": "",
            "id": "-MKMNINJRu8L_oGHZ_79"
        },
        {
            "name": "lvl4_slots_total",
            "current": 0,
            "max": "",
            "id": "-MKMNINJRu8L_oGHZ_7A"
        },
        {
            "name": "lvl5_slots_total",
            "current": 0,
            "max": "",
            "id": "-MKMNINJRu8L_oGHZ_7B"
        },
        {
            "name": "lvl6_slots_total",
            "current": 0,
            "max": "",
            "id": "-MKMNINJRu8L_oGHZ_7C"
        },
        {
            "name": "lvl7_slots_total",
            "current": 0,
            "max": "",
            "id": "-MKMNINKpnVlMzQ6kUB6"
        },
        {
            "name": "lvl8_slots_total",
            "current": 0,
            "max": "",
            "id": "-MKMNINKpnVlMzQ6kUB7"
        },
        {
            "name": "lvl9_slots_total",
            "current": 0,
            "max": "",
            "id": "-MKMNINKpnVlMzQ6kUB8"
        },
        {
            "name": "medicine_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINSshBKnFpyfs_F"
        },
        {
            "name": "nature_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINRivsRNvs6M8F7"
        },
        {
            "name": "npc",
            "current": "1",
            "max": "",
            "id": "-MKMNINFUU-wcdDLOvql"
        },
        {
            "name": "npc_name_flag",
            "current": "{{name=@{npc_name}}}",
            "max": "",
            "id": "-MKMNING1yqnLFZbhOqW"
        },
        {
            "name": "npc_options-flag",
            "current": "0",
            "max": "",
            "id": "-MKMNINXlMgZ16dfdLFX"
        },
        {
            "name": "options-class-selection",
            "current": "0",
            "max": "",
            "id": "-MKMNING1yqnLFZbhOqZ"
        },
        {
            "name": "passive_wisdom",
            "current": 10,
            "max": "",
            "id": "-MKMNINUa41MsnAMe9HV"
        },
        {
            "name": "pb",
            "current": "2",
            "max": "",
            "id": "-MKMNINKpnVlMzQ6kUB9"
        },
        {
            "name": "pbd_safe",
            "current": "",
            "max": "",
            "id": "-MKMNINMONVkm_lxKSZH"
        },
        {
            "name": "perception_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINSshBKnFpyfs_G"
        },
        {
            "name": "performance_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINT0vad1mkQeYPD"
        },
        {
            "name": "persuasion_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINT0vad1mkQeYPE"
        },
        {
            "name": "race_display",
            "current": "",
            "max": "",
            "id": "-MKMNINIHI2RKSZ2tAaa"
        },
        {
            "name": "religion_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINRivsRNvs6M8F8"
        },
        {
            "name": "rtype",
            "current": "@{advantagetoggle}",
            "max": "",
            "id": "-MKMNINFUU-wcdDLOvqm"
        },
        {
            "name": "showleveler",
            "current": 0,
            "max": "",
            "id": "-MKMNINXlMgZ16dfdLFY"
        },
        {
            "name": "sleight_of_hand_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINQxMNA-z18lr5g"
        },
        {
            "name": "spell_attack_bonus",
            "current": "0",
            "max": "",
            "id": "-MKMNINMONVkm_lxKSZI"
        },
        {
            "name": "spell_save_dc",
            "current": "0",
            "max": "",
            "id": "-MKMNINN7yWQYazoQBQs"
        },
        {
            "name": "stealth_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINQxMNA-z18lr5h"
        },
        {
            "name": "strength_mod",
            "current": 0,
            "max": "",
            "id": "-MKMNINYEb2NdkGwZW8U"
        },
        {
            "name": "strength_save_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINN7yWQYazoQBQw"
        },
        {
            "name": "survival_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINSshBKnFpyfs_H"
        },
        {
            "name": "version",
            "current": 4.21,
            "max": "",
            "id": "-MKMNING1yqnLFZbhOqX"
        },
        {
            "name": "wisdom_mod",
            "current": 0,
            "max": "",
            "id": "-MKMNINZEApKGiyKGp1K"
        },
        {
            "name": "wisdom_save_bonus",
            "current": 0,
            "max": "",
            "id": "-MKMNINOtDjSC1w7ydWF"
        }
    ],
    "abilities": [
        {
            "name": "-------Tabelas-----",
            "description": "",
            "istokenaction": false,
            "action": "",
            "order": -1
        }'''

excesion=('txt')
for root, dirs, files in os.walk('.'):
     for name_table in files:
        if name_table.split(".")[-1] in excesion:
            name_table=os.path.splitext(os.path.basename(open(name_table).name))[0]
            txt=txt+''',
        {
            "name": "'''+name_table+'''",
            "description": "",
            "istokenaction": false,
            "action": "&{template:npcaction} {{rname='''+name_table+'''}} } {{description= [1t['''+name_table+''']]}}",
            "order": -1
        }'''

txt=txt+'''
        
    ]
}
'''

with open(os.path.join(".","Tabelas.json"),"w",encoding='utf8') as my_file:
    my_file.write(txt)