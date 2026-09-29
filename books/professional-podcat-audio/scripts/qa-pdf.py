from pathlib import Path
import pypdfium2 as pdfium
from PIL import Image,ImageDraw,ImageFont
from pypdf import PdfReader
root=Path(__file__).resolve().parents[1];pdf=root/'dist/professional-podcat-audio.pdf';out=root/'build/qa'
out.mkdir(parents=True,exist_ok=True)
doc=pdfium.PdfDocument(pdf); reader=PdfReader(pdf)
for i,page in enumerate(doc):
 im=page.render(scale=1.6).to_pil().convert('RGB');im.save(out/f'page-{i+1:02}.png')
for start in range(0,len(doc),8):
 sheet=Image.new('RGB',(1680,1240),'#bfc7cc');d=ImageDraw.Draw(sheet)
 for k,i in enumerate(range(start,min(start+8,len(doc)))):
  im=Image.open(out/f'page-{i+1:02}.png');im.thumbnail((400,574));x=(k%4)*420+10;y=(k//4)*620+30;sheet.paste(im,(x,y));d.text((x,y-20),f'PAGE {i+1}',fill='black')
 sheet.save(out/f'contact-{start//8+1}.jpg')
report=[]
for i,p in enumerate(reader.pages):
 t=p.extract_text() or ''; report.append(f'{i+1:02} {len(t):5} chars {t[:85].replace(chr(10)," / ")}')
(out/'page-text-summary.txt').write_text('\n'.join(report)+'\n')
print(f'Rendered {len(doc)} pages; {((len(doc)+7)//8)} contact sheets')
