from tkinter import Label,Tk #Tkinter GUI (Grafik Kullanıcı Arayüzü) paketidir. Yani Tkinter bir python kütüphanesidir.
import time # time paketinden digital_clock fonksiyonunu kullanacağız

# penceremizin boyutlandırılması  
app_window = Tk()
app_window.title("Dijital Saat")
app_window.geometry("420x150") 
app_window.resizable(height = None, width = None)

# penceremizin renklendirilmesi ve yazı tipi yerleştirilmesi
text_font= ("Boulder", 68, 'bold')
background = "#f2505b"
foreground= "#0d0101"
border_width = 25
label = Label(app_window, 
              font=text_font, 
              bg=background, 
              fg=foreground, 
              bd=border_width)
label.grid(row=0, column=1)

# dijital saat fonksiyonunu kullanma
def digital_clock():
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live)
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
