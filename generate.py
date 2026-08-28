import json

data = [
  {
    "family": "Family 1 — Structure",
    "description": "Identifying the building blocks of an argument without evaluating its validity.",
    "contrast_theme": "Role vs. Main Point",
    "types": [
      {
        "name": "Main Conclusion",
        "task": "Identify the primary claim the author is trying to prove.",
        "stem": "Which one of the following most accurately expresses the main conclusion of the argument?",
        "method": "Find the conclusion. Apply the 'Why Test' (does it support something else, or is it supported?). Watch out for intermediate conclusion traps.",
        "contrast_note": "Focuses on the entire argument's ultimate endpoint."
      },
      {
        "name": "Argument Part",
        "task": "Identify the function of a specific phrase within the argument.",
        "stem": "The claim that [X] plays which one of the following roles in the argument?",
        "method": "Locate the phrase. Ask: 'Does it support something?' and 'Is it supported by something?' Determine content vs. function.",
        "contrast_note": "Focuses on the structural role of a single specific piece, not the overall point."
      }
    ]
  },
  {
    "family": "Family 2 — Patterns & Flaws",
    "description": "Analyzing how an argument is built and where its reasoning breaks down.",
    "contrast_theme": "Description vs. Replication vs. Error",
    "types": [
      {
        "name": "Method of Reasoning",
        "task": "Describe the argumentative strategy used.",
        "stem": "The argument proceeds by...",
        "method": "Abstract the argument's structure. Match the description in the choices to the stimulus.",
        "contrast_note": "Pure description of valid or invalid logic."
      },
      {
        "name": "Flaw",
        "task": "Identify why the reasoning is structurally invalid.",
        "stem": "The reasoning in the argument is most vulnerable to criticism on the grounds that...",
        "method": "Play Devil's Advocate. Ask 'How could the evidence be true while the conclusion is still wrong?' Identify the logical gap.",
        "contrast_note": "Describes an error in logic."
      },
      {
        "name": "Parallel Reasoning",
        "task": "Find an argument with the identical logical structure.",
        "stem": "Which one of the following exhibits a pattern of reasoning most similar to that in the argument above?",
        "method": "Identify the conclusion's force and scope. Match the premises' structure. Verify the logical flow matches exactly.",
        "contrast_note": "Replicates valid logic."
      },
      {
        "name": "Parallel Flaw",
        "task": "Find an argument with the identical structural error.",
        "stem": "The flawed pattern of reasoning in the argument above is most similar to that in which one of the following?",
        "method": "Identify the specific flaw. Find the choice that commits the exact same logical sin.",
        "contrast_note": "Replicates an error in logic."
      }
    ]
  },
  {
    "family": "Family 3 — Argument Impact & Assumptions",
    "description": "Interacting with the logical gap between premises and conclusion.",
    "contrast_theme": "Bridging vs. Breaking vs. Needing",
    "types": [
      {
        "name": "Strengthen",
        "task": "Make the conclusion more likely to be true.",
        "stem": "Which one of the following, if true, most strengthens the argument?",
        "method": "Identify the gap. Find a new fact that helps bridge the gap or rules out an alternate cause.",
        "contrast_note": "Helps the argument, doesn't need to prove it 100%."
      },
      {
        "name": "Weaken",
        "task": "Make the conclusion less likely to be true.",
        "stem": "Which one of the following, if true, most seriously weakens the argument?",
        "method": "Identify the gap. Find a new fact that widens the gap, introduces an alternate cause, or attacks the assumption.",
        "contrast_note": "Hurts the argument, doesn't need to destroy it entirely."
      },
      {
        "name": "Evaluate",
        "task": "Identify a question whose answer would test the argument's validity.",
        "stem": "The answer to which one of the following questions would be most useful to know in evaluating the argument?",
        "method": "Apply the Variance Test: Supply polar opposite answers (e.g., yes/no, high/low) to the choice and see if it both strengthens and weakens.",
        "contrast_note": "Tests the gap's vulnerability."
      },
      {
        "name": "Sufficient Assum.",
        "task": "Provide a premise that fully guarantees the conclusion.",
        "stem": "The conclusion follows logically if which one of the following is assumed?",
        "method": "Identify New/Dangling Terms. Look for an Entry, Middle, or End Gap. Insert the answer and rerun the chain.",
        "contrast_note": "Must guarantee the conclusion (100% proof)."
      },
      {
        "name": "Necessary Assum.",
        "task": "Identify a premise the argument requires to survive.",
        "stem": "Which one of the following is an assumption on which the argument depends?",
        "method": "Look for gaps. Apply the Negation Test: logically negate the choice. If the negated choice destroys the argument, it's correct.",
        "contrast_note": "Required by the conclusion, but doesn't have to prove it."
      }
    ]
  },
  {
    "family": "Family 4 — Principles",
    "description": "Working with general rules applied to specific situations.",
    "contrast_theme": "Creating Rules vs. Following Rules",
    "types": [
      {
        "name": "Principle Strengthen",
        "task": "Find a general rule that helps justify the specific reasoning.",
        "stem": "Which one of the following principles, if valid, most helps to justify the reasoning?",
        "method": "Identify the gap. Find a broad rule that connects the premises to the conclusion.",
        "contrast_note": "Moves from specific gap to general rule."
      },
      {
        "name": "Principle Apply",
        "task": "Apply a given rule to a new specific situation.",
        "stem": "Which one of the following judgments conforms most closely to the principle cited above?",
        "method": "Convert the rule to a strict checklist. A choice must meet all sufficient conditions or fail a necessary one.",
        "contrast_note": "Moves from general rule to specific application."
      },
      {
        "name": "Principle Generalize",
        "task": "Extract a general rule from a specific situation.",
        "stem": "The situation described above most closely conforms to which one of the following generalizations?",
        "method": "Identify the underlying logic or moral of the specific case. Find the abstract rule that matches.",
        "contrast_note": "Moves from specific case to general rule."
      }
    ]
  },
  {
    "family": "Family 5 — Inference",
    "description": "Deriving conclusions based purely on the provided facts.",
    "contrast_theme": "Absolute Truth vs. Strong Support",
    "types": [
      {
        "name": "Must Be True",
        "task": "Identify a statement that is 100% guaranteed by the stimulus.",
        "stem": "If the statements above are true, which one of the following must also be true?",
        "method": "Combine facts strictly. Ask 'Could this possibly be false?' Avoid outside information.",
        "contrast_note": "Requires absolute certainty."
      },
      {
        "name": "Most Strongly Supp.",
        "task": "Identify a statement highly likely to be true based on the stimulus.",
        "stem": "The statements above, if true, most strongly support which one of the following?",
        "method": "Synthesize the facts. Find a safe, reasonable conclusion. Doesn't need formal 100% proof, just 99% safety.",
        "contrast_note": "Allows a tiny margin of doubt compared to MBT."
      },
      {
        "name": "Must Be False",
        "task": "Identify a statement that absolutely contradicts the stimulus.",
        "stem": "If the statements above are true, which one of the following must be false?",
        "method": "Apply the Coexistence Test: can this choice exist in the same universe as the stimulus? If no, it's correct.",
        "contrast_note": "Requires absolute contradiction."
      },
      {
        "name": "Fill in the Blank",
        "task": "Complete the logical thought at the end of the stimulus.",
        "stem": "Which one of the following most logically completes the argument? ... ______.",
        "method": "Read for the direction of the argument. Predict the logical endpoint based on the immediately preceding sentences.",
        "contrast_note": "Contextual inference based on flow."
      }
    ]
  },
  {
    "family": "Family 6 — Paradox / Explain",
    "description": "Resolving apparent contradictions or explaining surprising facts.",
    "contrast_theme": "Bridging the Unexpected",
    "types": [
      {
        "name": "Paradox / Explain",
        "task": "Find a fact that allows two seemingly contradictory statements to both be true.",
        "stem": "Which one of the following, if true, does most to resolve the apparent discrepancy?",
        "method": "Preserve both facts. Find the hidden distinction or bridge that explains how they coexist peacefully.",
        "contrast_note": "Focuses on resolving mystery, not arguing."
      }
    ]
  },
  {
    "family": "Family 7 — Dialogue",
    "description": "Analyzing interactions between two speakers.",
    "contrast_theme": "Point of Contention vs. Common Ground",
    "types": [
      {
        "name": "Disagree",
        "task": "Identify the exact statement both speakers have an opinion on, and disagree about.",
        "stem": "The dialogue provides the most support for the claim that X and Y disagree over whether...",
        "method": "Apply the Speaker-by-Speaker Commitment Test. Speaker 1 must say yes/no, and Speaker 2 must say the exact opposite.",
        "contrast_note": "Focuses on explicit conflict."
      },
      {
        "name": "Agree",
        "task": "Identify a statement both speakers would endorse.",
        "stem": "The dialogue provides the most support for the claim that X and Y agree that...",
        "method": "Apply the Speaker-by-Speaker Commitment Test. Both speakers must be committed to the exact same position.",
        "contrast_note": "Focuses on shared assumptions or explicit agreement."
      }
    ]
  }
]

