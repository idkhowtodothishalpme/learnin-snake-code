$chance = Get-Random -Minimum 1 -Maximum 25

if ($chance -eq 1) {

$delaySeconds = Get-Random -Minimum 0 -Maximum 6000

Start-Sleep -Seconds $delaySeconds

Start-Process "chrome.exe" "https://www.youtube.com/watch?v=32FB-gYr49Y"