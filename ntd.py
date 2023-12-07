import tkinter as tk
import xml.etree.ElementTree as ET
from tkinter import *

root = ET.Element("article")
contrib_group= ET.SubElement(root, "contrib-group")
form_author= ET.SubElement(contrib_group, "contrib")
name_author = ET.SubElement(form_author, "name")
author_givennames=[]
author_surnames=[]
author_orcids=[]
author_emails=[]
numbers=[]
class Author:
    def check_user():
        number=author_number.get()
        if number in numbers:
            return Author.add_author
        else:
            return Author.add_new_author
        

    def add_new_author():
        form_author= ET.SubElement(contrib_group, "contrib")
        name_author = ET.SubElement(form_author, "name")

        givenname = given_name_entry.get()
        surname = surname_entry.get()
        form=author_form.get()
        lang = author_lang.get()
        selected_form = author_form.get()
        form_author.set("contrib-type", selected_form)
        if givenname and surname and form and lang:
            selected_form = author_form.get()
            form_author.set("contrib-type", selected_form)

            author_givenname = ET.SubElement(name_author, "given-names", attrib={"xml:lang": lang})
            author_givenname.text=givenname
            author_givennames.append(author_givenname)
            given_name_entry.delete(0, "end")

            author_surname = ET.SubElement(name_author, "surname", attrib={"xml:lang": lang})
            author_surname.text= surname
            author_surnames.append(author_surname)
            surname_entry.delete(0, "end")      

    def add_author():
        givenname = given_name_entry.get()
        surname = surname_entry.get()
        form=author_form.get()
        lang = author_lang.get()
        if givenname and surname and form and lang :
            selected_form = author_form.get()
            form_author.set("contrib-type", selected_form)

            author_givenname = ET.SubElement(name_author, "given-names", attrib={"xml:lang": lang})
            author_givenname.text=givenname
            author_givennames.append(author_givenname)
            given_name_entry.delete(0, "end")

            author_surname = ET.SubElement(name_author, "surname", attrib={"xml:lang": lang})
            author_surname.text= surname
            author_surnames.append(author_surname)
            surname_entry.delete(0, "end")

def add_email():
    email=email_entry.get()
    if email:
        selected_form = author_form.get()
        form_author.set("contrib-type", selected_form)

        author_email= ET. SubElement(form_author, "email")
        author_email.text=email
        author_emails.append(author_email)
        email_entry.delete(0, "end")

def add_orcid():
    orcid=orcid_id_entry.get()
    if orcid:
        selected_form = author_form.get()
        form_author.set("contrib-type", selected_form)

        author_orcid = ET.SubElement(form_author, "xref", attrib={"ref-type":"orcid", "rid":orcid})
        author_orcid.text=author_orcid
        author_orcids.append(author_orcid)
        orcid_id_entry.delete(0,"end")
#    else:
#        form_author= ET.SubElement(contrib_group, "contrib")
#        name_author = ET.SubElement(form_author, "name")
#
#        givenname = given_name_entry.get()
#        surname = surname_entry.get()
#        orcid=orcid_id_entry.get()
#        email=email_entry.get()
#        form=author_form.get()
#        lang = author_lang.get()
#
#        if (givenname and surname) or orcid and email and form and lang:
#            selected_form = author_form.get()
#
#            # Set the xml:lang attribute in the article tag
#            form_author.set("contrib-type", selected_form)
#        
#            author_givenname = ET.SubElement(name_author, "given-names", attrib={"xml:lang": lang})
#            author_givenname.text=givenname
#            author_givennames.append(author_givenname)
#            given_name_entry.delete(0, "end")
#
#            author_surname = ET.SubElement(name_author, "surname", attrib={"xml:lang": lang}, )
#            author_surname.text= surname
#            author_surnames.append(author_surname)
#            surname_entry.delete(0, "end")
#
#            author_email= ET. SubElement(form_author, "email")
#            author_email.text=email
#            author_emails.append(author_email)
#            email_entry.delete(0, "end")
#
#            author_orcid = ET.SubElement(form_author, "xref", attrib={"ref-type":"orcid", "rid":orcid})
#            numbers.append(number)
def generate_jats_xml():
    jats_xml = ET.tostring(root, encoding="unicode")
    output_text.delete("1.0", "end")
    output_text.insert("1.0", jats_xml)

window = tk.Tk()
window.title("JATS XML Generator")
window.geometry('1900x1000')

#=============
author_form_label=tk.Label(window, text="Select:")
author_form_label.pack()

author_form=tk.StringVar()
author_form.set("corresponding-author")
author_form_menu=tk.OptionMenu(window,author_form, "corresponding-author", "author")
author_form_menu.pack()

author_number_label = tk.Label(window, text="Number")
author_number_label.pack()
author_number_entry=tk.Entry(window)
author_number_entry.pack()


author_lang = tk.StringVar()
author_lang.set("en")
author_lang_menu=tk.OptionMenu(window,author_lang, "az", "en", "ru", "tr", "ar", "fa")
author_lang_menu.pack()
# Create author input fields
given_name_label = tk.Label(window, text="Given Name:")
given_name_label.pack()
given_name_entry = tk.Entry(window)
given_name_entry.pack()

surname_label = tk.Label(window, text="Surname:")
surname_label.pack()
surname_entry = tk.Entry(window)
surname_entry.pack()
add_author_button = tk.Button(window, text="Add Author", command=Author.check_user)
add_author_button.pack()

add_author_button = tk.Button(window, text="Add New Author", command=Author.check_user)
add_author_button.pack()

email_label = tk.Label(window, text="Email:")
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()

add_author_button = tk.Button(window, text="Add Email", command=add_email)
add_author_button.pack()

orcid_id_label = tk.Label(window, text="ORCID ID:")
orcid_id_label.pack()
orcid_id_entry = tk.Entry(window)
orcid_id_entry.pack()

add_author_button = tk.Button(window, text="Add orcid", command=add_orcid)
add_author_button.pack()



# Create a button to generate JATS XML
generate_button = tk.Button(window, text="Generate JATS XML", command=generate_jats_xml)
generate_button.pack()

# Create output field for the generated JATS XML
output_label = tk.Label(window, text="Generated JATS XML:")
output_label.pack()
output_text = tk.Text(window, height=15)
output_text.pack()

window.mainloop()