from flask import Blueprint, request, make_response,jsonify
from UseSqlite import RiskQuery
from PIL import Image
import os


api_bp= Blueprint("api_bp", __name__,static_folder="static",template_folder="template")

#Code to send Json file details of all photos
def get_database_photos():
    rq=RiskQuery('./static/RiskDB.db')
    rq.instructions("SELECT * FROM photo ")
    rq.do()
    rows=rq.fetcher()
    output=[]
    for row in rows:
        size = os.path.getsize(row[2])
        output.append({"Photo ID":row[3].rstrip(row[3][-1]),"data of upload":row[0],"photo size":str(size)+" bytes","photo description":row[1]})
    return output
    

@api_bp.route("/json")
def show():
    return make_response(jsonify(get_database_photos()),200)