# Database Backup & Restore System

## 1. Daily Backup Script

File: daily_backup.bat

### Purpose:
Automatically creates a backup of PostgreSQL database every day.

### Command used:
pg_dump -U postgres -F c employee_management > backup.sql

### Output:
Backup file stored in:
C:\db_backups\

---

## 2. Restore Script

File: restore.bat

### Purpose:
Restores database from backup file.

### Command used:
psql -U postgres -d employee_management < backup.sql

---

## 3. How to Run

### Backup:
Double click daily_backup.bat

### Restore:
Double click restore.bat

---

## 4. Notes

- Ensure PostgreSQL is installed
- Ensure pg_dump and psql are added to PATH
- Keep backup folder secure