# 檔案地圖（File Map）· 自動產生

> ⚠️ **此檔案由 `scripts/generate_file_map.sh` 自動產生，請勿手動編輯。**
>
> 執行方式：
> ```bash
> bash scripts/generate_file_map.sh
> ```

**最後產生時間**：2026-05-25 06:27:31

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
| `personas/p001-北捷通勤族.md` | p001-北捷通勤族 | 北捷通勤族 | validated | 2025-05-25 | [payment-flow, returning-user, mobile-first] |

## 📁 `research-insights/`

| 檔案路徑 | ID | 標題 | 狀態 | 最後更新 | 標籤 |
|---|---|---|---|---|---|
| `research-insights/r2025-05-001-北捷乘車碼訪談.md` | r2025-05-001-北捷乘車碼訪談 | 北捷乘車碼使用情境訪談 | validated | 2025-05-25 | [payment-flow, payment-failure, mobile-first, returning-user] |

## 📁 `design-system/`

| 檔案路徑 | ID | 標題 | 狀態 | 最後更新 | 標籤 |
|---|---|---|---|---|---|
| `design-system/ds-pattern-乘車碼頁.md` | ds-pattern-乘車碼頁 | 乘車碼頁設計模式 | draft | 2025-05-25 | [payment-flow, mobile-first, loading-state, error-handling] |

## 📁 `product-context/`

| 檔案路徑 | ID | 標題 | 狀態 | 最後更新 | 標籤 |
|---|---|---|---|---|---|
| `product-context/pc-核心流程-北捷乘車碼.md` | pc-核心流程-北捷乘車碼 | 北捷乘車碼核心流程與技術脈絡 | validated | 2025-05-25 | [payment-flow, account-binding] |
| `product-context/pc-業務-國外小額匯兌.md` | pc-業務-國外小額匯兌 | 國外小額匯兌業務脈絡 | draft | 2025-05-25 | [trust-security, kyc-verification] |
| `product-context/pc-法規-國外匯兌法規.md` | pc-法規-國外匯兌法規 | 國外小額匯兌法規限制 | draft | 2025-05-25 | [trust-security, kyc-verification] |

## 📁 `business-goals/`

| 檔案路徑 | ID | 標題 | 狀態 | 最後更新 | 標籤 |
|---|---|---|---|---|---|
| `business-goals/bg-2025-Q3-北捷乘車碼優化.md` | bg-2025-Q3-北捷乘車碼優化 | 提升北捷乘車碼使用率與進站成功率 | validated | 2025-05-25 | [conversion, activation, payment-flow] |
| `business-goals/bg-2026-Q1-國外小額匯兌MVP.md` | bg-2026-Q1-國外小額匯兌MVP | 國外小額匯兌 MVP 上線 | draft | 2025-05-25 | [activation, revenue, kyc-verification] |

---

## ⚠️ 需要關注的檔案

### Status: `draft`（尚未驗證，引用時要小心）

- `design-system/ds-pattern-乘車碼頁.md` — 乘車碼頁設計模式
- `product-context/pc-業務-國外小額匯兌.md` — 國外小額匯兌業務脈絡
- `product-context/pc-法規-國外匯兌法規.md` — 國外小額匯兌法規限制
- `business-goals/bg-2026-Q1-國外小額匯兌MVP.md` — 國外小額匯兌 MVP 上線

### Status: `deprecated`（已淘汰，保留歷史）

_(無)_

### 超過 180 天未更新的檔案（建議 review）

- `personas/p001-北捷通勤族.md` — 北捷通勤族（last_updated: 2025-05-25）
- `research-insights/r2025-05-001-北捷乘車碼訪談.md` — 北捷乘車碼使用情境訪談（last_updated: 2025-05-25）
- `design-system/ds-pattern-乘車碼頁.md` — 乘車碼頁設計模式（last_updated: 2025-05-25）
- `product-context/pc-核心流程-北捷乘車碼.md` — 北捷乘車碼核心流程與技術脈絡（last_updated: 2025-05-25）
- `product-context/pc-業務-國外小額匯兌.md` — 國外小額匯兌業務脈絡（last_updated: 2025-05-25）
- `product-context/pc-法規-國外匯兌法規.md` — 國外小額匯兌法規限制（last_updated: 2025-05-25）
- `business-goals/bg-2025-Q3-北捷乘車碼優化.md` — 提升北捷乘車碼使用率與進站成功率（last_updated: 2025-05-25）
- `business-goals/bg-2026-Q1-國外小額匯兌MVP.md` — 國外小額匯兌 MVP 上線（last_updated: 2025-05-25）
