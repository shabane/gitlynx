    #!/usr/bin/env python3
import streamlit as st
import github
import hashlib
import os
import base64
import json


def err(msg: str):
    print(f"Help: set {msg} varialbe")
    raise("you forgot to set environvariable")

if __name__=="__main__":
    token = os.environ.get("TOKEN") if os.environ.get("TOKEN") else err("TOKEN")
    owner = os.environ.get("OWNER") if os.environ.get("OWNER") else err("OWNER")
    repo = os.environ.get("REPO") if os.environ.get("REPO") else err("REPO")
    
    tab_file, tab_text = st.tabs(["File", "Text"])
    
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
                res = github.upload(token, fli_name, fli, repo, owner)
                if res.status_code == 201:
                    res = json.loads(res.content)
                    st.success("Done")
                    st.code(res['content']['download_url'])
                elif res.status_code == 429:
                    st.error("We had too many upload today, try again later.")
                elif res.status_code == 422:
                    st.warning("this file was exist before!")
                    st.code(f"https://raw.githubusercontent.com/{owner}/{repo}/master/{fli_name}")
                else:
                    st.error(f"there were an error with status code of: {res.status_code}")
            else:
                st.error("file size should be under 100MB")
    with tab_text:
        st.info("i will do it :)")
        # TODO: craete this tab to place plain text on github
