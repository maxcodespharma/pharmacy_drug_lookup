# Drug Information Lookup Tool
# Portfolio Project #1
# Created October 25, 2025

# Drug database - storing mutliple drugs with their info
drug_database = {
    "metformin": {
        "class": "Biguanide",
        "use": "Type 2 Diabetes",
        "typical_dose": "500-1000mg twice daily with meals",
        "major_interactions": "Contrast dye (hold 48hr), alcohol",
        "contraindications": "Severe renal impairment (eGFR < 30)",
        "controlled": False,
        "brand_name": "Glucophage",
        "rank": 3
    },
    "lisinopril": {
        "class": "ACE Inhibitor",
        "use": "Hypertension, Heart Failure, Post-MI",
        "typical_dose": "10-40mg once daily",
        "major_interactions": "NSAIDS, potassium supplements, spironolactone",
        "contraindications": "Pregnancy, angioedema history",
        "controlled": False,
        "brand_name": "Prinivil, Zestril",
        "rank": 4
    },
    "atorvastatin": {
        "class": "HMG-CoA Reductase Inhibitor (Statin)",
        "use": "Hyperlipidemia, CVD prevention",
        "typical_dose": "10-80mg once daily in evening",
        "major_interactions": "Gemfibrozil, grapefruit juice, clarithromycin",
        "contraindications": "Active liver disease, pregnancy",
        "controlled": False,
        "brand_name": "Lipitor",
        "rank": 1
    },
    "levothyroxine": {
        "class": "Thyroid Hormone Replacement",
        "use": "Hypothyroidism", 
        "typical_dose": "25-200mcg once daily on empty stomach",
        "major_interactions": "Iron, calcium, PPIs (separate by 4 hours)",
        "contraindications": "Untreated adrenal insufficiency",
        "controlled": False,
        "brand_name": "Synthroid, Levoxyl",
        "rank": 2
    }, 
    "omeprazole": {
        "class": "Proton Pump Inhibitor",
        "use": "GERD, Peptic Ulcer Disease",
        "typical_dose": "20-40mg once daily before meals",
        "major_interactions": "Clopidogrel (reduced efficacy)",
        "contraindications": "Hypersensitivity to PPIs",
        "controlled": False,
        "brand_name": "Prilosec",
        "rank": 7
    },
    "hydrocodone": {
        "class": "Opioid Analgesic",
        "use": "Moderate to severe pain",
        "typical_dose": "5-10mg every 4-6 hours as needed",
        "major_interactions": "Benzodiazepines, alcohol, other CNS depressants",
        "contraindications": "Respiratory depression, acute asthma",
        "controlled": True,
        "brand_name": "Vicodin, Norco",
        "rank": None
    },
    "albuterol": {
        "class": "Beta-2 Agonist",
        "use": "Asthma, COPD",
        "typical_dose": "2 puffs every 4-6 hours as needed",
        "major_interactions": "Beta blockers (reduced efficacy)",
        "contraindications": "Hypersensitivity",
        "controlled": False,
        "brand_name": "ProAir, Ventolin",
        "rank": 9
    },
    "gabapentin": {
        "class": "Anticonvulsant",
        "use": "Neuropathic pain, seizures",
        "typical_dose": "300-600mg three times daily",
        "major_interactions": "Antacids (reduced absorption)",
        "contraindications": "Severe renal impairment",
        "controlled": False,
        "brand_name": "Neurontin",
        "rank": 10
    },
    "amlodipine": {
        "class": "Calcium Channel Blocker",
        "use": "Hypertension, Angina",
        "typical_dose": "5-10mg once daily",
        "major_interactions": "Simvastatin (increased statin levels)",
        "contraindications": "Severe aortic stenosis",
        "controlled": False,
        "brand_name": "Norvasc",
        "rank": 5
    },
    "sertraline": {
        "class": "SSRI Antidepressant",
        "use": "Depression, Anxiety, OCD",
        "typical_dose": "50-200mg once daily",
        "major_interactions": "MAOIs (serotonin syndrome), NSAIDs (bleeding risk)",
        "contraindications": "MAOI use within 14 days",
        "controlled": False,
        "brand_name": "Zoloft",
        "rank": None
    },
    "prednisone": {
        "class": "Corticosteroid",
        "use": "Inflammation, Autoimmune conditions",
        "typical_dose": "5-60mg daily (varies by indication)",
        "major_interactions": "NSAIDs (GI bleeding risk), live vaccines",
        "contraindications": "Systemic fungal infections",
        "controlled": False,
        "brand_name": "Deltasone",
        "rank": None
    },
    "warfarin": {
        "class": "Anticoagulant",
        "use": "DVT/PE prevention, Atrial fibrillation",
        "typical_dose": "2-10mg daily (INR-guided)",
        "major_interactions": "NSAIDs, antibiotics, vitamin K-rich foods",
        "contraindications": "Active bleeding, pregnancy",
        "controlled": False,
        "brand_name": "Coumadin",
        "rank": None
    },
    "alprazolam": {
        "class": "Benzodiazepine",
        "use": "Anxiety disorders, Panic disorder",
        "typical_dose": "0.25-0.5mg three times daily",
        "major_interactions": "Opioids (respiratory depression), alcohol",
        "contraindications": "Acute narrow-angle glaucoma",
        "controlled": True,
        "brand_name": "Xanax",
        "rank": None
    },
    "montelukast": {
        "class": "Leukotriene Receptor Antagonist",
        "use": "Asthma, Allergic rhinitis",
        "typical_dose": "10mg once daily in evening",
        "major_interactions": "Phenobarbital (reduced efficacy)",
        "contraindications": "Hypersensitivity",
        "controlled": False,
        "brand_name": "Singulair",
        "rank": None
    },
    "losartan": {
        "class": "ARB (Angiotensin Receptor Blocker)",
        "use": "Hypertension, Diabetic nephropathy",
        "typical_dose": "25-100mg once or twice daily",
        "major_interactions": "Potassium supplements, NSAIDs",
        "contraindications": "Pregnancy",
        "controlled": False,
        "brand_name": "Cozaar",
        "rank": 8
    },
    "furosemide": {
        "class": "Loop Diuretic",
        "use": "Edema, Heart failure, Hypertension",
        "typical_dose": "20-80mg once or twice daily",
        "major_interactions": "Aminoglycosides (ototoxicity), lithium",
        "contraindications": "Anuria, severe electrolyte depletion",
        "controlled": False,
        "brand_name": "Lasix",
        "rank": None
    },
    "insulin_glargine": {
        "class": "Long-acting Insulin",
        "use": "Type 1 and Type 2 Diabetes",
        "typical_dose": "10-40 units subcutaneously once daily",
        "major_interactions": "Beta blockers (mask hypoglycemia symptoms)",
        "contraindications": "Hypoglycemia",
        "controlled": False,
        "brand_name": "Lantus",
        "rank": None
    },
    "tramadol": {
        "class": "Opioid Analgesic",
        "use": "Moderate to moderately severe pain",
        "typical_dose": "50-100mg every 4-6 hours as needed",
        "major_interactions": "SSRIs (serotonin syndrome), MAOIs",
        "contraindications": "Seizure disorder, acute intoxication",
        "controlled": True,
        "brand_name": "Ultram",
        "rank": None
    },
    "clopidogrel": {
        "class": "Antiplatelet Agent",
        "use": "Post-MI, Stroke prevention, PAD",
        "typical_dose": "75mg once daily",
        "major_interactions": "PPIs (reduced efficacy), NSAIDs (bleeding risk)",
        "contraindications": "Active pathological bleeding",
        "controlled": False,
        "brand_name": "Plavix",
        "rank": None
    },
    "escitalopram": {
        "class": "SSRI Antidepressant",
        "use": "Depression, Generalized anxiety disorder",
        "typical_dose": "10-20mg once daily",
        "major_interactions": "MAOIs (serotonin syndrome), NSAIDs",
        "contraindications": "MAOI use within 14 days, hypersensitivity",
        "controlled": False,
        "brand_name": "Lexapro",
        "rank": None
    }, 
    "aspirin": {
        "class": "Antiplatelet/NSAID",
        "use": "Pain, Fever, Cardiovascular protection",
        "typical_dose": "81-325mg once daily (cardioprotection), 325-650mg every 4-6hrs (pain)",
        "major_interactions": "Warfarin (bleeding risk), NSAIDs",
        "contraindications": "Active bleeding, children with viral illness (Reye's syndrome)",
        "controlled": False,
        "brand_name": "Bayer, Ecotrin",
        "rank": None
    },
    "ibuprofen": {
        "class": "NSAID",
        "use": "Pain, Fever, Inflammation",
        "typical_dose": "200-800mg every 6-8 hours",
        "major_interactions": "Warfarin (bleeding), ACE inhibitors (reduced efficacy)",
        "contraindications": "Active GI bleeding, severe heart failure",
        "controlled": False,
        "brand_name": "Advil, Motrin",
        "rank": None
    },
    "acetaminophen": {
        "class": "Analgesic/Antipyretic",
        "use": "Pain, Fever",
        "typical_dose": "325-1000mg every 4-6 hours (max 4g/day)",
        "major_interactions": "Warfarin (may enhance effect), chronic alcohol use",
        "contraindications": "Severe hepatic impairment",
        "controlled": False,
        "brand_name": "Tylenol",
        "rank": None
    },
    "amoxicillin": {
        "class": "Penicillin Antibiotic",
        "use": "Bacterial infections (respiratory, ear, urinary)",
        "typical_dose": "250-500mg three times daily or 500-875mg twice daily",
        "major_interactions": "Methotrexate (increased toxicity), oral contraceptives",
        "contraindications": "Penicillin allergy",
        "controlled": False,
        "brand_name": "Amoxil",
        "rank": None
    },
    "azithromycin": {
        "class": "Macrolide Antibiotic",
        "use": "Bacterial infections (respiratory, skin)",
        "typical_dose": "500mg day 1, then 250mg daily for 4 days",
        "major_interactions": "Warfarin, digoxin (increased levels)",
        "contraindications": "History of cholestatic jaundice with azithromycin",
        "controlled": False,
        "brand_name": "Zithromax, Z-Pak",
        "rank": None
    },
    "ciprofloxacin": {
        "class": "Fluoroquinolone Antibiotic",
        "use": "Bacterial infections (UTI, respiratory, GI)",
        "typical_dose": "250-750mg twice daily",
        "major_interactions": "Theophylline, warfarin, antacids (reduced absorption)",
        "contraindications": "Tendon disorders, myasthenia gravis",
        "controlled": False,
        "brand_name": "Cipro",
        "rank": None
    },
    "doxycycline": {
        "class": "Tetracycline Antibiotic",
        "use": "Bacterial infections, Acne, Malaria prophylaxis",
        "typical_dose": "100mg twice daily",
        "major_interactions": "Antacids, iron (reduced absorption), warfarin",
        "contraindications": "Pregnancy, children under 8",
        "controlled": False,
        "brand_name": "Vibramycin",
        "rank": None
    },
    "ranitidine": {
        "class": "H2 Receptor Antagonist",
        "use": "GERD, Peptic ulcer (NOTE: Recalled in 2020 due to NDMA)",
        "typical_dose": "150mg twice daily",
        "major_interactions": "Ketoconazole (reduced absorption)",
        "contraindications": "Hypersensitivity (HISTORICAL - no longer available)",
        "controlled": False,
        "brand_name": "Zantac (discontinued)",
        "rank": None
    },
    "pantoprazole": {
        "class": "Proton Pump Inhibitor",
        "use": "GERD, Erosive esophagitis",
        "typical_dose": "40mg once daily",
        "major_interactions": "Clopidogrel (may reduce efficacy), methotrexate",
        "contraindications": "Hypersensitivity to PPIs",
        "controlled": False,
        "brand_name": "Protonix",
        "rank": None
    },
    "metoprolol": {
        "class": "Beta Blocker",
        "use": "Hypertension, Angina, Heart failure, Post-MI",
        "typical_dose": "25-100mg twice daily (tartrate) or 25-200mg once daily (succinate)",
        "major_interactions": "Verapamil/diltiazem (bradycardia), insulin (masks hypoglycemia)",
        "contraindications": "Severe bradycardia, cardiogenic shock",
        "controlled": False,
        "brand_name": "Lopressor, Toprol-XL",
        "rank": 6
    },
    "carvedilol": {
        "class": "Alpha/Beta Blocker",
        "use": "Heart failure, Hypertension, Post-MI",
        "typical_dose": "3.125-25mg twice daily",
        "major_interactions": "Digoxin (increased levels), rifampin (reduced efficacy)",
        "contraindications": "Severe bradycardia, decompensated heart failure",
        "controlled": False,
        "brand_name": "Coreg",
        "rank": None
    },
    "hydrochlorothiazide": {
        "class": "Thiazide Diuretic",
        "use": "Hypertension, Edema",
        "typical_dose": "12.5-50mg once daily",
        "major_interactions": "Lithium (increased toxicity), NSAIDs (reduced efficacy)",
        "contraindications": "Anuria, sulfonamide allergy",
        "controlled": False,
        "brand_name": "Microzide",
        "rank": None
    },
    "spironolactone": {
        "class": "Potassium-Sparing Diuretic",
        "use": "Heart failure, Hypertension, Edema, Hyperaldosteronism",
        "typical_dose": "25-100mg once or twice daily",
        "major_interactions": "ACE inhibitors/ARBs (hyperkalemia), lithium",
        "contraindications": "Hyperkalemia, severe renal impairment",
        "controlled": False,
        "brand_name": "Aldactone",
        "rank": None
    },
    "digoxin": {
        "class": "Cardiac Glycoside",
        "use": "Heart failure, Atrial fibrillation",
        "typical_dose": "0.125-0.25mg once daily",
        "major_interactions": "Amiodarone (increased levels), loop diuretics (hypokalemia increases toxicity)",
        "contraindications": "Ventricular fibrillation",
        "controlled": False,
        "brand_name": "Lanoxin",
        "rank": None
    },
    "diltiazem": {
        "class": "Calcium Channel Blocker",
        "use": "Hypertension, Angina, Atrial fibrillation",
        "typical_dose": "120-360mg once daily (extended-release)",
        "major_interactions": "Beta blockers (bradycardia), simvastatin (increased statin levels)",
        "contraindications": "Sick sinus syndrome, severe hypotension",
        "controlled": False,
        "brand_name": "Cardizem, Tiazac",
        "rank": None
    },
    "nitroglycerin": {
        "class": "Nitrate Vasodilator",
        "use": "Angina",
        "typical_dose": "0.3-0.6mg sublingual as needed (max 3 doses in 15 min)",
        "major_interactions": "PDE5 inhibitors (severe hypotension), alcohol",
        "contraindications": "Recent PDE5 inhibitor use, severe hypotension",
        "controlled": False,
        "brand_name": "Nitrostat",
        "rank": None
    },
    "sildenafil": {
        "class": "PDE5 Inhibitor",
        "use": "Erectile dysfunction, Pulmonary hypertension",
        "typical_dose": "25-100mg one hour before activity (ED), 20mg three times daily (PAH)",
        "major_interactions": "Nitrates (severe hypotension), alpha blockers",
        "contraindications": "Nitrate use, severe cardiovascular disease",
        "controlled": False,
        "brand_name": "Viagra, Revatio",
        "rank": None
    },
    "tamsulosin": {
        "class": "Alpha-1 Blocker",
        "use": "Benign prostatic hyperplasia (BPH)",
        "typical_dose": "0.4mg once daily",
        "major_interactions": "Other alpha blockers (hypotension), PDE5 inhibitors",
        "contraindications": "Hypersensitivity",
        "controlled": False,
        "brand_name": "Flomax",
        "rank": None
    },
    "finasteride": {
        "class": "5-Alpha Reductase Inhibitor",
        "use": "Benign prostatic hyperplasia, Male pattern baldness",
        "typical_dose": "5mg once daily (BPH), 1mg once daily (hair loss)",
        "major_interactions": "None significant",
        "contraindications": "Pregnancy (teratogenic), hypersensitivity",
        "controlled": False,
        "brand_name": "Proscar, Propecia",
        "rank": None
    },
    "allopurinol": {
        "class": "Xanthine Oxidase Inhibitor",
        "use": "Gout, Hyperuricemia",
        "typical_dose": "100-300mg once daily",
        "major_interactions": "Azathioprine/mercaptopurine (increased toxicity), warfarin",
        "contraindications": "Hypersensitivity",
        "controlled": False,
        "brand_name": "Zyloprim",
        "rank": None
    },
    "colchicine": {
        "class": "Anti-Inflammatory (Gout)",
        "use": "Gout flares, Familial Mediterranean fever",
        "typical_dose": "0.6mg once or twice daily (prophylaxis), 1.2mg then 0.6mg 1hr later (acute)",
        "major_interactions": "Statins (myopathy), clarithromycin (toxicity)",
        "contraindications": "Severe renal/hepatic impairment with P-gp/CYP3A4 inhibitors",
        "controlled": False,
        "brand_name": "Colcrys",
        "rank": None
    },
    "methylprednisolone": {
        "class": "Corticosteroid",
        "use": "Inflammation, Autoimmune conditions, Allergic reactions",
        "typical_dose": "4-48mg daily (varies by indication)",
        "major_interactions": "NSAIDs (GI bleeding), live vaccines, warfarin",
        "contraindications": "Systemic fungal infections",
        "controlled": False,
        "brand_name": "Medrol",
        "rank": None
    },
    "cyclobenzaprine": {
        "class": "Muscle Relaxant",
        "use": "Muscle spasms",
        "typical_dose": "5-10mg three times daily",
        "major_interactions": "MAOIs (contraindicated), CNS depressants, tramadol (serotonin syndrome)",
        "contraindications": "Recent MI, arrhythmias, MAOI use",
        "controlled": False,
        "brand_name": "Flexeril",
        "rank": None
    },
    "tizanidine": {
        "class": "Alpha-2 Agonist Muscle Relaxant",
        "use": "Muscle spasticity",
        "typical_dose": "2-4mg every 6-8 hours as needed",
        "major_interactions": "Fluvoxamine/ciprofloxacin (contraindicated), CNS depressants",
        "contraindications": "Hepatic impairment, concurrent fluvoxamine/ciprofloxacin",
        "controlled": False,
        "brand_name": "Zanaflex",
        "rank": None
    },
    "meloxicam": {
        "class": "NSAID",
        "use": "Osteoarthritis, Rheumatoid arthritis",
        "typical_dose": "7.5-15mg once daily",
        "major_interactions": "Warfarin (bleeding), ACE inhibitors (reduced efficacy)",
        "contraindications": "CABG surgery, active GI bleeding",
        "controlled": False,
        "brand_name": "Mobic",
        "rank": None
    },
    "celecoxib": {
        "class": "COX-2 Selective NSAID",
        "use": "Osteoarthritis, Rheumatoid arthritis, Pain",
        "typical_dose": "100-200mg once or twice daily",
        "major_interactions": "Warfarin (bleeding), fluconazole (increased levels)",
        "contraindications": "Sulfonamide allergy, CABG surgery",
        "controlled": False,
        "brand_name": "Celebrex",
        "rank": None
    },
    "ondansetron": {
        "class": "5-HT3 Antagonist Antiemetic",
        "use": "Nausea/vomiting (chemotherapy, post-op)",
        "typical_dose": "4-8mg every 8 hours as needed",
        "major_interactions": "Apomorphine (contraindicated), QT-prolonging drugs",
        "contraindications": "Congenital long QT syndrome, apomorphine use",
        "controlled": False,
        "brand_name": "Zofran",
        "rank": None
    },
    "promethazine": {
        "class": "Antihistamine/Antiemetic",
        "use": "Nausea/vomiting, Allergic reactions, Motion sickness",
        "typical_dose": "12.5-25mg every 4-6 hours",
        "major_interactions": "CNS depressants, MAOIs",
        "contraindications": "Children under 2 (respiratory depression), comatose states",
        "controlled": False,
        "brand_name": "Phenergan",
        "rank": None
    },
    "diphenhydramine": {
        "class": "Antihistamine",
        "use": "Allergies, Insomnia, Motion sickness",
        "typical_dose": "25-50mg every 4-6 hours",
        "major_interactions": "CNS depressants, MAOIs, anticholinergics",
        "contraindications": "Acute asthma, narrow-angle glaucoma, nursing infants",
        "controlled": False,
        "brand_name": "Benadryl",
        "rank": None
    },
    "fexofenadine": {
        "class": "Non-Sedating Antihistamine",
        "use": "Allergic rhinitis, Chronic urticaria",
        "typical_dose": "60mg twice daily or 180mg once daily",
        "major_interactions": "Fruit juices (reduced absorption), antacids",
        "contraindications": "Hypersensitivity",
        "controlled": False,
        "brand_name": "Allegra",
        "rank": None
    }, "buspirone": {
        "class": "Anxiolytic (Non-Benzodiazepine)",
        "use": "Generalized anxiety disorder",
        "typical_dose": "15-30mg twice daily",
        "major_interactions": "MAOIs (serotonin syndrome), grapefruit juice",
        "contraindications": "MAOI use",
        "controlled": False,
        "brand_name": "BuSpar",
        "rank": None
    },
    "mirtazapine": {
        "class": "Atypical Antidepressant",
        "use": "Depression, Insomnia",
        "typical_dose": "15-45mg once daily at bedtime",
        "major_interactions": "MAOIs (serotonin syndrome), CNS depressants",
        "contraindications": "MAOI use within 14 days",
        "controlled": False,
        "brand_name": "Remeron",
        "rank": None
    },
    "venlafaxine": {
        "class": "SNRI Antidepressant",
        "use": "Depression, Anxiety disorders",
        "typical_dose": "75-225mg once daily",
        "major_interactions": "MAOIs (serotonin syndrome), NSAIDs (bleeding risk)",
        "contraindications": "MAOI use within 14 days",
        "controlled": False,
        "brand_name": "Effexor",
        "rank": None
    },
    "clonazepam": {
        "class": "Benzodiazepine",
        "use": "Panic disorder, Seizures",
        "typical_dose": "0.25-2mg twice daily",
        "major_interactions": "Opioids (respiratory depression), CNS depressants",
        "contraindications": "Acute narrow-angle glaucoma",
        "controlled": True,
        "brand_name": "Klonopin",
        "rank": None
    },
    "bupropion": {
        "class": "Atypical Antidepressant/Smoking Cessation",
        "use": "Depression, Smoking cessation",
        "typical_dose": "150-450mg daily (divided or XL formulation)",
        "major_interactions": "MAOIs (hypertensive crisis), seizure risk drugs",
        "contraindications": "Seizure disorder, eating disorders, MAOI use",
        "controlled": False,
        "brand_name": "Wellbutrin, Zyban",
        "rank": None
    },
    "methylphenidate": {
        "class": "CNS Stimulant",
        "use": "ADHD, Narcolepsy",
        "typical_dose": "10-60mg daily in divided doses",
        "major_interactions": "MAOIs (hypertensive crisis), antihypertensives",
        "contraindications": "Anxiety, glaucoma, MAOI use",
        "controlled": True,
        "brand_name": "Ritalin, Concerta",
        "rank": None
    },
    "amphetamine-dextroamphetamine": {
        "class": "CNS Stimulant",
        "use": "ADHD, Narcolepsy",
        "typical_dose": "5-40mg daily in divided doses",
        "major_interactions": "MAOIs (hypertensive crisis), antihypertensives",
        "contraindications": "Cardiovascular disease, hyperthyroidism, MAOI use",
        "controlled": True,
        "brand_name": "Adderall",
        "rank": None
    },
    "quetiapine": {
        "class": "Atypical Antipsychotic",
        "use": "Schizophrenia, Bipolar disorder, Depression adjunct",
        "typical_dose": "150-800mg daily (varies by indication)",
        "major_interactions": "CNS depressants, CYP3A4 inhibitors (increased levels)",
        "contraindications": "Hypersensitivity",
        "controlled": False,
        "brand_name": "Seroquel",
        "rank": None
    },
    "aripiprazole": {
        "class": "Atypical Antipsychotic",
        "use": "Schizophrenia, Bipolar disorder, Depression adjunct",
        "typical_dose": "10-30mg once daily",
        "major_interactions": "CYP3A4/2D6 inhibitors (adjust dose)",
        "contraindications": "Hypersensitivity",
        "controlled": False,
        "brand_name": "Abilify",
        "rank": None
    },
    "lamotrigine": {
        "class": "Anticonvulsant/Mood Stabilizer",
        "use": "Bipolar disorder, Seizures",
        "typical_dose": "100-400mg daily (requires slow titration)",
        "major_interactions": "Valproic acid (increases lamotrigine levels), oral contraceptives",
        "contraindications": "Hypersensitivity",
        "controlled": False,
        "brand_name": "Lamictal",
        "rank": None
    },
    "rosuvastatin": {
        "class": "HMG-CoA Reductase Inhibitor (Statin)",
        "use": "Hyperlipidemia, CVD prevention",
        "typical_dose": "5-40mg once daily",
        "major_interactions": "Gemfibrozil, cyclosporine, certain antivirals",
        "contraindications": "Active liver disease, pregnancy",
        "controlled": False,
        "brand_name": "Crestor",
        "rank": None
    },
    "simvastatin": {
        "class": "HMG-CoA Reductase Inhibitor (Statin)",
        "use": "Hyperlipidemia, CVD prevention",
        "typical_dose": "10-40mg once daily in evening",
        "major_interactions": "Amiodarone, amlodipine, diltiazem, grapefruit juice",
        "contraindications": "Active liver disease, pregnancy",
        "controlled": False,
        "brand_name": "Zocor",
        "rank": None
    },
    "pravastatin": {
        "class": "HMG-CoA Reductase Inhibitor (Statin)",
        "use": "Hyperlipidemia, CVD prevention",
        "typical_dose": "10-80mg once daily",
        "major_interactions": "Cyclosporine, gemfibrozil",
        "contraindications": "Active liver disease, pregnancy",
        "controlled": False,
        "brand_name": "Pravachol",
        "rank": None
    },
    "ezetimibe": {
        "class": "Cholesterol Absorption Inhibitor",
        "use": "Hyperlipidemia (often combined with statin)",
        "typical_dose": "10mg once daily",
        "major_interactions": "Fibrates (increased risk of gallstones), cyclosporine",
        "contraindications": "Active liver disease when used with statin",
        "controlled": False,
        "brand_name": "Zetia",
        "rank": None
    },
    "fenofibrate": {
        "class": "Fibric Acid Derivative",
        "use": "Hypertriglyceridemia, Mixed dyslipidemia",
        "typical_dose": "48-145mg once daily",
        "major_interactions": "Statins (myopathy risk), warfarin",
        "contraindications": "Severe renal/hepatic impairment, gallbladder disease",
        "controlled": False,
        "brand_name": "Tricor, Trilipix",
        "rank": None
    },
    "niacin": {
        "class": "B Vitamin/Lipid-Lowering Agent",
        "use": "Hyperlipidemia, Low HDL",
        "typical_dose": "500-2000mg daily (extended-release)",
        "major_interactions": "Statins (myopathy), antihypertensives (hypotension)",
        "contraindications": "Active liver disease, active peptic ulcer",
        "controlled": False,
        "brand_name": "Niaspan",
        "rank": None
    },
    "enalapril": {
        "class": "ACE Inhibitor",
        "use": "Hypertension, Heart failure",
        "typical_dose": "5-40mg daily in 1-2 divided doses",
        "major_interactions": "NSAIDs, potassium supplements, lithium",
        "contraindications": "Pregnancy, angioedema history",
        "controlled": False,
        "brand_name": "Vasotec",
        "rank": None
    },
    "ramipril": {
        "class": "ACE Inhibitor",
        "use": "Hypertension, Heart failure, Post-MI",
        "typical_dose": "2.5-20mg once daily",
        "major_interactions": "NSAIDs, potassium supplements, lithium",
        "contraindications": "Pregnancy, angioedema history",
        "controlled": False,
        "brand_name": "Altace",
        "rank": None
    },
    "benazepril": {
        "class": "ACE Inhibitor",
        "use": "Hypertension",
        "typical_dose": "10-40mg once daily or in divided doses",
        "major_interactions": "NSAIDs, potassium supplements, lithium",
        "contraindications": "Pregnancy, angioedema history",
        "controlled": False,
        "brand_name": "Lotensin",
        "rank": None
    },
    "valsartan": {
        "class": "ARB (Angiotensin Receptor Blocker)",
        "use": "Hypertension, Heart failure, Post-MI",
        "typical_dose": "80-320mg once daily",
        "major_interactions": "NSAIDs, potassium supplements, lithium",
        "contraindications": "Pregnancy",
        "controlled": False,
        "brand_name": "Diovan",
        "rank": None
    },
    "olmesartan": {
        "class": "ARB (Angiotensin Receptor Blocker)",
        "use": "Hypertension",
        "typical_dose": "20-40mg once daily",
        "major_interactions": "NSAIDs, potassium supplements",
        "contraindications": "Pregnancy",
        "controlled": False,
        "brand_name": "Benicar",
        "rank": None
    },
    "irbesartan": {
        "class": "ARB (Angiotensin Receptor Blocker)",
        "use": "Hypertension, Diabetic nephropathy",
        "typical_dose": "150-300mg once daily",
        "major_interactions": "NSAIDs, potassium supplements",
        "contraindications": "Pregnancy",
        "controlled": False,
        "brand_name": "Avapro",
        "rank": None
    },
    "telmisartan": {
        "class": "ARB (Angiotensin Receptor Blocker)",
        "use": "Hypertension",
        "typical_dose": "20-80mg once daily",
        "major_interactions": "NSAIDs, potassium supplements, digoxin",
        "contraindications": "Pregnancy, biliary obstruction",
        "controlled": False,
        "brand_name": "Micardis",
        "rank": None
    },
    "atenolol": {
        "class": "Selective Beta-1 Blocker",
        "use": "Hypertension, Angina, Post-MI",
        "typical_dose": "25-100mg once daily",
        "major_interactions": "Calcium channel blockers, insulin, clonidine",
        "contraindications": "Severe bradycardia, heart block, cardiogenic shock",
        "controlled": False,
        "brand_name": "Tenormin",
        "rank": None
    },
    "bisoprolol": {
        "class": "Selective Beta-1 Blocker",
        "use": "Hypertension, Heart failure",
        "typical_dose": "2.5-10mg once daily",
        "major_interactions": "Calcium channel blockers, rifampin",
        "contraindications": "Severe bradycardia, cardiogenic shock",
        "controlled": False,
        "brand_name": "Zebeta",
        "rank": None
    },
    "nebivolol": {
        "class": "Selective Beta-1 Blocker with Vasodilatory Properties",
        "use": "Hypertension",
        "typical_dose": "5-40mg once daily",
        "major_interactions": "CYP2D6 inhibitors, calcium channel blockers",
        "contraindications": "Severe bradycardia, heart block, severe hepatic impairment",
        "controlled": False,
        "brand_name": "Bystolic",
        "rank": None
    },
    "labetalol": {
        "class": "Alpha/Beta Blocker",
        "use": "Hypertension (including pregnancy), Hypertensive emergency",
        "typical_dose": "100-400mg twice daily",
        "major_interactions": "Calcium channel blockers, nitroglycerin",
        "contraindications": "Asthma, severe bradycardia, heart block",
        "controlled": False,
        "brand_name": "Trandate",
        "rank": None
    },
    "clonidine": {
        "class": "Central Alpha-2 Agonist",
        "use": "Hypertension, ADHD, Opioid withdrawal",
        "typical_dose": "0.1-0.3mg twice daily (hypertension)",
        "major_interactions": "Beta blockers, tricyclic antidepressants",
        "contraindications": "Hypersensitivity, abrupt discontinuation risk",
        "controlled": False,
        "brand_name": "Catapres",
        "rank": None
    },
    "nifedipine": {
        "class": "Dihydropyridine Calcium Channel Blocker",
        "use": "Hypertension, Angina",
        "typical_dose": "30-90mg once daily (extended-release)",
        "major_interactions": "CYP3A4 inhibitors, grapefruit juice",
        "contraindications": "Cardiogenic shock, immediate-release for hypertensive emergencies",
        "controlled": False,
        "brand_name": "Procardia, Adalat",
        "rank": None
    },
    "isosorbide_mononitrate": {
        "class": "Nitrate Vasodilator",
        "use": "Angina prevention",
        "typical_dose": "30-120mg once daily (extended-release)",
        "major_interactions": "PDE5 inhibitors (severe hypotension), alcohol",
        "contraindications": "Recent PDE5 inhibitor use, severe hypotension",
        "controlled": False,
        "brand_name": "Imdur",
        "rank": None
    },
    "clopidogrel": {
        "class": "Antiplatelet (P2Y12 Inhibitor)",
        "use": "ACS, Recent MI/stroke, Peripheral arterial disease",
        "typical_dose": "75mg once daily",
        "major_interactions": "PPIs (especially omeprazole), NSAIDs",
        "contraindications": "Active pathological bleeding",
        "controlled": False,
        "brand_name": "Plavix",
        "rank": None
    },
    "ticagrelor": {
        "class": "Antiplatelet (P2Y12 Inhibitor)",
        "use": "ACS, Post-MI",
        "typical_dose": "90mg twice daily",
        "major_interactions": "Strong CYP3A4 inhibitors/inducers, aspirin >100mg",
        "contraindications": "Active bleeding, history of intracranial hemorrhage",
        "controlled": False,
        "brand_name": "Brilinta",
        "rank": None
    },
    "dabigatran": {
        "class": "Direct Thrombin Inhibitor",
        "use": "DVT/PE treatment, Afib stroke prevention",
        "typical_dose": "150mg twice daily",
        "major_interactions": "P-gp inhibitors/inducers",
        "contraindications": "Active pathological bleeding, mechanical heart valve",
        "controlled": False,
        "brand_name": "Pradaxa",
        "rank": None
    },
    "edoxaban": {
        "class": "Direct Factor Xa Inhibitor",
        "use": "DVT/PE treatment, Afib stroke prevention",
        "typical_dose": "60mg once daily",
        "major_interactions": "P-gp inhibitors/inducers",
        "contraindications": "Active pathological bleeding",
        "controlled": False,
        "brand_name": "Savaysa",
        "rank": None
    },
    "torsemide": {
        "class": "Loop Diuretic",
        "use": "Edema, Heart failure, Hypertension",
        "typical_dose": "5-20mg once daily",
        "major_interactions": "Aminoglycosides (ototoxicity), lithium, NSAIDs",
        "contraindications": "Anuria, severe electrolyte depletion",
        "controlled": False,
        "brand_name": "Demadex",
        "rank": None
    },
    "bumetanide": {
        "class": "Loop Diuretic",
        "use": "Edema, Heart failure",
        "typical_dose": "0.5-2mg once or twice daily",
        "major_interactions": "Aminoglycosides (ototoxicity), lithium, NSAIDs",
        "contraindications": "Anuria, severe electrolyte depletion",
        "controlled": False,
        "brand_name": "Bumex",
        "rank": None
    },
    "chlorthalidone": {
        "class": "Thiazide-like Diuretic",
        "use": "Hypertension, Edema",
        "typical_dose": "12.5-25mg once daily",
        "major_interactions": "Lithium (increased toxicity), NSAIDs",
        "contraindications": "Anuria, sulfonamide allergy",
        "controlled": False,
        "brand_name": "Thalitone",
        "rank": None
    },
    "triamterene_hctz": {
        "class": "Potassium-Sparing/Thiazide Diuretic Combination",
        "use": "Hypertension, Edema",
        "typical_dose": "37.5mg/25mg to 75mg/50mg once or twice daily",
        "major_interactions": "ACE inhibitors/ARBs (hyperkalemia), lithium",
        "contraindications": "Hyperkalemia, severe renal impairment",
        "controlled": False,
        "brand_name": "Dyazide, Maxzide",
        "rank": None
    },
    "eplerenone": {
        "class": "Aldosterone Antagonist",
        "use": "Heart failure post-MI, Hypertension",
        "typical_dose": "25-50mg once daily",
        "major_interactions": "ACE inhibitors/ARBs (hyperkalemia), strong CYP3A4 inhibitors",
        "contraindications": "Hyperkalemia, severe renal impairment, strong CYP3A4 inhibitors",
        "controlled": False,
        "brand_name": "Inspra",
        "rank": None
    },
    "amiodarone": {
        "class": "Class III Antiarrhythmic",
        "use": "Atrial fibrillation, Ventricular arrhythmias",
        "typical_dose": "400-600mg daily for loading, then 200-400mg daily maintenance",
        "major_interactions": "Warfarin, digoxin, statins, many drugs (extensive list)",
        "contraindications": "Severe sinus node dysfunction, cardiogenic shock",
        "controlled": False,
        "brand_name": "Cordarone, Pacerone",
        "rank": None
    },
    "sotalol": {
        "class": "Class III Antiarrhythmic (Beta-Blocker Properties)",
        "use": "Atrial fibrillation, Ventricular arrhythmias",
        "typical_dose": "80-160mg twice daily",
        "major_interactions": "QT-prolonging drugs, calcium channel blockers",
        "contraindications": "Bronchial asthma, sinus bradycardia, prolonged QT",
        "controlled": False,
        "brand_name": "Betapace",
        "rank": None
    },
    "flecainide": {
        "class": "Class IC Antiarrhythmic",
        "use": "Atrial fibrillation, PSVT",
        "typical_dose": "50-150mg twice daily",
        "major_interactions": "Amiodarone, CYP2D6 inhibitors",
        "contraindications": "Structural heart disease, heart block",
        "controlled": False,
        "brand_name": "Tambocor",
        "rank": None
    },
    "sacubitril_valsartan": {
        "class": "Angiotensin Receptor-Neprilysin Inhibitor (ARNI)",
        "use": "Heart failure with reduced ejection fraction",
        "typical_dose": "49mg/51mg to 97mg/103mg twice daily",
        "major_interactions": "ACE inhibitors (contraindicated within 36 hours), potassium supplements",
        "contraindications": "History of angioedema, concurrent ACE inhibitor use",
        "controlled": False,
        "brand_name": "Entresto",
        "rank": None
    },
    "ivabradine": {
        "class": "HCN Channel Blocker",
        "use": "Heart failure, Inappropriate sinus tachycardia",
        "typical_dose": "5-7.5mg twice daily",
        "major_interactions": "CYP3A4 inhibitors, heart rate-lowering drugs",
        "contraindications": "Acute decompensated heart failure, severe hepatic impairment, resting HR <70",
        "controlled": False,
        "brand_name": "Corlanor",
        "rank": None
    },
    "dapagliflozin": {
        "class": "SGLT2 Inhibitor",
        "use": "Type 2 Diabetes, Heart failure, CKD",
        "typical_dose": "5-10mg once daily",
        "major_interactions": "Diuretics (volume depletion), insulin (hypoglycemia)",
        "contraindications": "Severe renal impairment (eGFR <25), dialysis",
        "controlled": False,
        "brand_name": "Farxiga",
        "rank": None
    },
    "empagliflozin": {
        "class": "SGLT2 Inhibitor",
        "use": "Type 2 Diabetes, Heart failure, CKD",
        "typical_dose": "10-25mg once daily",
        "major_interactions": "Diuretics (volume depletion), insulin (hypoglycemia)",
        "contraindications": "Severe renal impairment, dialysis",
        "controlled": False,
        "brand_name": "Jardiance",
        "rank": None
    },
    "canagliflozin": {
        "class": "SGLT2 Inhibitor",
        "use": "Type 2 Diabetes, CKD",
        "typical_dose": "100-300mg once daily before first meal",
        "major_interactions": "UGT inducers (rifampin), diuretics",
        "contraindications": "Severe renal impairment, dialysis",
        "controlled": False,
        "brand_name": "Invokana",
        "rank": None
    },
    "glipizide": {
        "class": "Sulfonylurea",
        "use": "Type 2 Diabetes",
        "typical_dose": "5-20mg once or twice daily",
        "major_interactions": "Beta blockers (mask hypoglycemia), sulfonamides",
        "contraindications": "Type 1 diabetes, diabetic ketoacidosis, sulfa allergy",
        "controlled": False,
        "brand_name": "Glucotrol",
        "rank": None
    },
    "glyburide": {
        "class": "Sulfonylurea",
        "use": "Type 2 Diabetes",
        "typical_dose": "1.25-20mg once or twice daily",
        "major_interactions": "Beta blockers (mask hypoglycemia), sulfonamides",
        "contraindications": "Type 1 diabetes, diabetic ketoacidosis, sulfa allergy",
        "controlled": False,
        "brand_name": "DiaBeta, Micronase",
        "rank": None
    },
    "glimepiride": {
        "class": "Sulfonylurea",
        "use": "Type 2 Diabetes",
        "typical_dose": "1-8mg once daily",
        "major_interactions": "Beta blockers (mask hypoglycemia), sulfonamides",
        "contraindications": "Type 1 diabetes, diabetic ketoacidosis, sulfa allergy",
        "controlled": False,
        "brand_name": "Amaryl",
        "rank": None
    }
}

