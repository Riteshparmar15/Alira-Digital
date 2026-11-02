@echo off
echo ========================================================
echo   Pushing Alira Digital to GitHub: Riteshparmar15/Alira-Digital
echo ========================================================
git branch -M main
git push -u origin main
echo.
echo If the push was successful, your site is being deployed via GitHub Actions!
echo Check your deployment status here:
echo https://github.com/Riteshparmar15/Alira-Digital/actions
echo.
pause

