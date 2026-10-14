import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

# ── Image Paths ────────────────────────────────────────────────────────────────
CURRENT_DIR = "/Users/BlankUser/Desktop/A4 presentation"

MLFLOW_IMG    = os.path.join(CURRENT_DIR, "mflow.png")
STREAMLIT_IMG = os.path.join(CURRENT_DIR, "streamlit.png")
GRAFANA_IMG   = os.path.join(CURRENT_DIR, "grafana.png")
DRIFT_COMP_IMG = os.path.join(CURRENT_DIR, "model_comparison_drift_impact.png")
VERIFY_IMG     = os.path.join(CURRENT_DIR, "model_performance_verification.png")

# ── Palette ───────────────────────────────────────────────────────────────────
NAVY       = RGBColor(0x1E, 0x3A, 0x8A)
BLUE       = RGBColor(0x2B, 0x5C, 0x8F)
LIGHT_BLUE = RGBColor(0xDB, 0xEA, 0xFE)
ACCENT     = RGBColor(0xF5, 0x9E, 0x0B)
GREEN      = RGBColor(0x10, 0xB9, 0x81)
GREEN_DARK = RGBColor(0x06, 0x5F, 0x46)
RED        = RGBColor(0xC9, 0x4A, 0x29)
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
DARK_GRAY  = RGBColor(0x1F, 0x29, 0x37)
LIGHT_GRAY = RGBColor(0xF1, 0xF5, 0xF9)
PURPLE     = RGBColor(0x7C, 0x3A, 0xED)
ORANGE     = RGBColor(0xE6, 0x6C, 0x00)
TEAL       = RGBColor(0x0D, 0x94, 0x88)
CODE_BG    = RGBColor(0x0D, 0x11, 0x17)
CODE_GRN   = RGBColor(0x3F, 0xB9, 0x50)

# Section branding colours
A1_COL  = RGBColor(0x1D, 0x4E, 0xD8)
A1_DARK = RGBColor(0x1E, 0x3A, 0x8A)
A2_COL  = RGBColor(0x05, 0x96, 0x69)
A2_DARK = RGBColor(0x06, 0x5F, 0x46)
A3_COL  = RGBColor(0x92, 0x40, 0x0E)
A3_DARK = RGBColor(0x78, 0x35, 0x00)

SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)
TOTAL   = 18

prs = Presentation()
prs.slide_width  = SLIDE_W
prs.slide_height = SLIDE_H
blank = prs.slide_layouts[6]

# ── Helper Functions ──────────────────────────────────────────────────────────
def rect(slide, l, t, w, h, fill=None, line=None, lw=None):
    s = slide.shapes.add_shape(1, l, t, w, h)
    if fill:
        s.fill.solid(); s.fill.fore_color.rgb = fill
    else:
        s.fill.background()
    if line:
        s.line.color.rgb = line
        if lw: s.line.width = lw
    else:
        s.line.fill.background()
    return s

def tb(slide, text, l, t, w, h, size=14, bold=False, italic=False,
       color=DARK_GRAY, align=PP_ALIGN.LEFT, wrap=True, link=None):
    box = slide.shapes.add_textbox(l, t, w, h)
    tf  = box.text_frame
    tf.word_wrap = wrap
    p   = tf.paragraphs[0]
    p.alignment = align
    r   = p.add_run()
    r.text = text
    r.font.size  = Pt(size)
    r.font.bold  = bold
    r.font.italic = italic
    r.font.color.rgb = color
    if link:
        r.hyperlink.address = link
    return box

def bullets(slide, lines, l, t, w, h, size=13, color=DARK_GRAY):
    box = slide.shapes.add_textbox(l, t, w, h)
    tf  = box.text_frame
    tf.word_wrap = True
    first = True
    for lvl, txt in lines:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.level = lvl
        p.alignment = PP_ALIGN.LEFT
        r = p.add_run()
        r.text = ("• " if lvl == 0 else "   – ") + txt
        r.font.size = Pt(size - lvl * 1.5)
        r.font.color.rgb = color
        p.space_after = Pt(3)

def sidebar(slide, sec_color=NAVY):
    rect(slide, 0, 0, Inches(0.35), SLIDE_H, fill=sec_color)

def header(slide, title, subtitle="", sec_color=NAVY):
    rect(slide, Inches(0.35), 0, SLIDE_W - Inches(0.35), Inches(1.4), fill=sec_color)
    tb(slide, title, Inches(0.6), Inches(0.12), Inches(12.5), Inches(0.85),
       size=32, bold=True, color=WHITE)
    if subtitle:
        tb(slide, subtitle, Inches(0.6), Inches(0.92), Inches(12.5), Inches(0.45),
           size=14, italic=True, color=RGBColor(0xBF, 0xDB, 0xFF))

def footer(slide, num, sec_label="", sec_color=NAVY):
    rect(slide, 0, SLIDE_H - Inches(0.38), SLIDE_W, Inches(0.38), fill=sec_color)
    label = f"{sec_label}  ·  " if sec_label else ""
    tb(slide, f"{label}420-976-VA  ·  Rahime Nacak  ·  Vanier College  ·  Fall 2026",
       Inches(0.5), SLIDE_H - Inches(0.36), Inches(10), Inches(0.34),
       size=10, color=RGBColor(0xBF, 0xDB, 0xFF))
    tb(slide, f"{num} / {TOTAL}",
       Inches(12.3), SLIDE_H - Inches(0.36), Inches(0.9), Inches(0.34),
       size=10, color=WHITE, align=PP_ALIGN.RIGHT)

def accent_line(slide, color=ACCENT):
    rect(slide, Inches(0.45), Inches(1.42), SLIDE_W - Inches(0.55), Inches(0.04), fill=color)

