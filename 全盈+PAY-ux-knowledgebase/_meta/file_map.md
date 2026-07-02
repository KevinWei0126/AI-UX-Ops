# 檔案地圖（File Map）· 自動產生

> ⚠️ **此檔案由 `scripts/generate_file_map.sh` 自動產生，請勿手動編輯。**
>
> 執行方式：
> ```bash
> bash scripts/generate_file_map.sh
> ```

**最後產生時間**：2026-07-02 06:22:20

---

## 用途

- 列出知識庫所有 md 檔的完整路徑、id、標題、狀態、最後更新時間
- 當 `INDEX.md` 沒涵蓋到、或你懷疑 `INDEX.md` 過期，來這查
- grep 此檔可以快速定位檔案位置：
  ```bash
  grep -n "支付" _meta/file_map.md
  ```

---


## 📁 `personas/`

| 檔案路徑 | ID | 標題 | 狀態 | 最後更新 | 標籤 |
|---|---|---|---|---|---|
| `personas/p002-越南產業移工.md` | p002-越南產業移工 | 越南產業移工（工廠作業員） | draft | 2026-07-02 | [migrant-worker, credit-loan, multilingual, trust-security, low-income] |
| `personas/p003-印尼家庭看護.md` | p003-印尼家庭看護 | 印尼家庭看護 | draft | 2026-07-02 | [migrant-worker, credit-loan, multilingual, trust-security, accessibility] |
| `personas/p004-菲律賓移工.md` | p004-菲律賓移工 | 菲律賓移工（英語能力較佳） | draft | 2026-07-02 | [migrant-worker, credit-loan, trust-security, form-design, conversion] |

## 📁 `research-insights/`

| 檔案路徑 | ID | 標題 | 狀態 | 最後更新 | 標籤 |
|---|---|---|---|---|---|
| `research-insights/r2026-07-001-移工信貸桌面研究.md` | r2026-07-001-移工信貸桌面研究 | 移工信用貸款桌面研究（次級資料 + 研究目標） | draft | 2026-07-02 | [credit-loan, migrant-worker, multilingual, trust-security, conversion] |

## 📁 `design-system/`

| 檔案路徑 | ID | 標題 | 狀態 | 最後更新 | 標籤 |
|---|---|---|---|---|---|
| _(此分區尚未有檔案)_ | | | | | |

## 📁 `product-context/`

| 檔案路徑 | ID | 標題 | 狀態 | 最後更新 | 標籤 |
|---|---|---|---|---|---|
| `product-context/pc-業務-移工信用貸款.md` | pc-業務-移工信用貸款 | 玉山 × 全盈+PAY 移工信用貸款業務脈絡 | draft | 2026-07-02 | [credit-loan, migrant-worker, account-binding, kyc-verification, trust-security, revenue] |
| `product-context/pc-競品-移工信貸競品分析.md` | pc-競品-移工信貸競品分析 | 移工信用貸款競品分析（數位信貸 App） | draft | 2026-07-02 | [credit-loan, migrant-worker, multilingual, trust-security, form-design, conversion] |

## 📁 `business-goals/`

| 檔案路徑 | ID | 標題 | 狀態 | 最後更新 | 標籤 |
|---|---|---|---|---|---|
| _(此分區尚未有檔案)_ | | | | | |

---

## ⚠️ 需要關注的檔案

### Status: `draft`（尚未驗證，引用時要小心）

- `research-insights/r2026-07-001-移工信貸桌面研究.md` — 移工信用貸款桌面研究（次級資料 + 研究目標）
- `product-context/pc-業務-移工信用貸款.md` — 玉山 × 全盈+PAY 移工信用貸款業務脈絡
- `product-context/pc-競品-移工信貸競品分析.md` — 移工信用貸款競品分析（數位信貸 App）
- `personas/p004-菲律賓移工.md` — 菲律賓移工（英語能力較佳）
- `personas/p002-越南產業移工.md` — 越南產業移工（工廠作業員）
- `personas/p003-印尼家庭看護.md` — 印尼家庭看護

### Status: `deprecated`（已淘汰，保留歷史）

_(無)_

### 超過 180 天未更新的檔案（建議 review）

_(無)_