# Get user input
def display_drug_info(drug_name, drug_data):
    """Display formatted drug information"""
    print("\n" + "=" * 60)
    print(f"DRUG: {drug_name.upper()}")
    print(f"Brand Name(s): {drug_data['brand_name']}")
    print("=" * 60)
    print(f"Class: {drug_data['class']}")
    print(f"Primary Use: {drug_data['use']}")
    print(f"Typical Dosing: {drug_data['typical_dose']}")
    print(f"Major Interactions: {drug_data['major_interactions']}")
    print(f"Contraindications: {drug_data['contraindications']}")

    if drug_data['controlled']:
        print("\n⚠️ CONTROLLED SUBSTANCE")
        print("   → Verify prescription validity")
        print("   → Check patient ID")
        print("   → Log in controlled substance registry")

    print("=" * 60)

def search_drugs(search_term):
    """Search for drugs by partial name match"""
    if not search_term or search_term.strip() == "":
            print("\n❌ Error: Search term cannot be empty")
            return

    search_term = search_term.lower() # Convert to lowercase for case-insensitive search
    results = [] # Empty list to store matches

    for drug_name in drug_database: # Loop through all drug names in your dictionary
        if search_term in drug_name.lower(): # Check if search term is in drug name
            results.append(drug_name) # Add matching drug to results list

    if results: # If we found matches
        print(f"\nFound {len(results)} match(es):")
        for drug in results:
            print(f"- {drug}")
    else: 
        print(f"\nNo drugs found matching '{search_term}'")


