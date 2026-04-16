"""Generate a printable, one-page exit ticket PDF for the Raisin in the Sun
+ Justice InDeed covenants lesson. Designed for students to fill out and
upload to Canvas."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.enums import TA_LEFT

OUT = "/Users/ryanbot/Desktop/Housing/exit_ticket.pdf"

# Colors matching the web lesson
INK = HexColor("#1a1a1a")
ACCENT = HexColor("#a8311a")
ACCENT_SOFT = HexColor("#f3d9d2")
RULE = HexColor("#d9d2c3")
MUTED = HexColor("#5a5a5a")

PAGE_W, PAGE_H = letter
MARGIN = 0.6 * inch

c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle("Exit Ticket — A Raisin in the Sun & Michigan's Hidden Walls")
c.setAuthor("Housing & Segregation Lesson")

# --- HEADER BAR ---
c.setFillColor(INK)
c.rect(0, PAGE_H - 0.85 * inch, PAGE_W, 0.85 * inch, fill=1, stroke=0)
c.setFillColor(ACCENT)
c.rect(0, PAGE_H - 0.92 * inch, PAGE_W, 0.07 * inch, fill=1, stroke=0)

c.setFillColor(white)
c.setFont("Times-Bold", 16)
c.drawString(MARGIN, PAGE_H - 0.45 * inch, "EXIT TICKET")
c.setFont("Times-Italic", 11)
c.drawString(MARGIN, PAGE_H - 0.68 * inch,
             "A Raisin in the Sun  \u2022  Michigan's Hidden Walls")

# Right side: upload note
c.setFont("Helvetica", 8)
c.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.45 * inch,
                  "Upload to Canvas for participation credit")
c.drawRightString(PAGE_W - MARGIN, PAGE_H - 0.60 * inch,
                  "Dexter Community Schools  \u2022  English / Social Studies")

# --- NAME / DATE / HOUR FIELDS ---
y = PAGE_H - 1.25 * inch
c.setFillColor(INK)
c.setFont("Helvetica-Bold", 9)
c.drawString(MARGIN, y, "NAME")
c.drawString(MARGIN + 3.2 * inch, y, "DATE")
c.drawString(MARGIN + 5.0 * inch, y, "HOUR")

c.setStrokeColor(INK)
c.setLineWidth(0.75)
c.line(MARGIN + 0.5 * inch, y - 2, MARGIN + 3.0 * inch, y - 2)
c.line(MARGIN + 3.2 * inch + 0.4 * inch, y - 2, MARGIN + 4.8 * inch, y - 2)
c.line(MARGIN + 5.0 * inch + 0.45 * inch, y - 2, PAGE_W - MARGIN, y - 2)

# --- SECTION 1: MAP FINDINGS ---
y -= 0.35 * inch
c.setFillColor(ACCENT)
c.setFont("Helvetica-Bold", 10)
c.drawString(MARGIN, y, "1.  WHAT YOU FOUND ON THE MAP")
c.setFillColor(MUTED)
c.setFont("Helvetica-Oblique", 8)
c.drawString(MARGIN, y - 0.15 * inch,
             "Record two covenants from our school district \u2014 try the Ann Arbor Country Club area or Baseline Lake.")

# Table for map findings
y -= 0.30 * inch
col_x = [MARGIN,
         MARGIN + 1.6 * inch,
         MARGIN + 2.5 * inch,
         MARGIN + 4.3 * inch]
col_w = [1.6 * inch, 0.9 * inch, 1.8 * inch, PAGE_W - MARGIN - (MARGIN + 4.3 * inch)]
row_h = 0.42 * inch

# Header row
c.setFillColor(ACCENT_SOFT)
c.rect(MARGIN, y - 0.22 * inch, PAGE_W - 2 * MARGIN, 0.22 * inch, fill=1, stroke=0)
c.setFillColor(INK)
c.setFont("Helvetica-Bold", 8.5)
headers = ["Street / Neighborhood", "Year", "Groups Excluded", "Anything that stood out"]
for i, h in enumerate(headers):
    c.drawString(col_x[i] + 3, y - 0.15 * inch, h)

# Data rows (2 rows)
c.setStrokeColor(RULE)
c.setLineWidth(0.5)
for r in range(2):
    top = y - 0.22 * inch - r * row_h
    bot = top - row_h
    # horizontal rules
    c.line(MARGIN, bot, PAGE_W - MARGIN, bot)
    # vertical rules
    for x in col_x[1:]:
        c.line(x, top, x, bot)
    c.line(MARGIN, top, MARGIN, bot)
    c.line(PAGE_W - MARGIN, top, PAGE_W - MARGIN, bot)
# top rule of table
c.line(MARGIN, y, PAGE_W - MARGIN, y)
c.line(MARGIN, y - 0.22 * inch, PAGE_W - MARGIN, y - 0.22 * inch)

y = y - 0.22 * inch - 2 * row_h

# --- SECTION 2: MAIN PROMPT ---
y -= 0.20 * inch
c.setFillColor(ACCENT)
c.setFont("Helvetica-Bold", 10)
c.drawString(MARGIN, y, "2.  SHORT RESPONSE  (4\u20136 sentences)")

# Prompt box
y -= 0.15 * inch

styles = getSampleStyleSheet()
prompt_style = ParagraphStyle(
    "prompt",
    parent=styles["Normal"],
    fontName="Times-Roman",
    fontSize=10,
    leading=13,
    textColor=INK,
    alignment=TA_LEFT,
)
prompt_text = (
    "<b>Prompt:</b> Lorraine Hansberry set <i>A Raisin in the Sun</i> in Chicago, "
    "not Alabama. Based on today's lesson \u2014 and what you saw on the map "
    "around the <b>Ann Arbor Country Club</b> and <b>Baseline Lake</b> \u2014 "
    "<b>why does that matter?</b> What does the Younger family's struggle reveal "
    "about segregation in the North that a story set in the Deep South might "
    "<i>not</i> show us? <b>Use one specific detail from the covenant map and "
    "one specific moment from the play.</b>"
)
p = Paragraph(prompt_text, prompt_style)
avail_w = PAGE_W - 2 * MARGIN - 16
pw, ph = p.wrapOn(c, avail_w, 2 * inch)
prompt_h = ph + 12  # padding top+bottom

# Draw the box sized to the text
c.setFillColor(ACCENT_SOFT)
c.setStrokeColor(ACCENT)
c.setLineWidth(0.75)
c.rect(MARGIN, y - prompt_h, PAGE_W - 2 * MARGIN, prompt_h, fill=1, stroke=1)

# Draw paragraph inside the box
p.drawOn(c, MARGIN + 8, y - 6 - ph)

y -= prompt_h
y -= 0.12 * inch

# Writing lines (8 lines)
c.setStrokeColor(INK)
c.setLineWidth(0.5)
line_gap = 0.28 * inch
for i in range(8):
    ly = y - i * line_gap
    c.line(MARGIN, ly, PAGE_W - MARGIN, ly)
y = y - 8 * line_gap

# --- SECTION 3: CHALLENGE ---
y -= 0.10 * inch
c.setFillColor(ACCENT)
c.setFont("Helvetica-Bold", 10)
c.drawString(MARGIN, y, "3.  CHALLENGE  (one sentence)")
challenge_style = ParagraphStyle(
    "challenge",
    parent=styles["Normal"],
    fontName="Times-Roman",
    fontSize=9.5,
    leading=12,
    textColor=INK,
    alignment=TA_LEFT,
)
challenge_text = (
    "Covenants in our school district \u2014 at the Country Club, on Baseline Lake \u2014 "
    "are still in the deeds today. Should they be removed, kept as history, or something else?"
)
cp = Paragraph(challenge_text, challenge_style)
cw, ch = cp.wrapOn(c, PAGE_W - 2 * MARGIN, 1 * inch)
cp.drawOn(c, MARGIN, y - 0.05 * inch - ch)
y -= 0.05 * inch + ch + 0.10 * inch
c.setStrokeColor(INK)
c.setLineWidth(0.5)
for i in range(2):
    ly = y - i * line_gap
    c.line(MARGIN, ly, PAGE_W - MARGIN, ly)

# --- FOOTER ---
c.setFillColor(MUTED)
c.setFont("Helvetica-Oblique", 7.5)
c.drawString(MARGIN, 0.35 * inch,
             "Map source: Justice InDeed (University of Michigan)  \u2022  justiceindeedmi.org")
c.drawRightString(PAGE_W - MARGIN, 0.35 * inch,
                  "Submit via Canvas  \u2022  Participation credit")

c.showPage()
c.save()
print(f"Wrote {OUT}")
