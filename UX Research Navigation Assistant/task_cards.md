# AI UX Workflow｜Prompt 任務卡資料

> 此檔彙整 `ux-knowledge/prompts/` 內的 Prompt 任務卡版本。每張 Prompt 都包含 metadata front matter，可供 Claude 依任務卡機制判斷何時使用、何時不使用、需要哪些輸入、會產出什麼，以及完成後的 Next Best Actions。

---

---
prompt_id: "AI-A-001"
task_name: "主題分群"
stage: "資料分析與洞察"
task_type: "synthesize"
when_to_use: "當你已有逐字稿、研究資料，並需要將資料收斂、分群或整合成「主題分群表 / Topic Cluster」時"
when_not_to_use: "當缺少Research Data、User Quote，或資料量不足以支撐「主題分群」判斷時"
input_required:
  - "Research Data"
  - "User Quote"
output:
  - "主題分群表 / Topic Cluster"
next_best_actions:
  - "AI-A-003｜重複議題合併"
  - "AI-A-005｜行為模式分組"
---

# AI-A-001 主題分群

**所屬階段：** 資料分析與洞察

**適用情境：** Affinity Mapping

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請根據以下研究資料進行主題分群。
 
 請協助：
 - 找出重複議題
 - 建立主題分類
 - 整理關聯性
 - 合併相似觀點
 - 萃取代表性內容
 
 # 格式要求
 請以 affinity mapping 形式輸出。
 
 # 情境
 [輸入逐字稿、觀察資料或研究內容]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**逐字稿、研究資料**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Research Data | ✅ 必填 | U01：不理解手續費；U02：擔心資料填錯；U03：不確定交易狀態 |
| User Quote | ✅ 必填 | U02：「我怕名字填錯錢就不見。」 |
| Observation Note | 選填 | 多位受訪者在確認頁反覆查看費用資訊 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 主題分群表 / Topic Cluster

- [ ] 每個主題是否有足夠證據
- [ ] 是否避免過度合併不同問題
- [ ] 是否保留原始語意
- [ ] 是否能看出主題差異

---

## 完成後下一步

> ✅ 建議接續：**AI-A-003、AI-A-005 AI-A-003、AI-A-005**


---

---
prompt_id: "AI-A-002"
task_name: "Affinity Mapping"
stage: "資料分析與洞察"
task_type: "synthesize"
when_to_use: "當你已有使用者資料，並需要將資料收斂、分群或整合成「Affinity Group」時"
when_not_to_use: "當缺少使用者資料，或資料量不足以支撐「Affinity Mapping」判斷時"
input_required:
  - "使用者資料"
output:
  - "Affinity Group"
next_best_actions:
  - "DO-A-001｜關鍵發現摘要生成"
  - "回到使用者原話｜補強洞察證據"
---

# AI-A-002 Affinity Mapping

**所屬階段：** 資料分析與洞察

**適用情境：** UX Research

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請根據以下研究資料建立 Affinity Mapping。
 
 請包含：
 - Cluster 名稱
 - 關聯觀點
 - 使用者原話
 - 問題模式
 - 代表性洞察
 
 # 格式要求
 請使用分群階層格式輸出。
 
 # 情境
 [輸入研究資料]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**使用者資料**

**此 Prompt 產出：** Affinity Group


---

---
prompt_id: "AI-A-003"
task_name: "重複議題合併"
stage: "資料分析與洞察"
task_type: "refine"
when_to_use: "當你已有多份研究資料，並需要將資料收斂、分群或整合成「合併後主題清單」時"
when_not_to_use: "當缺少Research Data、User Quote，或資料量不足以支撐「重複議題合併」判斷時"
input_required:
  - "Research Data"
  - "User Quote"
output:
  - "合併後主題清單"
next_best_actions:
  - "AI-A-005｜行為模式分組"
  - "DO-A-001｜關鍵發現摘要生成"
---

# AI-A-003 重複議題合併

**所屬階段：** 資料分析與洞察

**適用情境：** Synthesis

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請辨識以下資料中的重複議題並進行整合。
 
 請包含：
 - 重複問題
 - 相似觀點
 - 合併原因
 - 統整後主題
 
 # 格式要求
 請以「原始議題 → 合併後主題」格式輸出。
 
 # 情境
 [輸入研究資料]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**多份研究資料**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Research Data | ✅ 必填 | 主題 A：費用理解困難；主題 B：手續費來源不清楚 |
| User Quote | ✅ 必填 | U01：「我不知道這個費用是誰收的。」U03：「總共扣多少我不確定。」 |
| Duplicate Feedback | 選填 | 費用不清楚、手續費不清楚、扣款金額不清楚 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 合併後主題清單

- [ ] 是否避免把原因不同的問題過度合併
- [ ] 是否保留重要差異
- [ ] 是否有原話證據
- [ ] 是否能降低後續分析雜訊

---

## 完成後下一步

> ✅ 建議接續：**AI-A-005、DO-A-001 AI-A-005、DO-A-001**


---

---
prompt_id: "AI-A-005"
task_name: "行為模式分組"
stage: "資料分析與洞察"
task_type: "analyze"
when_to_use: "當你已有行為資料，並需要將資料收斂、分群或整合成「使用者行為模式分組」時"
when_not_to_use: "當缺少Behavior Data、Flow Description、Interview Summary，或資料量不足以支撐「行為模式分組」判斷時"
input_required:
  - "Behavior Data"
  - "Flow Description"
  - "Interview Summary"
output:
  - "使用者行為模式分組"
next_best_actions:
  - "DO-A-001｜關鍵發現摘要生成"
  - "DO-B-001｜User Flow 生成"
  - "DO-B-003｜Persona 文件化"
---

# AI-A-005 行為模式分組

**所屬階段：** 資料分析與洞察

**適用情境：** User Research

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請分析以下研究資料中的使用者行為模式。
 
 請包含：
 - 常見行為
 - 操作順序
 - 決策模式
 - 高風險行為
 - 使用習慣
 
 # 格式要求
 請以 behavior pattern table 輸出。
 
 # 情境
 [輸入研究資料]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**行為資料**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Behavior Data | ✅ 必填 | 使用者會反覆確認受款人資料、截圖交易結果、詢問朋友 |
| Flow Description | ✅ 必填 | 設定匯款人資料 → 新增受款人 → 輸入金額 → 確認資訊 → 付款 → 查詢狀態 |
| Interview Summary | ✅ 必填 | 多位受訪者提到會在確認頁停留較久，並重新檢查金額與姓名 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 使用者行為模式分組

- [ ] 是否基於實際訪談或觀察資料
- [ ] 是否能對應到流程節點
- [ ] 是否清楚說明行為背後可能原因
- [ ] 是否避免只描述單一個案

---

## 完成後下一步

> ✅ 建議接續：**DO-A-001、DO-B-001、DO-B-003 DO-A-001、DO-B-001、DO-B-003**


---

---
prompt_id: "DC-A-001"
task_name: "延伸追問生成"
stage: "資料蒐集與執行"
task_type: "probe"
when_to_use: "當你已有訪談內容、逐字稿或使用者回覆，並需要進行「延伸追問生成」以支援後續分析時"
when_not_to_use: "當缺少Transcript、Interview Question、Research Goal，或資料量不足以支撐「延伸追問生成」判斷時"
input_required:
  - "Transcript"
  - "Interview Question"
  - "Research Goal"
output:
  - "延伸追問清單"
next_best_actions:
  - "DC-A-002｜深入探詢問題建議"
  - "DC-A-003｜對話摘要整理"
---

# DC-A-001 延伸追問生成

**所屬階段：** 資料蒐集與執行

**適用情境：** 使用者訪談

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 根據以下訪談內容，生成適合深入挖掘使用者行為與動機的延伸追問。
 
 請包含：
 - 行為追問
 - 動機追問
 - 情緒追問
 - 情境追問
 - 決策追問
 
 # 格式要求
 請依照問題類型分類輸出。
 
 # 情境
 [輸入逐字稿或使用者回覆]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**訪談逐字稿**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Transcript | ✅ 必填 | 使用者：我通常會請朋友幫我看，因為我怕填錯名字 |
| Interview Question | ✅ 必填 | 你通常怎麼確認受款人資料是正確的？ |
| Research Goal | ✅ 必填 | 想了解使用者在受款人資料設定時的不確定感與信任來源 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 延伸追問清單

- [ ] 是否根據使用者原話追問
- [ ] 是否避免引導受訪者
- [ ] 是否能挖掘行為原因、情境細節與信任來源
- [ ] 是否與研究目標相關

---

## 完成後下一步

> ✅ 建議接續：**DC-A-002、DC-A-003 DC-A-002、DC-A-003**


---

---
prompt_id: "DC-A-002"
task_name: "深入探詢問題建議"
stage: "資料蒐集與執行"
task_type: "probe"
when_to_use: "當你已有訪談內容、逐字稿或使用者回覆，並需要進行「深入探詢問題建議」以支援後續分析時"
when_not_to_use: "當缺少Research Goal、Transcript，或資料量不足以支撐「深入探詢問題建議」判斷時"
input_required:
  - "Research Goal"
  - "Transcript"
output:
  - "深入探詢問題"
next_best_actions:
  - "DC-A-003｜對話摘要整理"
---

# DC-A-002 深入探詢問題建議

**所屬階段：** 資料蒐集與執行

**適用情境：** 深度訪談

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 根據以下研究目標與訪談內容，生成適合的深入探詢問題。
 
 請協助探索：
 - 使用原因
 - 使用障礙
 - 行為模式
 - 潛在需求
 - 未被滿足的期待
 
 # 格式要求
 請以訪談問題列表輸出。
 
 # 情境
 [輸入研究目標與訪談內容]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**研究目標、逐字稿**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Research Goal | ✅ 必填 | 了解移工在跨境匯兌流程中的使用原因、阻礙與潛在需求 |
| Transcript | ✅ 必填 | 我怕按錯之後錢就不見，所以會一直看確認頁 |
| User Quote | 選填 | 我不確定這樣是不是已經送出了 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 深入探詢問題

- [ ] 是否能深入挖掘原因、情境、行為與決策因素
- [ ] 是否避免替使用者下結論
- [ ] 是否能補足研究問題的資訊缺口

