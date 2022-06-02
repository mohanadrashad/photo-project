from flask import Blueprint
from UseSqlite import RiskQuery
from PIL import Image

show_bp= Blueprint("show_bp", __name__,static_folder="static",template_folder="template")
def make_html_paragraph(s):
    if s.strip()=='':
        return ''
    lst=s.split(',')
    picture_path=lst[2].strip()
    picture_name=lst[3].strip()
    im = Image.open(picture_path)
    im.thumbnail((400, 300))
    im.save('./static/figure/'+picture_name, 'jpeg')
    result='<p>'
    result+='<i>%s</i><br/>'%(lst[0])
    result+='<i>%s</i><br/>'%(lst[1])
    result+='<a href="%s"><img src="../static/figure/%s"alt="风景图"></a>'%(picture_path,picture_name)
    return result+'</p>'

#Code to Fetch photos
def get_database_photos():
    rq=RiskQuery('./static/RiskDB.db')
    rq.instructions("SELECT * FROM photo ORDER By time desc")
    rq.do()
    record='<p>My past photo</p>'
    for r in rq.format_results().split('\n\n'):
        record+='%s'%(make_html_paragraph(r))
    return record+'</table>\n'

@show_bp.route("")
def show():
    return get_database_photos()
