#!/usr/bin/env python3
"""
Script de generation de PDF a partir de Markdown.
Version simplifiee utilisant fpdf2 (fonctionne nativement sur Windows).

Usage:
    python generate_pdf_simple.py <fichier.md> [output.pdf]
"""

import sys
import re
from pathlib import Path

try:
    from fpdf import FPDF
except ImportError:
    print("Erreur: fpdf2 n'est pas installe.")
    print("Installation: pip install fpdf2")
    sys.exit(1)


class MarkdownPDF(FPDF):
    """PDF personnalise pour Markdown."""

    def __init__(self):
        super().__init__()
        self.add_page()
        # Police par defaut compatible Unicode
        self.add_font('DejaVu', '', 'C:/Windows/Fonts/arial.ttf')
        self.add_font('DejaVu', 'B', 'C:/Windows/Fonts/arialbd.ttf')
        self.add_font('DejaVu', 'I', 'C:/Windows/Fonts/ariali.ttf')
        self.set_font('DejaVu', '', 11)
        self.set_auto_page_break(True, margin=15)

    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font('DejaVu', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')
        self.set_text_color(0)

    def chapter_title(self, title, level=1):
        """Ajoute un titre."""
        sizes = {1: 18, 2: 15, 3: 13, 4: 12}
        size = sizes.get(level, 11)

        self.set_font('DejaVu', 'B', size)

        if level == 1:
            self.set_text_color(51, 51, 51)
            self.ln(5)
        elif level == 2:
            self.set_text_color(68, 68, 68)
            self.ln(4)
        else:
            self.set_text_color(85, 85, 85)
            self.ln(3)

        self.multi_cell(0, size * 0.5, title)

        if level == 1:
            self.set_draw_color(51, 51, 51)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(3)

        self.set_text_color(0)
        self.set_font('DejaVu', '', 11)
        self.ln(2)

    def body_text(self, text):
        """Ajoute du texte normal."""
        self.set_font('DejaVu', '', 11)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def bullet_point(self, text):
        """Ajoute un point de liste."""
        self.set_font('DejaVu', '', 11)
        self.set_x(15)
        self.multi_cell(0, 6, "- " + text)

    def checkbox(self, text, checked=False):
        """Ajoute une checkbox."""
        self.set_font('DejaVu', '', 11)
        symbol = "[X] " if checked else "[ ] "
        self.set_x(15)
        self.multi_cell(0, 6, symbol + text)

    def add_table(self, rows):
        """Ajoute un tableau."""
        if not rows or len(rows) == 0:
            return

        col_count = len(rows[0])
        col_width = (self.w - 20) / col_count

        self.set_font('DejaVu', 'B', 10)

        # En-tete
        if rows:
            self.set_fill_color(224, 224, 224)
            for cell in rows[0]:
                self.cell(col_width, 8, cell[:30], border=1, fill=True, align='C')
            self.ln()

        # Donnees
        self.set_font('DejaVu', '', 10)
        for row in rows[1:]:
            for cell in row:
                text = cell[:40] if len(cell) > 40 else cell
                self.cell(col_width, 7, text, border=1)
            self.ln()

        self.ln(3)

    def horizontal_rule(self):
        """Ajoute une ligne horizontale."""
        self.ln(3)
        self.set_draw_color(200, 200, 200)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)


def clean_text(text):
    """Nettoie le texte Markdown."""
    # Liens [texte](url) -> texte
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # Gras **texte** -> texte
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    # Italique *texte* -> texte
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    # Code inline `texte` -> texte
    text = re.sub(r'`([^`]+)`', r'\1', text)
    return text.strip()