def search_drugs_by_class(drug_class):
    """Find all drugs in a specific class"""
    results = []
    for name, data in drug_database.items():
        if drug_class.lower() in data['class'].lower():
            results.append(name)
    return results

def search_drugs_by_condition(condition):
    """Find all drugs used for a specific medical condition"""
    results = []
    for name, data in drug_database.items():
        # Check if condition appears in the "use" field
        if condition.lower() in data['use'].lower():
            results.append(name)
    return results

def get_top_prescribed():
    """Get top 10 most commonly prescribed drugs"""
    ranked_drugs = []
    for name, data in drug_database.items():
        if data.get('rank') is not None: #Has a rank
            ranked_drugs.append((name, data))
    
    # Sort by rank (lowest number = highest rank)
    ranked_drugs.sort(key=lambda x: x[1]['rank'])
    return ranked_drugs

def get_database_stats():
    """Generate statistics about the drug database"""
    total_drugs = len(drug_database)

    # Count controlled substances
    controlled_count = sum(1 for drug in drug_database.values() if drug['controlled'])

    # Count drugs by class
    class_counts = {}
    for drug_data in drug_database.values():
        drug_class = drug_data['class']
        class_counts[drug_class] = class_counts.get(drug_class, 0) + 1 

    # Find most common class
    most_common_class = max(class_counts, key=class_counts.get)
    most_common_count = class_counts[most_common_class]

    # Get top ranked drug
    top_drug = None
    top_brand = None
    for name, data in drug_database.items():
        if data.get('rank') == 1:
            top_drug = name
            top_brand = data['brand_name']
            break

    return {
        'total': total_drugs,
        'controlled': controlled_count,
        'top_class': most_common_class,
        'top_class_count': most_common_count,
        'top_drug': top_drug,
        'top_brand': top_brand
    }