---

## 完成後下一步

> ✅ 建議接續：**DC-A-003 對話摘要整理**


---

---
prompt_id: "DC-A-003"
task_name: "對話摘要整理"
stage: "資料蒐集與執行"
task_type: "summarize"
when_to_use: "當你已有訪談內容、逐字稿或使用者回覆，並需要進行「對話摘要整理」以支援後續分析時"
when_not_to_use: "當缺少Transcript、Participant Background，或資料量不足以支撐「對話摘要整理」判斷時"
input_required:
  - "Transcript"
  - "Participant Background"
output:
  - "訪談摘要報告"
next_best_actions:
  - "AI-A-001｜主題分群"
---

# DC-A-003 對話摘要整理

**所屬階段：** 資料蒐集與執行

**適用情境：** 研究整理

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請根據以下訪談內容，整理重點摘要。
 
 請包含：
 - 核心觀點
 - 主要痛點
 - 關鍵原話
 - 行為模式
 - 待驗證問題
 
 # 格式要求
 請區分「Summary」、「Pain Point」、「Key Quote」。
 
 # 情境
 [輸入逐字稿]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**訪談逐字稿**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Transcript | ✅ 必填 | U01 00:03：我不太確定這個手續費是不是全部費用 |
| Interview Note | 選填 | 受訪者提到會請同鄉協助確認英文姓名 |
| Participant Background | ✅ 必填 | U01：印尼籍移工，在台 3 年，每月匯款 1 次 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 訪談摘要報告

- [ ] 是否保留使用者原話
- [ ] 是否避免直接下最終洞察
- [ ] 是否能追溯到受訪者
- [ ] 是否清楚區分事實、觀察與推論

---

## 完成後下一步

> ✅ 建議接續：**AI-A-001 主題分群**


---

---
prompt_id: "DC-B-001"
task_name: "行為紀錄整理"
stage: "資料蒐集與執行"
task_type: "capture"
when_to_use: "當你已有測試觀察、操作紀錄或任務資料，並需要整理成「行為流程整理」時"
when_not_to_use: "當缺少操作觀察資料，或資料量不足以支撐「行為紀錄整理」判斷時"
input_required:
  - "操作觀察資料"
output:
  - "行為流程整理"
next_best_actions:
  - "回到逐字稿 / 觀察紀錄補充證據｜提升後續分析品質"
---

# DC-B-001 行為紀錄整理

**所屬階段：** 資料蒐集與執行

**適用情境：** 易用性測試

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請根據以下觀察紀錄，整理使用者操作行為。
 
 請包含：
 - 操作步驟
 - 停留時間
 - 猶豫點
 - 操作錯誤
 - 返回操作
 
 # 格式要求
 請依照時間順序輸出。
 
 # 情境
 [輸入觀察紀錄]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**操作觀察資料**

**此 Prompt 產出：** 行為流程整理


---

---
prompt_id: "DC-B-002"
task_name: "情緒標記"
stage: "資料蒐集與執行"
task_type: "capture"
when_to_use: "當你已有測試觀察、操作紀錄或任務資料，並需要整理成「情緒時間軸」時"
when_not_to_use: "當缺少測試觀察資料，或資料量不足以支撐「情緒標記」判斷時"
input_required:
  - "測試觀察資料"
output:
  - "情緒時間軸"
next_best_actions:
  - "回到逐字稿 / 觀察紀錄補充證據｜提升後續分析品質"
---

# DC-B-002 情緒標記

**所屬階段：** 資料蒐集與執行

**適用情境：** 使用者觀察

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請根據以下測試觀察內容，標記使用者情緒變化。
 
 請包含：
 - 情緒類型
 - 發生時間點
 - 觸發原因
 - 對任務影響
 
 # 格式要求
 請依照時間軸輸出。
 
 # 情境
 [輸入觀察紀錄]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**測試觀察資料**

**此 Prompt 產出：** 情緒時間軸


---

---
prompt_id: "DC-B-003"
task_name: "任務完成紀錄"
stage: "資料蒐集與執行"
task_type: "capture"
when_to_use: "當你已有測試觀察、操作紀錄或任務資料，並需要整理成「任務完成報告」時"
when_not_to_use: "當缺少測試結果，或資料量不足以支撐「任務完成紀錄」判斷時"
input_required:
  - "測試結果"
output:
  - "任務完成報告"
next_best_actions:
  - "回到逐字稿 / 觀察紀錄補充證據｜提升後續分析品質"
---

# DC-B-003 任務完成紀錄

**所屬階段：** 資料蒐集與執行

**適用情境：** 易用性測試

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請根據以下 usability testing 結果，整理任務完成狀況。
 
 請包含：
 - 是否成功完成
 - 完成時間
 - 中斷原因
 - 操作問題
 - 使用者回饋
 
 # 格式要求
 請以 task-based table 格式輸出。
 
 # 情境
 [輸入 usability testing 紀錄]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**測試結果**

**此 Prompt 產出：** 任務完成報告


---

---
prompt_id: "DO-A-001"
task_name: "關鍵發現摘要生成"
stage: "產出物製作"
task_type: "report"
when_to_use: "當你已有研究洞察或分析結果，並需要整理成可溝通的報告內容或故事化摘要時"
when_not_to_use: "當缺少Insight Data、User Quote或任務目標不是「關鍵發現摘要生成」時"
input_required:
  - "Insight Data"
  - "User Quote"
output:
  - "關鍵發現摘要"
next_best_actions:
  - "DO-B-001｜User Flow 生成"
  - "DO-B-002｜Journey Map 草稿生成"
  - "DO-B-003｜Persona 文件化"
  - "DO-C-002｜商業價值轉譯"
---

# DO-A-001 關鍵發現摘要生成

**所屬階段：** 產出物製作

**適用情境：** UX Report

---

## Prompt 本文

```
# 角色
 你是一位擅長 Storytelling 的資深 UX 研究員。
 
 # 任務
 根據以下研究洞察與研究資料，提煉最重要的 3-5 個關鍵發現。
 
 請包含：
 - 使用者核心痛點
 - 行為模式
 - 情緒反應
 - 造成問題的可能原因
 - 對產品的影響
 
 # 格式要求
 請區分：
 - Key Insight
 - Evidence
 - Potential Impact
 
 # 情境
 [輸入研究背景、逐字稿、觀察資料、研究洞察]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**洞察資料**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Insight Data | ✅ 必填 | 洞察：使用者不是不願意支付手續費，而是不理解費用來源 |
| User Quote | ✅ 必填 | U01：「我不知道這個費用是誰收的。」 |
| Behavior Pattern | 選填 | 受訪者會截圖、請朋友確認、反覆查看交易紀錄 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 關鍵發現摘要

- [ ] 是否聚焦 3-5 個最重要發現
- [ ] 是否有證據支撐
- [ ] 是否能被非 UX 角色理解
- [ ] 是否避免只列現象不說影響

---

## 完成後下一步

> ✅ 建議接續：**DO-B-001、DO-B-002、DO-B-003、DO-C-002 DO-B-001、DO-B-002、DO-B-003、DO-C-002**


---

---
prompt_id: "DO-A-002"
task_name: "簡報架構生成"
stage: "產出物製作"
task_type: "report"
when_to_use: "當你已有研究洞察或分析結果，並需要整理成可溝通的報告內容或故事化摘要時"
when_not_to_use: "當缺少洞察資料或任務目標不是「簡報架構生成」時"
input_required:
  - "洞察資料"
output:
  - "Slide Outline"
next_best_actions:
  - "停下來進行人工檢查｜確認溝通對象與輸出目的是否正確"
---

# DO-A-002 簡報架構生成

**所屬階段：** 產出物製作

**適用情境：** Stakeholder Report

---

## Prompt 本文

```
# 角色
 你是一位擅長高層溝通的資深 UX 研究員。
 
 # 任務
 根據以下研究洞察，生成一份適合管理層閱讀的簡報架構。
 
 請包含：
 - 問題背景
 - 研究目的
 - 關鍵洞察
 - 使用者影響
 - 商業影響
 - 建議方向
 - 下一步行動
 
 # 格式要求
 請使用簡報章節格式輸出。
 
 # 情境
 [輸入研究背景、洞察、KPI、商業目標]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**洞察資料**

**此 Prompt 產出：** Slide Outline


---

---
prompt_id: "DO-A-003"
task_name: "洞察故事化表達"
stage: "產出物製作"
task_type: "report"
when_to_use: "當你已有研究洞察或分析結果，並需要整理成可溝通的報告內容或故事化摘要時"
when_not_to_use: "當缺少使用者洞察或任務目標不是「洞察故事化表達」時"
input_required:
  - "使用者洞察"
output:
  - "User Narrative"
next_best_actions:
  - "停下來進行人工檢查｜確認溝通對象與輸出目的是否正確"
---

# DO-A-003 洞察故事化表達

**所屬階段：** 產出物製作

**適用情境：** Executive Presentation

---

## Prompt 本文

```
# 角色
 你是一位擅長 Storytelling 的資深 UX 研究員。
 
 # 任務
 請根據以下研究資料，將研究洞察轉換成具體的使用者故事。
 
 請包含：
 - 使用情境
 - 使用者目標
 - 情緒變化
 - 遇到的問題
 - 問題造成的影響
 - 最終結果
 
 # 格式要求
 請區分：
 - User Story
 - Emotional Journey
 - Key Insight
 
 # 情境
 [輸入使用者原話、研究洞察、觀察紀錄]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**使用者洞察**

**此 Prompt 產出：** User Narrative


---

---
prompt_id: "DO-B-001"
task_name: "User Flow 生成"
stage: "產出物製作"
task_type: "produce"
when_to_use: "當你已有研究洞察、流程資料或設計方案，並需要具象化為「使用者操作流程 / User Flow」時"
when_not_to_use: "當缺少Flow And Research Data、Usage Scenario、User Behavior或任務目標不是「User Flow 生成」時"
input_required:
  - "Flow And Research Data"
  - "Usage Scenario"
  - "User Behavior"
output:
  - "使用者操作流程 / User Flow"
next_best_actions:
  - "DO-B-002｜Journey Map 草稿生成"
  - "DO-B-005｜設計決策說明生成"
---

# DO-B-001 User Flow 生成

**所屬階段：** 產出物製作

**適用情境：** UX Design

---

## Prompt 本文

```
# 角色
 你是一位精通資訊架構與使用者流程設計的資深 UX 設計師。
 
 # 任務
 根據以下研究洞察與產品情境，生成 User Flow 草稿。
 
 請包含：
 - 使用者目標
 - 關鍵操作步驟
 - 決策點
 - 錯誤情境
 - 流程結束條件
 
 # 格式要求
 請使用步驟式流程輸出。
 
 # 情境
 [輸入研究洞察、產品流程、使用情境]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**流程與研究資料**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Flow And Research Data | ✅ 必填 | 流程：設定資料 → 選擇受款人 → 輸入金額 → 確認 → 付款 → 查詢狀態 |