def render_scaffold(content, extra_css=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LR Question Type Map - Level 4B</title>
<style>
  :root{{
    --denim:#344E73;
    --slate:#425C81;
    --haze:#556E91;
    --gold:#C9A149;
    --ochre:#9F7633;
    --petal:#7F501D;
    --soft-white:#F8F9F9;
    --canvas:#F7F8FA;
    --deep-ink:#0A1625;
    --body-ink:#26313F;
    --line:#DDE3EA;
    --paper:#FFFFFF;

    --page-w:10in;
    --page-h:8in;
    --safe-x:0.68in;
    --safe-y:0.56in;
  }}

  *{{box-sizing:border-box}}
  html,body{{margin:0;padding:0}}

  body{{
    background:#E8EDF2;
    color:var(--body-ink);
    font-family:"Inter", Helvetica, Arial, sans-serif;
  }}

  .export-toolbar{{
    position:sticky;
    top:0;
    z-index:50;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:16px;
    padding:10px 18px;
    background:var(--deep-ink);
    color:var(--soft-white);
    font-size:13px;
  }}
  .export-toolbar button{{
    border:0; border-bottom:3px solid var(--gold); border-radius:999px;
    padding:9px 15px; background:var(--denim); color:white;
    font:700 12px/1 "Inter", Helvetica, Arial, sans-serif;
    letter-spacing:.08em; text-transform:uppercase; cursor:pointer;
  }}

  .document{{ width:max-content; margin:28px auto 56px; }}

  .pdf-page{{
    position:relative; width:var(--page-w); height:var(--page-h);
    margin:0 auto 24px; overflow:hidden; background:var(--paper);
    box-shadow:0 14px 36px rgba(10,22,37,.15);
    break-after:page; page-break-after:always;
  }}

  .has-bloom::before{{
    content:""; position:absolute; inset:0; pointer-events:none;
    background: radial-gradient(circle at 8% 92%, rgba(127,80,29,.16) 0%, rgba(159,118,51,.13) 14%, rgba(201,161,73,.11) 28%, rgba(85,110,145,.07) 43%, transparent 62%);
  }}

  .pdf-page-content{{
    position:absolute; inset:var(--safe-y) var(--safe-x) 0.68in; overflow:hidden;
  }}

  .pdf-page-footer{{
    position:absolute; left:var(--safe-x); right:var(--safe-x); bottom:0.24in;
    display:flex; justify-content:space-between; align-items:center;
    padding-top:0.09in; border-top:1px solid var(--line);
    color:var(--haze); font-size:9pt;
  }}

  .eyebrow{{
    margin:0 0 10px; color:var(--ochre);
    font:700 9pt/1.2 "Outfit","Inter",sans-serif;
    letter-spacing:.18em; text-transform:uppercase;
  }}

  h1,h2,h3{{ color:var(--deep-ink); font-family:"Fraunces", Georgia, serif; font-weight:normal; }}
  h1{{ margin:0 0 12px; font-size:31pt; line-height:1.02; letter-spacing:-.02em; }}
  h1 em,h2 em,h3 em{{ color:var(--gold); font-style:italic; }}

  .lede{{ margin:0; color:var(--body-ink); font-size:13.5pt; line-height:1.55; }}
  .gold-rule{{ width:2.4in; height:3px; margin:0.22in 0 0.28in; background:linear-gradient(90deg,var(--gold),transparent); }}

  .label{{
    display:block; margin-bottom:0.08in; color:var(--denim);
    font:700 8pt/1.2 "Outfit","Inter",sans-serif; letter-spacing:.16em; text-transform:uppercase;
  }}

  @page{{ size:10in 8in; margin:0; }}
  @media print{{
    html,body{{ width:10in; margin:0 !important; padding:0 !important; background:#fff !important; }}
    .export-toolbar{{ display:none !important; }}
    .document{{ width:auto; margin:0; }}
    .pdf-page{{ width:10in; height:8in; margin:0; box-shadow:none; break-after:page; page-break-after:always; print-color-adjust:exact; -webkit-print-color-adjust:exact; }}
  }}
  {extra_css}
</style>
</head>
<body>
<div class="export-toolbar">
  <strong>Level 4B — Family Contrast Map</strong>
  <button type="button" onclick="window.print()">Print / Save as PDF</button>
</div>
<main class="document">
{content}
</main>
</body>
</html>"""

def make_variant1():
    # Vertical Matrix Layout
    css = """
    .grid-matrix { display:flex; gap:0.18in; height:5in; margin-top:0.2in; }
    .col-type { flex:1; display:flex; flex-direction:column; border:1px solid var(--line); border-radius:12px; overflow:hidden; background:var(--canvas); }
    .col-header { background:var(--denim); color:white; padding:0.15in; text-align:center; }
    .col-header h3 { color:white; margin:0; font-size:14pt; }
    .col-body { padding:0.15in; display:flex; flex-direction:column; gap:0.12in; flex:1; }
    .sec-block { border-bottom:1px solid var(--line); padding-bottom:0.1in; }
    .sec-block:last-child { border:none; }
    .sec-title { font:700 7.5pt/1.2 "Outfit","Inter",sans-serif; color:var(--haze); text-transform:uppercase; letter-spacing:0.1em; margin-bottom:4px; }
    .sec-content { font-size:9pt; line-height:1.4; color:var(--body-ink); }
    .contrast-banner { background:var(--soft-white); padding:0.1in; border-left:4px solid var(--gold); margin-bottom:0.1in; }
    .contrast-banner h2 { margin:0; font-size:16pt; color:var(--deep-ink); }
    .contrast-highlight { color:var(--petal); font-weight:bold; }
    .stem-text { font-style:italic; color:var(--slate); font-size:8.5pt; }
    .method-text { font-size:8.5pt; line-height:1.4; }
    """

    html = ""
    # Cover page
    html += f"""
    <section class="pdf-page has-bloom">
      <div class="pdf-page-content">
        <p class="eyebrow">Level 4B · Variant 1</p>
        <h1>Family Contrast Map: <em>Vertical Matrix</em></h1>
        <div class="gold-rule"></div>
        <p class="lede">A highly structured, side-by-side comparative layout. Each family is represented as a matrix of columns, allowing direct horizontal juxtaposition of the defining traits, methods, and specific structural differences.</p>
      </div>
      <footer class="pdf-page-footer"><span>Variant 1</span><span>Cover</span></footer>
    </section>
    """

    for i, fam in enumerate(data):
        # We need to handle cases where there are more than 3 types, they might not fit in one page nicely.
        # But we have up to 5 types in a family (e.g., Family 3). 5 columns might be tight.
        types_html = ""
        for t in fam["types"]:
            types_html += f"""
            <div class="col-type">
              <div class="col-header"><h3>{t['name']}</h3></div>
              <div class="col-body">
                <div class="sec-block">
                  <div class="sec-title">The Task</div>
                  <div class="sec-content">{t['task']}</div>
                </div>
                <div class="sec-block">
                  <div class="sec-title">Key Contrast</div>
                  <div class="sec-content contrast-highlight">{t['contrast_note']}</div>
                </div>
                <div class="sec-block">
                  <div class="sec-title">Stem Example</div>
                  <div class="sec-content stem-text">"{t['stem']}"</div>
                </div>
                <div class="sec-block">
                  <div class="sec-title">The Method</div>
                  <div class="sec-content method-text">{t['method']}</div>
                </div>
              </div>
            </div>
            """

        html += f"""
        <section class="pdf-page">
          <div class="pdf-page-content">
            <p class="eyebrow">{fam['family']}</p>
            <div class="contrast-banner">
              <div class="label">Central Contrast Theme</div>
              <h2>{fam['contrast_theme']}</h2>
              <p style="margin:6px 0 0; font-size:10pt;">{fam['description']}</p>
            </div>
            <div class="grid-matrix">
              {types_html}
            </div>
          </div>
          <footer class="pdf-page-footer"><span>Variant 1</span><span>{i+1}</span></footer>
        </section>
        """

    return render_scaffold(html, css)

def make_variant2():
    # Diverging Path / Horizontal Bands with "VS" separators
    css = """
    .band-layout { display:flex; flex-direction:column; gap:0.1in; margin-top:0.15in; height: 5.5in;}
    .band { display:flex; background:var(--canvas); border-left:4px solid var(--denim); border-radius:0 8px 8px 0; padding:0.15in; gap:0.2in; align-items:center; }
    .band-title { flex:0 0 1.5in; }
    .band-title h3 { margin:0 0 4px; font-size:16pt; color:var(--deep-ink); }
    .band-title .task { font-size:8.5pt; color:var(--haze); line-height:1.3; }
    .band-contrast { flex:0 0 1.5in; background:white; padding:0.1in; border:1px solid var(--line); border-radius:6px; font-size:9pt; font-weight:bold; color:var(--ochre); text-align:center; }
    .band-details { flex:1; display:flex; flex-direction:column; gap:0.08in; }
    .band-details .stem { font-style:italic; color:var(--slate); font-size:9pt; }
    .band-details .method { font-size:9pt; line-height:1.4; color:var(--body-ink); }
    .vs-marker { text-align:center; color:var(--gold); font-family:"Fraunces", serif; font-size:14pt; font-style:italic; margin: -0.05in 0; z-index:2; position:relative; }

    .header-zone { display:flex; justify-content:space-between; align-items:flex-end; border-bottom:2px solid var(--gold); padding-bottom:0.1in; margin-bottom:0.1in; }
    .header-zone h1 { margin:0; font-size:26pt; }
    .header-zone .theme { text-align:right; max-width: 3in; }
    .header-zone .theme-title { font-weight:bold; color:var(--denim); text-transform:uppercase; font-size:9pt; letter-spacing:0.1em; }
    .header-zone .theme-desc { font-size:10pt; color:var(--haze); margin-top:4px; }
    """

    html = ""
    # Cover page
    html += f"""
    <section class="pdf-page has-bloom">
      <div class="pdf-page-content">
        <p class="eyebrow">Level 4B · Variant 2</p>
        <h1>Family Contrast Map: <em>Horizontal Bands</em></h1>
        <div class="gold-rule"></div>
        <p class="lede">A horizontal, sequence-driven layout. Question types are stacked in expansive bands, separated by clear 'vs.' markers that emphasize their distinct roles within the family ecosystem.</p>
      </div>
      <footer class="pdf-page-footer"><span>Variant 2</span><span>Cover</span></footer>
    </section>
    """

    for i, fam in enumerate(data):
        # We need to split if types > 3, or maybe they just fit?
        # A band is 0.15in padding top/bot + content. Roughly 0.7-1in each.
        # With 5 items (Family 3), it might exceed the page height. Let's do a quick paginator if types > 3.
        # Family 3 has 5. We can split into 3 and 2.

        type_chunks = [fam["types"][x:x+3] for x in range(0, len(fam["types"]), 3)]

        for chunk_idx, chunk in enumerate(type_chunks):
            bands_html = ""
            for j, t in enumerate(chunk):
                if j > 0 or chunk_idx > 0 and j == 0 and len(type_chunks)>1 and j!=0:
                    bands_html += f'<div class="vs-marker">versus</div>'
                elif chunk_idx > 0 and j == 0:
                    # Previous page ended, next page starts
                    pass

                bands_html += f"""
                <div class="band">
                  <div class="band-title">
                    <h3>{t['name']}</h3>
                    <div class="task">{t['task']}</div>
                  </div>
                  <div class="band-contrast">{t['contrast_note']}</div>
                  <div class="band-details">
                    <div class="stem">Stem: "{t['stem']}"</div>
                    <div class="method">Method: {t['method']}</div>
                  </div>
                </div>
                """

            page_suffix = f" (Part {chunk_idx+1})" if len(type_chunks) > 1 else ""

            html += f"""
            <section class="pdf-page">
              <div class="pdf-page-content">
                <div class="header-zone">
                  <div>
                    <p class="eyebrow">{fam['family']}{page_suffix}</p>
                    <h1>{fam['family'].split('—')[1].strip() if '—' in fam['family'] else fam['family']}</h1>
                  </div>
                  <div class="theme">
                    <div class="theme-title">{fam['contrast_theme']}</div>
                    <div class="theme-desc">{fam['description']}</div>
                  </div>
                </div>
                <div class="band-layout">
                  {bands_html}
                </div>
              </div>
              <footer class="pdf-page-footer"><span>Variant 2</span><span>{i+1}{chr(97+chunk_idx) if len(type_chunks)>1 else ''}</span></footer>
            </section>
            """

    return render_scaffold(html, css)

def make_variant3():
    # Editorial Deep-Dive Spreads
    css = """
    .spread-layout { display:flex; gap:0.4in; height:6.2in; margin-top:0.2in; }
    .sidebar { flex:0 0 2.2in; }
    .main-content { flex:1; display:flex; flex-direction:column; gap:0.2in; }

    .family-meta { margin-bottom:0.3in; }
    .family-meta h1 { font-size:28pt; line-height:1.1; margin:0 0 0.1in; }
    .family-desc { font-size:11pt; line-height:1.5; color:var(--body-ink); margin-bottom:0.2in; }

    .theme-box { background:var(--canvas); padding:0.15in; border:1px solid var(--line); border-radius:8px; }
    .theme-box h4 { margin:0 0 0.05in; color:var(--ochre); font-size:9pt; text-transform:uppercase; letter-spacing:0.1em; }
    .theme-box p { margin:0; font-family:"Fraunces",serif; font-size:14pt; color:var(--deep-ink); line-height:1.2; }

    .type-card { border-top:1px solid var(--gold); padding-top:0.15in; }
    .type-header { display:flex; justify-content:space-between; align-items:baseline; margin-bottom:0.1in; }
    .type-header h2 { margin:0; font-size:18pt; color:var(--denim); }
    .type-contrast { font:700 8.5pt/1 "Outfit",sans-serif; color:var(--petal); text-transform:uppercase; letter-spacing:0.05em; background:var(--soft-white); padding:4px 8px; border-radius:4px; }

    .type-body { display:grid; grid-template-columns:1fr 1fr; gap:0.2in; }
    .type-col h5 { margin:0 0 0.05in; color:var(--slate); font:700 7.5pt/1 "Outfit",sans-serif; text-transform:uppercase; letter-spacing:0.1em; }
    .type-col p { margin:0; font-size:9.5pt; line-height:1.5; color:var(--body-ink); }
    .stem-quote { font-style:italic; border-left:2px solid var(--haze); padding-left:0.1in; margin:0.05in 0 !important; color:var(--slate) !important; }
    """

    html = ""
    # Cover page
    html += f"""
    <section class="pdf-page has-bloom">
      <div class="pdf-page-content">
        <p class="eyebrow">Level 4B · Variant 3</p>
        <h1>Family Contrast Map: <em>Editorial Spreads</em></h1>
        <div class="gold-rule"></div>
        <p class="lede">A spacious, academic reading layout. Embraces generative whitespace, placing the macro-family contrast in a dedicated sidebar while giving each question type an elegant, text-focused deep dive in the main column.</p>
      </div>
      <footer class="pdf-page-footer"><span>Variant 3</span><span>Cover</span></footer>
    </section>
    """

    for i, fam in enumerate(data):
        type_chunks = [fam["types"][x:x+2] for x in range(0, len(fam["types"]), 2)]

        for chunk_idx, chunk in enumerate(type_chunks):
            types_html = ""
            for t in chunk:
                types_html += f"""
                <div class="type-card">
                  <div class="type-header">
                    <h2>{t['name']}</h2>
                    <div class="type-contrast">{t['contrast_note']}</div>
                  </div>
                  <div class="type-body">
                    <div class="type-col">
                      <h5>The Task</h5>
                      <p>{t['task']}</p>
                      <h5 style="margin-top:0.1in">Example Stem</h5>
                      <p class="stem-quote">"{t['stem']}"</p>
                    </div>
                    <div class="type-col">
                      <h5>The Method</h5>
                      <p>{t['method']}</p>
                    </div>
                  </div>
                </div>
                """

            page_suffix = f" (Part {chunk_idx+1})" if len(type_chunks) > 1 else ""

            html += f"""
            <section class="pdf-page">
              <div class="pdf-page-content">
                <div class="spread-layout">
                  <div class="sidebar">
                    <div class="family-meta">
                      <p class="eyebrow">{fam['family'].split('—')[0].strip()}{page_suffix}</p>
                      <h1>{fam['family'].split('—')[1].strip() if '—' in fam['family'] else fam['family']}</h1>
                      <p class="family-desc">{fam['description']}</p>
                    </div>
                    <div class="theme-box">
                      <h4>Core Contrast</h4>
                      <p>{fam['contrast_theme']}</p>
                    </div>
                  </div>
                  <div class="main-content">
                    {types_html}
                  </div>
                </div>
              </div>
              <footer class="pdf-page-footer"><span>Variant 3</span><span>{i+1}{chr(97+chunk_idx) if len(type_chunks)>1 else ''}</span></footer>
            </section>
            """

    return render_scaffold(html, css)

with open("variant1.html", "w") as f:
    f.write(make_variant1())
with open("variant2.html", "w") as f:
    f.write(make_variant2())
with open("variant3.html", "w") as f:
    f.write(make_variant3())

print("HTML files generated successfully.")
