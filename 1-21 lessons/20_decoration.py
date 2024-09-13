import webbrowser

def validator(func):   # принимает функцию "open_url(url)"
    def wrapper(url):  # разделяет open_url() и url
        if "." in url: 
            func(url)
        else:
            print("Incorrect url")
    return wrapper


@validator
def open_url(url):
    webbrowser.open(url)
open_url("https://itproger.com")

