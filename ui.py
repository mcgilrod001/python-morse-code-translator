import customtkinter as ct# import playsound
import morse

# sets default theme to dark blue
ct.set_default_color_theme('dark-blue')
ct.set_appearance_mode('dark')
root = ct.CTk()
root.title('morse code translator')
root.geometry('500x250')

# creates frame 
frame = ct.CTkFrame(master=root)
frame.pack(pady=20  , padx=50, fill="both", expand=True)

# creates label
label = ct.CTkLabel(master=frame, text="morse code translator", font=("roboto", 20))
label.pack(pady=12,padx=10)

# creates entry
entry1 = ct.CTkEntry(master=frame, placeholder_text="enter text here", font=("roboto", 20), width=240,height=60)
entry1.pack(pady=12,padx=10, expand=True, fill="both")

# creates text box 
# ctk_text = ct.CTkTextbox(master=frame, font=("roboto", 20)).pack(expand=True, fill="both")
label2 = ct.CTkLabel(master=frame, text="translated text", font=("roboto", 20))
label2.pack(pady=12,padx=10)
def get_inf_from_text():
    translated_text = morse.translate(plain_text=entry1.get())
    label2.configure(text=translated_text)
    print(translated_text)
# creats button
button = ct.CTkButton(master=frame, text="translate", font=("roboto", 20),command=get_inf_from_text).pack(pady=12,padx=10)




root.mainloop()