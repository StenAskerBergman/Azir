[CmdletBinding()]
param(
    [ValidateSet('Auto', 'Save', 'Fresh', 'Menu')]
    [string]$Mode = 'Auto',
    [ValidatePattern('^[A-Z0-9]{3}$')]
    [string]$Country = 'VOI',
    [string]$Save,
    [switch]$GameDebug,
    [switch]$Preview,
    [string]$GameDirectory = 'E:/SteamLibrary/steamapps/common/Hearts of Iron IV',
    [string]$CandidateDirectory
)

$ErrorActionPreference = 'Stop'
$userDirectory = (Resolve-Path (Join-Path $PSScriptRoot '../../..')).Path
$saveDirectory = Join-Path $userDirectory 'save games'
$continueFile = Join-Path $userDirectory 'continue_game.json'
$exe = Join-Path $GameDirectory 'hoi4.exe'
if (-not (Test-Path -LiteralPath $exe -PathType Leaf)) { throw "HOI4 executable missing: $exe" }
if ($Save -and $Mode -in 'Fresh', 'Menu') { throw '-Save requires Auto or Save mode.' }

$selected = $null
if ($Save) {
    if ([IO.Path]::GetFileName($Save) -ne $Save -or $Save -notlike '*.hoi4') {
        throw '-Save must be a .hoi4 filename in the local save games folder.'
    }
    $selected = Get-Item -LiteralPath (Join-Path $saveDirectory $Save)
    if ($selected.PSIsContainer) { throw '-Save must name a save file.' }
} elseif ($Mode -in 'Auto', 'Save') {
    $selected = Get-ChildItem -LiteralPath $saveDirectory -Filter "${Country}_*.hoi4" -File -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTimeUtc, Name -Descending | Select-Object -First 1
}
if ($Mode -eq 'Save' -and -not $selected) { throw "No prepared $Country save found." }

$launchArguments = @()
if ($GameDebug) { $launchArguments += '-debug' }
if ($selected) {
    $launchArguments += '-continuelastsave'
    Write-Host "Resume $($selected.Name)"
} elseif ($Mode -ne 'Menu') {
    $launchArguments += "-start_tag=$Country"
    Write-Host "Start a fresh game as $Country"
} else {
    Write-Host 'Open the main menu'
}
Write-Host "Arguments: $($launchArguments -join ' ')"
if ($CandidateDirectory) {
    $candidate = Get-Item -LiteralPath $CandidateDirectory
    $bundle = Join-Path $candidate.FullName 'RuneterraSprint'
    if (-not (Test-Path -LiteralPath (Join-Path $candidate.FullName 'build-receipt.json') -PathType Leaf) -or
        -not (Test-Path -LiteralPath (Join-Path $bundle 'descriptor.mod') -PathType Leaf)) {
        throw "Expected a frozen sprint candidate in $CandidateDirectory."
    }

    $settings = Get-Content -LiteralPath (Join-Path $userDirectory 'dlc_load.json') -Raw | ConvertFrom-Json
    $enabled = @($settings.enabled_mods | Where-Object { $_ })
    if ($enabled.Count -ne 1) {
        throw "Select only $($candidate.Name) in the launcher. Saved playset contains $($enabled.Count) enabled mods: $($enabled -join ', ')."
    }
    $descriptor = Join-Path $userDirectory $enabled[0]
    $target = @(Select-String -LiteralPath $descriptor -Pattern '^\s*path\s*=\s*"([^"]+)"\s*$')
    if ($target.Count -ne 1) { throw "Expected one package path in $descriptor." }
    $selectedPath = $target[0].Matches[0].Groups[1].Value
    $resolvedTarget = [IO.Path]::GetFullPath($selectedPath, $userDirectory)
    if ($resolvedTarget.TrimEnd('\', '/') -ne $bundle) {
        throw "Saved playset selects $resolvedTarget. Select only $bundle to test $($candidate.Name)."
    }
    Write-Host "Saved playset selects $($candidate.Name) only ($($enabled[0]))."
}
if ($Preview) { return }
if (Get-Process hoi4 -ErrorAction SilentlyContinue) {
    throw 'HOI4 is already running. Exit it before launching a different test session.'
}

if ($selected) {
    $current = if (Test-Path -LiteralPath $continueFile) {
        Get-Content -LiteralPath $continueFile -Raw | ConvertFrom-Json
    }
    if ($current.filename -ne $selected.Name -or $current.is_remote) {
        if (Test-Path -LiteralPath $continueFile) {
            Copy-Item -LiteralPath $continueFile -Destination "$continueFile.azir-previous"
        }
        $pointer = @{
            title = $selected.BaseName
            desc = ''
            date = $selected.LastWriteTime.ToString('ddd MMM d HH:mm:ss yyyy', [Globalization.CultureInfo]::InvariantCulture)
            filename = $selected.Name
            is_remote = $false
        } | ConvertTo-Json
        [IO.File]::WriteAllText($continueFile, $pointer)
    }
}

$launch = @{ FilePath = $exe; WorkingDirectory = $GameDirectory; WindowStyle = 'Normal' }
if ($launchArguments.Count) { $launch.ArgumentList = $launchArguments }
Start-Process @launch
