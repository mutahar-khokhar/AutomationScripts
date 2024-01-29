Get-ChildItem -Path "the/specified/path" -Filter *.mp3 | ForEach-Object {
    $newName = "Specified_Prefix" + $_.Name
    Rename-Item -Path $_.FullName -NewName $newName
}