@echo off
chcp 65001 > nul
echo.
echo ============================================
echo  BMA Accident Analysis — Push to GitHub
echo ============================================
echo.

:: ตรวจสอบว่า git มีอยู่
where git >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] ไม่พบ Git — กรุณาติดตั้งจาก https://git-scm.com/download/win
    pause
    exit /b 1
)

:: ไปยังโฟลเดอร์นี้
cd /d "%~dp0"
echo [INFO] โฟลเดอร์: %~dp0
echo.

:: อ่าน token จากตัวแปรแวดล้อม
if "%GITHUB_TOKEN%"=="" (
    echo [ERROR] ไม่พบ GITHUB_TOKEN
    echo [INFO] ตั้งค่าก่อนรัน เช่น:
    echo        set GITHUB_TOKEN=YOUR_PAT_TOKEN
    pause
    exit /b 1
)
set REPO_URL=https://BMA-Statistics-PW:%GITHUB_TOKEN%@github.com/BMA-Statistics-PW/BMA-Accident-Analysis.git

:: init หรือ reinit
if exist ".git" (
    echo [INFO] ใช้ .git ที่มีอยู่
) else (
    echo [INFO] กำลัง git init...
    git init
)

:: ตั้งค่า user
git config user.name "BMA-Statistics-PW"
git config user.email "bma.statistics@gmail.com"
git config core.quotepath false

:: remote
git remote remove origin 2>nul
git remote add origin %REPO_URL%

:: stage และ commit
echo.
echo [INFO] กำลัง add ไฟล์...
git add .

git status

echo.
echo [INFO] กำลัง commit...
git commit -m "Update BMA Accident Analysis dashboard and data" 2>nul

:: branch และ push
git branch -M main
echo.
echo [INFO] กำลัง push ขึ้น GitHub...
git push -u origin main

echo.
if %errorlevel% equ 0 (
    echo ============================================
    echo  SUCCESS! Push เรียบร้อยแล้ว
    echo  Dashboard: https://bma-statistics-pw.github.io/BMA-Accident-Analysis/
    echo  (รอ 1-3 นาทีเพื่อให้ GitHub Pages อัปเดต)
    echo ============================================
) else (
    echo [ERROR] Push ไม่สำเร็จ — ตรวจสอบ Token หรือสิทธิ์ repo
)
echo.
pause