| Usage Scenario | ✅ 必填 | 移工在發薪後使用手機匯款給母國家人 |
| User Behavior | ✅ 必填 | 確認頁會停留較久；完成後會截圖傳給家人 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 使用者操作流程 / User Flow

- [ ] 是否反映真實使用情境
- [ ] 是否能對應使用者行為資料
- [ ] 是否避免只畫理想流程
- [ ] 是否清楚標示卡點與資訊需求

---

## 完成後下一步

> ✅ 建議接續：**DO-B-002、DO-B-005 DO-B-002、DO-B-005**


---

---
prompt_id: "DO-B-002"
task_name: "Journey Map 草稿生成"
stage: "產出物製作"
task_type: "produce"
when_to_use: "當你已有研究洞察、流程資料或設計方案，並需要具象化為「Journey Map 草稿」時"
when_not_to_use: "當缺少Emotion And Behavior Data、User Flow、User Feedback或任務目標不是「Journey Map 草稿生成」時"
input_required:
  - "Emotion And Behavior Data"
  - "User Flow"
  - "User Feedback"
output:
  - "Journey Map 草稿"
next_best_actions:
  - "DO-B-005｜設計決策說明生成"
  - "DO-C-002｜商業價值轉譯"
---

# DO-B-002 Journey Map 草稿生成

**所屬階段：** 產出物製作

**適用情境：** Service Design

---

## Prompt 本文

```
# 角色
 你是一位精通使用者心理與體驗設計的資深 UX 設計師。
 
 # 任務
 根據以下研究資料，生成 Journey Map 草稿。
 
 請包含：
 - 使用階段
 - 使用者目標
 - 行為
 - 情緒變化
 - 痛點
 - 機會點
 
 # 格式要求
 請使用 Journey Map 表格格式輸出。
 
 # 情境
 [輸入研究洞察、情緒資料、使用者行為]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**情緒與行為資料**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Emotion And Behavior Data | ✅ 必填 | 新增受款人：焦慮；確認頁：不確定；完成付款：希望獲得明確結果 |
| User Flow | ✅ 必填 | 設定資料 → 選擇受款人 → 輸入金額 → 確認 → 付款 → 查詢狀態 |
| User Feedback | ✅ 必填 | 我怕名字填錯錢就不見；我不確定交易處理中代表什麼 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** Journey Map 草稿

- [ ] 是否每個階段都有明確行為
- [ ] 情緒變化是否有依據
- [ ] 痛點與機會點是否能對應流程
- [ ] 是否避免只描述理想流程

---

## 完成後下一步

> ✅ 建議接續：**DO-B-005、DO-C-002 DO-B-005、DO-C-002**


---

---
prompt_id: "DO-B-003"
task_name: "Persona 文件化"
stage: "產出物製作"
task_type: "produce"
when_to_use: "當你已有研究洞察、流程資料或設計方案，並需要具象化為「Persona 文件草稿」時"
when_not_to_use: "當缺少Segmentation And Insight、User Needs、Behavior Pattern或任務目標不是「Persona 文件化」時"
input_required:
  - "Segmentation And Insight"
  - "User Needs"
  - "Behavior Pattern"
output:
  - "Persona 文件草稿"
next_best_actions:
  - "DO-B-005｜設計決策說明生成"
  - "DO-C-003｜簡報講稿生成"
---

# DO-B-003 Persona 文件化

**所屬階段：** 產出物製作

**適用情境：** UX Strategy

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 根據以下研究資料，生成 Persona 文件。
 
 請包含：
 - 基本背景
 - 使用目標
 - 痛點
 - 行為模式
 - 使用習慣
 - 動機
 - 數位能力
 
 # 格式要求
 請使用 Persona 卡片格式輸出。
 
 # 情境
 [輸入研究洞察、分群結果、使用者原話]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**分群與洞察**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Segmentation And Insight | ✅ 必填 | 類型 A：高度依賴同鄉協助者；類型 B：能獨立操作但重視確認資訊者 |
| User Needs | ✅ 必填 | 希望安全、快速地把錢匯給家人，並確認家人會收到 |
| Behavior Pattern | ✅ 必填 | 會截圖、請朋友確認、反覆查看交易紀錄 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** Persona 文件草稿

- [ ] 是否基於研究資料而非想像
- [ ] 是否避免刻板印象
- [ ] 是否能對應實際痛點與行為
- [ ] 是否有助於設計決策

---

## 完成後下一步

> ✅ 建議接續：**DO-B-005、DO-C-003 DO-B-005、DO-C-003**


---

---
prompt_id: "DO-B-004"
task_name: "UX 規格文件生成"
stage: "產出物製作"
task_type: "produce"
when_to_use: "當你已有研究洞察、流程資料或設計方案，並需要具象化為「UX Spec」時"
when_not_to_use: "當缺少功能與研究資料或任務目標不是「UX 規格文件生成」時"
input_required:
  - "功能與研究資料"
output:
  - "UX Spec"
next_best_actions:
  - "停下來進行人工檢查｜確認溝通對象與輸出目的是否正確"
---

# DO-B-004 UX 規格文件生成

**所屬階段：** 產出物製作

**適用情境：** Handoff

---

## Prompt 本文

```
# 角色
 你是一位具備產品與設計規格撰寫能力的資深 UX 設計師。
 
 # 任務
 請根據以下研究與設計資料，生成 UX 規格文件草稿。
 
 請包含：
 - 功能目的
 - 使用者需求
 - 操作流程
 - 狀態定義
 - 錯誤情境
 - Edge Case
 
 # 格式要求
 請使用 Markdown 層級標題輸出。
 
 # 情境
 [輸入研究洞察、設計方案、產品需求]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**功能與研究資料**

**此 Prompt 產出：** UX Spec


---

---
prompt_id: "DO-B-005"
task_name: "設計決策說明生成"
stage: "產出物製作"
task_type: "produce"
when_to_use: "當你已有研究洞察、流程資料或設計方案，並需要具象化為「設計決策說明」時"
when_not_to_use: "當缺少Design Proposal、Research Insight或任務目標不是「設計決策說明生成」時"
input_required:
  - "Design Proposal"
  - "Research Insight"
output:
  - "設計決策說明"
next_best_actions:
  - "DO-C-002｜商業價值轉譯"
  - "DO-C-006｜利害關係人問題預測"
---

# DO-B-005 設計決策說明生成

**所屬階段：** 產出物製作

**適用情境：** Stakeholder Review

---

## Prompt 本文

```
# 角色
 你是一位具備 UX 策略能力的資深 UX 設計師。
 
 # 任務
 請根據以下研究結果與設計方案，撰寫設計決策說明。
 
 請包含：
 - 設計目標
 - 研究依據
 - 為何採用此方案
 - 被解決的問題
 - 預期改善效果
 
 # 格式要求
 請區分：
 - Research Finding
 - Design Decision
 - Expected Outcome
 
 # 情境
 [輸入研究洞察、設計方案、測試結果]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**設計與研究資料**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Design Proposal | ✅ 必填 | 在確認頁補充費用來源說明，並強化交易處理中狀態說明 |
| Research Insight | ✅ 必填 | 使用者不理解交易狀態，導致信任感下降與反覆查詢 |
| User Behavior Data | 選填 | 使用者會在確認頁停留較久，並反覆查看費用資訊 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 設計決策說明

- [ ] 是否每個設計決策都有研究證據支撐
- [ ] 是否說明為何這樣設計
- [ ] 是否標示風險與待驗證事項
- [ ] 是否能支援利害關係人溝通

---

## 完成後下一步

> ✅ 建議接續：**DO-C-002、DO-C-006 DO-C-002、DO-C-006**


---

---
prompt_id: "DO-C-001"
task_name: "KPI 解釋與對齊"
stage: "產出物製作"
task_type: "translate"
when_to_use: "當你需要把 UX 研究結果轉譯給主管、PM、工程、營運或其他利害關係人時"
when_not_to_use: "當缺少UX 改動、年度目標、KPI，或尚未有足夠研究證據 / KPI 可支撐商業推論時"
input_required:
  - "UX 改動"
  - "年度目標"
  - "KPI"
output:
  - "KPI Alignment"
next_best_actions:
  - "停下來進行人工檢查｜確認溝通對象與輸出目的是否正確"
---

# DO-C-001 KPI 解釋與對齊

**所屬階段：** 產出物製作

**適用情境：** Report Management Review

---

## Prompt 本文

```
# 角色
 你是一位熟悉產品策略與數據分析的資深 UX 研究員。
 
 # 任務
 根據以下 UX 改動與公司 KPI，
 分析 UX 優化如何影響商業目標。
 
 請包含：
 
 - UX 問題與 KPI 的關聯
 - UX 改善可能帶來的指標變化
 - 哪些指標最能衡量 UX 成效
 - 改善前後應如何比較
 - 建議的觀察期間
 
 請協助建立：
 - Leading KPI
 - Lagging KPI
 
 # 格式要求
 請區分：
 
 ## UX 問題
 ## KPI 關聯
 ## 建議追蹤指標
 ## 預期改善方向
 ## 風險與限制
 
 # 情境
 [輸入 UX 改動內容、研究發現、年度 KPI]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**UX 改動、年度目標、KPI**

**此 Prompt 產出：** KPI Alignment


---