def calculate_total_cost(quantity, price_per_unit):
    """Calculate total cost of a prescription"""
    total = quantity * price_per_unit
    print(f"Total cost: ${total:.2f}")
    return total

def compare_drugs(drug1_name, drug2_name):
    """Display two drugs side-by-side for comparision"""
    drug1 = drug_database.get(drug1_name)
    drug2 = drug_database.get(drug2_name)

    if not drug1:
        return None, f"'{drug1_name}' not found in database"
    if not drug2:
        return None, f"'{drug2_name}' not found in database"
    
    # Display comparison
    print("\n" + "=" * 80)
    print( "DRUG COMPARISON".center(80))
    print("=" * 80)

    # Drug names and brands
    print(f"\n{'Drug 1:':20} {drug1_name.upper():30} {'DRUG 2:':10} {drug2_name.upper()}")
    print(f" {'Brand Name:':20} {drug1['brand_name']:30} {'':10} {drug2['brand_name']}")
    print("-" * 80)

    # Class
    print(f"{'Class:':20} {drug1['class']:30} {'':10} {drug2['class']}")
    print()

    # Primary Use
    print(f"{'Primary Use:':20}")
    print(f"   • {drug1['use']:28}   • {drug2['use']}")
    print()

    # Typical Dosing
    print(f"{'Typical Dosing:':20}")
    print(f"   • {drug1['typical_dose']}")
    print(f"   • {drug2['typical_dose']}")
    print()

    # Major Interactions
    print(f"{'Major Interactions:':20}")
    print(f"   • {drug1['major_interactions']}")
    print(f"   • {drug2['major_interactions']}")
    print()

    # Contraindications
    print(f"{'Contraindications':20}")
    print(f"   • {drug1['contraindications']}")
    print(f"   • {drug2['contraindications']}")
    print()

    # Controlled status
    drug1_status =  "⚠️  CONTROLLED" if drug1['controlled'] else "Not controlled"
    drug2_status =  "⚠️  CONTROLLED" if drug2['controlled'] else "Not controlled"
    print(f"{'Status:':20} {drug1_status:30} {'':10} {drug2_status}")

    print("=" * 80)

    return True, None


