# YouTube 影片標題爬取器 🎥🔍

這是一個使用 **Python + Selenium** 的爬蟲工具，可以搜尋 **YouTube** 指定關鍵字，並擷取搜尋結果中的影片標題。  
本專案使用 **Poetry** 來管理 Python 環境與套件。

---

## **功能 🚀**

✅ 自動搜尋 YouTube 指定關鍵字  
✅ 擷取搜尋結果中的所有影片標題  
✅ 透過 **Selenium** 操控瀏覽器爬取資料  
✅ 支援 **Poetry** 環境管理

---

## **安裝環境 🛠️**

### **1️⃣ Clone 專案**

```bash
git clone https://github.com/doudouu0504/youtube-scraper.git
cd youtube-scraper
```

### **2️⃣ 安裝 Poetry**

如果尚未安裝 Poetry，請參考官方文件，或執行：

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### **3️⃣ 建立虛擬環境並安裝依賴**

```bash
poetry install
```

### **4️⃣ 安裝 ChromeDriver**

本專案使用 Selenium 來自動化操作瀏覽器，因此需要安裝 ChromeDriver。
可參考[安裝文章](https://doudouu0504.github.io/posts/%E5%AE%89%E8%A3%9Dselenium%E4%B8%A6%E4%B8%8B%E8%BC%89chromedriver/)
或是

```bash
brew install chromedriver
```

---

## **使用方法 📌**

### **1️⃣ 進入 Poetry 虛擬環境**

```bash
poetry shell
```

### **2️⃣ 執行爬蟲程式**

```bash
python practice.py
```

### **3️⃣ 輸入搜尋關鍵字**

在終端機輸入 搜尋關鍵字（例如："比特幣"），按下 Enter。

### **4️⃣ 取得結果**
