@echo off
title md2nexus
cd ".."

"C:\Tools\md2nexus\md2nexus" -i "docs/description-md" -o "docs/description-nexus"
robocopy "docs\description-md" "docs\description-nexus" *.txt /it