# Get statistics
stats = get_database_stats()

# Display header with stats
# Main program loop

print("=" * 60)
print("         DRUG INFORMATION LOOKUP TOOL v1.0")
print("=" * 60)
print()
print("📊 DATABASE STATISTICS:")
print(f"   • Total Drugs: {stats['total']}")
print(f"   • Controlled Substances: {stats['controlled']}")
print(f"   • Most Common Class: {stats['top_class']} ({stats['top_class_count']} drugs)")
print(f"   • Coverage: Cardiac, Diabetes, Pain, Mental Health, +more")
print()
if stats['top_drug']:
    print(f"⭐ #1 Most Prescribed: {stats['top_drug'].capitalize()} ({stats['top_brand']})")
    print(f"📚 Quick Stats: {stats['total']} drugs available")
    print()
print("=" * 60)
print("\nOptions:")
print("1. Look up specific drug")
print("2. Search by drug class")
print("3. List all drugs in database")
print("4. View controlled substances only")
print("5. Search by medical condition")
print("6. View Top 10 most prescribed drugs")
print("7. Compare two drugs side-by-side")
print("8. Search by partial name")
print("9. Calculate total cost")

choice = input("\nEnter choice (1-9): ")

if choice == "1":
    drug_name = input("Enter drug name: ").lower().strip()
    if drug_name in drug_database:
        display_drug_info(drug_name, drug_database[drug_name])
    else: 
        print(f"\n❌ '{drug_name} not found in database.")
        print("Available drugs:", ", ".join(drug_database.keys()))

