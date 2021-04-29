import string
from DFA import DFA
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use("TkAgg")


def normalization(text):
    """Remove punctuations and covert all alphabets to lower case."""

    accepted_alphabet = [char for char in string.ascii_lowercase] + [" "]

    # convert all uppercase to lowercase
    text = text.lower()

    # remove punctuations
    new_text = ""
    for c in text:
        if c in accepted_alphabet:
            new_text += c

    return new_text


def run_dfa():
    """Run the DFA to find strings that match the required patterns"""

    # clear previous logs
    logField.config(state=NORMAL)
    logField.delete("1.0", END)

    detected_words = {}

    input_text = inputField.get("1.0", END)
    normalized_text = normalization(input_text)
    word_list = normalized_text.split()

    # if user doesn't input anything or input strings that are not accepted, show error message.
    if len(word_list) == 0:
        messagebox.showerror("Error Message", "Invalid Input. Please enter again.")
    else:
        logField.insert(END, "\n======================================================================\n")

        # for each word, run DFA to get the status (accepted or rejected)
        for word in word_list:
            myDFA.clear_logs()
            accepted, logs = myDFA.run_machine(list(word))
            # print logs
            logField.insert(END, f"\nSTRING: {word}\n\n")
            logField.insert(END, logs)

            if accepted:
                if word not in detected_words:
                    detected_words[word] = 1
                else:
                    detected_words[word] += 1
                logField.insert(END, "\nSTATUS: Accepted\n")
            else:
                logField.insert(END, "\nSTATUS: Rejected\n")

            logField.insert(END, "\n======================================================================\n")

        # highlight status in the log
        highlight_pattern(logField, "STATUS: Accepted", "status_accept", exact=True)
        highlight_pattern(logField, "STATUS: Rejected", "status_reject", exact=True)

        if len(detected_words) != 0:
            # highlight detected words in the input text
            for word in detected_words:
                highlight_pattern(inputField, word, "highlight")
            show_chart(detected_words)
        else:
            messagebox.showinfo("Info Message", "No English Conjunctions / Adverbs / Adjectives detected. ")
    logField.config(state=DISABLED)


def clear_input():
    """Clear all text in the input field and log field"""
    inputField.delete("1.0", END)
    logField.config(state=NORMAL)
    logField.delete("1.0", END)
    logField.config(state=DISABLED)


def highlight_pattern(widget, word, tag, exact=False):
    """Apply the given tag to all text that matches the given string pattern"""

    widget.mark_set("matchStart", "1.0")
    widget.mark_set("matchEnd", "1.0")

    while True:
        if exact:
            index = widget.search(word, "matchEnd", END, count=len(word))
        else:
            index = widget.search(r'(^|\n|\W)%s($|\n|\W)' % word, "matchEnd", END, count=len(word) + 1,
                                  regexp=True, nocase=1)
        if index == "":
            break
        widget.mark_set("matchStart", index)
        widget.mark_set("matchEnd", "%s+%sc" % (index, len(word) + 1))
        widget.tag_add(tag, "matchStart", "matchEnd")


def show_chart(word_list):
    """Draw a bar chart showing the number of occurrence for each detected word."""

    chart_win = Tk()
    chart_win.title("Bar Chart")

    Label(chart_win, text="Occurrence of Each Detected Word", font=('Times', 16, 'bold')).pack()

    figure = Figure(figsize=(16, 5), dpi=100)

    plot = figure.add_subplot(1, 1, 1)
    plot.bar([word for word in word_list], [word_list[word] for word in word_list])
    plot.tick_params('x', rotation=90)

    figure.tight_layout()

    canvas = FigureCanvasTkAgg(figure, chart_win)
    canvas.get_tk_widget().pack(padx=10, pady=10)


