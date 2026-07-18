# SkyUI Columns

## SkyUI (Default)

equipColumn
iconColumn

itemNameColumn
arColumn
subTypeColumn
materialColumn
classColumn
magnitudeColumn
durationColumn
magicMagnitudeColumn
magicDurationColumn
damageColumn
weightColumn
valueColumn
valueWeightColumn
magicNameColumn
spellCostColumn
word0Column
word1Column
word2Column
schoolColumn
levelColumn
timeRemainingColumn
effectItemColumn
craftNameColumn
disenchantEffectColumn
soulSizeColumn
alchWeightColumn
alchValueColumn
alchValueWeightColumn



[ITEM VIEWS]
equipColumn, iconColumn, itemNameColumn, [DEFAULT]
subTypeColumn, [DEFAULT, -KEYS]
    materialColumn, damageColumn, [WEAPONS]
    classColumn, materialColumn, arColumn, [ARMOR]
    magnitudeColumn, durationColumn, [POTIONS, SCROLLS]
weightColumn, valueColumn, valueWeightColumn [DEFAULT]


[MAGIC VIEWS]
equipColumn, iconColumn, magicNameColumn, [DEFAULT]
    schoolColumn, [ALL/FAVORITES]
    levelColumn, [ALL/FAVORITES, SPELLS]
    magicMagnitudeColumn, [SPELLS]
    magicDurationColumn, [SPELLS, POWERS]
    spellCostColumn [ALL/FAVORITES, SPELLS, POWERS]
    word0Column, word1Column, word2Column [SHOUTS]
    timeRemainingColumn, effectItemColumn [EFFECTS]


[CRAFTING VIEWS]
equipColumn, iconColumn, craftNameColumn, [DEFAULT]
    disenchantEffectColumn, [DISENCHANT]
    materialColumn, [ENCHANT_ITEM, CRAFT_WEAPON, CRAFT_ARMOR]
    damageColumn, [CRAFT_WEAPON]
    soulSizeColumn, [CRAFT_ARMOR]
subTypeColumn, [DEFAULT, -ENCHANTMENT, -ALCHEMY]
weightColumn, valueColumn, valueWeightColumn [DEFAULT, -ENCHANTMENT, -ALCHEMY]
    alchWeightColumn, alchValueColumn, alchValueWeightColumn [ALCHEMY]



## AIT (v4.5.0)

itemNameColumn
itemSubTypeColumn
itemValColumn
itemTValColumn
itemValWtColumn
itemWtColumn
itemTWtColumn

gearNameColumn
gearMaterialColumn

weaponEquipColumn
weaponDamageColumn
weaponBaseDamageColumn
weaponCritDamageColumn
weaponReachColumn
weaponSpeedColumn
weaponStaggerColumn

armorRatingColumn
armorBaseRatingColumn
armorSlotsColumn
armorClassColumn
armorCCWarmthColumn
armorFFWarmthColumn
armorFFCoverageColumn
armorSHWarmthColumn

// itemResistColumn
itemMagnitudeColumn
itemDurationColumn

foodCCHungerColumn
foodCCRestoreColdColumn
foodCCFortifyWarmthColumn
foodSHHungerColumn
foodSHThirstColumn
foodSHFortifyWarmthColumn
foodGreenPactColumn

bookNameColumn


magicNameColumn
allMagicSchoolColumn
allMagicMagnitudeColumn
allMagicDurationColumn
allMagicCostColumn
magicClassColumn
magicSubTypeColumn
magicLevelColumn
magicMagnitudeColumn

// spellResistColumn
spellDurationColumn
spellCostColumn

powerDurationColumn
powerCostColumn
// powerCooldownColumn

shoutWord1Column
shoutWord2Column
shoutWord3Column

effectSourceColumn
effectDurationColumn


craftNameColumn
craftSubTypeColumn
craftValColumn
craftValWtColumn
craftWtColumn

enchantEffectColumn
enchantSoulColumn

