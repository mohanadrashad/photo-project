# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:42:51 2019

@author: Administrator
"""

from flask import Flask
from template.show_bp import show_bp
from template.upload_bp import upload_bp
from template.search_bp import search_bp
from template.api_bp import api_bp
app=Flask(__name__)

#blueprint for displaying all photos
app.register_blueprint(show_bp,url_prefix="/show")

#blueprint for uploading photos
app.register_blueprint(upload_bp,url_prefix="/upload")

#blueprint for searching specific image
app.register_blueprint(search_bp,url_prefix="/search")

#blueprint for api 
app.register_blueprint(api_bp,url_prefix="/api")

#Landing page
@app.route("/")
def main():
    return "WELCOME"    
if __name__=='__main__':
    app.run(debug=True)