---
prompt_id: "DO-C-002"
task_name: "商業價值轉譯"
stage: "產出物製作"
task_type: "translate"
when_to_use: "當你需要把 UX 研究結果轉譯給主管、PM、工程、營運或其他利害關係人時"
when_not_to_use: "當缺少UX Insight、Research Result、Product Goal，或尚未有足夠研究證據 / KPI 可支撐商業推論時"
input_required:
  - "UX Insight"
  - "Research Result"
  - "Product Goal"
output:
  - "商業價值摘要"
next_best_actions:
  - "DO-C-006｜利害關係人問題預測"
  - "DO-C-003｜簡報講稿生成"
---

# DO-C-002 商業價值轉譯

**所屬階段：** 產出物製作

**適用情境：** Cross-functional Meeting

---

## Prompt 本文

```
# 角色
 你是一位具備商業思維的資深 UX 研究員。
 
 # 任務
 根據以下研究結果與 UX 洞察，
 協助我將 UX 發現轉譯成商業價值。
 
 請分析：
 
 - 對轉換率的可能影響
 - 對留存率的可能影響
 - 對客服成本的可能影響
 - 對使用者信任感的影響
 - 對產品競爭力的影響
 - 對營運效率的影響
 
 請同時說明：
 - 為什麼這些 UX 問題會影響商業 KPI
 - 哪些指標最值得優先追蹤
 
 # 格式要求
 請區分：
 
 ## UX 發現
 ## 商業影響
 ## 風險
 ## 建議追蹤 KPI
 ## 建議行動
 
 # 情境
 [輸入研究結果、使用者洞察、商業目標]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**UX 洞察、研究結果、商業 KPI**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| UX Insight | ✅ 必填 | 使用者不理解交易處理中的狀態，導致信任感下降與重複查詢 |
| Research Result | ✅ 必填 | 本次訪談發現移工最在意安全、資料正確性與到帳確認 |
| Business KPI | 選填 | 受款人設定完成率 68%；交易處理中相關客服詢問佔 15% |
| Product Goal | ✅ 必填 | 提升首次匯款完成率、降低客服詢問量、提高使用者信任 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 商業價值摘要

- [ ] 是否有對應產品目標或 KPI
- [ ] 是否避免空泛描述
- [ ] 是否清楚說明 UX 問題如何影響完成率、客服量、信任或留存

---

## 完成後下一步

> ✅ 建議接續：**DO-C-006、DO-C-003 DO-C-006、DO-C-003**


---

---
prompt_id: "DO-C-003"
task_name: "簡報講稿生成"
stage: "產出物製作"
task_type: "communicate"
when_to_use: "當你需要把 UX 研究結果轉譯給主管、PM、工程、營運或其他利害關係人時"
when_not_to_use: "當缺少Research Outcome、Business Context、Insight Data，或尚未有足夠研究證據 / KPI 可支撐商業推論時"
input_required:
  - "Research Outcome"
  - "Business Context"
  - "Insight Data"
  - "Recommendation"
output:
  - "跨部門簡報講稿"
next_best_actions:
  - "停下來進行人工檢查｜確認溝通對象與輸出目的是否正確"
---

# DO-C-003 簡報講稿生成

**所屬階段：** 產出物製作

**適用情境：** Stakeholder Presentation

---

## Prompt 本文

```
# 角色
 你是一位擅長 Storytelling 與跨部門溝通的資深 UX 研究員。
 
 # 任務
 根據以下研究成果，
 協助我生成一份適合跨部門會議的簡報講稿。
 
 請包含：
 
 - 問題背景
 - 使用者情境
 - 關鍵研究發現
 - 商業影響
 - UX 改善方向
 - 建議行動方案
 
 請特別強化：
 - 說服力
 - 邏輯流暢度
 - 非設計部門可理解性
 
 # 格式要求
 請區分：
 
 ## 開場
 ## 問題說明
 ## 使用者故事
 ## 關鍵洞察
 ## 商業影響
 ## 建議方案
 ## 結尾與行動呼籲
 
 # 情境
 [輸入研究專案背景、洞察、商業目標]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**研究成果、商業背景、洞察資料**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Research Outcome | ✅ 必填 | 本次訪談發現移工最在意安全、資料正確性與到帳確認 |
| Business Context | ✅ 必填 | 團隊希望提升首次匯款完成率並降低交易狀態相關客服詢問 |
| Insight Data | ✅ 必填 | 洞察 1：使用者把資料填寫正確視為匯款是否安全的關鍵 |
| Recommendation | ✅ 必填 | 優化確認頁資訊層級；補充交易處理中說明；強化資料送出前確認 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 跨部門簡報講稿

- [ ] 是否針對非設計角色說明
- [ ] 是否有清楚問題、證據、影響與建議
- [ ] 是否避免過多 UX 術語
- [ ] 是否能導向決策

---


---

---
prompt_id: "DO-C-006"
task_name: "利害關係人問題預測"
stage: "產出物製作"
task_type: "communicate"
when_to_use: "當你需要把 UX 研究結果轉譯給主管、PM、工程、營運或其他利害關係人時"
when_not_to_use: "當缺少Proposal Content、Research Result，或尚未有足夠研究證據 / KPI 可支撐商業推論時"
input_required:
  - "Proposal Content"
  - "Research Result"
output:
  - "利害關係人 QA / Objection List"
next_best_actions:
  - "DO-C-003｜簡報講稿生成"
---

# DO-C-006 利害關係人問題預測

**所屬階段：** 產出物製作

**適用情境：** Proposal Review

---

## Prompt 本文

```
# 角色
 你是一位具備產品策略與跨部門溝通能力的資深 UX 研究員。
 
 # 任務
 根據以下提案內容與研究結果，
 預測利害關係人可能提出的質疑與問題。
 
 請分析：
 
 - 管理層可能疑慮
 - PM 可能疑慮
 - 工程團隊可能疑慮
 - 商業部門可能疑慮
 - 數據可信度問題
 - 資源與成本問題
 
 並協助提供：
 - 建議回應方式
 - 補充數據建議
 - 溝通策略
 
 # 格式要求
 請區分：
 
 ## 潛在問題
 ## 為何會被質疑
 ## 建議回應
 ## 建議補充資料
 
 # 情境
 [輸入提案內容、研究結果、商業背景]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**提案內容、研究結果、商業風險**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Proposal Content | ✅ 必填 | 建議優化確認頁資訊層級，並補充交易處理中的狀態說明 |
| Research Result | ✅ 必填 | 使用者對資料正確性、費用來源與交易狀態最容易產生不確定感 |
| Business Risk | 選填 | 修改流程可能增加頁面資訊量；狀態說明需符合法規與營運邏輯 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 利害關係人 QA / Objection List

- [ ] 是否涵蓋不同角色的關切
- [ ] 是否能連結研究證據與商業影響
- [ ] 是否避免只列問題不提供回應方向

---

## 完成後下一步

> ✅ 建議接續：**DO-C-003 簡報講稿生成**


---

---
prompt_id: "DO-D-001"
task_name: "HMW 問題生成"
stage: "產出物製作"
task_type: "synthesize"
when_to_use: "當你已有研究洞察、關鍵發現或 Persona，並需要將其轉為「How Might We 設計問題」以定義設計方向、銜接後續發想時"
when_not_to_use: "當研究洞察或 Persona 尚未成形、痛點仍不清楚，無法收斂出有意義的設計問題時"
input_required:
  - "Insight Data"
  - "Persona"
output:
  - "HMW 問題集 / How Might We 問題"
next_best_actions:
  - "DO-B-001｜User Flow 生成"
  - "DO-C-002｜商業價值轉譯"
---

# DO-D-001 HMW 問題生成

**所屬階段：** 產出物製作

**適用情境：** 設計問題定義 / 機會框架

---

## Prompt 本文

```
# 角色
 你是一位資深 UX / 服務設計師，擅長將研究洞察轉化為可發想的設計問題。
 
 # 任務
 根據以下研究洞察、關鍵發現與 Persona，生成一組「How Might We（我們如何）」設計問題。
 
 請遵循：
 - 每個 HMW 由一個洞察或痛點轉化而來，並標註其來源
 - 保持在適當高度：不要窄到已內含解法，也不要廣到無法發想
 - 依主題（Theme）分組，並標註對應的 Persona 與商業目標
 - 每個 HMW 以「我們如何……？」開頭，語氣正向、聚焦機會
 
 # 格式要求
 請以下列結構輸出：
 - Theme（主題）
 - 對應洞察 / 痛點（來源）
 - 對應 Persona 與商業槓桿
 - HMW 問題（2-4 條）
 最後彙整「候選設計方向」清單，供收斂使用。
 
 # 情境
 [輸入研究洞察 / 關鍵發現 / Persona / 機會點]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**研究洞察、關鍵發現、Persona、機會點**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Insight Data | ✅ 必填 | 洞察：移工怕被騙，「怕被騙」是送件前最大流失點 |
| Persona | ✅ 必填 | 印尼社福看護 Siti：只懂印尼語、社交孤立、易被地下錢莊吸收 |
| 機會點 / 商業目標 | 選填 | 機會點：試算前置；商業槓桿：名單費（試算→送件轉換） |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** HMW 問題集 / How Might We 問題

- [ ] 每個 HMW 是否可追溯到具體洞察或痛點
- [ ] 高度是否適中（未內含解法、也非空泛）
- [ ] 是否以「我們如何……？」正向開放句型呈現
- [ ] 是否依主題分組並連結 Persona 與商業目標
- [ ] 是否能直接銜接後續發想 / 設計方向收斂

---

## 完成後下一步

> ✅ 建議接續：**DO-B-001 User Flow 生成、DO-C-002 商業價值轉譯**


---

---
prompt_id: "IT-A-001"
task_name: "啟發式評估"
stage: "迭代測試"
task_type: "validate"
when_to_use: "當你已有設計稿、Prototype 或流程，並需要做設計品質、可用性或一致性檢查時"
when_not_to_use: "當缺少設計稿、Prototype、測試資料或明確任務目標時"
input_required:
  - "Prototype"
output:
  - "Heuristic Report"
next_best_actions:
  - "整理測試結果｜決定是否進入成效追蹤或設計修正"
---

# IT-A-001 啟發式評估

