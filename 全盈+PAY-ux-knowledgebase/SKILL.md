---
name: quanying-pay-ux
description: 「全盈+PAY」產品的 UX 專屬知識庫。當使用者在進行全盈+PAY 相關的設計決策、查詢產品 persona、研究洞察、設計系統規範、產品脈絡、商業目標，或在做任何需要參考全盈+PAY 既有知識的設計工作時使用。也用於設計師查找參考資料、設計師＋PM 共同維護的活文件、新人 onboarding 教材、以及讓 Claude 引用既有 UX 知識做設計輔助決策的場景。本 skill 內含五個主題資料夾（personas、research-insights、design-system、product-context、business-goals）、三層防呆機制（INDEX.md 人工目錄、自動產生的檔案地圖、標籤搜尋指南），以及依資料夾分區的 changelog 版本紀錄。
---

# 全盈+PAY UX Knowledge Base

這是「全盈+PAY」產品的專屬 UX 知識庫 skill。它是一個**活文件系統**——設計師＋PM 共同維護、新人可以自學、Claude 可以引用做設計決策。

---

## 使用本 skill 的步驟

**步驟 1｜先判斷使用者的查詢屬於哪一類**

| 使用者意圖 | 該查哪個資料夾 |
|---|---|
| 「我們的使用者是誰？」「目標族群？」 | `personas/` |
| 「先前訪談發現什麼？」「之前研究結論？」 | `research-insights/` |
| 「按鈕／顏色／元件規範？」「設計 token？」 | `design-system/` |
| 「這個產品在做什麼？」「商業模式？」「核心流程？」 | `product-context/` |
| 「KPI？」「OKR？」「這次改版要解決的商業問題？」 | `business-goals/` |
| 「這個 skill 裡有什麼？」「找不到對應檔案」 | 先讀 `_meta/INDEX.md` |

**步驟 2｜不要一次把整個資料夾讀進來**

知識庫會越長越大，盲目 `view` 整個資料夾或 `cat` 所有 md 會炸 context。標準查找流程：

```bash
# (a) 先看人工維護的目錄
view _meta/INDEX.md

# (b) 找不到時，看自動產生的檔案地圖
view _meta/file_map.md

# (c) 用關鍵字精準定位
grep -rn "關鍵字" personas/ research-insights/

# (d) 確認檔案位置後再 view 該檔
view personas/p001-小資族行動支付者.md
```

**步驟 3｜引用知識庫內容做設計建議前，先做來源檢查**

- 確認該 md 檔最後更新日期（看 frontmatter 的 `last_updated`）
- 確認該知識的「狀態」（`status: validated` / `draft` / `deprecated`）
- 若狀態是 `draft` 或 `deprecated`，引用時必須明確標註，不可當作確定事實
- 若資料超過 6 個月未更新，提醒使用者該知識可能需要重新驗證

**步驟 4｜任何寫入／修改都要更新 changelog**

每個子資料夾下有自己的 `CHANGELOG.md`。新增、修改、刪除任何 md 檔，都要同步在該資料夾的 CHANGELOG.md 補一筆紀錄。詳見「Changelog 規則」章節。

---

## 資料夾結構

```
quanying-pay-ux/
├── SKILL.md                  ← 你現在讀的這份
├── _meta/                    ← 知識庫的後設資料
│   ├── INDEX.md              ← 人工維護的總目錄（防呆 Layer 1）
│   ├── file_map.md           ← 自動產生的檔案地圖（防呆 Layer 2）
│   ├── tags.md               ← 標籤系統與搜尋指南（防呆 Layer 3）
│   ├── CHANGELOG.md          ← 知識庫總 changelog
│   └── templates/            ← 各類 md 檔的模板
│       ├── persona.template.md
│       ├── insight.template.md
│       ├── design-spec.template.md
│       ├── product-doc.template.md
│       └── business-goal.template.md
├── scripts/
│   └── generate_file_map.sh  ← 自動更新 file_map.md 的腳本
├── personas/
│   ├── CHANGELOG.md
│   └── (p001, p002, ... 個別 persona 檔)
├── research-insights/
│   ├── CHANGELOG.md
│   └── (r2025-01-xxx, ... 個別研究檔)
├── design-system/
│   ├── CHANGELOG.md
│   └── (個別設計規範檔)
├── product-context/
│   ├── CHANGELOG.md
│   └── (產品脈絡檔)
└── business-goals/
    ├── CHANGELOG.md
    └── (商業目標檔)
```

---

## 三層防呆機制：快速找到對應 md 檔

### Layer 1｜INDEX.md（人工維護的目錄）

`_meta/INDEX.md` 是給人類看的索引，由設計師＋PM 手動維護。當你新增一個重要的 md 檔，就在 INDEX.md 加一行說明。它是「最權威但更新最慢」的入口。

**使用時機**：當你想找的東西有明確語意（例如「找小資族 persona」、「找去年的支付流程訪談」）。

### Layer 2｜file_map.md（自動產生的檔案地圖）

`_meta/file_map.md` 由 `scripts/generate_file_map.sh` 自動產生，列出所有 md 檔的路徑、標題、最後更新時間、狀態（validated / draft / deprecated）。這是「永遠最新但較難閱讀」的入口。

**使用時機**：當 INDEX.md 沒有你要的東西，或你懷疑 INDEX.md 過期。執行：

```bash
bash scripts/generate_file_map.sh
view _meta/file_map.md
```

### Layer 3｜tags.md（標籤系統＋搜尋指南）

