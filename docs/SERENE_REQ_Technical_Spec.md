# SERENE-REQ Technical Specification & ISO Mapping
**Version:** 1.0 (Proprietary)
**Author:** Umer Tanveer (PhD Researcher)
**Framework:** Surgical Data Engineering (SDE)

## 1. Executive Summary
The SERENE-REQ dataset is a high-fidelity synthetic benchmark designed to bridge the "Green Gap" in Requirements Engineering. Unlike legacy datasets (e.g., PROMISE), SERENE-REQ introduces the **Energy (EN)** class as a fundamental 12th NFR, mapped to international sustainability standards.

## 2. Dataset Architecture
| Metric | Value |
| :--- | :--- |
| **Total Records** | 50,000 |
| **NFR Classes** | 12 (11 PROMISE + 1 Energy) |
| **Semantic Overlap** | **0.00%** (Verified via Jaccard Index) |
| **Class Distribution** | 100% Balanced (Surgically Equalized) |
| **Traceability** | Anchored to 300+ Industrial Software Scenarios |

## 3. ISO Standard Mapping (The 20 Standards)
The requirements in this dataset strictly follow the syntax and semantics of the following international standards:

### A. General Quality & RE
1.  **ISO/IEC/IEEE 29148**: Systems and software engineering — Life cycle processes — Requirements engineering.
2.  **ISO/IEC 25010**: Systems and software quality requirements and evaluation (SQuaRE).
3.  **ISO/IEC 25012**: Data quality model.

### B. Energy & Sustainability (The Green AI Core)
4.  **ISO 50001**: Energy management systems.
5.  **ISO/IEC 30134**: Information technology — Data centres — Key performance indicators (PUE/CUE/WUE).
6.  **ITU-T L.1470**: Greenhouse gas emissions trajectories for the ICT sector.
7.  **IEEE P2807**: Framework of Knowledge Graphs for Sustainable AI.

### C. Security, AI & Reliability
8.  **ISO/IEC 27001**: Information security management.
9.  **ISO/IEC 23053**: Framework for Artificial Intelligence (AI) Systems Using Machine Learning (ML).
10. **ISO/IEC 42001**: Information technology — Artificial intelligence — Management system.
11. **ISO/IEC 24029**: Assessment of the robustness of neural networks.
12. **ISO 22301**: Business continuity management systems (Reliability).

### D. Usability & Specialization
13. **ISO 9241**: Ergonomics of human-system interaction.
14. **ISO/IEC 40500**: Web Content Accessibility Guidelines (WCAG) 2.0.
15. **ISO/IEC 19770**: IT asset management.

## 4. Validation Protocol
Data integrity was verified using the **SERENE-SDE Audit Suite**:
1.  **Collision Filter**: MD5 Hash check to ensure zero duplicate strings.
2.  **Linguistic Fingerprinting**: Class-isolated vocabularies ensure 0% cross-contamination.
3.  **Project Solidarity**: Requirements are grouped into 300 distinct projects (e.g., Project-EN-01) to maintain architectural context.

---
**Confidentiality Notice:** This specification is part of the proprietary SERENE-REQ framework. Unauthorized distribution is prohibited.