alchValColumn
alchTValColumn
alchValWtColumn
alchWtColumn
alchTWtColumn



[ITEM VIEWS]
equipColumn, iconColumn, [DEFAULT]
    gearNameColumn, [FAVORITES, ALL, WEAPONS, ARMOR]
itemNameColumn, [POTIONS, SCROLLS, FOOD, INGREDIENTS, KEYS, MISC]
    bookNameColumn, [BOOKS]
    itemSubTypeColumn [DEFAULT]
    armorClassColumn [ARMOR]
    gearMaterialColumn [WEAPONS, ARMOR]
    weaponEquipColumn, weaponDamageColumn, weaponBaseDamageColumn, weaponCritDamageColumn, weaponSpeedColumn, weaponReachColumn, weaponStaggerColumn, [WEAPONS]
    armorSlotsColumn, armorRatingColumn, armorBaseRatingColumn, armorCCWarmthColumn, armorSHWarmthColumn, armorFFWarmthColumn, armorFFCoverageColumn, [ARMOR]
    itemMagnitudeColumn, itemDurationColumn, [POTIONS, SCROLLS]
    foodGreenPactColumn, [FOOD, INGREDIENTS]
    foodCCHungerColumn, foodCCRestoreColdColumn, foodCCFortifyWarmthColumn, foodSHHungerColumn, foodSHThirstColumn, foodSHFortifyWarmthColumn, [FOOD]
itemValColumn, itemTValColumn, itemValWtColumn, itemWtColumn, itemTWtColumn [DEFAULT]


[MAGIC VIEWS]
equipColumn, iconColumn, magicNameColumn, [DEFAULT]
magicSubTypeColumn, magicClassColumn, [ALL, FAVORITES, SPELLS, POWERS]
    allMagicSchoolColumn, [ALL, FAVORITES]
magicLevelColumn [ALL, FAVORITES, SPELLS, POWERS]
    allMagicMagnitudeColumn, allMagicDurationColumn, allMagicCostColumn [ALL, FAVORITES]
    magicMagnitudeColumn, spellDurationColumn, spellCostColumn [SPELLS]
    shoutWord1Column, shoutWord2Column, shoutWord3Column [SHOUTS]
    powerDurationColumn, powerCostColumn [POWERS]
    effectDurationColumn, effectSourceColumn [EFFECTS]


[CRAFTING VIEWS]
equipColumn, iconColumn, [DEFAULT]
itemNameColumn, [DISENCHANT, ENCHANTMENT, SOULGEM]
    gearNameColumn, [DEFAULT, WEAPONS, ARMOR]
    craftNameColumn [ENCHANTMENT]
    enchantEffectColumn, [DISENCHANT]
craftSubTypeColumn, craftValColumn, craftValWtColumn, craftWtColumn [DEFAULT/COCKS]
itemSubTypeColumn, [DISENCHANT, ENCHANT_ITEM, CRAFT_WEAPON, CRAFT_ARMOR]
    enchantSoulColumn, [ENCHANT_SOULGEM]
    armorClassColumn, [CRAFT_ARMOR]
    gearMaterialColumn, [ENCHANT_ITEM, CRAFT_WEAPON, CRAFT_ARMOR]
    weaponDamageColumn, weaponBaseDamageColumn, weaponCritDamageColumn, weaponSpeedColumn, weaponReachColumn, weaponStaggerColumn, [CRAFT_WEAPON]
    armorSlotsColumn, armorRatingColumn, armorBaseRatingColumn, armorCCWarmthColumn, armorSHWarmthColumn, armorFFWarmthColumn, armorFFCoverageColumn, [CRAFT_ARMOR]
itemValColumn, itemTValColumn, itemValWtColumn, itemWtColumn, itemTWtColumn [DISENCHANT, ENCHANT_ITEM, ENCHANT_SOULGEM, CRAFT_WEAPON, CRAFT_ARMOR]


