@echo off

set DB_NAME=employee_management
set DB_USER=postgres
set DB_PASSWORD=your_password
set BACKUP_PATH=C:\db_backups

set DATE=%date:~-4%-%date:~3,2%-%date:~0,2%

pg_dump -U %DB_USER% -F c %DB_NAME% > %BACKUP_PATH%\backup_%DATE%.sql

echo Backup completed successfully!
pause