def section_tag(slide, label, color):
    rect(slide, SLIDE_W - Inches(1.55), Inches(0.12), Inches(1.1), Inches(0.38), fill=color)
    tb(slide, label, SLIDE_W - Inches(1.54), Inches(0.14), Inches(1.08), Inches(0.34),
       size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

def mini_win(slide, l, t, w, h, title, col=BLUE):
    rect(slide, l, t, w, h, fill=LIGHT_GRAY,
         line=RGBColor(0xCB, 0xD5, 0xE1), lw=Pt(0.5))
    rect(slide, l, t, w, Inches(0.38), fill=col)
    for dx, dc in [(0.12, RGBColor(0xFF,0x5F,0x57)),
                   (0.26, RGBColor(0xFF,0xBD,0x2E)),
                   (0.40, RGBColor(0x28,0xCA,0x41))]:
        rect(slide, l+Inches(dx), t+Inches(0.1), Inches(0.11), Inches(0.11), fill=dc)
    tb(slide, title, l+Inches(0.55), t+Inches(0.06), w-Inches(0.6), Inches(0.28),
       size=10, bold=True, color=WHITE)

def metric_box(slide, l, t, w, h, value, label, col=NAVY):
    rect(slide, l, t, w, h, fill=col)
    tb(slide, value, l, t+Inches(0.08), w, Inches(0.65),
       size=30, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    tb(slide, label, l, t+Inches(0.68), w, Inches(0.45),
       size=11, color=WHITE, align=PP_ALIGN.CENTER)

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 1 — TITLE / COVER
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=NAVY)
rect(s, SLIDE_W-Inches(3.2), 0, Inches(3.2), SLIDE_H, fill=RGBColor(0x16,0x2B,0x6B))
rect(s, 0, Inches(3.9), SLIDE_W, Inches(0.07), fill=ACCENT)

tb(s, "VANIER COLLEGE  ·  420-976-VA  ·  FALL 2026",
   Inches(0.7), Inches(1.1), Inches(10), Inches(0.5),
   size=13, bold=True, color=ACCENT)
tb(s, "AG News Topic Classification",
   Inches(0.7), Inches(1.7), Inches(12), Inches(0.9),
   size=40, bold=True, color=WHITE)
tb(s, "End-to-End MLOps Pipeline  ·  Final Project Presentation",
   Inches(0.7), Inches(2.65), Inches(12), Inches(0.6),
   size=22, color=RGBColor(0xBF,0xDB,0xFF))
tb(s, "Model Training  ·  API Deployment  ·  Versioning & Monitoring",
   Inches(0.7), Inches(3.28), Inches(12), Inches(0.45),
   size=14, italic=True, color=RGBColor(0x93,0xC5,0xFD))

for i, (lbl, col) in enumerate([("Model Training", A1_COL), ("API Deployment", A2_COL), ("MLOps Monitoring", A3_COL)]):
    bx = Inches(0.7) + i * Inches(3.0)
    rect(s, bx, Inches(4.15), Inches(2.6), Inches(0.5), fill=col)
    tb(s, lbl, bx, Inches(4.18), Inches(2.6), Inches(0.44),
       size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

tb(s, "Rahime Nacak", Inches(0.7), Inches(4.95), Inches(6), Inches(0.55),
   size=22, bold=True, color=WHITE)
tb(s, "LEA.EU — Artificial Intelligence & Data Science",
   Inches(0.7), Inches(5.52), Inches(8), Inches(0.4),
   size=14, color=RGBColor(0xBF,0xDB,0xFF))
tb(s, "October 2026", Inches(0.7), Inches(5.96), Inches(4), Inches(0.38),
   size=13, italic=True, color=RGBColor(0x93,0xC5,0xFD))

footer(s, 1)

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 2 — A1 SECTION DIVIDER
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=A1_DARK)
rect(s, SLIDE_W-Inches(4.5), 0, Inches(4.5), SLIDE_H, fill=A1_COL)
rect(s, 0, Inches(3.5), SLIDE_W, Inches(0.08), fill=ACCENT)
rect(s, 0, Inches(3.62), SLIDE_W, Inches(0.03), fill=RGBColor(0x93,0xC5,0xFD))

tb(s, "Part 1", Inches(0.8), Inches(0.9), Inches(5), Inches(1.2),
   size=80, bold=True, color=WHITE)
tb(s, "Model Training", Inches(0.8), Inches(2.3), Inches(7), Inches(0.85),
   size=40, bold=True, color=WHITE)
tb(s, "Dataset Exploration, Text Preprocessing, and Baseline Evaluation",
   Inches(0.8), Inches(3.25), Inches(8.5), Inches(0.45),
   size=16, italic=True, color=RGBColor(0xBF,0xDB,0xFF))


for i, t in enumerate([
    "Dataset Overview — AG News 4-class topic benchmark, two versioned corpora",
    "Preprocessing Pipeline — TF-IDF vectorization and feature configuration",
    "Model Training & Results — Classification metrics, drift impact, retraining",
    "Model Performance Verification — Logistic Regression vs XGBoost comparison",
]):
    rect(s, Inches(0.8), Inches(4.3)+i*Inches(0.52), Inches(8.2), Inches(0.44), fill=RGBColor(0x1D,0x4E,0xD8))
    tb(s, t, Inches(0.95), Inches(4.34)+i*Inches(0.52), Inches(7.9), Inches(0.38), size=13, bold=True, color=WHITE)

footer(s, 2, "Model Training", A1_DARK)

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 3 — A1 · DATASET OVERVIEW
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=WHITE)
sidebar(s, A1_COL)
header(s, "1. Dataset Overview", "AG News Topic Classification · 4 Target Categories · Versioned Subsets", A1_COL)
footer(s, 3, "Model Training", A1_DARK)
accent_line(s, A1_COL)


rect(s, Inches(0.5), Inches(1.6), Inches(5.9), Inches(4.65), fill=LIGHT_GRAY)
rect(s, Inches(0.5), Inches(1.6), Inches(5.9), Inches(0.48), fill=A1_COL)
tb(s, "Dataset v1.0.0 — Baseline Corpus", Inches(0.6), Inches(1.63), Inches(5.7), Inches(0.42), size=16, bold=True, color=WHITE)
bullets(s, [
    (0, "Source: AG News benchmark corpus"),
    (0, "8,000 total samples across balanced classes"),
    (0, "2,000 samples per category (Uniform distribution)"),
    (0, "Categories: World, Sports, Business, Sci/Tech"),
    (0, "Language: English news headlines & descriptions"),
    (0, "Primary feature: Unstructured article text"),
    (0, "Target variable: 4-class topic label (0 to 3)"),
    (0, "Tracked with SHA-256 digest hashing via MLflow Data"),
], Inches(0.6), Inches(2.15), Inches(5.6), Inches(3.9), size=14)

rect(s, Inches(6.6), Inches(1.6), Inches(6.4), Inches(4.65), fill=LIGHT_GRAY)
rect(s, Inches(6.6), Inches(1.6), Inches(6.4), Inches(0.48), fill=RED)
tb(s, "Dataset v2.0.0 — Drift Evaluation Set", Inches(6.7), Inches(1.63), Inches(6.2), Inches(0.42), size=16, bold=True, color=WHITE)
bullets(s, [
    (0, "Covariate shift: Integration of contemporary terminology:"),
    (1, "Generative AI, Large Language Models, Cloud GPUs"),
    (1, "Crypto Assets, Regulatory Actions, VAR refereeing"),
    (0, "Class distribution imbalance introduced:"),
    (1, "Sci/Tech increased to 40% (formerly 25%)"),
    (1, "Business shifted to 30% (formerly 25%)"),
    (1, "Sports and World reduced to 15% each"),
    (0, "Used to evaluate model robustness and trigger retraining"),
], Inches(6.7), Inches(2.15), Inches(6.1), Inches(3.9), size=14)

metric_box(s, Inches(0.5),  Inches(6.38), Inches(2.9), Inches(0.72), "8,000", "Samples (v1)", A1_COL)
metric_box(s, Inches(3.55), Inches(6.38), Inches(2.9), Inches(0.72), "4 Classes", "Target Categories", A1_DARK)
metric_box(s, Inches(6.6),  Inches(6.38), Inches(3.1), Inches(0.72), "v1 & v2", "Versioned Subsets", RED)
metric_box(s, Inches(9.85), Inches(6.38), Inches(3.1), Inches(0.72), "MLflow Data", "Dataset Artifact Tracking", GREEN)

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 4 — A1 · PREPROCESSING PIPELINE
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=WHITE)
sidebar(s, A1_COL)
header(s, "2. Preprocessing Pipeline", "Feature Extraction · Scikit-Learn Pipeline · Model Configuration Tuning", A1_COL)
footer(s, 4, "Model Training", A1_DARK)
accent_line(s, A1_COL)


