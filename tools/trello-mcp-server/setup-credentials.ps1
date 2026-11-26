# One-time helper: opens Trello's key page, then saves the key + token as user environment variables.
# Input is hidden and never written to any file in the repo.
Start-Process "https://trello.com/power-ups/admin"
Write-Host "1) In the browser: New -> name it 'Claude', workspace 'Cold Code', any email, URL https://example.com"
Write-Host "2) Open the 'API key' tab -> 'Generate a new API Key' -> copy the key"
Write-Host ""
$k = Read-Host "Paste API key" -AsSecureString
$key = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($k))
Start-Process "https://trello.com/1/authorize?expiration=never&scope=read,write&response_type=token&name=Claude&key=$key"
Write-Host "3) In the browser click Allow, then copy the long token shown."
$t = Read-Host "Paste token" -AsSecureString
$token = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($t))
[Environment]::SetEnvironmentVariable("TRELLO_API_KEY", $key, "User")
[Environment]::SetEnvironmentVariable("TRELLO_TOKEN", $token, "User")
Write-Host "Saved. Restart Claude Code and Codex."