def parse_and_generate(md_content, pdf):
    """Parse le Markdown et genere le PDF."""
    lines = md_content.split('\n')
    in_code = False
    in_table = False
    table_rows = []
    paragraph = []

    for line in lines:
        # Blocs de code
        if line.strip().startswith('```'):
            if in_code:
                in_code = False
            else:
                if paragraph:
                    pdf.body_text(clean_text(' '.join(paragraph)))
                    paragraph = []
                in_code = True
            continue

        if in_code:
            continue

        # Tableaux
        if line.strip().startswith('|') and '|' in line[1:]:
            if not in_table:
                if paragraph:
                    pdf.body_text(clean_text(' '.join(paragraph)))
                    paragraph = []
                in_table = True

            # Ignorer separateurs
            if not re.match(r'^\|[\s\-:|]+\|$', line.strip()):
                cells = [clean_text(c.strip()) for c in line.strip().split('|')[1:-1]]
                if cells:
                    table_rows.append(cells)
            continue
        elif in_table:
            if table_rows:
                pdf.add_table(table_rows)
            table_rows = []
            in_table = False

        # Ligne horizontale
        if re.match(r'^---+$', line.strip()):
            if paragraph:
                pdf.body_text(clean_text(' '.join(paragraph)))
                paragraph = []
            pdf.horizontal_rule()
            continue

        # Titres
        if line.startswith('# '):
            if paragraph:
                pdf.body_text(clean_text(' '.join(paragraph)))
                paragraph = []
            pdf.chapter_title(line[2:].strip(), level=1)
        elif line.startswith('## '):
            if paragraph:
                pdf.body_text(clean_text(' '.join(paragraph)))
                paragraph = []
            pdf.chapter_title(line[3:].strip(), level=2)
        elif line.startswith('### '):
            if paragraph:
                pdf.body_text(clean_text(' '.join(paragraph)))
                paragraph = []
            pdf.chapter_title(line[4:].strip(), level=3)
        elif line.startswith('#### '):
            if paragraph:
                pdf.body_text(clean_text(' '.join(paragraph)))
                paragraph = []
            pdf.chapter_title(line[5:].strip(), level=4)
        # Listes a puces
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            if paragraph:
                pdf.body_text(clean_text(' '.join(paragraph)))
                paragraph = []
            content = line.strip()[2:]
            if content.startswith('[ ] '):
                pdf.checkbox(clean_text(content[4:]), checked=False)
            elif content.startswith('[x] ') or content.startswith('[X] '):
                pdf.checkbox(clean_text(content[4:]), checked=True)
            else:
                pdf.bullet_point(clean_text(content))
        # Listes numerotees
        elif re.match(r'^\d+\. ', line.strip()):
            if paragraph:
                pdf.body_text(clean_text(' '.join(paragraph)))
                paragraph = []
            text = re.sub(r'^\d+\. ', '', line.strip())
            pdf.bullet_point(clean_text(text))
        # Paragraphes
        elif line.strip():
            paragraph.append(line)
        else:
            if paragraph:
                pdf.body_text(clean_text(' '.join(paragraph)))
                paragraph = []

    # Finaliser
    if paragraph:
        pdf.body_text(clean_text(' '.join(paragraph)))
    if in_table and table_rows:
        pdf.add_table(table_rows)


def generate_pdf(md_path, output_path=None):
    """Genere un PDF a partir d'un fichier Markdown."""
    md_path = Path(md_path)

    if not md_path.exists():
        print(f"Erreur: Le fichier {md_path} n'existe pas.")
        return None

    if output_path is None:
        output_path = md_path.with_suffix('.pdf')
    else:
        output_path = Path(output_path)

    print(f"Generation PDF: {md_path} -> {output_path}")

    try:
        md_content = md_path.read_text(encoding='utf-8')

        pdf = MarkdownPDF()
        parse_and_generate(md_content, pdf)

        pdf.output(str(output_path))
        print(f"PDF cree avec succes: {output_path}")
        return str(output_path)

    except Exception as e:
        print(f"Erreur lors de la generation: {e}")
        import traceback
        traceback.print_exc()
        return None


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    md_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    result = generate_pdf(md_file, output_file)
    if result is None:
        sys.exit(1)


if __name__ == '__main__':
    main()