**所屬階段：** 迭代測試

**適用情境：** UX QA

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請根據以下 Prototype 或畫面進行啟發式評估。
 
 請分析：
 - 系統狀態可見性
 - 一致性
 - 錯誤預防
 - 使用者控制感
 - 認知負擔
 
 # 格式要求
 請使用 heuristic evaluation table 輸出。
 
 # 情境
 [輸入 Prototype、畫面或流程]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**Prototype**

**此 Prompt 產出：** Heuristic Report


---

---
prompt_id: "IT-A-002"
task_name: "認知走查"
stage: "迭代測試"
task_type: "validate"
when_to_use: "當你已有設計稿、Prototype 或流程，並需要做設計品質、可用性或一致性檢查時"
when_not_to_use: "當缺少設計稿、Prototype、測試資料或明確任務目標時"
input_required:
  - "流程資料"
output:
  - "Walkthrough Analysis"
next_best_actions:
  - "整理測試結果｜決定是否進入成效追蹤或設計修正"
---

# IT-A-002 認知走查

**所屬階段：** 迭代測試

**適用情境：** Flow Review

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請針對以下操作流程進行認知走查。
 
 請分析：
 - 使用者是否理解下一步
 - 是否容易發現操作
 - 是否符合使用者預期
 - 是否容易迷失
 - 是否存在認知阻礙
 
 # 格式要求
 請依照步驟輸出分析。
 
 # 情境
 [輸入流程或 Prototype]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**流程資料**

**此 Prompt 產出：** Walkthrough Analysis


---

---
prompt_id: "IT-A-003"
task_name: "Design QA"
stage: "迭代測試"
task_type: "validate"
when_to_use: "當你已有設計稿、Prototype 或流程，並需要做設計品質、可用性或一致性檢查時"
when_not_to_use: "當缺少設計稿、Prototype、測試資料或明確任務目標時"
input_required:
  - "設計稿"
output:
  - "QA Report"
next_best_actions:
  - "整理測試結果｜決定是否進入成效追蹤或設計修正"
---

# IT-A-003 Design QA

**所屬階段：** 迭代測試

**適用情境：** Design Review

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請檢查以下設計稿是否存在 UX 問題。
 
 請包含：
 - 一致性問題
 - UI 可理解性
 - 操作風險
 - 錯誤情境
 - Accessibility 問題
 
 # 格式要求
 請以 QA checklist 輸出。
 
 # 情境
 [輸入設計稿或 Prototype]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**設計稿**

**此 Prompt 產出：** QA Report


---

---
prompt_id: "IT-A-004"
task_name: "無障礙檢查"
stage: "迭代測試"
task_type: "validate"
when_to_use: "當你已有設計稿、Prototype 或流程，並需要做設計品質、可用性或一致性檢查時"
when_not_to_use: "當缺少設計稿、Prototype、測試資料或明確任務目標時"
input_required:
  - "畫面與 Prototype"
output:
  - "Accessibility Report"
next_best_actions:
  - "整理測試結果｜決定是否進入成效追蹤或設計修正"
---

# IT-A-004 無障礙檢查

**所屬階段：** 迭代測試

**適用情境：** Accessibility QA

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請檢查以下介面是否符合無障礙設計原則。
 
 請分析：
 - 對比度
 - 可讀性
 - 操作可及性
 - 鍵盤操作
 - 輔助工具支援
 
 # 格式要求
 請依照 WCAG 檢查項目輸出。
 
 # 情境
 [輸入畫面或 Prototype]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**畫面與 Prototype**

**此 Prompt 產出：** Accessibility Report


---

---
prompt_id: "IT-A-005"
task_name: "互動一致性檢查"
stage: "迭代測試"
task_type: "validate"
when_to_use: "當你已有設計稿、Prototype 或流程，並需要做設計品質、可用性或一致性檢查時"
when_not_to_use: "當缺少設計稿、Prototype、測試資料或明確任務目標時"
input_required:
  - "流程與畫面"
output:
  - "Consistency Report"
next_best_actions:
  - "整理測試結果｜決定是否進入成效追蹤或設計修正"
---

# IT-A-005 互動一致性檢查

**所屬階段：** 迭代測試

**適用情境：** UI System QA

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請分析以下產品流程中的互動一致性。
 
 請包含：
 - UI Pattern 一致性
 - 名稱一致性
 - 操作邏輯一致性
 - 回饋機制一致性
 - 潛在認知混亂
 
 # 格式要求
 請以 consistency review table 輸出。
 
 # 情境
 [輸入流程或畫面]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**流程與畫面**

**此 Prompt 產出：** Consistency Report


---

---
prompt_id: "IT-B-001"
task_name: "任務成功率分析"
stage: "迭代測試"
task_type: "evaluate"
when_to_use: "當你已有測試結果或改善前後資料，並需要評估體驗差異或任務表現時"
when_not_to_use: "當缺少設計稿、Prototype、測試資料或明確任務目標時"
input_required:
  - "Testing Result"
output:
  - "Success KPI"
next_best_actions:
  - "整理測試結果｜決定是否進入成效追蹤或設計修正"
---

# IT-B-001 任務成功率分析

**所屬階段：** 迭代測試

**適用情境：** usability Analysis

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請根據以下 usability testing 結果分析任務成功率。
 
 請包含：
 - 成功率
 - 失敗率
 - 中斷位置
 - 高風險步驟
 - 使用者回饋
 
 # 格式要求
 請以 task success table 輸出。
 
 # 情境
 [輸入 usability testing 結果]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**Testing Result**

**此 Prompt 產出：** Success KPI


---

---
prompt_id: "IT-B-003"
task_name: "改善前後比較"
stage: "迭代測試"
task_type: "evaluate"
when_to_use: "當你已有測試結果或改善前後資料，並需要評估體驗差異或任務表現時"
when_not_to_use: "當缺少設計稿、Prototype、測試資料或明確任務目標時"
input_required:
  - "KPI Data"
output:
  - "Improvement Report"
next_best_actions:
  - "整理測試結果｜決定是否進入成效追蹤或設計修正"
---

# IT-B-003 改善前後比較

**所屬階段：** 迭代測試

**適用情境：** UX Iteration

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請比較以下 UX 改善前後的使用體驗差異。
 
 請包含：
 - 完成時間
 - 任務成功率
 - 錯誤次數
 - 使用者信心
 - 滿意度
 
 # 格式要求
 請以 comparison summary 輸出。
 
 # 情境
 [輸入測試數據]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**KPI Data**

**此 Prompt 產出：** Improvement Report


---

---
prompt_id: "IT-B-004"
task_name: "流程清晰度評估"
stage: "迭代測試"
task_type: "evaluate"
when_to_use: "當你已有測試結果或改善前後資料，並需要評估體驗差異或任務表現時"
when_not_to_use: "當缺少設計稿、Prototype、測試資料或明確任務目標時"
input_required:
  - "Testing Data"
output:
  - "Clarity Analysis"
next_best_actions:
  - "整理測試結果｜決定是否進入成效追蹤或設計修正"
---

# IT-B-004 流程清晰度評估

**所屬階段：** 迭代測試

**適用情境：** Flow Optimization

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請分析以下流程是否足夠清晰易懂。
 
 請包含：
 - 流程理解程度
 - UI 引導性
 - 文案清晰度
 - 認知負擔
 - 容易迷失的位置
 
 # 格式要求
 請使用 clarity evaluation table 輸出。
 
 # 情境
 [輸入流程與測試資料]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**Testing Data**

**此 Prompt 產出：** Clarity Analysis


---

---
prompt_id: "PT-A-001"
task_name: "完成率分析"
stage: "成效追蹤"
task_type: "measure"
when_to_use: "當你已有 KPI、產品分析或成效數據，並需要追蹤 UX 改動後的影響時"
when_not_to_use: "當缺少KPI Data，或尚未有足夠研究證據 / KPI 可支撐商業推論時"
input_required:
  - "KPI Data"
output:
  - "Completion Report"
next_best_actions:
  - "停下來進行人工檢查｜確認 KPI 解讀是否有足夠數據支持"
---

# PT-A-001 完成率分析

**所屬階段：** 成效追蹤

**適用情境：** Flow KPI

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請分析以下 User Flow 的任務完成率。
 
 請包含：
 - 完成率
 - 中斷率
 - 高風險步驟
 - 流程阻礙
 - 改善建議
 
 # 格式要求
 請以 KPI summary table 輸出。
 
 # 情境
 [輸入 User Flow KPI 資料]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**KPI Data**

**此 Prompt 產出：** Completion Report


---

---
prompt_id: "PT-A-002"
task_name: "完成時間分析"
stage: "成效追蹤"
task_type: "measure"
when_to_use: "當你已有 KPI、產品分析或成效數據，並需要追蹤 UX 改動後的影響時"
when_not_to_use: "當缺少KPI Data，或尚未有足夠研究證據 / KPI 可支撐商業推論時"
input_required:
  - "KPI Data"
output:
  - "Time Analysis"
next_best_actions:
  - "停下來進行人工檢查｜確認 KPI 解讀是否有足夠數據支持"
---

# PT-A-002 完成時間分析

**所屬階段：** 成效追蹤

**適用情境：** UX Optimization

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請分析以下 User Flow 的任務完成時間。
 
 請包含：
 - 平均完成時間
 - 最長停留步驟
 - 時間異常點
 - 流程效率問題
 - 改善方向
 
 # 格式要求
 請以 before / after KPI table 輸出。
 
 # 情境
 [輸入流程數據]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**KPI Data**

**此 Prompt 產出：** Time Analysis


---

---
prompt_id: "PT-A-003"
task_name: "跳出/猶豫點追蹤分析"
stage: "成效追蹤"
task_type: "measure"
when_to_use: "當你已有 KPI、產品分析或成效數據，並需要追蹤 UX 改動後的影響時"
when_not_to_use: "當缺少Funnel Data，或尚未有足夠研究證據 / KPI 可支撐商業推論時"
input_required:
  - "Funnel Data"
output:
  - "Drop-off Insight"
next_best_actions:
  - "停下來進行人工檢查｜確認 KPI 解讀是否有足夠數據支持"
---

# PT-A-003 跳出/猶豫點追蹤分析

