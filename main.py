from tkinter import *
def getEntry():
        university = universiteEntry.get()
        generateTitle(university)

def generateTitle(university):
    print("Génération de la page de titre en cours \n")
    title_tex_document = open("title.tex","w+")
    title_tex_document.write("\\newcommand{\\universite}{%s}\n" % university)
    """title_tex_document.write("\\newcommand{\\ecole}{%s}\n" % school)
    title_tex_document.write("\\newcommand{\\departement}{%s}\n" % department)
    title_tex_document.write("\\newcommand{\\specialite}{%s}\n" % speciality)
    title_tex_document.write("\\newcommand{\\typeDocument}{%s}\n" % typeDocument)
    title_tex_document.write("\\newcommand{\\matiere}{%s}\n" % matiere)
    title_tex_document.write("\\newcommand{\\nomProjet}{%s}\n" % nameProject)
    title_tex_document.write("\\newcommand{\\auteurs}{%s}\n" % authors)
    title_tex_document.write("\\newcommand{\\enseignant}{%s}\n" % teacher)
    title_tex_document.write("\\newcommand{\\promotion}{%s}\n" % promotion)
    title_tex_document.write("\\newcommand{\\groupe}{%s}\n" % group)
    title_tex_document.write("\\newcommand{\\anneeUniversitaire}{%s}\n" % universityYear)
    title_tex_document.write("\\newcommand{\\dateRapport}{%s}\n" % reportDate)"""
    print("Génération de la page de titre OK \n")



# TKINTER
fenetre = Tk()
fenetre.title("LaTeX Title Generator")
universityLabel = Label(fenetre, text="Université : ").grid(row=1,column=1)
radioValue = StringVar()
rdioOne = Radiobutton(fenetre, text='Institut National Polytechnique de Toulouse',
                             variable=radioValue, value="Institut National Polytechnique de Toulouse").grid(row = 1 , column = 2)
ecoleLabem = Label(fenetre, text="Ecole : ").grid(row=2,column=1)
radioValue = StringVar()
ecoleOne = Radiobutton(fenetre, text='Ecole Nationale Supérieure d\'Electrotechnique, d\'Electronique, d\'Informatique, d\'Hydraulique et des Telecommunications',
                             variable=radioValue, value="Ecole Nationale Supérieure d\'Electrotechnique, d\'Electronique, d\'Informatique, d\'Hydraulique et des Telecommunications").grid(row = 2 , column = 2)
ecoleOne = Radiobutton(fenetre, text='Ecole Nationale Superieure Agronomique de Toulouse',
                             variable=radioValue, value="Ecole Nationale Superieure Agronomique de Toulouse").grid(row = 3 , column = 2)
ecoleOne = Radiobutton(fenetre, text='ENSIACET',
                             variable=radioValue, value="ENSIACET").grid(row = 4 , column = 2)
fenetre.mainloop()