steps = [
    ("Raw Text\nCorpus",     "AG News news\narticle strings",  A1_COL),
    ("Text\nCleaning",      "Lowercase, strip,\ntoken cleaning", A1_DARK),
    ("TF-IDF\nVectorizer",  "(1,2) N-Grams\nMax 5,000 features", A1_COL),
    ("Logistic\nRegression","L-BFGS solver\nC=1.0 regularized", GREEN),
    ("Predicted\nCategory", "World / Sports\nBusiness / Sci-Tech", ACCENT),
]
bw = Inches(2.1); bh = Inches(1.3); aw = Inches(0.35)
total_w = len(steps)*float(bw) + (len(steps)-1)*float(aw)
sx = (float(SLIDE_W) - total_w) / 2
for i, (ttl, det, col) in enumerate(steps):
    bx = sx + i*(float(bw)+float(aw))
    rect(s, bx, Inches(1.7), bw, bh, fill=col)
    tb(s, ttl, bx, Inches(1.78), bw, Inches(0.55), size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    tb(s, det, bx, Inches(2.32), bw, Inches(0.62), size=11, color=WHITE, align=PP_ALIGN.CENTER)
    if i < len(steps)-1:
        tb(s, "▶", bx+float(bw), Inches(2.1), aw, Inches(0.5), size=18, bold=True, color=A1_DARK, align=PP_ALIGN.CENTER)

tb(s, "Hyperparameter Tuning: Baseline (v1) vs Retrained (v2)", Inches(0.5), Inches(3.22), Inches(12.5), Inches(0.45), size=17, bold=True, color=A1_DARK)
rect(s, Inches(0.5), Inches(3.62), SLIDE_W-Inches(0.9), Inches(0.04), fill=LIGHT_BLUE)

table_data = [
    ("Max TF-IDF Features", "5,000",             "8,000 (Expanded vocabulary)"),
    ("N-Gram Range",        "(1, 2)",             "(1, 3) (Includes trigrams)"),
    ("Sublinear Term Frequency", "Standard TF",  "Sublinear TF enabled"),
    ("Regularization Parameter (C)", "1.0",      "2.5 (Less smoothing)"),
    ("Solver Iterations",   "1,000",              "1,500"),
    ("Class Weighting",     "Uniform",            "Balanced (Inverse frequency)"),
    ("Training Set",        "Dataset v1.0.0",     "Dataset v2.0.0 (Updated)"),
]
for col_x, lbl, col_fill in [(Inches(0.5), "Pipeline Parameter", A1_DARK), (Inches(4.05), "Model v1 (Baseline)", A1_COL), (Inches(8.2), "Model v2 (Retrained)", RED)]:
    w = Inches(3.5) if col_x == Inches(0.5) else Inches(4.1) if col_x == Inches(4.05) else Inches(4.7)
    rect(s, col_x, Inches(3.68), w, Inches(0.36), fill=col_fill)
    tb(s, lbl, col_x+Inches(0.1), Inches(3.71), w-Inches(0.15), Inches(0.3), size=13, bold=True, color=WHITE)

for ri, (param, v1, v2) in enumerate(table_data):
    y = Inches(4.08) + ri*Inches(0.37)
    bg = LIGHT_GRAY if ri%2==0 else WHITE
    for rx, rw in [(Inches(0.5),Inches(3.5)),(Inches(4.05),Inches(4.1)),(Inches(8.2),Inches(4.7))]:
        rect(s, rx, y, rw, Inches(0.35), fill=bg)
    tb(s, param, Inches(0.6), y+Inches(0.06), Inches(3.3), Inches(0.26), size=12, bold=True, color=DARK_GRAY)
    tb(s, v1,   Inches(4.15), y+Inches(0.06), Inches(3.9), Inches(0.26), size=12, color=A1_COL)
    tb(s, v2,   Inches(8.3),  y+Inches(0.06), Inches(4.5), Inches(0.26), size=12, color=RED)

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 5 — A1 · MODEL TRAINING & RESULTS
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=WHITE)
sidebar(s, A1_COL)
header(s, "3. Model Training & Results", "Classification Metrics · Drift Impact · Performance Recovery", A1_COL)
footer(s, 5, "Model Training", A1_DARK)
accent_line(s, A1_COL)


scenarios = [
    ("Model v1 on Dataset v1", "89.31%", "Macro F1: 89.26%", "Baseline Benchmark", A1_COL),
    ("Model v1 on Dataset v2", "95.06%", "Macro F1: 95.17%", "Under Drift Evaluation", ORANGE),
    ("Model v2 on Dataset v2", "95.69%", "Macro F1: 95.41%", "Retrained Production (+0.63%)", GREEN),
]
for i, (lbl, acc, f1, note, col) in enumerate(scenarios):
    bx = Inches(0.5) + i*Inches(4.25)
    rect(s, bx, Inches(1.6), Inches(4.0), Inches(1.6), fill=col)
    tb(s, lbl, bx, Inches(1.65), Inches(4.0), Inches(0.35), size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    tb(s, acc, bx, Inches(2.0), Inches(4.0), Inches(0.7), size=36, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    tb(s, f"{f1}  ·  {note}", bx, Inches(2.75), Inches(4.0), Inches(0.35), size=11, color=WHITE, align=PP_ALIGN.CENTER)

rect(s, Inches(0.5), Inches(3.35), Inches(6.0), Inches(3.7), fill=LIGHT_GRAY, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.5))
rect(s, Inches(0.5), Inches(3.35), Inches(6.0), Inches(0.38), fill=A1_DARK)
tb(s, "MLflow Experiment Tracking Summary", Inches(0.6), Inches(3.38), Inches(5.8), Inches(0.3), size=12, bold=True, color=WHITE)

run_data = [
    ("Baseline Run (v1)", "LogisticRegression, TF-IDF 5k, C=1.0", "Acc: 89.31% | F1: 89.26%"),
    ("Drift Evaluation (v1)", "Model v1 evaluated on drifted v2", "Acc: 95.06% | F1: 95.17% (Shifted)"),
    ("Retrained Run (v2)","LogisticRegression, Sublinear 8k, C=2.5","Acc: 95.69% | F1: 95.41% (Optimal)"),
    ("Drift Indicators",  "Population Stability Index (PSI)",     "PSI = 0.1818 | Vocab Shift 24.3%"),
    ("Lifecycle Stage",   "v1: Archived_Baseline",                "v2: Production Candidate"),
]
for ri, (r1, r2, r3) in enumerate(run_data):
    ry = Inches(3.85) + ri * Inches(0.62)
    rect(s, Inches(0.6), ry, Inches(5.8), Inches(0.55), fill=WHITE)
    tb(s, r1, Inches(0.7), ry+Inches(0.04), Inches(2.5), Inches(0.24), size=10.5, bold=True, color=A1_COL)
    tb(s, r2, Inches(0.7), ry+Inches(0.26), Inches(5.5), Inches(0.22), size=9.5, color=DARK_GRAY)
    tb(s, r3, Inches(3.2), ry+Inches(0.04), Inches(3.1), Inches(0.24), size=10, bold=True, color=GREEN_DARK if "Gain" in r3 or "89.5" in r3 else RED if "Drop" in r3 else DARK_GRAY)

if os.path.exists(DRIFT_COMP_IMG):
    rect(s, Inches(6.7), Inches(3.35), Inches(6.15), Inches(3.7), fill=WHITE, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.5))
    s.shapes.add_picture(DRIFT_COMP_IMG, Inches(6.8), Inches(3.45), width=Inches(5.95), height=Inches(3.5))

# ═════════════════════════════════════════════════════════════════════════════

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 7 — A1 · MODEL PERFORMANCE VERIFICATION (NOTEBOOK VS RESULTS)
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=WHITE)
sidebar(s, A1_COL)
header(s, "4. Model Performance Verification", "Cross-referencing validation and test metrics between presentation and notebook output", A1_COL)
footer(s, 6, "Model Training", A1_DARK)
accent_line(s, A1_COL)


# Card 1: Logistic Regression (Baseline)
rect(s, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.5), fill=LIGHT_GRAY, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.8))
rect(s, Inches(0.8), Inches(1.8), Inches(5.6), Inches(0.45), fill=A1_COL)
tb(s, "Logistic Regression (Baseline)", Inches(1.0), Inches(1.86), Inches(5.2), Inches(0.35), size=13, bold=True, color=WHITE)

tb(s, "Validation Accuracy / F1", Inches(1.1), Inches(2.45), Inches(5.0), Inches(0.3), size=11, color=DARK_GRAY)
tb(s, "88.33% / 88.28%", Inches(1.1), Inches(2.8), Inches(5.0), Inches(0.6), size=28, bold=True, color=A1_DARK)

tb(s, "Final Test Accuracy / F1", Inches(1.1), Inches(3.6), Inches(5.0), Inches(0.3), size=11, color=DARK_GRAY)
tb(s, "88.50% / 88.47%", Inches(1.1), Inches(3.95), Inches(5.0), Inches(0.6), size=28, bold=True, color=GREEN_DARK)

rect(s, Inches(1.0), Inches(4.8), Inches(5.2), Inches(1.2), fill=WHITE, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.5))
bullets(s, [
    (0, "TF-IDF Vectorizer with 5,000 max features"),
    (0, "Consistent performance across validation & test sets"),
    (0, "Selected as baseline for REST API deployment and MLOps monitoring"),
], Inches(1.1), Inches(4.88), Inches(5.0), Inches(1.0), size=10.5)

# Card 2: XGBoost (Advanced Comparison)
rect(s, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.5), fill=LIGHT_GRAY, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.8))
rect(s, Inches(6.8), Inches(1.8), Inches(5.6), Inches(0.45), fill=BLUE)
tb(s, "XGBoost (Advanced Comparison)", Inches(7.0), Inches(1.86), Inches(5.2), Inches(0.35), size=13, bold=True, color=WHITE)