**所屬階段：** 成效追蹤

**適用情境：** Funnel Optimization

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請分析以下流程中的 Drop-off 狀況。
 
 請包含：
 - Drop-off 位置
 - 流失率
 - 可能原因
 - 使用者情緒
 - UX 問題
 
 # 格式要求
 請使用 funnel analysis 格式輸出。
 
 # 情境
 [輸入流程數據]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**Funnel Data**

**此 Prompt 產出：** Drop-off Insight


---

---
prompt_id: "PT-C-001"
task_name: "轉換率影響分析"
stage: "成效追蹤"
task_type: "measure"
when_to_use: "當你已有 KPI、產品分析或成效數據，並需要追蹤 UX 改動後的影響時"
when_not_to_use: "當缺少KPI 與 UX Data，或尚未有足夠研究證據 / KPI 可支撐商業推論時"
input_required:
  - "KPI 與 UX Data"
output:
  - "Conversion Report"
next_best_actions:
  - "停下來進行人工檢查｜確認 KPI 解讀是否有足夠數據支持"
---

# PT-C-001 轉換率影響分析

**所屬階段：** 成效追蹤

**適用情境：** Growth UX

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請分析以下 UX 改動對轉換率的影響。
 
 請包含：
 - 轉換率變化
 - 關鍵影響因素
 - 高影響步驟
 - 使用者行為變化
 - 商業影響
 
 # 格式要求
 請以 conversion impact report 輸出。
 
 # 情境
 [輸入 KPI 與 UX 改動資料]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**KPI 與 UX Data**

**此 Prompt 產出：** Conversion Report


---

---
prompt_id: "PT-C-002"
task_name: "留存率影響評估"
stage: "成效追蹤"
task_type: "measure"
when_to_use: "當你已有 KPI、產品分析或成效數據，並需要追蹤 UX 改動後的影響時"
when_not_to_use: "當缺少Retention Data，或尚未有足夠研究證據 / KPI 可支撐商業推論時"
input_required:
  - "Retention Data"
output:
  - "Retention Insight"
next_best_actions:
  - "停下來進行人工檢查｜確認 KPI 解讀是否有足夠數據支持"
---

# PT-C-002 留存率影響評估

**所屬階段：** 成效追蹤

**適用情境：** Product Strategy

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請分析以下 UX 改善是否影響使用者留存率。
 
 請包含：
 - 留存率變化
 - 使用者回流原因
 - 使用者流失原因
 - UX 影響因素
 - 改善方向
 
 # 格式要求
 請以 retention analysis summary 輸出。
 
 # 情境
 [輸入產品數據]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**Retention Data**

**此 Prompt 產出：** Retention Insight


---

---
prompt_id: "PT-C-003"
task_name: "客服工單降低分析"
stage: "成效追蹤"
task_type: "measure"
when_to_use: "當你已有 KPI、產品分析或成效數據，並需要追蹤 UX 改動後的影響時"
when_not_to_use: "當缺少CS Data，或尚未有足夠研究證據 / KPI 可支撐商業推論時"
input_required:
  - "CS Data"
output:
  - "Support Impact"
next_best_actions:
  - "停下來進行人工檢查｜確認 KPI 解讀是否有足夠數據支持"
---

# PT-C-003 客服工單降低分析

**所屬階段：** 成效追蹤

**適用情境：** Service Design

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請分析以下 UX 改善是否降低客服工單量。
 
 請包含：
 - 工單變化
 - 常見問題類型
 - 使用者困惑點
 - UX 改善效果
 - 營運影響
 
 # 格式要求
 請以 support ticket analysis 輸出。
 
 # 情境
 [輸入客服與 UX 資料]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**CS Data**

**此 Prompt 產出：** Support Impact


---

---
prompt_id: "PT-C-005"
task_name: "功能使用率分析"
stage: "成效追蹤"
task_type: "measure"
when_to_use: "當你已有 KPI、產品分析或成效數據，並需要追蹤 UX 改動後的影響時"
when_not_to_use: "當缺少Product Analytics，或尚未有足夠研究證據 / KPI 可支撐商業推論時"
input_required:
  - "Product Analytics"
output:
  - "Usage Insight"
next_best_actions:
  - "停下來進行人工檢查｜確認 KPI 解讀是否有足夠數據支持"
---

# PT-C-005 功能使用率分析

**所屬階段：** 成效追蹤

**適用情境：** Feature Optimization

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請分析以下功能的使用率與使用行為。
 
 請包含：
 - 使用率
 - 高頻功能
 - 低使用功能
 - 使用行為差異
 - UX 問題
 
 # 格式要求
 請以 feature usage analysis table 輸出。
 
 # 情境
 [輸入產品數據]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**Product Analytics**

**此 Prompt 產出：** Usage Insight


---

---
prompt_id: "PT-D-001"
task_name: "KPI Dashboard 摘要生成"
stage: "成效追蹤"
task_type: "measure"
when_to_use: "當你已有 KPI、產品分析或成效數據，並需要追蹤 UX 改動後的影響時"
when_not_to_use: "當缺少Dashboard Data，或尚未有足夠研究證據 / KPI 可支撐商業推論時"
input_required:
  - "Dashboard Data"
output:
  - "KPI Summary"
next_best_actions:
  - "停下來進行人工檢查｜確認 KPI 解讀是否有足夠數據支持"
---

# PT-D-001 KPI Dashboard 摘要生成

**所屬階段：** 成效追蹤

**適用情境：** Executive Review

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請根據以下 KPI Dashboard 數據生成摘要。
 
 請包含：
 - 核心 KPI 變化
 - 高風險指標
 - 改善成果
 - 潛在問題
 - 下一步建議
 
 # 格式要求
 請區分「Insight」、「Risk」、「Recommendation」。
 
 # 情境
 [輸入 Dashboard 數據]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**Dashboard Data**

**此 Prompt 產出：** KPI Summary


---

---
prompt_id: "PT-D-002"
task_name: "改善前後報告生成"
stage: "成效追蹤"
task_type: "measure"
when_to_use: "當你已有 KPI、產品分析或成效數據，並需要追蹤 UX 改動後的影響時"
when_not_to_use: "當缺少KPI Data，或尚未有足夠研究證據 / KPI 可支撐商業推論時"
input_required:
  - "KPI Data"
output:
  - "Improvement Report"
next_best_actions:
  - "停下來進行人工檢查｜確認 KPI 解讀是否有足夠數據支持"
---

# PT-D-002 改善前後報告生成

**所屬階段：** 成效追蹤

**適用情境：** Stakeholder Review

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請比較以下 UX 改善前後的成效。
 
 請包含：
 - KPI 差異
 - 使用者行為變化
 - UX 成果
 - 商業影響
 - 後續建議
 
 # 格式要求
 請以 before / after report 輸出。
 
 # 情境
 [輸入改善前後資料]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**KPI Data**

**此 Prompt 產出：** Improvement Report


---

---
prompt_id: "PT-D-004"
task_name: "管理層報告生成"
stage: "成效追蹤"
task_type: "measure"
when_to_use: "當你已有 KPI、產品分析或成效數據，並需要追蹤 UX 改動後的影響時"
when_not_to_use: "當缺少KPI 與研究資料，或尚未有足夠研究證據 / KPI 可支撐商業推論時"
input_required:
  - "KPI 與研究資料"
output:
  - "Executive Summary"
next_best_actions:
  - "停下來進行人工檢查｜確認 KPI 解讀是否有足夠數據支持"
---

# PT-D-004 管理層報告生成

**所屬階段：** 成效追蹤

**適用情境：** Leadership Meeting

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請根據以下研究成果生成管理層摘要報告。
 
 請包含：
 - 關鍵成果
 - 高風險問題
 - 商業影響
 - 優先改善項目
 - 下一步建議
 
 # 格式要求
 請使用 executive summary format。
 
 # 情境
 [輸入研究與 KPI 資料]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**KPI 與研究資料**

**此 Prompt 產出：** Executive Summary


---

---
prompt_id: "RP-A-001"
task_name: "AI Persona 建立"
stage: "研究規劃與準備"
task_type: "plan"
when_to_use: "當你需要在研究啟動階段釐清「AI Persona 建立」，並把產品背景、功能描述、整理成可執行研究方向時"
when_not_to_use: "當產品背景、研究目的或決策問題尚不清楚，無法定義「AI Persona 建立」時"
input_required:
  - "產品背景"
  - "功能描述"
output:
  - "目標用戶 Persona 文件"
next_best_actions:
  - "檢查研究目標與輸入資料是否足夠｜決定下一個研究規劃或招募任務"
---

# RP-A-001 AI Persona 建立

**所屬階段：** 研究規劃與準備

**適用情境：** 新產品探索、早期研究

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 根據以下情境，產出三種不同類型的使用者 Persona。
 
 請包含：
 - 基本背景
 - 使用情境
 - 主要目標
 - 痛點
 - 行為特徵
 - 數位能力
 - 對產品的期待
 
 # 格式要求
 請使用表格格式輸出。
 
 # 情境
 [輸入產品 / 功能 / 研究背景]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**產品背景、功能描述、**

**此 Prompt 產出：** 目標用戶 Persona 文件


---

---
prompt_id: "RP-A-002"
task_name: "使用者族群定義"
stage: "研究規劃與準備"
task_type: "plan"
when_to_use: "當你需要在研究啟動階段釐清「使用者族群定義」，並把產品情境、商業目標整理成可執行研究方向時"
when_not_to_use: "當產品背景、研究目的或決策問題尚不清楚，無法定義「使用者族群定義」時"
input_required:
  - "產品情境"
  - "商業目標"
output:
  - "使用者分群"
next_best_actions:
  - "檢查研究目標與輸入資料是否足夠｜決定下一個研究規劃或招募任務"
---

# RP-A-002 使用者族群定義

**所屬階段：** 研究規劃與準備

**適用情境：** 市場切分、功能規劃

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 根據以下產品情境，定義主要與次要使用者族群。
 
 請分析：
 - 使用者類型
 - 使用動機
 - 使用頻率
 - 行為差異
 - 關鍵需求
 - 高價值使用者特徵
 
 # 格式要求
 請以「主要族群 / 次要族群」分類輸出。
 
 # 情境
 [輸入產品 / 功能 / 研究背景]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**產品情境、商業目標**

