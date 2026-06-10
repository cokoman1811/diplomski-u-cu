# Cursor hook: nakon zavrsetka agenta, posalji promjene na GitHub.
# Ne blokira agenta ako sync padne (npr. nema mreze).

$ErrorActionPreference = "SilentlyContinue"
[void][Console]::In.ReadToEnd()

$ProjectRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$SyncScript = Join-Path $ProjectRoot "scripts\git-sync.ps1"

if (Test-Path $SyncScript) {
    & powershell -NoProfile -ExecutionPolicy Bypass -File $SyncScript -Quiet
}

exit 0
