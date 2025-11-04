gci * -Include *.wav -Recurse | %{
    $_.Name
    &ffprobe $_.FullName '-show_entries' 'format=duration' '-v' 'quiet' '-of' 'csv="p=0"'
}