**此 Prompt 產出：** 使用者分群


---

---
prompt_id: "RP-A-003"
task_name: "研究目標定義"
stage: "研究規劃與準備"
task_type: "plan"
when_to_use: "當你需要在研究啟動階段釐清「研究目標定義」，並把產品問題、研究背景整理成可執行研究方向時"
when_not_to_use: "當產品背景、研究目的或決策問題尚不清楚，無法定義「研究目標定義」時"
input_required:
  - "Product Context"
  - "Business Problem"
  - "Research Need"
output:
  - "研究目標文件"
next_best_actions:
  - "RP-A-004｜研究假設撰寫"
---

# RP-A-003 研究目標定義

**所屬階段：** 研究規劃與準備

**適用情境：** Kickoff、研究規劃

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 根據以下產品情境，定義本次 UX 研究目標。
 
 請協助分析：
 - 使用者問題
 - 商業問題
 - 欲驗證假設
 - 研究成功條件
 - 研究範圍
 
 # 格式要求
 請區分：
 - Primary Goal
 - Secondary Goal
 - Out of Scope
 
 # 情境
 [輸入產品 / 功能 / 研究背景]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**產品問題、研究背景**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Product Context | ✅ 必填 | 產品：小額跨境匯兌服務；對象：在台移工；階段：既有流程優化 |
| Business Problem | ✅ 必填 | 首次匯款完成率偏低，使用者在填寫資料或確認資訊時容易中斷 |
| Current Flow Problem | 選填 | 使用者不理解受款人資料欄位；不確定交易狀態代表什麼 |
| Research Need | ✅ 必填 | 了解移工在小額跨境匯兌流程中的理解困難、信任疑慮與操作阻礙 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 研究目標文件

- [ ] 是否聚焦在可研究的問題
- [ ] 是否避免研究目標過大
- [ ] 是否區分研究範圍與非研究範圍
- [ ] 是否能支援後續研究假設與研究問題生成

---

## 完成後下一步

> ✅ 建議接續：**RP-A-004 研究假設撰寫**


---

---
prompt_id: "RP-A-004"
task_name: "研究假設撰寫"
stage: "研究規劃與準備"
task_type: "plan"
when_to_use: "當你需要在研究啟動階段釐清「研究假設撰寫」，並把商業問題、使用者問題整理成可執行研究方向時"
when_not_to_use: "當產品背景、研究目的或決策問題尚不清楚，無法定義「研究假設撰寫」時"
input_required:
  - "Research Goal"
  - "Business Problem"
  - "User Problem"
output:
  - "研究假設列表"
next_best_actions:
  - "RP-A-005｜研究問題生成"
---

# RP-A-004 研究假設撰寫

**所屬階段：** 研究規劃與準備

**適用情境：** 假設驗證研究

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 根據以下研究背景，產出可驗證的 UX 研究假設。
 
 請包含：
 - 假設內容
 - 假設原因
 - 預期行為
 - 驗證方式
 - 可能風險
 
 # 格式要求
 請使用：
 「我們相信...因此預期使用者會...」
 格式輸出。
 
 # 情境
 [輸入產品 / 功能 / 研究背景]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**商業問題、使用者問題**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Research Goal | ✅ 必填 | 找出移工完成跨境匯兌流程中的關鍵阻礙 |
| Business Problem | ✅ 必填 | 受款人設定流程中斷可能影響首次匯款完成率 |
| User Problem | ✅ 必填 | 使用者擔心英文姓名填錯；不理解手續費與到帳資訊 |
| Current Assumption | 選填 | 若在確認頁補充費用說明，使用者信任感會提升 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 研究假設列表

- [ ] 是否每個假設都可被訪談驗證
- [ ] 是否避免過度推論
- [ ] 是否清楚區分使用者假設與商業假設
- [ ] 是否能支援後續研究問題生成

---

## 完成後下一步

> ✅ 建議接續：**RP-A-005 研究問題生成**


---

---
prompt_id: "RP-A-005"
task_name: "研究問題生成"
stage: "研究規劃與準備"
task_type: "plan"
when_to_use: "當你需要在研究啟動階段釐清「研究問題生成」，並把研究目標、產品情境整理成可執行研究方向時"
when_not_to_use: "當產品背景、研究目的或決策問題尚不清楚，無法定義「研究問題生成」時"
input_required:
  - "Research Goal"
  - "Product Scenario"
output:
  - "研究問題清單"
next_best_actions:
  - "RP-B-001｜受訪者條件定義"
  - "RP-D-001｜訪談腳本撰寫"
---

# RP-A-005 研究問題生成

**所屬階段：** 研究規劃與準備

**適用情境：** 訪談設計、研究設計

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 根據以下研究情境，生成適合 UX Research 的研究問題。
 
 請包含：
 - 行為問題
 - 動機問題
 - 心智模型問題
 - 痛點問題
 - 決策因素問題
 
 # 格式要求
 請將問題依照主題分類。
 
 # 情境
 [輸入產品 / 功能 / 研究背景]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**研究目標、產品情境**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Research Goal | ✅ 必填 | 主要目標：了解移工在跨境匯兌流程中的理解與信任阻礙 |
| Product Scenario | ✅ 必填 | 使用者下班後用手機匯款給母國家人，需要設定資料、輸入金額並確認交易狀態 |
| Open Questions | 選填 | 使用者是否理解英文姓名填寫規則？是否信任交易處理中的狀態？ |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 研究問題清單

- [ ] 是否每個問題都對應研究目標
- [ ] 是否避免誘導性問法
- [ ] 是否涵蓋行為、動機、理解、信任與流程阻礙
- [ ] 是否能支援訪談腳本設計

---

## 完成後下一步

> ✅ 建議接續：**RP-B-001、RP-D-001 RP-B-001、RP-D-001**


---

---
prompt_id: "RP-B-001"
task_name: "受訪者條件定義"
stage: "研究規劃與準備"
task_type: "recruit"
when_to_use: "當你已具備研究目標，並需要規劃招募、篩選或分群受訪者以產出「受訪者招募條件」時"
when_not_to_use: "當產品背景、研究目的或決策問題尚不清楚，無法定義「受訪者條件定義」時"
input_required:
  - "Research Goal"
  - "Product Context"
  - "Target User"
output:
  - "受訪者招募條件"
next_best_actions:
  - "RP-B-002｜招募問卷生成"
---

# RP-B-001 受訪者條件定義

**所屬階段：** 研究規劃與準備

**適用情境：** 使用者研究招募

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 根據以下研究目標，定義適合的受訪者條件。
 
 請分析：
 - 必要條件
 - 加分條件
 - 排除條件
 - 使用經驗
 - 行為特徵
 
 # 格式要求
 請使用表格格式輸出。
 
 # 情境
 [輸入產品 / 功能 / 研究背景]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**研究目標、產品背景**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Research Goal | ✅ 必填 | 了解移工在小額跨境匯兌流程中的操作行為、痛點與信任因素 |
| Product Context | ✅ 必填 | 手機小額跨境匯兌服務，服務在台移工匯款回母國 |
| Target User | ✅ 必填 | 在台工作的印尼、越南、菲律賓移工，曾有跨境匯款需求 |
| Usage Context | 選填 | 每月發薪後使用手機將部分薪資匯回母國家人 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 受訪者招募條件

- [ ] 是否能篩出符合研究目的的受訪者
- [ ] 是否避免條件過窄
- [ ] 是否涵蓋移工族群差異
- [ ] 是否有明確排除條件

---

## 完成後下一步

> ✅ 建議接續：**RP-B-002 招募問卷生成**


---

---
prompt_id: "RP-B-002"
task_name: "招募問卷生成"
stage: "研究規劃與準備"
task_type: "recruit"
when_to_use: "當你已具備研究目標，並需要規劃招募、篩選或分群受訪者以產出「招募問卷 / Screener」時"
when_not_to_use: "當產品背景、研究目的或決策問題尚不清楚，無法定義「招募問卷生成」時"
input_required:
  - "Research Purpose"
  - "Target Segment"
  - "Participant Criteria"
output:
  - "招募問卷 / Screener"
next_best_actions:
  - "RP-D-001｜訪談腳本撰寫"
---

# RP-B-002 招募問卷生成

**所屬階段：** 研究規劃與準備

**適用情境：** 訪談招募、易用性測試招募

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 根據以下研究需求，生成受訪者招募問卷。
 
 請包含：
 - 基本背景問題
 - 使用行為問題
 - 排除條件問題
 - 使用頻率問題
 - 分群問題
 
 # 格式要求
 請以問卷格式輸出。
 
 # 情境
 [輸入產品 / 功能 / 研究背景]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**研究目的、目標族群**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Research Purpose | ✅ 必填 | 了解移工在小額跨境匯兌流程中的資訊理解、信任與操作困難 |
| Target Segment | ✅ 必填 | 在台工作且過去 6 個月內有跨境匯款經驗的移工 |
| Participant Criteria | ✅ 必填 | 必要條件：有手機匯款或跨境匯款經驗；排除條件：完全沒有匯款經驗 |
| Exclusion Criteria | 選填 | 金融從業人員、公司內部員工、完全沒有匯款經驗者 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 招募問卷 / Screener

- [ ] 是否能有效篩選必要條件
- [ ] 是否避免誘導性問題
- [ ] 是否能排除不適合樣本
- [ ] 是否支援後續分群

---

## 完成後下一步

> ✅ 建議接續：**RP-D-001 訪談腳本撰寫**


---

---
prompt_id: "RP-B-003"
task_name: "受訪者分群"
stage: "研究規劃與準備"
task_type: "recruit"
when_to_use: "當你已具備研究目標，並需要規劃招募、篩選或分群受訪者以產出「分群架構」時"
when_not_to_use: "當產品背景、研究目的或決策問題尚不清楚，無法定義「受訪者分群」時"
input_required:
  - "使用者特徵"
  - "行為資料"
output:
  - "分群架構"
next_best_actions:
  - "檢查研究目標與輸入資料是否足夠｜決定下一個研究規劃或招募任務"
---

