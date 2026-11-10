"""Run within your portfolio repository to apply the JavaScript lab changes."""
from pathlib import Path
import shutil

root = Path.cwd()
source = Path(__file__).resolve().parent
html_path = root / 'index.html'
css_path = root / 'style.css'
if not html_path.is_file() or not css_path.is_file():
    raise SystemExit('Run this script from the folder containing your portfolio index.html and style.css')
html = html_path.read_text(encoding='utf-8')
css = css_path.read_text(encoding='utf-8')

script_tag = '  <script src="https://cdn.jsdelivr.net/npm/scrollreveal@4.0.9/dist/scrollreveal.min.js" defer></script>\n  <script src="site.js" defer></script>'
if 'src="site.js"' not in html:
    needle = '  <link rel="stylesheet" href="style.css">'
    if needle not in html: raise SystemExit('Could not locate the existing stylesheet in index.html')
    html = html.replace(needle, needle + '\n' + script_tag, 1)
if 'id="theme-toggle"' not in html:
    needle = '    </nav>\n  </header>'
    addition = '''    </nav>
    <button type="button" id="theme-toggle" aria-label="Switch to dark mode" aria-pressed="false">
      <span id="theme-icon" aria-hidden="true">☾</span>
      <span id="theme-label">Dark mode</span>
    </button>
  </header>'''
    if needle not in html: raise SystemExit('Could not locate the header navigation closing tags')
    html = html.replace(needle, addition, 1)

if '--project-surface:' not in css:
    css = css.replace('    --standard-gap: 24px;', '''    --standard-gap: 24px;
    --project-surface: #f9fbfa;
    --header-background: #18453b;
    --header-border: #0f3129;
    --footer-background: #0f3129;
    --image-border: #ffffff;''', 1)
    css = css.replace('    background-color: var(--accent);\n    color: white;\n    padding: 24px;', '    background-color: var(--header-background);\n    color: white;\n    padding: 24px;', 1)
    css = css.replace('    border-bottom: 5px solid var(--accent-dark);', '    border-bottom: 5px solid var(--header-border);', 1)
    css = css.replace('    border: 5px solid white;', '    border: 5px solid var(--image-border);', 1)
    css = css.replace('    background-color: #f9fbfa;', '    background-color: var(--project-surface);', 1)
    css = css.replace('    background-color: var(--accent-dark);\n    color: white;\n    text-align: center;', '    background-color: var(--footer-background);\n    color: white;\n    text-align: center;', 1)
if '/* JavaScript lab: inverse color palette */' not in css:
    css += '\n' + (source / 'theme-additions.css').read_text(encoding='utf-8')
for path in [html_path, css_path]:
    backup = path.with_suffix(path.suffix + '.before-js-lab.bak')
    if not backup.exists(): shutil.copy2(path, backup)
html_path.write_text(html, encoding='utf-8')
css_path.write_text(css, encoding='utf-8')
shutil.copy2(source / 'site.js', root / 'site.js')
print('Updated index.html and style.css, and created site.js.')
print('Backups saved as *.before-js-lab.bak. Review changes before committing.')