tb(s, "Validation Accuracy / F1", Inches(7.1), Inches(2.45), Inches(5.0), Inches(0.3), size=11, color=DARK_GRAY)
tb(s, "82.25% / 82.22%", Inches(7.1), Inches(2.8), Inches(5.0), Inches(0.6), size=28, bold=True, color=DARK_GRAY)

tb(s, "Key Empirical Observation", Inches(7.1), Inches(3.6), Inches(5.0), Inches(0.3), size=11, bold=True, color=BLUE)
rect(s, Inches(7.0), Inches(3.95), Inches(5.2), Inches(2.05), fill=WHITE, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.5))
bullets(s, [
    (0, "Logistic Regression outperforms XGBoost by +6.08% on sparse TF-IDF text features."),
    (0, "High-dimensional sparse matrices favor linear decision boundaries over tree splits."),
    (0, "XGBoost incurs substantially higher inference latency and memory footprint."),
    (0, "Empirical justification for linear model selection in latency-critical MLOps production."),
], Inches(7.1), Inches(4.05), Inches(5.0), Inches(1.85), size=11)

# SLIDE 7 — A2 SECTION DIVIDER
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=A2_DARK)
rect(s, SLIDE_W-Inches(4.5), 0, Inches(4.5), SLIDE_H, fill=A2_COL)
rect(s, 0, Inches(3.5), SLIDE_W, Inches(0.08), fill=ACCENT)
rect(s, 0, Inches(3.62), SLIDE_W, Inches(0.03), fill=RGBColor(0xA7,0xF3,0xD0))

tb(s, "Part 2", Inches(0.8), Inches(0.9), Inches(5), Inches(1.2),
   size=80, bold=True, color=WHITE)
tb(s, "API Deployment", Inches(0.8), Inches(2.3), Inches(7), Inches(0.85), size=40, bold=True, color=WHITE)
tb(s, "Containerization, REST Service Architecture, and Endpoint Contracts",
   Inches(0.8), Inches(3.25), Inches(8.5), Inches(0.45),
   size=16, italic=True, color=RGBColor(0xA7,0xF3,0xD0))

for i, t in enumerate([
    "Deployment Architecture — FastAPI REST server, Docker, multi-service setup",
    "Interface for Model Invocation — Swagger UI, Pydantic schemas, batch endpoints",
]):
    rect(s, Inches(0.8), Inches(4.3)+i*Inches(0.62), Inches(8.2), Inches(0.52), fill=A2_COL)
    tb(s, t, Inches(0.95), Inches(4.34)+i*Inches(0.62), Inches(7.9), Inches(0.44), size=14, bold=True, color=WHITE)

footer(s, 7, "API Deployment", A2_DARK)

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 8 — A2 · DEPLOYMENT ARCHITECTURE
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=WHITE)
sidebar(s, A2_COL)
header(s, "4. Deployment Architecture (Docker)", "FastAPI REST API · Docker Compose · Multi-Service Isolation", A2_COL)
footer(s, 8, "API Deployment", A2_DARK)
accent_line(s, A2_COL)