`_meta/tags.md` 維護全套標籤的定義（例如 `#payment-flow`、`#first-time-user`、`#error-handling`），並提供 grep 搜尋的常用範例。每份 md 檔在 frontmatter 都會帶 `tags: [...]`。

**使用時機**：當你的查詢是跨資料夾的主題（例如「所有關於支付失敗的設計與研究」）。

```bash
# 找所有跟支付失敗有關的檔案
grep -rln "payment-failure" .
```

---

## md 檔的 Frontmatter 規範

所有知識庫的 md 檔都必須帶 frontmatter，這是 file_map 與 grep 搜尋的基礎。範例：

```yaml
---
id: p001
title: 小資族行動支付者
type: persona              # persona / insight / design-spec / product-doc / business-goal
status: validated          # validated / draft / deprecated
owner: 設計師A
last_updated: 2025-05-20
tags: [payment-flow, first-time-user, mobile-first]
related: [r2025-03-002, ds-button-primary]
---
```

**欄位說明**：

- `id`：唯一識別碼，依資料夾命名規則（見各模板）
- `status`：知識的可信度。`validated` 才能當作設計決策依據；`draft` 是討論中；`deprecated` 是已淘汰但保留歷史
- `last_updated`：每次修改必須更新
- `tags`：對應 `_meta/tags.md` 已定義的標籤，禁止隨手新增未定義標籤
- `related`：用 id 連結到其他相關 md 檔

---

## Changelog 規則（依資料夾分區記錄）

每個子資料夾下都有自己的 `CHANGELOG.md`，記錄該分區的所有變更。另有一份 `_meta/CHANGELOG.md` 記錄知識庫整體的重大事件（資料夾新增、模板大改、規範變動）。

**寫入時機**：任何新增、修改、刪除 md 檔都要記錄。

**格式**（採 Keep a Changelog 格式，依日期由新到舊）：

```markdown
## [2025-05-25] - 設計師A
### Added
- p003-中高齡支付使用者.md：新增中高齡 persona，依 2025-04 訪談 r2025-04-001 整理

### Changed
- p001-小資族行動支付者.md：根據 r2025-05-002 訪談更新「支付動機」段落

### Deprecated
- p002-早期版本草稿.md：已被 p001 取代，保留歷史不刪除

### Removed
- (無)
```

**重要原則**：

1. **不刪除過時知識**——標記 `status: deprecated` 並在 changelog 註明，保留設計脈絡
2. **每筆 changelog 標註作者**——讓未來的人知道找誰確認
3. **重大變更要在 `_meta/CHANGELOG.md` 也記一筆**（例如新增 persona、研究方法論大改）

---

## 新增知識的標準流程

當設計師或 PM 要新增一份知識：

1. **確認類別**：屬於五個資料夾的哪一個？跨類別的話以「主要用途」為準
2. **複製對應模板**：從 `_meta/templates/` 取對應模板
3. **填寫 frontmatter**：特別注意 `id`、`status`、`tags`、`related`
4. **撰寫內容**：依模板的章節結構填寫
5. **更新 changelog**：在該資料夾的 `CHANGELOG.md` 新增 Added 項
6. **更新 INDEX.md**（若是重要知識）：人工把它加進 `_meta/INDEX.md`
7. **重新產生 file_map**：執行 `bash scripts/generate_file_map.sh`

---

## Claude 引用知識庫時的硬性規則

當你（Claude）被要求依據本 skill 做設計建議時：

1. **不可以憑印象回答**——必須真的 view 過對應 md 檔才能引用
2. **引用時要標註 id 與狀態**——例如「依據 p001（validated, 2025-05-20）」
3. **遇到 draft 或 deprecated 知識要明說**——不可當作確定事實
4. **找不到對應知識時要誠實說沒有**——不要編造，並建議設計師補資料
5. **跨資料夾推論時，要列出所有引用的來源 id**——讓設計師可追溯
6. **若使用者要新增知識，務必引導他走「新增知識的標準流程」**——不可以幫他繞過模板與 changelog

---

## 快速啟動範例

**情境一｜設計師問**：「我要設計支付失敗的錯誤頁面，有什麼可以參考的？」

你應該：

1. 看 `_meta/tags.md` 確認 `payment-failure` 是已定義標籤
2. 執行 `grep -rln "payment-failure" .` 取得所有相關檔案
3. 依資料夾分類整理（persona / insight / design-system / ...）
4. 每筆引用都標 id、狀態、最後更新日
5. 若有 `deprecated` 資料，明確標註但仍列出（保留設計脈絡）

**情境二｜PM 說**：「我剛訪談完三位新使用者，要把洞察加進來。」

你應該：

1. 引導走「新增知識的標準流程」
2. 複製 `_meta/templates/insight.template.md`
3. 提醒填 `id`（命名規則：r{年}-{月}-{流水號}）、`tags`、`related`
4. 提醒在 `research-insights/CHANGELOG.md` 加一筆 Added
5. 若洞察會影響既有 persona，提醒同步更新 persona 並在 `personas/CHANGELOG.md` 記 Changed

**情境三｜新人問**：「這個 skill 怎麼用？我要從哪裡看起？」

你應該：

1. 帶他讀 `SKILL.md`（這份）→ `_meta/INDEX.md` → 各資料夾的 README（若有）
2. 推薦從 `product-context/` 開始（先懂產品）→ `personas/` → `business-goals/` → 其他
3. 提醒他寫入前先讀「新增知識的標準流程」

---

**切記：這個 skill 的價值來自「資料品質」而不是「資料量」。寧可少而精準，不要多而過時。每一份知識的 `status` 與 `last_updated` 都是設計決策的根據。**
