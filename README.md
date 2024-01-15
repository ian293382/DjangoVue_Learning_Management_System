# Studynet - 學習平台

Studynet 是一個基於 Django 和 Vue.js 的學習平台，旨在提供使用者全方位且互動性強的學習體驗。

## 功能特色

- **用戶功能：** 實現註冊、登錄、登出等基本用戶功能，並使用 vuex 管理狀態。
- **課程管理：** 開發了後台功能，使管理課程、類別和內容更加輕鬆。
- **課程內容：** 設計課程內容頁面，包括課程列表、內容顯示和評論區。
- **測驗功能：** 實現了測驗的創建、顯示和回答，同時禁用了測驗的評論功能。
- **進度追蹤：** 開始實現學習進度追蹤，包括開始學習、標記完成等功能。

## 使用插件

- **後端模組：** Django、django-restframework、djoser
- **前端模組：** Vue.js、Bulma CSS Framework、axios
- **資料庫：** SQLite（可擴展至其他資料庫）

## 使用方法

1. **建立虛擬環境：** 使用 `python3 -m venv env` 創建虛擬環境，並透過 `source ./env/bin/activate` 啟用它。
2. **安裝相依套件：** 使用 `pip install -r requirements.txt` 安裝後端相依套件。
3. **初始化前端：** 進入 `studynet_vue` 目錄，運行 `npm install` 安裝前端相依套件。
4. **遷移資料庫：** 在 Django 專案目錄下，運行 `python manage.py migrate` 遷移資料庫。
5. **啟動後端伺服器：** 在 Django 專案目錄下，運行 `python manage.py runserver` 啟動後端伺服器。
6. **啟動前端伺服器：** 在 `studynet_vue` 目錄下，運行 `npm run serve` 啟動前端伺服器。

現在，您可以在瀏覽器中訪問 [http://localhost:8080](http://localhost:8080) 來使用 Studynet 學習平台。