rect(s, Inches(0.55), Inches(1.65), Inches(2.0), Inches(1.0), fill=A2_DARK)
tb(s, "Client Applications\n(cURL / Web UI)", Inches(0.55), Inches(1.75), Inches(2.0), Inches(0.8), size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
tb(s, "POST /predict\nGET /health\nGET /docs", Inches(2.6), Inches(1.9), Inches(1.5), Inches(0.7), size=10, italic=True, color=A2_COL)
tb(s, "→", Inches(2.59), Inches(2.0), Inches(0.3), Inches(0.4), size=20, bold=True, color=A2_DARK)

rect(s, Inches(4.15), Inches(1.6), Inches(2.5), Inches(4.1), fill=A2_COL)
tb(s, "Container Service", Inches(4.2), Inches(1.65), Inches(2.4), Inches(0.35), size=11, bold=True, color=ACCENT)
tb(s, "FastAPI\nserver.py", Inches(4.2), Inches(2.0), Inches(2.4), Inches(0.7), size=20, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
for j, pt in enumerate([
    "POST /predict: Text topic inference",
    "GET /health: Model readiness probe",
    "GET /: Responsive Jinja2 Web UI",
    "Pydantic schema validation & types",
    "Outputs full 4-class probabilities",
    "High-throughput Uvicorn ASGI server",
]):
    tb(s, "• "+pt, Inches(4.25), Inches(2.75)+j*Inches(0.3), Inches(2.35), Inches(0.28), size=10, color=WHITE)
tb(s, "Port 8000", Inches(4.2), Inches(5.38), Inches(2.4), Inches(0.28), size=12, bold=True, color=ACCENT, align=PP_ALIGN.CENTER, link="http://localhost:8000/docs")
tb(s, "→", Inches(6.68), Inches(2.05), Inches(0.3), Inches(0.4), size=20, bold=True, color=A2_DARK)

rect(s, Inches(7.0), Inches(1.6), Inches(2.4), Inches(2.0), fill=NAVY)
tb(s, "MLflow\nTracking Server", Inches(7.05), Inches(1.68), Inches(2.3), Inches(0.65), size=16, bold=True, color=WHITE, align=PP_ALIGN.CENTER, link="http://localhost:5001")
tb(s, "• Run metadata\n• Model registry\n• Artifact store\n• Port 5001", Inches(7.05), Inches(2.35), Inches(2.3), Inches(1.15), size=11, color=RGBColor(0xBF,0xDB,0xFF))

rect(s, Inches(7.0), Inches(3.75), Inches(2.4), Inches(1.0), fill=DARK_GRAY)
tb(s, "SQLite Store\nmetrics_export.sqlite", Inches(7.05), Inches(3.82), Inches(2.3), Inches(0.85), size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

rect(s, Inches(7.0), Inches(4.9), Inches(2.4), Inches(0.8), fill=ORANGE)
tb(s, "Grafana Dashboard\nPort 3005", Inches(7.05), Inches(4.95), Inches(2.3), Inches(0.7), size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER, link="http://localhost:3005")

tb(s, "↓", Inches(8.07), Inches(3.63), Inches(0.3), Inches(0.4), size=18, bold=True, color=DARK_GRAY)
tb(s, "↓", Inches(8.07), Inches(4.78), Inches(0.3), Inches(0.4), size=18, bold=True, color=ORANGE)

rect(s, Inches(9.65), Inches(1.6), Inches(3.45), Inches(4.1), fill=CODE_BG)
tb(s, "docker-compose.yml", Inches(9.7), Inches(1.65), Inches(3.35), Inches(0.38), size=13, bold=True, color=ACCENT)
tb(s,
   "services:\n"
   "  app:\n"
   "    build: .\n"
   "    ports:\n"
   '      - "8501:8501"\n'
   "  mlflow:\n"
   "    image: mlflow\n"
   "    ports:\n"
   '      - "5001:5000"\n'
   "  grafana:\n"
   "    image: grafana/grafana\n"
   "    ports:\n"
   '      - "3005:3000"\n'
   "    volumes:\n"
   "      - ./grafana:/etc/grafana",
   Inches(9.7), Inches(2.05), Inches(3.35), Inches(3.5), size=10, color=CODE_GRN)

for j, (k, v) in enumerate([
    ("Model Artifacts", "model.pkl (Scikit-Learn TF-IDF + Logistic Regression, 339 KB)"),
    ("Schema Validation", "Pydantic BaseModel with strict headline string validation"),
    ("REST Endpoints",   "GET /, GET /health, POST /predict, GET /docs (Swagger UI)"),
    ("Cloud Deployment", "Render Cloud live service + Docker containerized runtime"),
]):
    bx = Inches(0.55)+j*Inches(3.15)
    rect(s, bx, Inches(6.05), Inches(2.95), Inches(0.62), fill=LIGHT_GRAY)
    tb(s, k, bx+Inches(0.08), Inches(6.08), Inches(2.8), Inches(0.26), size=11, bold=True, color=A2_DARK)
    tb(s, v, bx+Inches(0.08), Inches(6.34), Inches(2.8), Inches(0.28), size=10, color=DARK_GRAY)

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 9 — A2 · INTERFACE FOR MODEL INVOCATION
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=WHITE)
sidebar(s, A2_COL)
header(s, "5. Interface for Model Invocation", "FastAPI Swagger Documentation · Live Prediction Form · Client cURL", A2_COL)
footer(s, 9, "API Deployment", A2_DARK)
accent_line(s, A2_COL)


mini_win(s, Inches(0.5), Inches(1.55), Inches(6.1), Inches(5.15),
         "FastAPI REST API Docs — http://localhost:8000/docs", A2_COL)

for endpoint, method, col, y, lnk in [
    ("/predict — AG News Topic Inference Endpoint",     "POST", GREEN, Inches(1.98), "http://localhost:8000/docs#/default/predict_predict_post"),
    ("/health — Service Readiness & Model Probe",       "GET",  A2_COL, Inches(5.22), "http://localhost:8000/health"),
    ("/ — Interactive Web UI (HTML / Jinja2)",          "GET",  NAVY,   Inches(5.6),  "http://localhost:8000"),
]:
    rect(s, Inches(0.55), y, Inches(6.0), Inches(0.32),
         fill=RGBColor(0x49,0x60,0x4A) if method=="POST" else RGBColor(0x1A,0x40,0x6B))
    rect(s, Inches(0.55), y, Inches(0.55), Inches(0.32), fill=col)
    tb(s, method, Inches(0.56), y+Inches(0.03), Inches(0.53), Inches(0.26), size=9, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    tb(s, endpoint, Inches(1.14), y+Inches(0.03), Inches(5.35), Inches(0.26), size=10, bold=True, color=WHITE, link=lnk)

rect(s, Inches(0.55), Inches(2.34), Inches(6.0), Inches(0.22), fill=RGBColor(0xE8,0xF4,0xFD))
tb(s, "Request Payload: PredictionRequest (application/json)", Inches(0.62), Inches(2.36), Inches(5.8), Inches(0.18), size=9, bold=True, color=A2_COL)
rect(s, Inches(0.55), Inches(2.58), Inches(6.0), Inches(0.72), fill=CODE_BG)
tb(s,
   '{\n'
   '  "text": "Nvidia launches Blackwell GPU architecture for enterprise AI"\n'
   '}', Inches(0.65), Inches(2.62), Inches(5.82), Inches(0.64), size=9.5, color=CODE_GRN)

rect(s, Inches(0.55), Inches(3.34), Inches(6.0), Inches(0.22), fill=RGBColor(0xD1,0xFA,0xE5))
tb(s, "Response Payload: PredictionResponse (200 OK)", Inches(0.62), Inches(3.36), Inches(5.8), Inches(0.18), size=9, bold=True, color=GREEN)
rect(s, Inches(0.55), Inches(3.58), Inches(6.0), Inches(1.58), fill=CODE_BG)
tb(s,
   '{\n'
   '  "text": "Nvidia launches Blackwell GPU architecture...",\n'
   '  "prediction": "Sci/Tech",\n'
   '  "class_id": 3,\n'
   '  "confidence": 0.8988,\n'
   '  "probabilities": {\n'
   '    "World": 0.0125, "Sports": 0.0084,\n'
   '    "Business": 0.0803, "Sci/Tech": 0.8988\n'
   '  }\n'
   '}', Inches(0.65), Inches(3.62), Inches(5.82), Inches(1.50), size=9, color=CODE_GRN)

rect(s, Inches(0.55), Inches(5.98), Inches(6.0), Inches(0.70), fill=CODE_BG)
tb(s,
   "curl -X POST http://localhost:8000/predict \\\n"
   '  -H "Content-Type: application/json" \\\n'
   '  -d \'{"text": "Nvidia launches Blackwell GPU for data centers"}\'',
   Inches(0.63), Inches(6.02), Inches(5.85), Inches(0.62), size=9, color=ACCENT)


mini_win(s, Inches(6.8), Inches(1.55), Inches(6.2), Inches(5.15),
         "Streamlit Prediction Panel — http://localhost:8501", TEAL)

rect(s, Inches(6.8), Inches(1.93), Inches(1.55), Inches(4.77), fill=RGBColor(0xE8,0xEF,0xF8))
tb(s, "Configuration", Inches(6.88), Inches(2.0), Inches(1.38), Inches(0.3), size=10, bold=True, color=A2_DARK)
tb(s, "Active Model\nModel v2", Inches(6.88), Inches(2.35), Inches(1.38), Inches(0.5), size=9, color=DARK_GRAY)
rect(s, Inches(6.88), Inches(2.83), Inches(1.38), Inches(0.28), fill=A2_COL)
tb(s, "  Model v2  ✓", Inches(6.89), Inches(2.86), Inches(1.36), Inches(0.22), size=9, bold=True, color=WHITE)
tb(s, "  Model v1", Inches(6.89), Inches(3.14), Inches(1.36), Inches(0.22), size=9, color=DARK_GRAY)
tb(s, "Threshold\n0.50", Inches(6.88), Inches(3.5), Inches(1.38), Inches(0.45), size=9, color=DARK_GRAY)

tb(s, "Input article text for classification:", Inches(8.45), Inches(2.0), Inches(4.4), Inches(0.3), size=11, bold=True, color=DARK_GRAY)
rect(s, Inches(8.45), Inches(2.34), Inches(4.4), Inches(0.85), fill=WHITE, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.8))
tb(s, "Nvidia launches Blackwell GPU architecture for\nenterprise compute workloads, reporting high throughput…", Inches(8.52), Inches(2.38), Inches(4.28), Inches(0.75), size=9, color=DARK_GRAY)
rect(s, Inches(8.45), Inches(3.26), Inches(1.5), Inches(0.32), fill=TEAL)
tb(s, "Classify Text", Inches(8.46), Inches(3.29), Inches(1.48), Inches(0.26), size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER, link="http://localhost:8501")

rect(s, Inches(8.45), Inches(3.68), Inches(4.4), Inches(1.55), fill=RGBColor(0xEF,0xFD,0xF6), line=GREEN, lw=Pt(0.8))
tb(s, "Predicted Class: Sci / Tech", Inches(8.55), Inches(3.74), Inches(4.2), Inches(0.3), size=11, bold=True, color=GREEN)
tb(s, "Confidence Score: 94.7%", Inches(8.55), Inches(4.06), Inches(4.2), Inches(0.28), size=12, bold=True, color=NAVY)
for label, val in [("Inference Latency:", "0.21 ms"), ("Serving Model:", "v2 (Production Candidate)"), ("Pipeline:", "Sublinear TF-IDF + LR")]:
    y_off = {"Inference Latency:": Inches(4.36), "Serving Model:": Inches(4.64), "Pipeline:": Inches(4.92)}[label]
    tb(s, f"{label}   {val}", Inches(8.55), y_off, Inches(4.2), Inches(0.28), size=11, color=DARK_GRAY)

tb(s, "Class Probability Distribution:", Inches(8.45), Inches(5.32), Inches(4.2), Inches(0.25), size=10, bold=True, color=DARK_GRAY)
for bi, (lbl, val, col) in enumerate([
    ("Sci/Tech", 0.947, TEAL), ("Business", 0.031, A2_COL),
    ("Sports", 0.014, NAVY), ("World", 0.008, LIGHT_BLUE)
]):
    by = Inches(5.6)+bi*Inches(0.22)
    tb(s, lbl, Inches(8.45), by, Inches(0.85), Inches(0.20), size=8.5, color=DARK_GRAY)
    bw2 = Inches(val*3.3)
    rect(s, Inches(9.32), by+Inches(0.03), bw2, Inches(0.15), fill=col)
    tb(s, f"{val*100:.1f}%", Inches(9.32)+bw2+Inches(0.05), by, Inches(0.5), Inches(0.20), size=8, bold=(bi==0), color=DARK_GRAY)

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 10 — A3 SECTION DIVIDER
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=A3_DARK)
rect(s, SLIDE_W-Inches(4.5), 0, Inches(4.5), SLIDE_H, fill=A3_COL)
rect(s, 0, Inches(3.5), SLIDE_W, Inches(0.08), fill=ACCENT)
rect(s, 0, Inches(3.62), SLIDE_W, Inches(0.03), fill=RGBColor(0xFE,0xD7,0xAA))

tb(s, "Part 3", Inches(0.8), Inches(0.9), Inches(5), Inches(1.2),
   size=80, bold=True, color=WHITE)
tb(s, "Versioning & Monitoring", Inches(0.8), Inches(2.3), Inches(7), Inches(0.85), size=40, bold=True, color=WHITE)
tb(s, "Model Lifecycle Management, Data Drift Detection, and Monitoring Stacks",
   Inches(0.8), Inches(3.25), Inches(8.5), Inches(0.45),
   size=16, italic=True, color=RGBColor(0xFE,0xD7,0xAA))

for i, t in enumerate([
    "MLflow Model Registry — Lifecycle management, staging tags, and artifact logging",
    "Dashboard Visuals — Interactive Streamlit application and Grafana monitoring",
    "Key Insights & Recommendations — Operational learnings and continuous monitoring",
    "Limitations & Future Work — Architectural trade-offs and future extensions",
]):
    rect(s, Inches(0.8), Inches(4.3)+i*Inches(0.52), Inches(8.2), Inches(0.44), fill=A3_COL)
    tb(s, t, Inches(0.95), Inches(4.34)+i*Inches(0.52), Inches(7.9), Inches(0.38), size=13, bold=True, color=WHITE)

footer(s, 10, "MLOps Monitoring", A3_DARK)

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 11 — A3 · MLFLOW MODEL REGISTRY
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=WHITE)
sidebar(s, A3_COL)
header(s, "6. MLflow Model Registry", "Lifecycle Management · Staged Model Tagging · Artifact Tracking", A3_COL)
footer(s, 11, "MLOps Monitoring", A3_DARK)
accent_line(s, A3_COL)


