import os, json

def push(code, data):
    os.system("./push " + code + " \'" + json.dumps(data) + "\'")

def push_note(code, title, body):
    push(code, {"type": "note", "title": title, "body": body})
    
def push_link(code, title, body, url):
    if not url.startswith("http"):
        url = "http://" + url
    push(code, {"type": "link", "title": title, "body": body, "url": url})

def push_list(code, title, items):
    push(code, {"type": "list", "title": title, "items": items})