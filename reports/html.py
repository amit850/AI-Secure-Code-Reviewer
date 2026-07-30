from pathlib import Path
from html import escape

def generate_html_report(findings, output_dir):
    report_file = Path(output_dir) / "report.html"
    severity_color={"Critical":"#dc3545","High":"#fd7e14","Medium":"#ffc107","Low":"#198754","Info":"#0dcaf0"}
    critical=sum(1 for f in findings if f.severity=="Critical")
    high=sum(1 for f in findings if f.severity=="High")
    medium=sum(1 for f in findings if f.severity=="Medium")
    low=sum(1 for f in findings if f.severity=="Low")
    info=sum(1 for f in findings if f.severity=="Info")
    html=f"""<!DOCTYPE html><html><head><meta charset='UTF-8'><title>AI Secure Code Reviewer</title><style>
body{{font-family:Arial;background:#f4f4f4;margin:30px}}
.cards{{display:flex;gap:15px;flex-wrap:wrap;margin:20px 0}}
.card{{padding:15px;border-radius:8px;color:#fff;font-weight:bold;min-width:110px}}
table{{width:100%;border-collapse:collapse;background:#fff}}
th{{background:#222;color:#fff;padding:10px}}
td{{padding:10px;border:1px solid #ddd}}
.badge{{padding:4px 8px;border-radius:5px;color:#fff}}
input{{width:100%;padding:12px;margin:15px 0}}
</style></head><body><h1>AI Secure Code Reviewer</h1>
<div class='cards'>
<div class='card' style='background:#343a40'>Total<br>{len(findings)}</div>
<div class='card' style='background:#dc3545'>Critical<br>{critical}</div>
<div class='card' style='background:#fd7e14'>High<br>{high}</div>
<div class='card' style='background:#ffc107;color:black'>Medium<br>{medium}</div>
<div class='card' style='background:#198754'>Low<br>{low}</div>
<div class='card' style='background:#0dcaf0;color:black'>Info<br>{info}</div>
</div>
<input id='search' placeholder='Search findings...' onkeyup='searchTable()'>
<table id='findingsTable'>
<tr><th>Title</th><th>Severity</th><th>File</th><th>Line</th><th>CWE</th><th>Description</th><th>Recommendation</th></tr>"""
    for finding in findings:
        c=severity_color.get(finding.severity,"#6c757d")
        html+=f"<tr><td>{escape(finding.title)}</td><td><span class='badge' style='background:{c}'>{escape(finding.severity)}</span></td><td>{escape(finding.file)}</td><td>{finding.line}</td><td>{escape(finding.cwe)}</td><td>{escape(finding.description)}</td><td>{escape(finding.recommendation)}</td></tr>"
    html+="""</table><script>
function searchTable(){let i=document.getElementById('search').value.toLowerCase();document.querySelectorAll('#findingsTable tr').forEach((r,n)=>{if(n==0)return;r.style.display=r.innerText.toLowerCase().includes(i)?'':'none';});}
</script></body></html>"""
    report_file.write_text(html,encoding="utf-8")
    return report_file