rect(s, Inches(0.5), Inches(1.55), Inches(4.8), Inches(5.15), fill=LIGHT_GRAY, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.5))
rect(s, Inches(0.5), Inches(1.55), Inches(4.8), Inches(0.4), fill=A3_COL)
tb(s, "Model Lifecycle Protocol", Inches(0.6), Inches(1.6), Inches(4.6), Inches(0.3), size=12, bold=True, color=WHITE)

flow = [
    (GREEN,  "1. Train & Register", "Model v1 (Baseline) & Model v2 (Retrained)"),
    (A3_COL, "2. Parameter Logging", "TF-IDF (1,3)-grams, C=2.5, balanced weights"),
    (NAVY,   "3. Metric Auditing",   "Acc: 95.7% | F1: 95.4% | Latency: 0.32 ms"),
    (PURPLE, "4. Stage Promotion",   "v1: Archived_Baseline | v2: Production"),
    (ORANGE, "5. Artifact Storage",  "model.pkl, confusion matrices, signatures"),
]
for fi, (col, ftitle, fdesc) in enumerate(flow):
    fy = Inches(2.1) + fi * Inches(0.8)
    rect(s, Inches(0.6), fy, Inches(4.6), Inches(0.72), fill=WHITE, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.5))
    rect(s, Inches(0.6), fy, Inches(0.12), Inches(0.72), fill=col)
    tb(s, ftitle, Inches(0.8), fy+Inches(0.06), Inches(4.3), Inches(0.26), size=11, bold=True, color=DARK_GRAY)
    tb(s, fdesc, Inches(0.8), fy+Inches(0.32), Inches(4.3), Inches(0.32), size=9.5, color=DARK_GRAY)

rect(s, Inches(0.6), Inches(6.15), Inches(4.6), Inches(0.45), fill=CODE_BG)
tb(s, "Registry UI: http://localhost:5001", Inches(0.7), Inches(6.22), Inches(4.4), Inches(0.3), size=11, bold=True, color=CODE_GRN, link="http://localhost:5001")

if os.path.exists(MLFLOW_IMG):
    rect(s, Inches(5.45), Inches(1.55), Inches(7.4), Inches(5.15), fill=WHITE, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.8))
    rect(s, Inches(5.45), Inches(1.55), Inches(7.4), Inches(0.38), fill=NAVY)
    tb(s, "MLflow Registry Interface (AGNews-TopicClassifier)", Inches(5.6), Inches(1.6), Inches(7.0), Inches(0.28), size=11, bold=True, color=WHITE)
    s.shapes.add_picture(MLFLOW_IMG, Inches(5.5), Inches(1.98), width=Inches(7.3), height=Inches(4.65))

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 12 — A3 · STREAMLIT DASHBOARD VISUALS
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=WHITE)
sidebar(s, TEAL)
header(s, "7. Dashboard Visuals — Streamlit Application", "Interactive Model Selection · Live Inference · Drift Visualization (Port 8501)", TEAL)
footer(s, 12, "MLOps Monitoring", TEAL)
accent_line(s, TEAL)


rect(s, Inches(0.5), Inches(1.55), Inches(4.5), Inches(5.15), fill=LIGHT_GRAY, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.5))
rect(s, Inches(0.5), Inches(1.55), Inches(4.5), Inches(0.4), fill=TEAL)
tb(s, "Application Capabilities", Inches(0.6), Inches(1.6), Inches(4.3), Inches(0.3), size=12, bold=True, color=WHITE)

bullets(s, [
    (0, "Tab 1: Dataset Exploration"),
    (1, "v1 vs v2 class balance visualizations"),
    (1, "Document character length distributions"),
    (0, "Tab 2: Model Serving & Live Test"),
    (1, "Dynamic switching between v1 and v2"),
    (1, "Real-time class probability breakdown"),
    (1, "Per-sample latency metrics (~0.2ms)"),
    (0, "Tab 3: Model Comparison"),
    (1, "Multi-metric performance radar plots"),
    (0, "Tab 4: SQLite Inference Audit"),
    (1, "Historical log of executed predictions"),
], Inches(0.6), Inches(2.1), Inches(4.3), Inches(3.8), size=12)

rect(s, Inches(0.6), Inches(6.15), Inches(4.3), Inches(0.45), fill=CODE_BG)
tb(s, "Launch: http://localhost:8501", Inches(0.7), Inches(6.22), Inches(4.1), Inches(0.3), size=11, bold=True, color=CODE_GRN, link="http://localhost:8501")

if os.path.exists(STREAMLIT_IMG):
    rect(s, Inches(5.15), Inches(1.55), Inches(7.7), Inches(5.15), fill=WHITE, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.8))
    rect(s, Inches(5.15), Inches(1.55), Inches(7.7), Inches(0.38), fill=TEAL)
    tb(s, "Streamlit User Interface & Inference Benchmark", Inches(5.3), Inches(1.6), Inches(7.3), Inches(0.28), size=11, bold=True, color=WHITE)
    s.shapes.add_picture(STREAMLIT_IMG, Inches(5.2), Inches(1.98), width=Inches(7.6), height=Inches(4.65))

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 13 — A3 · GRAFANA MONITORING VISUALS
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=WHITE)
sidebar(s, ORANGE)
header(s, "8. Dashboard Visuals — Grafana Monitoring", "Production Observability · PSI Drift Alerting · Live Telemetry (Port 3005)", ORANGE)
footer(s, 13, "MLOps Monitoring", ORANGE)
accent_line(s, ORANGE)


rect(s, Inches(0.5), Inches(1.55), Inches(4.5), Inches(5.15), fill=LIGHT_GRAY, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.5))
rect(s, Inches(0.5), Inches(1.55), Inches(4.5), Inches(0.4), fill=ORANGE)
tb(s, "Monitoring Dashboard Architecture", Inches(0.6), Inches(1.6), Inches(4.3), Inches(0.3), size=12, bold=True, color=WHITE)

bullets(s, [
    (0, "Automated YAML Provisioning"),
    (1, "Direct SQLite datasource connection"),
    (0, "Accuracy Gauges"),
    (1, "Production v2 accuracy: 95.7%"),
    (1, "Model v1 under drift: 95.1%"),
    (0, "Data Drift Indicator (PSI)"),
    (1, "PSI = 0.182 (Covariate shift tracked)"),
    (0, "Inference Latency & Telemetry"),
    (1, "Average latency: 0.470 ms"),
    (1, "Lifecycle model comparison & live logs"),
], Inches(0.6), Inches(2.1), Inches(4.3), Inches(3.8), size=12)

