@echo off

set DB_NAME=employee_management
set DB_USER=postgres
set BACKUP_FILE=C:\db_backups\backup_latest.sql

psql -U %DB_USER% -d %DB_NAME% < %BACKUP_FILE%

echo Restore completed successfully!
pause