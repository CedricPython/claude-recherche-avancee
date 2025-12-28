#!/usr/bin/env python3
"""
Script de generation de PDF a partir de Markdown.
Utilise plusieurs methodes selon les outils disponibles.

Methodes supportees (par ordre de preference):
1. md-to-pdf (Node.js) - Meilleure qualite
2. Pandoc + LaTeX - Tres professionnel
3. markdown + pdfkit (Python) - Solution de secours

Usage:
    python generate_pdf.py <fichier.md> [output.pdf]

Exemple:
    python generate_pdf.py rapport.md
    python generate_pdf.py rapport.md mon_rapport.pdf
"""

import sys
import subprocess
import shutil
from pathlib import Path


def check_command(cmd):
    """Verifie si une commande est disponible."""
    return shutil.which(cmd) is not None


def generate_with_mdpdf(md_path, output_path):
    """Genere un PDF via md-to-pdf (npm)."""
    try:
        # Essayer npx d'abord
        result = subprocess.run(
            ['npx', '--yes', 'md-to-pdf', str(md_path)],
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode == 0:
            # md-to-pdf genere le PDF a cote du fichier source
            generated = md_path.with_suffix('.pdf')
            if generated.exists() and output_path != generated:
                shutil.move(str(generated), str(output_path))
            print(f"PDF cree (md-to-pdf): {output_path}")
            return True
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    except Exception as e:
        print(f"Erreur md-to-pdf: {e}")

    return False


def generate_with_pandoc(md_path, output_path):
    """Genere un PDF via Pandoc."""
    if not check_command('pandoc'):
        return False

    try:
        # Essayer avec xelatex (meilleur support Unicode)
        result = subprocess.run([
            'pandoc', str(md_path),
            '-o', str(output_path),
            '--pdf-engine=xelatex',
            '-V', 'geometry:margin=2.5cm',
            '-V', 'fontsize=11pt',
            '-V', 'mainfont=Arial',
            '--toc',
            '--toc-depth=3'
        ], capture_output=True, text=True, timeout=120)

        if result.returncode == 0 and output_path.exists():
            print(f"PDF cree (pandoc+xelatex): {output_path}")
            return True

        # Fallback: pdflatex
        result = subprocess.run([
            'pandoc', str(md_path),
            '-o', str(output_path),
            '--pdf-engine=pdflatex',
            '-V', 'geometry:margin=2.5cm'
        ], capture_output=True, text=True, timeout=120)

        if result.returncode == 0 and output_path.exists():
            print(f"PDF cree (pandoc+pdflatex): {output_path}")
            return True

    except subprocess.TimeoutExpired:
        print("Timeout: La generation PDF a pris trop de temps.")
    except Exception as e:
        print(f"Erreur Pandoc: {e}")

    return False


def generate_with_wkhtmltopdf(md_path, output_path):
    """Genere un PDF via wkhtmltopdf (convertit d'abord en HTML)."""
    if not check_command('wkhtmltopdf'):
        return False

    try:
        import markdown

        # Lire et convertir en HTML
        md_content = md_path.read_text(encoding='utf-8')
        html_content = markdown.markdown(
            md_content,
            extensions=['tables', 'fenced_code', 'toc']
        )

        # Ajouter du style basique
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ font-family: Arial, sans-serif; margin: 2cm; line-height: 1.6; }}
                h1 {{ color: #333; border-bottom: 2px solid #333; }}
                h2 {{ color: #444; }}
                h3 {{ color: #555; }}
                table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f0f0f0; }}
                code {{ background-color: #f5f5f5; padding: 2px 5px; font-family: Consolas, monospace; }}
                pre {{ background-color: #f5f5f5; padding: 10px; overflow-x: auto; }}
                blockquote {{ border-left: 4px solid #ccc; margin-left: 0; padding-left: 1em; color: #666; }}
            </style>
        </head>
        <body>
        {html_content}
        </body>
        </html>
        """

        # Ecrire le HTML temporaire
        html_path = md_path.with_suffix('.temp.html')
        html_path.write_text(full_html, encoding='utf-8')

        # Convertir en PDF
        result = subprocess.run([
            'wkhtmltopdf',
            '--encoding', 'UTF-8',
            '--margin-top', '20mm',
            '--margin-bottom', '20mm',
            '--margin-left', '20mm',
            '--margin-right', '20mm',
            str(html_path),
            str(output_path)
        ], capture_output=True, text=True, timeout=60)

        # Nettoyer
        html_path.unlink(missing_ok=True)

        if result.returncode == 0 and output_path.exists():
            print(f"PDF cree (wkhtmltopdf): {output_path}")
            return True

    except ImportError:
        print("Module 'markdown' non installe. pip install markdown")
    except Exception as e:
        print(f"Erreur wkhtmltopdf: {e}")

    return False


def generate_with_python(md_path, output_path):
    """Genere un PDF en pure Python avec reportlab ou weasyprint."""

    # Essayer weasyprint
    try:
        from weasyprint import HTML
        import markdown

        md_content = md_path.read_text(encoding='utf-8')
        html_content = markdown.markdown(
            md_content,
            extensions=['tables', 'fenced_code', 'toc']
        )

        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                @page {{ margin: 2cm; }}
                body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
                h1 {{ color: #333; border-bottom: 2px solid #333; }}
                h2 {{ color: #444; }}
                table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; }}
                th {{ background-color: #f0f0f0; }}
                code {{ background-color: #f5f5f5; padding: 2px 5px; }}
                pre {{ background-color: #f5f5f5; padding: 10px; }}
            </style>
        </head>
        <body>{html_content}</body>
        </html>
        """

        HTML(string=full_html).write_pdf(str(output_path))
        print(f"PDF cree (weasyprint): {output_path}")
        return True

    except ImportError:
        pass
    except Exception as e:
        print(f"Erreur weasyprint: {e}")

    return False


def generate_pdf(md_path, output_path=None):
    """Tente de generer un PDF avec les outils disponibles."""
    md_path = Path(md_path)

    if not md_path.exists():
        print(f"Erreur: Le fichier {md_path} n'existe pas.")
        return None

    if output_path is None:
        output_path = md_path.with_suffix('.pdf')
    else:
        output_path = Path(output_path)

    print(f"Generation PDF: {md_path} -> {output_path}")

    # Essayer chaque methode
    methods = [
        ("md-to-pdf", generate_with_mdpdf),
        ("Pandoc", generate_with_pandoc),
        ("wkhtmltopdf", generate_with_wkhtmltopdf),
        ("Python (weasyprint)", generate_with_python),
    ]

    for name, method in methods:
        print(f"Tentative avec {name}...")
        if method(md_path, output_path):
            return str(output_path)

    # Aucune methode n'a fonctionne
    print("\n" + "="*60)
    print("ERREUR: Aucun outil de generation PDF disponible.")
    print("="*60)
    print("\nInstallez l'un des outils suivants:")
    print("\n1. md-to-pdf (recommande, necessite Node.js):")
    print("   npm install -g md-to-pdf")
    print("\n2. Pandoc + LaTeX (professionnel):")
    print("   winget install JohnMacFarlane.Pandoc")
    print("   winget install MiKTeX.MiKTeX")
    print("\n3. wkhtmltopdf:")
    print("   winget install wkhtmltopdf.wkhtmltopdf")
    print("\n4. Python weasyprint:")
    print("   pip install weasyprint markdown")
    print("="*60)

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
