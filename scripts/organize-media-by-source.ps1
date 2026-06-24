param(
    [string]$SourceRoot = 'D:\slike sve',
    [string]$ImageDestRoot = 'D:\media-po-izvoru',
    [string]$VideoDestRoot = 'D:\media-po-izvoru-video',
    [string]$MediaDesktop = '',
    [int]$Throttle = 8
)

$ErrorActionPreference = 'Stop'
if (-not $MediaDesktop) {
    $MediaDesktop = (Get-Item 'C:\Users\ToniJakeli*\Desktop\media' -ErrorAction Stop).FullName
}

$imgExt = @('.jpg','.jpeg','.png','.gif','.webp','.bmp','.heic','.heif','.tif','.tiff','.raw','.cr2','.nef','.dng')
$vidExt = @('.mp4','.mov','.avi','.mkv','.wmv','.m4v','.3gp','.webm','.mpeg','.mpg')
$allExt = $imgExt + $vidExt

function Get-SourceCategory {
    param([string]$FullPath, [string]$FileName)
    $p = $FullPath.Replace('/', '\').ToLowerInvariant()
    $f = $FileName.ToLowerInvariant()
    if ($p -match 'snimka zaslona|snimke zaslona|\\screenshots\\|\\screenshot\\') { return 'screenshot' }
    if ($f -match '^screenshot|^snimka') { return 'screenshot' }
    if ($p -match 'whatsapp|whatsapp images') { return 'whatsapp' }
    if ($f -match '^wa\d{4}|img-\d{4}-wa') { return 'whatsapp' }
    if ($p -match 'viber') { return 'viber' }
    if ($p -match 'telegram') { return 'telegram' }
    if ($p -match 'instagram') { return 'instagram' }
    if ($p -match '\\downloads\\|\\download\\') { return 'download' }
    if ($p -match '\\dcim\\|\\camera\\|\\100media\\|\\100andro\\') { return 'camera' }
    if ($f -match '^(img_|dsc|dsc_|mvimg_)') { return 'camera' }
    if ($f -match '^\d{8}_\d{6}') { return 'camera' }
    return 'ostalo'
}

function Get-UniqueDestPath([string]$Dir, [string]$BaseName) {
    $dest = Join-Path $Dir $BaseName
    if (-not (Test-Path -LiteralPath $dest)) { return $dest }
    $stem = [IO.Path]::GetFileNameWithoutExtension($BaseName)
    $ext = [IO.Path]::GetExtension($BaseName)
    for ($n = 1; $n -lt 10000; $n++) {
        $candidate = Join-Path $Dir ("{0}_{1}{2}" -f $stem, $n, $ext)
        if (-not (Test-Path -LiteralPath $candidate)) { return $candidate }
    }
    throw "Too many name collisions in $Dir for $BaseName"
}

function Ensure-Junction([string]$Link, [string]$Target) {
    if (Test-Path -LiteralPath $Link) {
        $item = Get-Item -LiteralPath $Link -Force
        if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { return }
        throw "Not a junction: $Link"
    }
    New-Item -ItemType Junction -Path $Link -Target $Target | Out-Null
}

if (-not (Test-Path -LiteralPath $SourceRoot)) { throw "Missing $SourceRoot" }
New-Item -ItemType Directory -Force -Path $ImageDestRoot, $VideoDestRoot | Out-Null

Write-Host "Building duplicate index..."
$dup = [System.Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
foreach ($root in @($MediaDesktop, $ImageDestRoot, $VideoDestRoot)) {
    if (-not (Test-Path -LiteralPath $root)) { continue }
    [System.IO.Directory]::EnumerateFiles($root, '*', [IO.SearchOption]::AllDirectories) | ForEach-Object {
        $fi = [IO.FileInfo]::new($_)
        [void]$dup.Add("$($fi.Name)|$($fi.Length)")
    }
}
Write-Host "Index size: $($dup.Count)"

$stats = @{ copied_img=0; copied_vid=0; skip_small=0; skip_dup=0; errors=0 }
$bySource = @{}
$createdDirs = @{}

$files = foreach ($e in $allExt) {
    $pat = "*" + $e
    [System.IO.Directory]::EnumerateFiles($SourceRoot, $pat, [IO.SearchOption]::AllDirectories)
}
$i = 0
foreach ($path in $files) {
    $i++
    if ($i % 10000 -eq 0) { Write-Host "Scan $i ... copied img=$($stats.copied_img) vid=$($stats.copied_vid)" }

    $ext = [IO.Path]::GetExtension($path).ToLowerInvariant()
    if ($allExt -notcontains $ext) { continue }

    $fi = [IO.FileInfo]::new($path)
    if ($fi.Length -lt 1024) { $stats.skip_small++; continue }

    $key = "$($fi.Name)|$($fi.Length)"
    if ($dup.Contains($key)) { $stats.skip_dup++; continue }

    $source = Get-SourceCategory $fi.FullName $fi.Name
    $year = $fi.LastWriteTime.Year
    if ($year -lt 1990 -or $year -gt 2030) { $year = $fi.CreationTime.Year }

    $isImg = $imgExt -contains $ext
    $rootDest = if ($isImg) { $ImageDestRoot } else { $VideoDestRoot }
    $destDir = Join-Path (Join-Path $rootDest $source) $year.ToString()
    if (-not $createdDirs.ContainsKey($destDir)) {
        [void][IO.Directory]::CreateDirectory($destDir)
        $createdDirs[$destDir] = $true
    }

    $destPath = Get-UniqueDestPath $destDir $fi.Name
    try {
        [IO.File]::Copy($fi.FullName, $destPath, $false)
        [void]$dup.Add($key)
        if (-not $bySource.ContainsKey($source)) { $bySource[$source] = @{ img=0; vid=0 } }
        if ($isImg) { $stats.copied_img++; $bySource[$source].img++ } else { $stats.copied_vid++; $bySource[$source].vid++ }
    } catch {
        $stats.errors++
        Write-Warning "Copy failed: $($fi.FullName) -> $destPath : $_"
    }
}

Ensure-Junction (Join-Path $MediaDesktop 'po-izvoru') $ImageDestRoot
Ensure-Junction (Join-Path $MediaDesktop 'video\po-izvoru') $VideoDestRoot

$report = [ordered]@{
    generated = (Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
    sourceRoot = $SourceRoot
    imageDestRoot = $ImageDestRoot
    videoDestRoot = $VideoDestRoot
    stats = $stats
    bySourceCopied = $bySource
}
$reportPath = Join-Path $MediaDesktop 'po-izvoru-stats.json'
$report | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $reportPath -Encoding UTF8
Write-Host ($report | ConvertTo-Json -Depth 6)