elif choice == "2":
    drug_class = input("Enter drug class to search: ")
    results = search_drugs_by_class(drug_class)
    if results: 
        print(f"\nDrugs in class containing '{drug_class}'")
        for drug in results:
            print(f"   - {drug}")
    else: 
        print(f"\n❌ No drugs found in class '{drug_class}")

elif choice == "3":
    print("\nAll drugs in database:")
    for drug_name in sorted(drug_database.keys()):
        drug_class = drug_database[drug_name]['class']
        print(f"   - {drug_name.capitalize()} ({drug_class})")

elif choice == "4":
    print("\n⚠️ CONTROLLED SUBSTANCES IN DATABASE:")
    print("=" * 60)

    controlled_drugs = []
    for name, data in drug_database.items():
        if data['controlled']:
            controlled_drugs.append(name)
    
    if controlled_drugs:
        for drug in sorted(controlled_drugs):
            drug_class = drug_database[drug]['class']
            brand = drug_database[drug]['brand_name']
            print(f"   - {drug.capitalize()} ({brand})")
            print(f"     Class: {drug_class}")
            print()
    else:
        print("   No controlled substances in database")
    
    print("=" * 60)

elif choice == "5":
    condition = input("Enter medical condition to search: ")
    results = search_drugs_by_condition(condition)

    if results:
        print(f"\nDrugs used for conditions containing '{condition}':")
        print("=" * 60)
        for drug in sorted(results):
            drug_class = drug_database[drug]['class']
            use = drug_database[drug]['use']
            print(f"    - {drug.capitalize()}")
            print(f"       Class: {drug_class}")
            print(f"       Indications: {use}")
            print()
    else: 
        print(f"\n❌ No drugs found for condition '{condition}'")

    print("=" * 60)

