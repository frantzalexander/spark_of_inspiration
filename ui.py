import smtplib

from tkinter import *
from decouple import config
from data import RequestData

BACKGROUND_COLOR = "#7091F5"
TEXT_COLOR = "#793FDF"
quote_text = ""

class QuoteInterface:
    
    def __init__(self):
        
        self.window = Tk()
        self.window.title("Spark of Inspiration")
        self.window.config(
            padx = 20,
            pady = 20,
            background = BACKGROUND_COLOR
        )
        self.quote_data = RequestData()
        
        self.canvas = Canvas(
            width = 300,
            height = 250,
            bg = "white"
        )
        self.quote_text = ""
        self.quote_text_display = self.canvas.create_text(
            150,
            125,
            width = 280,
            text = "Clear your mind & get inspired.💡",
            fill = TEXT_COLOR
        )
        
        self.canvas.grid(
            row = 1,
            column = 0,
            pady = 20
        )
        
        # Create Buttons
        self.email_button = Button(
            text = "Send To Email: ",
            command = self.send_email,
            highlightthickness = 0
        )
        
        einstein_image = "./images/Einstein Emoji.png"
        einstein_image_button = PhotoImage(file = einstein_image)
        self.next_quote = Button(
            image = einstein_image_button,
            highlightthickness = 0,
            command = self.refresh_quote,
            background= BACKGROUND_COLOR
        )
        
        self.next_quote.grid(
            row = 2,
            column = 0
        )
        
        self.email_button.grid(
            row = 3,
            column = 0
        )
        
        # Create Text Entry Field
        self.email_text = Entry(
            width = 30,
            )
        
        self.email_text.grid(
            row = 4,
            column = 0,
        )
        
        
        self.window.mainloop()
        
    def refresh_quote(self):
        global quote_text  
        
        self.refresh_quote_text = self.quote_data.get_quote()
        self.quote = self.refresh_quote_text["Quote"]
        self.author = self.refresh_quote_text["Author"]
        self.quote_text = f"{self.quote}\n\n{self.author}"
        quote_text = self.quote_text
        self.canvas.itemconfig(
            self.quote_text_display, 
            text = self.quote_text
            )
        
    def send_email(self):
        self.email_address = self.email_text.get()
        
        
        with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
            connection.starttls()
            connection.login(user = config("SENDER_EMAIL"), password = config("APP_PASSWORD"))
            connection.sendmail(
                from_addr = config("SENDER_EMAIL"),
                to_addrs = self.email_address,
                msg = f"Subject:Inspirational Quote\n\n{quote_text}"
            )