rect(s, Inches(0.6), Inches(6.15), Inches(4.3), Inches(0.45), fill=CODE_BG)
tb(s, "Monitoring: http://localhost:3005", Inches(0.7), Inches(6.22), Inches(4.1), Inches(0.3), size=10.5, bold=True, color=CODE_GRN, link="http://localhost:3005")

if os.path.exists(GRAFANA_IMG):
    rect(s, Inches(5.15), Inches(1.55), Inches(7.7), Inches(5.15), fill=WHITE, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.8))
    rect(s, Inches(5.15), Inches(1.55), Inches(7.7), Inches(0.38), fill=ORANGE)
    tb(s, "Grafana Monitoring Dashboard Panels", Inches(5.3), Inches(1.6), Inches(7.3), Inches(0.28), size=11, bold=True, color=WHITE)
    s.shapes.add_picture(GRAFANA_IMG, Inches(5.2), Inches(1.98), width=Inches(7.6), height=Inches(4.65))

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 14 — LIVE DEMO & DOCKER QUICK LAUNCH
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=WHITE)
sidebar(s, GREEN)
header(s, "Live Demo & Service Endpoints", "Direct Application Links · Containerized Service Execution", GREEN)
footer(s, 14, "DEMO", GREEN_DARK)
accent_line(s, GREEN)
section_tag(s, "LIVE", GREEN)

service_cards = [
    ("Streamlit Web Application", "http://localhost:8501", TEAL, 
     "Interactive model selection, single-text prediction, confidence distribution, and drift assessment"),
    ("FastAPI Swagger Documentation", "http://localhost:8000/docs", A2_COL,
     "Interactive REST testing, single & batch (/predict/batch) inference, input validation, and /health"),
    ("MLflow Tracking Server", "http://localhost:5001", NAVY,
     "Experiment comparative analysis, registered model stages, logged parameters, and artifact storage"),
    ("Grafana Monitoring Dashboard", "http://localhost:3005", ORANGE,
     "Real-time operational dashboards, Population Stability Index (PSI) drift alarms, and latency metrics"),
]

for idx, (s_name, s_url, s_col, s_desc) in enumerate(service_cards):
    col = idx % 2
    row = idx // 2
    card_x = Inches(0.6) + col * Inches(6.2)
    card_y = Inches(1.65) + row * Inches(1.8)
    
    rect(s, card_x, card_y, Inches(5.9), Inches(1.65), fill=LIGHT_GRAY, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.8))
    rect(s, card_x, card_y, Inches(5.9), Inches(0.42), fill=s_col)
    tb(s, s_name, card_x + Inches(0.2), card_y + Inches(0.08), Inches(5.5), Inches(0.3), size=13, bold=True, color=WHITE)
    
    rect(s, card_x + Inches(0.2), card_y + Inches(0.55), Inches(5.5), Inches(0.45), fill=WHITE, line=s_col, lw=Pt(1.2))
    tb(s, f"{s_url}", card_x + Inches(0.3), card_y + Inches(0.62), Inches(5.3), Inches(0.35),
       size=12, bold=True, color=s_col, link=s_url)
    
    tb(s, s_desc, card_x + Inches(0.2), card_y + Inches(1.08), Inches(5.5), Inches(0.5), size=10.5, color=DARK_GRAY)

rect(s, Inches(0.6), Inches(5.45), Inches(12.1), Inches(1.4), fill=CODE_BG)
rect(s, Inches(0.6), Inches(5.45), Inches(12.1), Inches(0.3), fill=DARK_GRAY)
tb(s, "Terminal Command: Launch Multi-Service Stack", Inches(0.75), Inches(5.5), Inches(11), Inches(0.22), size=10.5, bold=True, color=ACCENT)

cmd_text = (
    "# From the project root, launch FastAPI, Streamlit, MLflow, and Grafana in detached mode:\n"
    "cd \"/Users/BlankUser/Desktop/data mining A3\" && docker compose up -d"
)
tb(s, cmd_text, Inches(0.8), Inches(5.82), Inches(11.8), Inches(0.9), size=11, color=CODE_GRN)

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 15 — KEY INSIGHTS & RECOMMENDATIONS
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=WHITE)
sidebar(s, NAVY)
header(s, "8. Key Insights & Recommendations", "Cross-Assignment Findings · Operational Learnings · Production Strategy", NAVY)
footer(s, 15)
accent_line(s)

insight_blocks = [
    (A1_COL, "Quantitative Drift Detection & Analysis",
     ["Population Stability Index (PSI = 0.1818) detected moderate class distribution shift",
      "Vocabulary drift score reached 24.25% with 75.75% shared feature overlap",
      "Sci/Tech category increased to 40% while World and Sports contracted to 15% each"]),
    (A1_DARK,"Targeted Retraining & Performance Recovery",
     ["Expanded n-gram vocabulary (1,3) with 8,000 features and balanced class weights",
      "Retrained Model v2 achieved 95.69% accuracy on modern shifted news corpus",
      "Macro F1-score reached 95.41%, delivering strong generalization across all 4 categories"]),
    (A2_COL, "Robust REST API Contract Enforcement",
     ["Pydantic schema enforces strict headline string validation on POST /predict",
      "Full 4-class probability distribution returned with high confidence (e.g. 89.9%)",
      "GET /health probe verifies model pipeline memory residency for Docker & cloud orchestration"]),
    (A3_COL, "Full Traceability via MLflow & Docker",
     ["Datasets versioned with SHA-256 digest hashes via MLflow Data tracking",
      "Staged model promotion: Model v1 (Archived_Baseline) vs Model v2 (Production)",
      "Automated Grafana dashboards provisioned directly via Docker Compose and SQLite"]),
]
for i, (col, title, points) in enumerate(insight_blocks):
    row = i//2; c = i%2
    bx = Inches(0.5)+c*Inches(6.35)
    by = Inches(1.6)+row*Inches(2.5)
    rect(s, bx, by, Inches(6.1), Inches(2.35), fill=LIGHT_GRAY)
    rect(s, bx, by, Inches(6.1), Inches(0.45), fill=col)
    tb(s, title, bx+Inches(0.1), by+Inches(0.08), Inches(5.9), Inches(0.35), size=13, bold=True, color=WHITE)
    for j, pt in enumerate(points):
        tb(s, "•  "+pt, bx+Inches(0.15), by+Inches(0.55)+j*Inches(0.56), Inches(5.85), Inches(0.52), size=12, color=DARK_GRAY)

rect(s, Inches(0.5), Inches(6.75), SLIDE_W-Inches(0.9), Inches(0.48), fill=ACCENT)
tb(s, "Operational Recommendation: Automated CI/CD retraining triggered when PSI > 0.18 or macro F1 drops by >3%.",

   Inches(0.65), Inches(6.79), Inches(12.5), Inches(0.4), size=12, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 16 — LIMITATIONS & FUTURE WORK
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=WHITE)
sidebar(s, NAVY)
header(s, "9. Limitations & Future Work", "Current Architectural Constraints · Planned Production Enhancements", NAVY)
footer(s, 16)
accent_line(s)

rect(s, Inches(0.5), Inches(1.6), Inches(5.9), Inches(5.15), fill=LIGHT_GRAY)
rect(s, Inches(0.5), Inches(1.6), Inches(5.9), Inches(0.48), fill=RED)
tb(s, "Current Constraints", Inches(0.6), Inches(1.65), Inches(5.7), Inches(0.4), size=16, bold=True, color=WHITE)
bullets(s, [
    (0, "Static Evaluation Sets"),
    (1, "Dataset v2 captures discrete shift rather than continuous streaming"),
    (1, "Real-world news patterns require dynamic temporal tracking"),
    (0, "TF-IDF Vector Space Constraints"),
    (1, "Bag-of-words ignores word order and deep semantic context"),
    (1, "Cannot capture out-of-vocabulary semantic analogies"),
    (0, "SQLite Concurrency Limitations"),
    (1, "Single-file database lacks support for high concurrent write volumes"),
    (1, "Appropriate for development; requires managed database for scale"),
    (0, "Authentication Protocol"),
    (1, "FastAPI endpoints operate without token-based authentication"),
    (1, "Grafana dashboard uses default administration credentials"),
], Inches(0.62), Inches(2.15), Inches(5.65), Inches(4.5), size=12)