elif choice == "6":
    top_drugs = get_top_prescribed()

    print("\n⭐ TOP 10 MOST COMMONLY PRESCRIBED DRUGS IN US:")
    print("=" * 60)

    for drug_name, drug_data in top_drugs:
        rank = drug_data['rank']
        drug_class = drug_data['class']
        brand = drug_data['brand_name']
        use = drug_data['use']

        print(f"#{rank}. {drug_name.capitalize()} ({brand})")
        print(f"    Class: {drug_class}")
        print(f"    Primary Use: {use}")
        print()

    print("=" * 60)

elif choice == "7":
    print("\n--- DRUG COMPARISON ---")
    drug1 = input("Enter first drug name: ").lower().strip()
    drug2 = input("Enter second drug name: ").lower().strip()

    success, error = compare_drugs(drug1, drug2)

    if not success:
        print(f"\n❌ Error: {error}")
        print("Available drugs:", ", ".join(sorted(drug_database.keys())[:10]), "...")

elif choice == "8":
    search_term = input("Enter partial drug name to search: ")
    search_drugs(search_term)

elif choice  == "9":
    quantity = int(input("Enter quantity: "))
    price_per_unit = float(input("Enter price/unit"))
    calculate_total_cost(quantity, price_per_unit)

else: 
    print("\n❌ Invalid choice")

print("\n" + "=" * 60)
print("Lookup complete. GL KING/QUEEN!")
print("=" * 60)

...
