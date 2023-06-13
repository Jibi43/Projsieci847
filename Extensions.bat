@echo off

setlocal enabledelayedexpansion

set /p "path=Enter the directory path: "
set /p "extensions=Enter the file extensions (separated by spaces): "
set /p "output_format=Enter the output format (txt or html): "
set /p "output_directory=Enter the output directory: "

set "count=0"
set "report="

for %%E in (%extensions%) do (
    set "file_count=0"
    for /r "%path%" %%F in (*%%E) do (
        set /a "count+=1"
        set /a "file_count+=1"
    )
    set "report=!report!%%E : !file_count! "
    echo %%E : !file_count!
)

if "%output_format%"=="txt" (
    echo Total files: %count% > "%output_directory%\report.txt"
    echo File count per extension: >> "%output_directory%\report.txt"
    echo %report% >> "%output_directory%\report.txt"
    echo Report generated successfully. Press any key to exit.
) else if "%output_format%"=="html" (
    echo ^<html^>^<body^> > "%output_directory%\report.html"
    echo ^<h1^>Total files: %count%^</h1^> >> "%output_directory%\report.html"
    echo ^<h2^>File count per extension:^</h2^> >> "%output_directory%\report.html"
    echo ^<ul^> >> "%output_directory%\report.html"
    for %%E in (%extensions%) do (
        echo ^<li^>%%E : !file_count!^</li^> >> "%output_directory%\report.html"
    )
    echo ^</ul^> >> "%output_directory%\report.html"
    echo ^</body^>^</html^> >> "%output_directory%\report.html"
    echo Report generated successfully. Press any key to exit.
) else (
    echo Invalid output format. Please enter txt or html.
)

pause >nul

endlocal
