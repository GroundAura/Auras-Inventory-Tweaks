Hey everyone,
Thanks for taking an interest in AIT.

If you have any questions, problems, or want to make your own tweaks, read the pinned comments and the mod description first. You could also take a look at recent comments to see if your question has been answered recently. If you don't find the answers to your questions feel free to ask here or in [my Discord server](https://discord.gg/zft8DmbfKv). Also feel free to share any tweaks you make or suggestions you have and I might include them. Happy adventuring Dovahkiin!

\[color=#ffd966\]\[size=3\]**News:**\[/size\]\[/color\]
\[color=#93c47d\]**AIT v2 is out!**\[/color\]
I've completely rewritten the mod (again). It now uses an [Inventory Interface Information Injector](https://www.nexusmods.com/skyrimspecialedition/mods/85702) (I4) config to apply most of the data instead of config.txt. This should improve performance comparatively, and I4﻿ unlocks a lot of new options and features which I have utilized.
I've also created [Object Categorization Framework](https://www.nexusmods.com/skyrimspecialedition/mods/81469) (OCF), whose keywords I've utilized instead of creating AIT-exclusive keywords. OCF also has a lot more compatibility with modded items. **Make sure to keep OCF up to date as any updates I make to that will be utilized in AIT.** This means that updating OCF may dynamically add new item support which will show up in inventories, even if AIT itself doesn't need an update.

\[color=#ffd966\]\[size=3\]**Planned Features:**\[/size\]\[/color\]
\[spoiler\]

- Create additional icons.
- Make all info columns work regardless of what SWF files the user has. I have a couple ideas for this, but it might take a while.
- Make it so journals are detected by art object in a similar way to how notes are detected.
- Make a custom [Constructible Object Custom Keyword System](https://www.nexusmods.com/skyrimspecialedition/mods/81409) (COCKS) patch, utilizing OCF's keywords. I need to figure out a system for material keywords for OCF before I start on this.
- Reorganize the favorites menu to make it easier and more satisfying to use. Make it use AIT's sorting, maybe add new tabs, etc.
- Add language translations for unsupported languages. If anyone would be willing to help translate AIT so more people can enjoy it, get in touch with me through [my Discord](https://discord.gg/zft8DmbfKv) or Nexus PMs.
- Improve some of the icon colors for the lighter menu patches.
- Add item card and 3D item offset presets for MCM Helper.
- Update [QuickLoot EE](https://www.nexusmods.com/skyrimspecialedition/mods/69980)'s loot menu widget, [TrueHud](https://www.nexusmods.com/skyrimspecialedition/mods/62775)'s item pickup widget, and [iEquip](https://www.nexusmods.com/skyrimspecialedition/mods/27008)'s widget, to be fully compatible with AIT's new icons/types. It looks like Parapets is considering making an API so I4 configs can work with modded widgets like these, so I'll wait until I hear more about that.
- Figure out how to sort negative active effects on top.
- Look into displaying more survival data for more survival mods. The mods on my radar to look at are: [CC Survival Mode](https://en.uesp.net/wiki/Skyrim:Survival_Mode), [SunHelm](https://www.nexusmods.com/skyrimspecialedition/mods/39414), [Frostfall](https://www.nexusmods.com/skyrimspecialedition/mods/671), [Frostbite](https://www.nexusmods.com/skyrimspecialedition/mods/27693), [iNeed](https://www.nexusmods.com/skyrimspecialedition/mods/645)/[Continued](https://www.nexusmods.com/skyrimspecialedition/mods/19390), [ELAF Hypothermia](https://www.nexusmods.com/skyrimspecialedition/mods/78307), [Hypothermia Plus](https://www.nexusmods.com/skyrimspecialedition/mods/12809), [Immersive Needs](https://www.nexusmods.com/skyrimspecialedition/mods/29317), [Last Seed](https://www.nexusmods.com/skyrimspecialedition/mods/56393), [RND](https://www.nexusmods.com/skyrimspecialedition/mods/3487)/[2.0](https://www.nexusmods.com/skyrimspecialedition/mods/23799), [The Frozen North](https://www.nexusmods.com/skyrimspecialedition/mods/33068), [CACO](https://www.nexusmods.com/skyrimspecialedition/mods/19924), [CCSM - Realistic Food Hunger Points](https://www.nexusmods.com/skyrimspecialedition/mods/58853), [CCSM - Realistic Food Patch](https://www.nexusmods.com/skyrimspecialedition/mods/33291), [CCSM - Improved SKSE](https://www.nexusmods.com/skyrimspecialedition/mods/78244), [CCSM - Conner's Survival Mode](https://www.nexusmods.com/skyrimspecialedition/mods/19152), CCSM - Simple Survival Mode Tweaks.
\[/spoiler\]

\[color=#ffd966\]\[size=3\]**Equipped Items on Top:**\[/size\]\[/color\]
The way I have equipped items on top set up is state 2 of the icon column arrow. This means if you click the arrow above the icon column so that it's pointing [b]down[/b], equipped items (as well as unread books) are put on top. If you want to change sorting by equipped to the default behavior, just switch the 1st and 2nd states of the icon column.
[spoiler]
**Change this:**
```
; ICON COLUMN -------------------------------------------------------
columns.iconColumn.type = ITEM_ICON
columns.iconColumn.states = 2
columns.iconColumn.icon.size = n_iconSize
columns.iconColumn.border = a_iconBorder

columns.iconColumn.state1.label.text = ' '
columns.iconColumn.state1.label.arrowDown = false
columns.iconColumn.state1.sortAttributes = <'timeRemaining', 'effectIsDetrimental', 'magicSchool', 'itemType', 'itemClass', 'itemSort', 'armorClass', 'soulGemStats', 'magicClassDisplay', 'subTypeDisplay', 'weaponStats', 'armorStats', 'potionStats', 'scrollStats', 'foodStats', 'spellStats', 'cardName', 'text'>
columns.iconColumn.state1.sortOptions = <{ASCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {ASCENDING | CASEINSENSITIVE}, {ASCENDING | CASEINSENSITIVE}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {ASCENDING | CASEINSENSITIVE}, {ASCENDING | CASEINSENSITIVE}>

columns.iconColumn.state2.label.text = ' '
columns.iconColumn.state2.label.arrowDown = true
columns.iconColumn.state2.sortAttributes = <'isEquipped', 'isRead', 'timeRemaining', 'effectIsDetrimental', 'magicSchool', 'itemType', 'itemClass', 'itemSort', 'armorClass', 'soulGemStats', 'magicClassDisplay', 'subTypeDisplay', 'weaponStats', 'armorStats', 'potionStats', 'scrollStats', 'foodStats', 'spellStats', 'cardName', 'text'>
columns.iconColumn.state2.sortOptions = <{DESCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {ASCENDING | CASEINSENSITIVE}, {ASCENDING | CASEINSENSITIVE}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {ASCENDING | CASEINSENSITIVE}, {ASCENDING | CASEINSENSITIVE}>
```

**To this:**
```
; ICON COLUMN -------------------------------------------------------
columns.iconColumn.type = ITEM_ICON
columns.iconColumn.states = 2
columns.iconColumn.icon.size = n_iconSize
columns.iconColumn.border = a_iconBorder

columns.iconColumn.state1.label.text = ' '
columns.iconColumn.state1.label.arrowDown = true
columns.iconColumn.state1.sortAttributes = <'isEquipped', 'isRead', 'timeRemaining', 'effectIsDetrimental', 'magicSchool', 'itemType', 'itemClass', 'itemSort', 'armorClass', 'soulGemStats', 'magicClassDisplay', 'subTypeDisplay', 'weaponStats', 'armorStats', 'potionStats', 'scrollStats', 'foodStats', 'spellStats', 'cardName', 'text'>
columns.iconColumn.state1.sortOptions = <{DESCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {ASCENDING | CASEINSENSITIVE}, {ASCENDING | CASEINSENSITIVE}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {ASCENDING | CASEINSENSITIVE}, {ASCENDING | CASEINSENSITIVE}>

columns.iconColumn.state2.label.text = ' '
columns.iconColumn.state2.label.arrowDown = false
columns.iconColumn.state2.sortAttributes = <'timeRemaining', 'effectIsDetrimental', 'magicSchool', 'itemType', 'itemClass', 'itemSort', 'armorClass', 'soulGemStats', 'magicClassDisplay', 'subTypeDisplay', 'weaponStats', 'armorStats', 'potionStats', 'scrollStats', 'foodStats', 'spellStats', 'cardName', 'text'>
columns.iconColumn.state2.sortOptions = <{ASCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {ASCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {ASCENDING | CASEINSENSITIVE}, {ASCENDING | CASEINSENSITIVE}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {DESCENDING | NUMERIC}, {ASCENDING | CASEINSENSITIVE}, {ASCENDING | CASEINSENSITIVE}>
```
**Feel free to just copy the 2nd section of code and replace the 1st section of code if your config.txt.**
\[/spoiler\]