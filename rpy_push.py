import os, json

def push(code, data):
    os.system("./push " + code + " \'" + data + "\'")

def push_note(code, title, body):
    jason = {"type": "note", "title": title, "body": body}
    push(code, json.dumps(jason))
    
def push_link(code, title, body, url):
    if not url.startswith("http"):
        url = "http://" + url
    jason = {"type": "link", "title": title, "body": body, "url": url}
    push(code, json.dumps(jason))

def push_list(code, title, items):
    jason = {"type": "list", "title": title, "items": items}
    push(code, json.dumps(jason))