if __name__ == "__main__":
    # Initialize the DFA and output text
    myDFA = DFA(
        states=['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15',
                'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30',
                'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41', 'q42', 'q43', 'q44', 'q45',
                'q46', 'q47', 'q48', 'q49', 'q50', 'q51', 'q52', 'q53', 'q54', 'q55', 'q56', 'q57', 'q58', 'q59', 'q60',
                'q61', 'q62', 'q63', 'q64', 'q65', 'q66', 'q67', 'q68', 'q69', 'q70', 'q71', 'q72', 'q73', 'q74', 'q75',
                'q76', 'q77', 'q78', 'q79', 'q80', 'q81', 'q82', 'q83', 'q84', 'q85', 'q86', 'q87', 'q88', 'q89', 'q90',
                'q91', 'q92', 'q93', 'q94', 'q95', 'q96', 'q97', 'q98', 'q99', 'q100', 'q101', 'q102', 'q103', 'q104',
                'q105', 'q106', 'q107', 'q108', 'q109', 'q110', 'q111', 'q112', 'q113', 'q114', 'q115', 'q116', 'q117',
                'q118', 'q119', 'q120', 'q121', 'q122', 'q123', 'q124', 'q125', 'q126', 'q127', 'q128', 'q129', 'q130',
                'q131', 'q132', 'q133', 'q134', 'q135', 'q136', 'q137', 'q138', 'q139', 'q140', 'q141', 'q142', 'q143',
                'q144', 'q145', 'q146', 'q147', 'q148', 'q149', 'q150', 'q151', 'q152', 'q153', 'q154', 'q155', 'q156',
                'q157', 'q158', 'q159', 'q160', 'q161', 'q162', 'q163', 'q164', 'q165', 'q166', 'q167', 'q168', 'q169',
                'q170', 'q171', 'q172', 'q173', 'q174', 'q175', 'q176', 'q177', 'q178', 'q179', 'q180', 'q181', 'q182',
                'q183', 'q184', 'q185', 'q186', 'q187', 'q188', 'q189', 'q190', 'q191', 'q192', 'q193', 'q194', 'q195',
                'q196', 'q197', 'q198', 'q199', 'q200', 'q201', 'q202', 'q203', 'q204'],
        alphabets=[char for char in string.ascii_lowercase] + [" "],
        transition_dict={
            'q0': {'a': 'q1', 'b': 'q14', 'c': 'q25', 'd': 'q33', 'e': 'q39', 'f': 'q62', 'g': 'q65', 'h': 'q80',
                   'i': 'q111', 'm': 'q120', 'o': 'q134', 'p': 'q136', 'r': 'q148', 's': 'q151', 't': 'q167',
                   'u': 'q180', 'w': 'q188', 'y': 'q199'},
            'q1': {'l': 'q2', 'n': 'q5', 't': 'q7'},
            'q2': {'s': 'q3'},
            'q3': {'o': 'q4'},
            'q5': {'d': 'q6'},
            'q7': {'h': 'q8'},
            'q8': {'l': 'q9'},
            'q9': {'e': 'q10'},
            'q10': {'t': 'q11'},
            'q11': {'i': 'q12'},
            'q12': {'c': 'q13'},
            'q14': {'l': 'q15', 'r': 'q21'},
            'q15': {'a': 'q16', 'u': 'q19'},
            'q16': {'c': 'q17'},
            'q17': {'k': 'q18'},
            'q19': {'e': 'q20'},
            'q21': {'o': 'q22'},
            'q22': {'w': 'q23'},
            'q23': {'n': 'q24'},
            'q25': {'o': 'q26'},
            'q26': {'n': 'q27'},
            'q27': {'t': 'q28'},
            'q28': {'r': 'q29'},
            'q29': {'a': 'q30'},
            'q30': {'r': 'q31'},
            'q31': {'y': 'q32'},
            'q33': {'o': 'q34'},
            'q34': {'u': 'q35'},
            'q35': {'b': 'q36'},
            'q36': {'l': 'q37'},
            'q37': {'e': 'q38'},
            'q39': {'n': 'q40', 's': 'q48', 'x': 'q57'},
            'q40': {'e': 'q41'},
            'q41': {'r': 'q42'},
            'q42': {'g': 'q43'},
            'q43': {'e': 'q44'},
            'q44': {'t': 'q45'},
            'q45': {'i': 'q46'},
            'q46': {'c': 'q47'},
            'q48': {'p': 'q49'},
            'q49': {'e': 'q50'},
            'q50': {'c': 'q51'},
            'q51': {'i': 'q52'},
            'q52': {'a': 'q53'},
            'q53': {'l': 'q54'},
            'q54': {'l': 'q55'},
            'q55': {'y': 'q56'},
            'q57': {'t': 'q58'},
            'q58': {'r': 'q59'},
            'q59': {'e': 'q60'},
            'q60': {'m': 'q61'},
            'q61': {'e': 'q54'},
            'q62': {'u': 'q63'},
            'q63': {'n': 'q64'},
            'q65': {'e': 'q66', 'o': 'q71', 'r': 'q74'},
            'q66': {'n': 'q67'},
            'q67': {'e': 'q68'},
            'q68': {'r': 'q69'},
            'q69': {'a': 'q70'},
            'q70': {'l': 'q54'},
            'q71': {'o': 'q72'},
            'q72': {'d': 'q73'},
            'q74': {'a': 'q75', 'e': 'q77'},
            'q75': {'y': 'q76'},
            'q77': {'e': 'q78'},
            'q78': {'n': 'q79'},
            'q80': {'a': 'q81', 'e': 'q85', 'i': 'q97', 'o': 'q100', 'u': 'q105'},
            'q81': {'r': 'q82'},
            'q82': {'s': 'q83'},
            'q83': {'h': 'q84'},
            'q85': {'t': 'q86'},
            'q86': {'e': 'q87'},
            'q87': {'r': 'q88'},
            'q88': {'o': 'q89'},
            'q89': {'c': 'q90'},
            'q90': {'h': 'q91'},
            'q91': {'r': 'q92'},
            'q92': {'o': 'q93'},
            'q93': {'m': 'q94'},
            'q94': {'i': 'q95'},
            'q95': {'c': 'q96'},
            'q97': {'g': 'q98'},
            'q98': {'h': 'q99'},
            'q100': {'t': 'q101'},
            'q101': {'t': 'q102'},
            'q102': {'e': 'q103'},
            'q103': {'r': 'q104'},
            'q105': {'n': 'q106'},
            'q106': {'t': 'q107'},
            'q107': {'i': 'q108'},
            'q108': {'n': 'q109'},
            'q109': {'g': 'q110'},
            'q111': {'m': 'q112'},
            'q112': {'p': 'q113'},
            'q113': {'o': 'q114'},
            'q114': {'r': 'q115'},
            'q115': {'t': 'q116'},
            'q116': {'a': 'q117'},
            'q117': {'n': 'q118'},
            'q118': {'t': 'q119'},
            'q120': {'a': 'q121', 'e': 'q124', 'o': 'q129'},
            'q121': {'n': 'q122'},
            'q122': {'y': 'q123'},
            'q124': {'n': 'q125'},
            'q125': {'t': 'q126'},
            'q126': {'a': 'q127'},
            'q127': {'l': 'q128'},
            'q129': {'r': 'q130', 's': 'q132'},
            'q130': {'e': 'q131'},
            'q132': {'t': 'q133'},
            'q134': {'r': 'q135'},
            'q136': {'h': 'q137', 'r': 'q144'},
            'q137': {'y': 'q138'},
            'q138': {'s': 'q139'},
            'q139': {'i': 'q140'},
            'q140': {'c': 'q141'},
            'q141': {'a': 'q142'},
            'q142': {'l': 'q143'},
            'q144': {'o': 'q145'},
            'q145': {'n': 'q146'},
            'q146': {'e': 'q147'},
            'q148': {'e': 'q149'},
            'q149': {'d': 'q150'},
            'q151': {'i': 'q152', 't': 'q159'},
            'q152': {'b': 'q153'},
            'q153': {'e': 'q154'},
            'q154': {'r': 'q155'},
            'q155': {'i': 'q156'},
            'q156': {'a': 'q157'},
            'q157': {'n': 'q158'},
            'q159': {'i': 'q160', 'r': 'q163'},
            'q160': {'l': 'q161'},
            'q161': {'l': 'q162'},
            'q163': {'o': 'q164'},
            'q164': {'n': 'q165'},
            'q165': {'g': 'q166'},
            'q167': {'h': 'q168', 'y': 'q172'},
            'q168': {'i': 'q169'},
            'q169': {'c': 'q170'},
            'q170': {'k': 'q171'},
            'q172': {'p': 'q173'},
            'q173': {'i': 'q174'},
            'q174': {'c': 'q175'},
            'q175': {'a': 'q176'},
            'q176': {'l': 'q177'},
            'q177': {'l': 'q178'},
            'q178': {'y': 'q179'},
            'q180': {'s': 'q187', 'n': 'q181'},
            'q181': {'i': 'q182'},
            'q182': {'d': 'q183'},
            'q183': {'e': 'q184'},
            'q184': {'a': 'q185'},
            'q185': {'l': 'q186'},
            'q187': {'u': 'q175'},
            'q188': {'h': 'q189', 'o': 'q193'},
            'q189': {'i': 'q190'},
            'q190': {'t': 'q191'},
            'q191': {'e': 'q192'},
            'q193': {'r': 'q194'},
            'q194': {'k': 'q195'},
            'q195': {'i': 'q196'},
            'q196': {'n': 'q197'},
            'q197': {'g': 'q198'},
            'q199': {'e': 'q200'},
            'q200': {'l': 'q201'},
            'q201': {'l': 'q202'},
            'q202': {'o': 'q203'},
            'q203': {'w': 'q204'}},
        start_state='q0',
        accept_states=['q4', 'q6', 'q13', 'q18', 'q20', 'q24', 'q32', 'q38', 'q47', 'q56', 'q64', 'q73', 'q76', 'q79',
                       'q84', 'q96', 'q99', 'q104', 'q110', 'q119', 'q123', 'q128', 'q131', 'q133', 'q135', 'q143',
                       'q147', 'q150', 'q158', 'q162', 'q166', 'q171', 'q179', 'q186', 'q192', 'q198', 'q204']
    )

    # ============= #
    #      GUI      #
    # ============= #

    root = Tk()
    root.state("zoomed")
    root.title("English Conjunctions, Adverbs and Adjectives Finder")

    # Create widgets
    title = Label(root, text="English Conjunctions, Adverbs and Adjectives Finder", font=('Times', 16, 'bold'))
    frame = LabelFrame(root, text="Input Text", padx=10, pady=10)
    inputField = Text(frame, height=10, width=100, wrap=WORD, padx=10, pady=10, bd=0, font=('Helvetica', 10))
    logField = ScrolledText(frame, height=10, width=70, wrap=WORD, bd=0, bg="#000", fg="#fff", padx=20, pady=10,
                            state=DISABLED, font=('Courier', 10))

    startBtn = Button(frame, text="Start", padx=20, command=run_dfa, bg="green", fg="#fff", bd=0, cursor="mouse")
    againBtn = Button(frame, text="Clear", padx=17, command=clear_input, bg="green", fg="#fff", bd=0, cursor="mouse")
    exitBtn = Button(root, text="Exit", padx=20, command=root.quit, bg="#555555", fg="#fff", bd=0, cursor="mouse")
    startBtn.flash()
    againBtn.flash()
    exitBtn.flash()

    # Add tags to modify font colors
    inputField.tag_config("highlight", foreground="green")
    logField.tag_config("status_accept", foreground="cyan")
    logField.tag_config("status_reject", foreground="yellow")

    # Display the widgets
    title.pack(pady=10)
    frame.pack(padx=20, pady=10)
    inputField.grid(row=1, column=0, columnspan=2)
    startBtn.grid(row=2, column=0, sticky="E")
    againBtn.grid(row=3, column=0, sticky="E")
    logField.grid(row=2, column=1, rowspan=2, pady=10, sticky="E")
    exitBtn.pack()

    root.mainloop()