rect(s, Inches(6.65), Inches(1.6), Inches(6.35), Inches(5.15), fill=LIGHT_GRAY)
rect(s, Inches(6.65), Inches(1.6), Inches(6.35), Inches(0.48), fill=GREEN)
tb(s, "Future Extensions", Inches(6.75), Inches(1.65), Inches(6.15), Inches(0.4), size=16, bold=True, color=WHITE)
bullets(s, [
    (0, "Transformer-Based Embeddings"),
    (1, "Evaluate DistilBERT / RoBERTa for context-aware representation"),
    (1, "Projected accuracy improvement of 3-5% across technical classes"),
    (0, "Continuous Ingestion Pipeline"),
    (1, "Integrate live RSS news streams for real-time inference"),
    (1, "Automated scheduled retraining based on continuous drift"),
    (0, "CI/CD & Governance Automation"),
    (1, "GitHub Actions pipeline triggered by PSI drift alarms"),
    (1, "Automated validation gate before promoting models to Production"),
    (0, "Cloud Managed Infrastructure"),
    (1, "Deploy container services to Google Cloud Run"),
    (1, "Migrate metrics storage to managed PostgreSQL / BigQuery"),
], Inches(6.75), Inches(2.15), Inches(6.15), Inches(4.5), size=12)

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 17 — AI USE DISCLOSURE
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=WHITE)
sidebar(s, PURPLE)
header(s, "AI Use Disclosure", "Academic Integrity · AI-Assisted Learning & Development", PURPLE)
footer(s, 17, "DISCLOSURE", PURPLE)
accent_line(s, PURPLE)


# Statement Banner
rect(s, Inches(0.5), Inches(1.6), Inches(12.3), Inches(0.85), fill=LIGHT_GRAY, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.8))
rect(s, Inches(0.5), Inches(1.6), Inches(0.12), Inches(0.85), fill=PURPLE)
tb(s, "AI-Assisted Tool: Google Gemini", Inches(0.8), Inches(1.68), Inches(11.8), Inches(0.3), size=13, bold=True, color=PURPLE)
tb(s, "In completing this project, Google Gemini was utilized as an AI-assisted tool strictly to support the learning process, troubleshoot technical challenges, and ensure high code quality across development stages.",
   Inches(0.8), Inches(1.98), Inches(11.8), Inches(0.4), size=11, color=DARK_GRAY)

# Two-column cards for use cases
col1_items = [
    ("Debugging code errors and tracing complex exceptions", "Assisted in resolving pipeline errors and Docker environment path issues."),
    ("Clarifying NLP concepts and vectorization theory", "Conceptual understanding of TF-IDF, sublinear term weighting, and n-grams."),
    ("Configuring MLflow tracking and Docker Compose", "Guidance on volume mounts, network bridges, and persistent artifact logging."),
    ("Refining visualization and dashboard layouts", "Design suggestions for Streamlit tab hierarchies and Grafana metric gauges."),
]

col2_items = [
    ("FastAPI lifespan handlers and schema validation", "Understanding Pydantic ConfigDict settings and asynchronous server startup."),
    ("Reviewing Grafana SQLite datasource connections", "Verification of table schemas and SQL query syntax for telemetry panels."),
    ("Proofreading documentation and technical phrasing", "Grammar correction and technical clarity across project deliverables."),
    ("General coding best practices and modularization", "Adherence to clean code architecture, error handling, and type hinting."),
]

# Left Column
rect(s, Inches(0.5), Inches(2.65), Inches(6.0), Inches(4.35), fill=WHITE, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.8))
rect(s, Inches(0.5), Inches(2.65), Inches(6.0), Inches(0.4), fill=PURPLE)
tb(s, "Technical & Architecture Support", Inches(0.7), Inches(2.7), Inches(5.6), Inches(0.3), size=12, bold=True, color=WHITE)

for idx, (title, desc) in enumerate(col1_items):
    item_y = Inches(3.2) + idx * Inches(0.92)
    rect(s, Inches(0.7), item_y, Inches(5.6), Inches(0.8), fill=LIGHT_GRAY)
    tb(s, f"✓  {title}", Inches(0.85), item_y + Inches(0.08), Inches(5.3), Inches(0.28), size=11, bold=True, color=NAVY)
    tb(s, desc, Inches(0.85), item_y + Inches(0.38), Inches(5.3), Inches(0.35), size=9.5, color=DARK_GRAY)

# Right Column
rect(s, Inches(6.8), Inches(2.65), Inches(6.0), Inches(4.35), fill=WHITE, line=RGBColor(0xCB,0xD5,0xE1), lw=Pt(0.8))
rect(s, Inches(6.8), Inches(2.65), Inches(6.0), Inches(0.4), fill=PURPLE)
tb(s, "Implementation & Quality Assurance", Inches(7.0), Inches(2.7), Inches(5.6), Inches(0.3), size=12, bold=True, color=WHITE)

for idx, (title, desc) in enumerate(col2_items):
    item_y = Inches(3.2) + idx * Inches(0.92)
    rect(s, Inches(7.0), item_y, Inches(5.6), Inches(0.8), fill=LIGHT_GRAY)
    tb(s, f"✓  {title}", Inches(7.15), item_y + Inches(0.08), Inches(5.3), Inches(0.28), size=11, bold=True, color=NAVY)
    tb(s, desc, Inches(7.15), item_y + Inches(0.38), Inches(5.3), Inches(0.35), size=9.5, color=DARK_GRAY)

# ═════════════════════════════════════════════════════════════════════════════
# SLIDE 18 — THANK YOU / Q&A
# ═════════════════════════════════════════════════════════════════════════════
s = prs.slides.add_slide(blank)
rect(s, 0, 0, SLIDE_W, SLIDE_H, fill=NAVY)
rect(s, SLIDE_W-Inches(3.2), 0, Inches(3.2), SLIDE_H, fill=RGBColor(0x16,0x2B,0x6B))
rect(s, 0, Inches(3.9), SLIDE_W, Inches(0.07), fill=ACCENT)

tb(s, "Thank You", Inches(1.0), Inches(1.2), Inches(10), Inches(1.2), size=58, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
tb(s, "Questions & Discussion", Inches(1.0), Inches(2.45), Inches(10), Inches(0.65), size=26, italic=True, color=ACCENT, align=PP_ALIGN.CENTER)
tb(s, "AG News Topic Classification  ·  End-to-End MLOps Lifecycle Pipeline", Inches(1.0), Inches(4.1), Inches(11), Inches(0.5), size=14, color=RGBColor(0xBF,0xDB,0xFF), align=PP_ALIGN.CENTER)

for i, (lbl, col) in enumerate([("Model Training", A1_COL), ("API Deployment", A2_COL), ("MLOps Monitoring", A3_COL)]):
    bx = Inches(2.3)+i*Inches(2.9)
    rect(s, bx, Inches(4.72), Inches(2.6), Inches(0.45), fill=col)
    tb(s, lbl, bx, Inches(4.75), Inches(2.6), Inches(0.39), size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

tb(s, "Rahime Nacak", Inches(1.0), Inches(5.35), Inches(11), Inches(0.6), size=24, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
tb(s, "420-976-VA  ·  Data Mining Project  ·  Vanier College  ·  Fall 2026", Inches(1.0), Inches(5.98), Inches(11), Inches(0.45), size=14, color=RGBColor(0xBF,0xDB,0xFF), align=PP_ALIGN.CENTER)
tb(s, "October 2026", Inches(1.0), Inches(6.48), Inches(11), Inches(0.4), size=13, italic=True, color=RGBColor(0x93,0xC5,0xFD), align=PP_ALIGN.CENTER)

footer(s, 18)

# ── Save ──────────────────────────────────────────────────────────────────────
out = "/Users/BlankUser/Desktop/A4 presentation/A4_Presentation_Rahime_Nacak.pptx"
prs.save(out)
print(f"✅ Successfully compiled presentation in 100% natural English: {out}")