# RP-B-003 受訪者分群

**所屬階段：** 研究規劃與準備

**適用情境：** Persona 驗證、研究規劃

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 根據以下研究情境，提出適合的受訪者分群方式。
 
 請分析：
 - 行為差異
 - 使用頻率
 - 經驗程度
 - 動機差異
 - 高風險族群
 
 # 格式要求
 請以 segmentation table 格式輸出。
 
 # 情境
 [輸入產品 / 功能 / 研究背景]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**使用者特徵、行為資料**

**此 Prompt 產出：** 分群架構


---

---
prompt_id: "RP-B-004"
task_name: "招募條件驗證"
stage: "研究規劃與準備"
task_type: "recruit"
when_to_use: "當你已具備研究目標，並需要規劃招募、篩選或分群受訪者以產出「風險分析」時"
when_not_to_use: "當產品背景、研究目的或決策問題尚不清楚，無法定義「招募條件驗證」時"
input_required:
  - "招募條件"
  - "研究目標"
output:
  - "風險分析"
next_best_actions:
  - "檢查研究目標與輸入資料是否足夠｜決定下一個研究規劃或招募任務"
---

# RP-B-004 招募條件驗證

**所屬階段：** 研究規劃與準備

**適用情境：** 招募QA

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請檢查以下受訪者招募條件是否存在偏誤或樣本風險。
 
 請分析：
 - 樣本偏誤
 - 招募盲點
 - 族群覆蓋不足
 - 過度限制條件
 - 研究可信度風險
 
 # 格式要求
 請輸出：
 - 發現問題
 - 可能影響
 - 改善建議
 
 # 情境
 [輸入產品 / 功能 / 招募條件]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**招募條件、研究目標**

**此 Prompt 產出：** 風險分析


---

---
prompt_id: "RP-C-001"
task_name: "競品分析"
stage: "研究規劃與準備"
task_type: "explore"
when_to_use: "當你需要用競品、趨勢或 UX Pattern 輔助前期設計判斷，並產出「競品分析報告」時"
when_not_to_use: "當產品背景、研究目的或決策問題尚不清楚，無法定義「競品分析」時"
input_required:
  - "產品資訊"
  - "競品名單"
output:
  - "競品分析報告"
next_best_actions:
  - "檢查研究目標與輸入資料是否足夠｜決定下一個研究規劃或招募任務"
---

# RP-C-001 競品分析

**所屬階段：** 研究規劃與準備

**適用情境：** 新功能規劃、市場研究

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 根據以下產品情境，分析主要競品的 UX 策略與功能差異。
 
 請包含：
 - 核心功能
 - UX 優勢
 - UX 缺點
 - Onboarding 流程
 - 資訊架構
 - 使用流程特色
 
 # 格式要求
 請使用競品比較表輸出。
 
 # 情境
 [輸入產品 / 功能 / 市場]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**產品資訊、競品名單**

**此 Prompt 產出：** 競品分析報告


---

---
prompt_id: "RP-C-002"
task_name: "功能比較"
stage: "研究規劃與準備"
task_type: "explore"
when_to_use: "當你需要用競品、趨勢或 UX Pattern 輔助前期設計判斷，並產出「Feature Matrix」時"
when_not_to_use: "當產品背景、研究目的或決策問題尚不清楚，無法定義「功能比較」時"
input_required:
  - "功能清單"
  - "競品資訊"
output:
  - "Feature Matrix"
next_best_actions:
  - "檢查研究目標與輸入資料是否足夠｜決定下一個研究規劃或招募任務"
---

# RP-C-002 功能比較

**所屬階段：** 研究規劃與準備

**適用情境：** 功能策略分析

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 請比較以下競品功能差異。
 
 請分析：
 - 功能完整度
 - 操作流程
 - 使用門檻
 - 差異化特色
 - 缺漏功能
 
 # 格式要求
 請以 feature comparison table 輸出。
 
 # 情境
 [輸入產品 / 功能 / 競品]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**功能清單、競品資訊**

**此 Prompt 產出：** Feature Matrix


---

---
prompt_id: "RP-C-003"
task_name: "UX Pattern 研究"
stage: "研究規劃與準備"
task_type: "explore"
when_to_use: "當你需要用競品、趨勢或 UX Pattern 輔助前期設計判斷，並產出「UX Pattern 整理」時"
when_not_to_use: "當產品背景、研究目的或決策問題尚不清楚，無法定義「UX Pattern 研究」時"
input_required:
  - "產品類型"
  - "使用情境"
output:
  - "UX Pattern 整理"
next_best_actions:
  - "檢查研究目標與輸入資料是否足夠｜決定下一個研究規劃或招募任務"
---

# RP-C-003 UX Pattern 研究

**所屬階段：** 研究規劃與準備

**適用情境：** Interaction Design 研究

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 研究以下產品情境中常見的 UX Pattern。
 
 請分析：
 - 常見互動模式
 - 業界最佳實踐
 - 使用者預期
 - Pattern 優缺點
 - 適用情境
 
 # 格式要求
 請依照 Pattern 分類輸出。
 
 # 情境
 [輸入產品 / 功能 / 市場]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**產品類型、使用情境**

**此 Prompt 產出：** UX Pattern 整理


---

---
prompt_id: "RP-C-004"
task_name: "趨勢分析"
stage: "研究規劃與準備"
task_type: "explore"
when_to_use: "當你需要用競品、趨勢或 UX Pattern 輔助前期設計判斷，並產出「趨勢洞察」時"
when_not_to_use: "當產品背景、研究目的或決策問題尚不清楚，無法定義「趨勢分析」時"
input_required:
  - "市場資訊"
  - "產品方向"
output:
  - "趨勢洞察"
next_best_actions:
  - "檢查研究目標與輸入資料是否足夠｜決定下一個研究規劃或招募任務"
---

# RP-C-004 趨勢分析

**所屬階段：** 研究規劃與準備

**適用情境：** 新產品探索

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 分析以下產品領域目前的 UX 與產品趨勢。
 
 請包含：
 - 使用者行為變化
 - 新興功能模式
 - AI 應用方向
 - 市場變化
 - 使用者期待變化
 
 # 格式要求
 請區分：
 - Current Trend
 - Emerging Trend
 - Potential Risk
 
 # 情境
 [輸入產品 / 功能 / 市場]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**市場資訊、產品方向**

**此 Prompt 產出：** 趨勢洞察


---

---
prompt_id: "RP-D-001"
task_name: "訪談腳本撰寫"
stage: "研究規劃與準備"
task_type: "plan"
when_to_use: "當你需要把研究目標、研究問題或專案限制轉成可執行的研究計畫或訪談腳本時"
when_not_to_use: "當產品背景、研究目的或決策問題尚不清楚，無法定義「訪談腳本撰寫」時"
input_required:
  - "Research Goal"
  - "Product Scenario"
  - "Research Questions"
output:
  - "使用者訪談腳本"
next_best_actions:
  - "DC-A-001｜延伸追問生成"
  - "DC-A-002｜深入探詢問題建議"
  - "DC-A-003｜對話摘要整理"
---

# RP-D-001 訪談腳本撰寫

**所屬階段：** 研究規劃與準備

**適用情境：** 使用者訪談

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 根據以下研究目標，生成使用者訪談腳本。
 
 請包含：
 - 開場問題
 - 背景問題
 - 行為問題
 - 動機問題
 - 深入追問
 - 收尾問題
 
 # 格式要求
 請依照訪談流程排序。
 
 # 情境
 [輸入產品 / 功能 / 研究目標]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**研究目標、產品情境**

## 執行前請確認以下輸入欄位

| 欄位 | 是否必填 | 範例 |
|------|----------|------|
| Research Goal | ✅ 必填 | 找出移工在設定受款人、確認匯款資訊與理解交易狀態時的阻礙 |
| Product Scenario | ✅ 必填 | 使用手機完成一筆跨境匯兌，包含資料設定、受款人選擇、金額輸入、確認與交易狀態查詢 |
| Research Questions | ✅ 必填 | 使用者如何判斷匯款服務是否可信？哪些欄位最容易造成理解困難？ |
| Participant Background | 選填 | 在台工作 1 年以上、有定期匯款回母國經驗的移工 |

若使用者未提供必填欄位，請在貼出 Prompt 本文時，於 # 情境 區塊內以註解形式標註「此欄位必填，請補齊」，由使用者在 # 情境 內補齊後回傳。不要另外開一份問卷或表格要求使用者逐欄填答。

---

## 輸出品質標準

**產出物名稱：** 使用者訪談腳本

- [ ] 是否符合研究目標
- [ ] 是否避免誘導性問法
- [ ] 是否從容易回答的問題進入
- [ ] 是否包含流程、信任、理解、痛點與行為面向

---

## 完成後下一步

> ✅ 建議接續：**DC-A-001、DC-A-002、DC-A-003 DC-A-001、DC-A-002、DC-A-003**


---

---
prompt_id: "RP-D-004"
task_name: "研究時程規劃"
stage: "研究規劃與準備"
task_type: "plan"
when_to_use: "當你需要把研究目標、研究問題或專案限制轉成可執行的研究計畫或訪談腳本時"
when_not_to_use: "當產品背景、研究目的或決策問題尚不清楚，無法定義「研究時程規劃」時"
input_required:
  - "專案時程"
  - "研究範圍"
output:
  - "研究時程"
next_best_actions:
  - "檢查研究目標與輸入資料是否足夠｜決定下一個研究規劃或招募任務"
---

# RP-D-004 研究時程規劃

**所屬階段：** 研究規劃與準備

**適用情境：** 專案規劃

---

## Prompt 本文

```
# 角色
 你是一位資深 UX 研究員。
 
 # 任務
 根據以下研究需求，規劃 UX Research 時程。
 
 請包含：
 - 前期準備
 - 招募時間
 - 訪談執行
 - 資料分析
 - 報告整理
 - 利害關係人同步
 
 # 格式要求
 請以 timeline format 輸出。
 
 # 情境
 [輸入產品 / 功能 / 專案時程]
```

---

## 可接受的上游輸入

此 Prompt 接受以下素材作為輸入：**專案時程、研究範圍**

**此 Prompt 產出：** 研究時程


---
