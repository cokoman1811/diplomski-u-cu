#Requires -Version 5.1
<#
.SYNOPSIS
    Commit + push svih promjena na GitHub (diplomski-u-cu).

.EXAMPLE
    .\scripts\git-sync.ps1
    .\scripts\git-sync.ps1 -CommitMessage "Dodani testovi"
    .\scripts\git-sync.ps1 -Quiet
    .\scripts\git-sync.ps1 -SetupRemote
#>
param(
    [switch]$Quiet,
    [switch]$SetupRemote,
    [string]$RemoteUrl = "",
    [string]$CommitMessage = ""
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $ProjectRoot

$DefaultRemote = "https://github.com/cokoman1811/diplomski-u-cu.git"

function Write-Info([string]$Message) {
    if (-not $Quiet) { Write-Host $Message }
}

function Invoke-Git {
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$GitArgs)

    $previousPreference = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    $output = & git @GitArgs 2>&1
    $exitCode = $LASTEXITCODE
    $ErrorActionPreference = $previousPreference

    if ($exitCode -ne 0) {
        $detail = ($output | Out-String).Trim()
        if ($detail) {
            throw "git $($GitArgs -join ' ') nije uspio (exit $exitCode): $detail"
        }
        throw "git $($GitArgs -join ' ') nije uspio (exit $exitCode)."
    }
}

function Get-RemoteUrl {
    try {
        return (git remote get-url origin 2>$null)
    } catch {
        return $null
    }
}

if (-not (Test-Path ".git")) {
    Write-Info "Inicijaliziram git repozitorij..."
    git init | Out-Null
    git branch -M main 2>$null
}

if ($SetupRemote -or (-not (Get-RemoteUrl) -and $RemoteUrl)) {
    $url = if ($RemoteUrl) { $RemoteUrl } else { $DefaultRemote }
    if (Get-RemoteUrl) {
        git remote set-url origin $url
    } else {
        git remote add origin $url
    }
    Write-Info "Remote postavljen: $url"
} elseif (-not (Get-RemoteUrl)) {
    git remote add origin $DefaultRemote 2>$null
    if (Get-RemoteUrl) {
        Write-Info "Remote postavljen: $DefaultRemote"
    }
}

git add -A

$status = git status --porcelain
if (-not $status) {
    Write-Info "Nema promjena za commit."
    $remote = Get-RemoteUrl
    if ($remote) {
        Invoke-Git fetch origin
        Invoke-Git pull --rebase origin main
        Invoke-Git push -u origin main
        Write-Info "Sync OK (bez novih commita)."
    }
    exit 0
}

if (-not $CommitMessage) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
    $CommitMessage = "Auto-sync: $timestamp"
}

$env:GIT_AUTHOR_NAME = "Toni Jakelic"
$env:GIT_AUTHOR_EMAIL = "jakelictoni@gmail.com"
$env:GIT_COMMITTER_NAME = "Toni Jakelic"
$env:GIT_COMMITTER_EMAIL = "jakelictoni@gmail.com"

git commit -m $CommitMessage
if ($LASTEXITCODE -ne 0) { throw "Commit nije uspio." }

Write-Info "Commit: $CommitMessage"

$remote = Get-RemoteUrl
if (-not $remote) {
    Write-Info "Commit lokalno spremljen. Za upload pokreni -SetupRemote."
    exit 0
}

Invoke-Git fetch origin
Invoke-Git pull --rebase origin main
Invoke-Git push -u origin main

Write-Info "Upload na GitHub uspjesan: $remote"
