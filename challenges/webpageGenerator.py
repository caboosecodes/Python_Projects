

import webbrowser

f = open("sale.html", "w")
f.write(" \
    <html>\
        <body>\
            <h1>\
        Stay tuned for our Amazing summer sale!\
            </h1>\
        </body>\
    </html>\
    ")
f.close()

webbrowser.open_new_tab("sale.html")
