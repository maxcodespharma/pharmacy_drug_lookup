# Pharmacy Drug Information Lookup Tool
**Version:** 1.0.0  
**Last Updated:** October 2025
A comprehensive drug reference tool with 100 medications (targeting top 300), built for pharmacy students to quickly lookup drug information, compare medications, and study for exams. Expanding toward 300-drug coverage.

## Features
**Search and Analysis Options**
1. **Lookup specific drug** - Search by name for complete drug profile
2. **Search by drug class** - Find all drugs in a therapeutic category
3. **List all drugs** - View complete database alphabetically
4. **Filter controlled substances** - Show only scheduled medications
5. **Search by medical condition** - Find drugs treating specific conditions
6. **Top 10 most prescribed** - View highest-volume medications
7. **Side-by-side comparison** - Compare two drugs across all fields
**Current Database:**
- 100 drugs across major therapeutic classes (33% toward top 300 goal)
- Cardiac, diabetes, pain management, mental health medications
- 6 controlled substances with safety warnings
- Brand names and generic information
I plan to continuously add features throughout pharm school, allowing for more in-depth search options

## Why This Tool?

Built to solve common pharmacy student challenges:
- **Quick reference** without juggling multiple resources
- **Active learning** through comparison and exploration  
- **Exam prep** focused on top prescribed medications
- **Growing resource** that expands with my education

Useful for:
- Pre-pharmacy and pharmacy students
- Practicing pharmacists needing quick lookups
- Anyone learning pharmacology

## Technical Information
**Language:** Python 3.13
**Data Structure**: Nested dictionaries with key-value pairs for drug storage
**Core Functions:**
- `display_drug_info()` - Displays formatted drug information (class, dosing, interactions, contraindications, controlled status, brand names)
- `search_drugs_by_class()` - Filters database by therapeutic class
- `search_drugs_by_condition()` - Searches by medical indication
- `get_top_prescribed()` - Returns ranked list of most prescribed drugs
- `get_database_stats()` - Generates database statistics (total drugs, controlled substances, class distribution)
- `compare_drugs()` - Side-by-side comparison of two medications

## How to Use

**Requirements:**
- Python 3.10 or higher

**Run the program:**
```bash
python drug_lookup_tool.py
```

**Navigation:**
- Select from menu options (1-7)
- Follow prompts for search criteria
- Type drug names or conditions as requested
- Results display automatically

**Example workflow:**
1. Run program → See database statistics
2. Choose option 7 (Compare drugs)
3. Enter first drug: "metformin"
4. Enter second drug: "insulin"
5. View side-by-side comparison

## Sample Output
**Database Dashboard**
============================================================
         DRUG INFORMATION LOOKUP TOOL v1.0
============================================================

📊 DATABASE STATISTICS:
   • Total Drugs: 60
   • Controlled Substances: 6
   • Most Common Class: Proton Pump Inhibitor (2 drugs)
   • Coverage: Cardiac, Diabetes, Pain, Mental Health, +more

⭐ #1 Most Prescribed: Atorvastatin (Lipitor)
📚 Quick Stats: 60 drugs available

============================================================

Options:
1. Look up specific drug
2. Search by drug class
3. List all drugs in database
4. View controlled substances only
5. Search by medical condition
6. View Top 10 most prescribed drugs
7. Compare two drugs side-by-side
'''

**Single Drug Lookup**
Enter choice (1-7): 1
Enter drug name: metformin

============================================================
DRUG: METFORMIN
Brand Name(s): Glucophage
============================================================
Class: Biguanide
Primary Use: Type 2 Diabetes
Typical Dosing: 500-1000mg twice daily with meals
Major Interactions: Contrast dye (hold 48hr), alcohol
Contraindications: Severe renal impairment (eGFR < 30)
============================================================

============================================================
Lookup complete. GL KING/QUEEN!

**Drug Comparison**

Enter choice (1-7): 7

--- DRUG COMPARISON ---
Enter first drug name: methylprednisolone
Enter second drug name: fexofenadine

================================================================================
                                DRUG COMPARISON                               

================================================================================

Drug 1:              METHYLPREDNISOLONE             DRUG 2:    FEXOFENADINE   
 Brand Name:          Medrol                                    Allegra       
--------------------------------------------------------------------------------
Class:               Corticosteroid                            Non-Sedating Antihistamine

Primary Use:
   • Inflammation, Autoimmune conditions, Allergic reactions   • Allergic rhinitis, Chronic urticaria

Typical Dosing:
   • 4-48mg daily (varies by indication)
   • 60mg twice daily or 180mg once daily

Major Interactions:
   • NSAIDs (GI bleeding), live vaccines, warfarin
   • Fruit juices (reduced absorption), antacids

Contraindications
   • Systemic fungal infections
   • Hypersensitivity

Status:              Not controlled                            Not controlled 
================================================================================

============================================================
Lookup complete. GL KING/QUEEN!
============================================================


## Roadmap

**Near-term (Next 3 months):**
- Expand to 100+ drugs covering core pharmacy curriculum
- Add search loop (multiple searches without restarting)
- Improve typo tolerance in drug name searches

**Mid-term (6 months):**
- Reach 200+ drug coverage
- Add biochemical pathway information
- Enhanced drug interaction checking
- Drug shortage alerts

**Long-term (2026+):**
- Full 300-drug database aligned with pharmacy school curriculum
- FDA API integration for real-time data
- Mobile-friendly interface
- Advanced filtering options

## Tech + Learning Focus
Learning focus: This project was my very first introduction into using Python code. My goal was to get more comfortable with basic introductory techniques like file handling, data structure, and user interface logic. The idea was to connect my self-taught programming education with real-world pharmacy applications that will be useful as I pursue my PharmD education. 

## Progress Toward Top 300

**Current Coverage:** 100/300 drugs (33%)

**Last Updated:** November 2, 2025

**Drug Classes Covered:**
- Cardiovascular (ACE inhibitors, ARBs, Beta blockers, Calcium channel blockers, Diuretics, Antiarrhythmics, Anticoagulants, Antiplatelets)
- Diabetes (Metformin, Sulfonylureas, SGLT2 inhibitors, Insulin)
- Statins & Lipid-Lowering Agents
- Mental Health (SSRIs, SNRIs, Atypical antidepressants, Benzodiazepines, Antipsychotics)
- Pain Management (NSAIDs, Opioids, Muscle relaxants)
- Antibiotics (Penicillins, Macrolides, Fluoroquinolones, Tetracyclines)
- GI (PPIs, H2 blockers, Antiemetics)
- Respiratory (Beta-2 agonists, Leukotriene antagonists)
- And more...


## About

**Developer:** Max S. - Pre-PharmD Student  
**Start Date:** October 2025  
**Education:** Beginning PharmD program June 2026  
**Purpose:** Learning portfolio demonstrating AI + Pharmacy integration
**Disclaimer**: Self-taught; Built with guidance from AI assisted learning tools. My very first coding + pharmacy hybrid tool.

**GitHub:** github.com/maxcodespharma