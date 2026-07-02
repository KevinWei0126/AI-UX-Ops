# 標籤系統與搜尋指南

> 所有 md 檔的 frontmatter `tags` 欄位都**只能使用本檔已定義的標籤**。
> 需要新標籤時，先在這裡新增定義，並在 `_meta/CHANGELOG.md` 補記錄。

**最後更新**：2026-07-02

---

## 為什麼需要標籤系統？

知識會跨資料夾。同一個主題（例如「支付失敗」）可能同時存在於 personas、research-insights、design-system 三個資料夾。
標籤是「跨資料夾的橫向索引」，讓你能用 grep 一次抓出所有相關檔案。

---

## 標籤分類

### A. 流程／功能類（feature & flow）

| Tag | 定義 | 使用範例 |
|---|---|---|
| `payment-flow` | 與「付款行為」直接相關的內容 | 支付頁、確認頁、結果頁 |
| `payment-failure` | 支付失敗、錯誤、中斷 | 餘額不足、卡片過期、網路中斷 |
| `onboarding` | 新使用者首次接觸產品的歷程 | 註冊、KYC、首次綁卡 |
| `kyc-verification` | 身分驗證與審核 | 上傳證件、人臉辨識 |
| `account-binding` | 綁卡、綁定銀行帳戶 | 信用卡、金融卡、超商代收 |
| `merchant-side` | 商家端體驗（如 QR 掃碼） | 商家收款、對帳 |
| `coupon-promotion` | 優惠券、活動、行銷機制 | 折扣碼、回饋金 |
| `transaction-history` | 交易紀錄、帳單、明細 | 對帳、匯出、查詢 |
| `notification` | 推播、通知、訊息中心 | 交易通知、行銷通知 |
| `credit-loan` | 與「信用貸款」相關的申貸、試算、對保、撥款、還款流程 | 移工信貸試算頁、對保簽約、還款進度 |

### B. 使用者類（user attribute）

| Tag | 定義 | 使用範例 |
|---|---|---|
| `first-time-user` | 第一次使用全盈+PAY 的使用者 | 註冊流程、首購引導 |
| `returning-user` | 既有使用者 | 老客戶留存、進階功能 |
| `power-user` | 高頻、高活躍使用者 | 進階偏好設定、捷徑 |
| `senior-user` | 中高齡使用者 | 字級、易讀性、簡化流程 |
| `low-income` | 小資族、預算敏感族群 | 對優惠的高敏感度 |
| `migrant-worker` | 在台外籍移工族群（印/越/菲/泰） | 產業移工、家庭看護、跨語言/跨境需求 |

### C. 設計議題類（design concern）

| Tag | 定義 | 使用範例 |
|---|---|---|
| `mobile-first` | 行動裝置優先的設計考量 | 拇指區、單手操作 |
| `accessibility` | 無障礙、可及性 | 色彩對比、語音輔助、WCAG |
| `error-handling` | 錯誤狀態的處理 | 表單錯誤、流程中斷、回復 |
| `trust-security` | 信任感、安全感 | 雙重驗證、資安提示 |
| `loading-state` | 載入狀態與等候體驗 | Skeleton、Progress |
| `empty-state` | 空狀態畫面 | 無交易紀錄、無通知 |
| `form-design` | 表單設計議題 | 輸入驗證、欄位順序 |
| `multilingual` | 多語系／跨語言溝通的設計考量 | 語言切換、白話金融用語、四/五語落地頁 |

### D. 商業類（business）

| Tag | 定義 | 使用範例 |
|---|---|---|
| `conversion` | 轉換率相關 | 漏斗、流失點 |
| `retention` | 留存率相關 | 回訪、再購 |
| `activation` | 啟用率相關 | 從註冊到首筆交易 |
| `revenue` | 營收相關 | ARPU、手續費 |

---

## grep 搜尋常用範例

```bash
# 找所有跟「支付失敗」相關的檔案（跨資料夾）
grep -rln "payment-failure" .

# 找所有「新手＋支付」的交集
grep -rln "first-time-user" . | xargs grep -l "payment-flow"

# 找特定 persona 被哪些 insight 引用
grep -rln "p001" research-insights/

# 找所有 status: draft 的檔案（需要 review 的）
grep -rln "status: draft" .

# 找最近一個月內更新的檔案（依 frontmatter 的 last_updated）
grep -rln "last_updated: 2025-05" .
```

---

## 新增標籤的規則

1. 先確認既有標籤無法表達——避免標籤膨脹
2. 在本檔對應分類新增定義（標籤名、定義、使用範例）
3. 在 `_meta/CHANGELOG.md` 記一筆 `Added: 新標籤 #xxx`
4. 新標籤一律小寫、用連字號分隔（kebab-case），例如 `payment-flow` 不是 `paymentFlow`

---

## 廢棄標籤

> 已淘汰的標籤保留在這裡，方便回查歷史檔案的語意。

_(尚未有廢棄標籤)_
