#!/usr/bin/env python3
import streamlit as st
import github
import hashlib
import os
import base64
import json
import tools
import config


def err(msg: str):
    print(f"Help: set {msg} varialbe")
    raise Exception(f"you forgot to set environvariable {msg}")

def resErr(err: int):
    if err == 429:
        st.error("We had too many upload today, try again later.")
    else:
        st.error(f"there were an error with status code of: {res.status_code}")

if __name__=="__main__":
    token = os.environ.get("TOKEN") if os.environ.get("TOKEN") else err("TOKEN")
    owner = os.environ.get("OWNER") if os.environ.get("OWNER") else err("OWNER")
    repo = os.environ.get("REPO") if os.environ.get("REPO") else err("REPO")
    pages_link = os.environ.get("PAGES") if os.environ.get("PAGES") else err("PAGES")

    st.set_page_config(
    page_title = config.PAGE_TITLE,
    page_icon = config.FAVICON,
    layout = config.LAYOUT,
    initial_sidebar_state = config.INITIAL_SIDEBAR_STATE,
    menu_items = config.MENU_ITEM,
)
    
    tab_file, tab_text, tab_link = st.tabs(["File", "Text", "Link"])
    
    with tab_file:
        fli = st.file_uploader(label="Select File", accept_multiple_files=False, help="file size should be under 100MB")
        
        st.info("Maximum file size is 100MB")
        
        st.divider()
        if fli is not None:
            fli_ext = fli.name
            fli_ext = fli_ext.split('.')[-1]
            fli = fli.getvalue()
            if (len(fli)/(2**20)) < 100:
                fli_name = hashlib.md5(fli).hexdigest() + '.' + fli_ext
                fli = base64.b64encode(fli).decode()
                res = github.upload(token, fli_name, fli, repo, owner, 'files')
                if res.status_code == 201:
                    res = json.loads(res.content)
                    st.success("Done")
                    st.code(res['content']['download_url'])
                elif res.status_code == 422:
                    st.warning("this file was exist before!")
                    st.code(f"https://raw.githubusercontent.com/{owner}/{repo}/master/files/{fli_name}")
                else:
                    resErr(res.status_code)
            else:
                st.error("file size should be under 100MB")
    with tab_text:
        text = st.text_area("Paste your text here", placeholder="write your text here.", height=400)
        if st.button("Upload"):
            fli_name = hashlib.md5(bytes(text, encoding='utf-8')).hexdigest() + ".txt"
            fli = base64.b64encode(bytes(text, encoding='utf-8')).decode()
            res = github.upload(token, fli_name, fli, repo, owner, 'files')
            if res.status_code == 201:
                res = json.loads(res.content)
                st.success("Done")
                st.code(res['content']['download_url'])
            elif res.status_code == 422:
                    st.warning("this file was exist before!")
                    st.code(f"https://raw.githubusercontent.com/{owner}/{repo}/master/files/{fli_name}")
                    st.divider()
            else:
                resErr(res.status_code)
    with tab_link:
        link = st.text_input(label="URL shortner", placeholder="place your URL here to be shorten")
        if st.button("Make it Short"):
            if tools.isValidateLink(link):
                fli_name = tools.chooseName()
                while fli_name in github.getContents(token, repo, owner):
                    fli_name = tools.chooseName()
                fli = base64.b64encode(bytes(tools.makeShort(link), encoding='utf-8')).decode()
                res = github.upload(token, fli_name+".html", fli, repo, owner)
                if res.status_code != 201:
                    resErr(res.status_code)
                res = json.loads(res.content)
                st.code(pages_link+"/"+fli_name)
                st.warning("it may take some minute to deploy the link")
            else:
                st.error("URL is invalid")
#TODO: use os.path.join()
