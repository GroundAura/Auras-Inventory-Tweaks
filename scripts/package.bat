@echo off
title package
cd ".."

copy "docs\images\brand\Main.png" "dist\Aura's Inventory Tweaks\fomod\images"

del "build\Aura's Inventory Tweaks.zip"
cd "dist\Aura's Inventory Tweaks"
"C:\Program Files\7-Zip\7z" a -tzip "..\..\build\Aura's Inventory Tweaks.zip"
cd "..\.."

copy "build\Aura's Inventory Tweaks.zip" "D:\Games\Bethesda\Elder Scrolls\Skyrim\MO2\downloads"
copy "build\MO2\Aura's Inventory Tweaks.zip.meta" "D:\Games\Bethesda\Elder Scrolls\Skyrim\MO2\downloads"

