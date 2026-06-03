# BMA Accident Analysis | Dashboard Year 2566–2568

> **วิเคราะห์อุบัติเหตุบาดเจ็บสาหัสและเสียชีวิต กองบัญชาการตำรวจนครบาล (บช.น.)**  
> ปี 2566–2568 · Portfolio Project · Data Analytics for Public Sector

🔗 **Live Dashboard:** [bma-statistics-pw.github.io/BMA-Accident-Analysis](https://bma-statistics-pw.github.io/BMA-Accident-Analysis/)

---

## 📊 ภาพรวมโครงการ

Dashboard วิเคราะห์ข้อมูลอุบัติเหตุทางถนนในกรุงเทพมหานคร จากฐานข้อมูลของกองบัญชาการตำรวจนครบาล (บช.น.) ครอบคลุม **2,600 เหตุการณ์** และผู้ประสบเหตุ **5,615 ราย** ใน 3 ปี เพื่อสนับสนุนการตัดสินใจเชิงนโยบายในการแก้ไขปัญหาอุบัติเหตุจราจรทางถนน

| ปี | เหตุการณ์ | ผู้ประสบเหตุ | เสียชีวิต | อัตราเสียชีวิต |
|---|---|---|---|---|
| 2566 | 899 | 1,895 | 772 | 40.7% |
| 2567 | 933 | 2,018 | 812 | 40.2% |
| 2568 | 768 | 1,702 | 727 | 42.7% |
| **รวม** | **2,600** | **5,615** | **2,311** | **41.2%** |

---

## 🗂️ หน้าวิเคราะห์ใน Dashboard

| หน้า | เนื้อหา |
|---|---|
| 📊 สรุปภาพรวม | KPI 3 ปีรวม, เปรียบเทียบรายปี, ชนิดรถ, พฤติกรรม |
| 📈 แนวโน้มรายปี | เหตุการณ์/เสียชีวิตรายเดือน, แสงสว่าง, ลักษณะถนน |
| 🏍️ ยานพาหนะ | ชนิดรถ × สถานะ, รูปแบบอุบัติเหตุ, หมวก, เข็มขัด |
| ⚠️ พฤติกรรม & ปัจจัย | พฤติกรรม 8 ปัจจัย, แอลกอฮอล์, ประเภทถนน, อาชีพ |
| 👤 กลุ่มเสี่ยง | อายุ, เพศ, บทบาทบนท้องถนน |
| 🌏 สัญชาติ | ไทย vs ต่างชาติ, อัตราเสียชีวิต CLMV |
| 📍 พื้นที่ & ถนน | บก. Top 9, ประเภทถนน, อัตราเสียชีวิตตามลักษณะถนน |
| 📋 ข้อเสนอแนะ | 4 ลำดับความสำคัญ + ตารางแนวโน้มนโยบาย |
| 👤 ผู้วิเคราะห์ | Analyst profile, methodology, tech stack |

---

## 🔍 ข้อค้นพบสำคัญ

1. **รถจักรยานยนต์** พัวพัน 53.6% ของผู้ประสบเหตุ และมีผู้เสียชีวิตจาก จยย. กว่า 80% ทุกปี
2. **ไม่สวมหมวกนิรภัย** → อัตราเสียชีวิต 62.3% vs สวมหมวก 56.5%
3. **ขับเร็วเกินกำหนด** เป็นปัจจัยอันดับ 1 ทุกปี (2,154 ครั้ง รวม 3 ปี)
4. **แรงงาน CLMV** มีอัตราเสียชีวิตสูงกว่าคนไทย 10–20% (ลาว 60%, เมียนมา 52.9%)
5. **บก.2** มีเหตุการณ์และเสียชีวิตสูงสุดทุกปีอย่างต่อเนื่อง

---

## 🧠 Portfolio Positioning (Data Science + Graphic Design)

โปรเจกต์นี้ถูกออกแบบให้เป็น **Case Study สำหรับ Portfolio** โดยเน้น 3 องค์ประกอบหลัก

1. **Data Science Rigor**
- Data cleaning, integration, validation
- Cross-tabulation, trend analysis, risk profiling
- Metric ที่ตรวจสอบย้อนกลับได้และตีความเชิงนโยบายได้จริง

2. **Visual Communication**
- โครงหน้าแบบ Executive Dashboard (KPI → Trend → Insight → Action)
- Color hierarchy สำหรับแยกสถานะความเสี่ยง
- กราฟที่สื่อสารคำถามเดียวชัดเจน อ่านได้เร็ว

3. **Policy Relevance**
- แปลผลข้อมูลสู่ข้อเสนอแนะเชิงปฏิบัติ
- ระบุกลุ่มเสี่ยง พื้นที่เป้าหมาย และลำดับความสำคัญ
- รองรับการใช้งานทั้งผู้บริหารและนักวิเคราะห์

### Case Study Snapshot

| Dimension | Summary |
|---|---|
| Problem | อุบัติเหตุรุนแรงใน กทม. มีอัตราเสียชีวิตสูงต่อเนื่อง |
| Data | ข้อมูล บช.น. 3 ปี (2,600 เหตุการณ์ / 5,615 ผู้ประสบเหตุ) |
| Approach | Data pipeline + statistical analysis + dashboard storytelling |
| Outcome | ได้ dashboard ที่ใช้ตัดสินใจเชิงนโยบายและสื่อสารความเสี่ยงได้ชัดเจน |

---

## 🛠️ Tech Stack

```
Python 3  ·  pandas  ·  numpy  ·  openpyxl
HTML5  ·  CSS3  ·  JavaScript (ES6)  ·  Chart.js 4.4
Responsive Design (PC / Tablet / Mobile)
GitHub Pages
```

## 🎨 Design Standard

- Typography: ใช้ฟอนต์ Sarabun ทั้งระบบ เพื่อความสม่ำเสมอในการนำเสนอภาษาไทย
- Responsive: ออกแบบรองรับ 3 ขนาดหน้าจอหลัก
	- PC: > 1100px
	- Tablet: 768-1100px
	- Mobile: < 768px
- Dashboard พร้อมใช้งานบน GitHub Pages โดยคงความอ่านง่ายและลำดับข้อมูลแบบมืออาชีพทุกอุปกรณ์

---

## 📁 โครงสร้างไฟล์หลัก

```text
github/
├── index.html
├── data/
│   ├── data_2566.js
│   ├── data_2567.js
│   ├── data_2568.js
│   └── data_all.js
├── README.md
└── push_to_github.py
```

- `index.html` โหลดข้อมูลจากไฟล์ในโฟลเดอร์ `data/` และมีตัวเลือกปี (2566, 2567, 2568, รวมทุกปี)
- `data_all.js` ใช้สำหรับกราฟเปรียบเทียบข้ามปี
- `push_to_github.py` push ไฟล์ทั้งหมดในโฟลเดอร์นี้ขึ้น GitHub อัตโนมัติ

---

## 🚀 วิธี Push ขึ้น GitHub

1. ตั้งค่า GitHub token ใน environment (แนะนำ)

```powershell
$env:GITHUB_TOKEN="YOUR_GITHUB_PAT"
```

2. รันสคริปต์

```powershell
python push_to_github.py
```

3. สคริปต์จะ push ไฟล์ทั้งหมดในโฟลเดอร์ `github/` ไปยัง

```text
https://github.com/BMA-Statistics-PW/BMA-Accident-Analysis
```

หมายเหตุ: เวอร์ชันนี้ไม่มีการฝัง token ในไฟล์แล้ว เพื่อความปลอดภัย

---

## 👤 ผู้วิเคราะห์

**© Prapawadee W.**  
Professional-Level Statistician  
กลุ่มงานสถิติและวิจัย กองนโยบายและแผนงาน  
สำนักการจราจรและขนส่ง กรุงเทพมหานคร  
*Statistics & Research Group, Policy & Planning Division, Traffic and Transportation Department, BMA*

---

## 📁 ผลงานอื่นๆ

- 🚦 [BMA Congestion Analysis](https://bma-statistics-pw.github.io/BMA-Congestion-Problem/) — วิเคราะห์จุดปัญหาจราจรติดขัด 2566–2568

---

> ข้อมูลและการวิเคราะห์จัดทำขึ้นเพื่อประโยชน์สาธารณะ ไม่อนุญาตให้นำไปใช้แสวงหาผลประโยชน์ส่วนบุคคล  
> © 2026 Prapawadee W. · For BMA public-sector use
