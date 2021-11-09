
#kullanacağım kütüphaneleri import ettim
import tkinter as tk
from tkinter import PhotoImage
from tkinter import filedialog
from PIL import ImageTk, Image

img_name="" #yükelenecek olan fotoğraf için boş bir değer atadım
window=tk.Tk()#penceremiz hazır
window.geometry("1080x640") #1080x640 boyutunda pencere
window.wm_title("Cats and Dogs Classification Project")#penceremizin ismini oluşturdum
window.iconbitmap("worry-cat.ico")
"""burada dikkat etmeniz gerek siz istediğiniz bir iconu koymak isterseniz bilgisayar
üzerindeki yolunu kopyalayıp yapıştırabilir veya  çalıştığınız dosya içerisine koyabilirsiniz"""

def informationtext(): #projemiz hakkında bilgilendirme içeren pencere için bir fonksiyon
    tpp=tk.Tk() #tpp adında olarak yeni bir pencere oluşturdum
    tpp.geometry("1080x1080")#burada yine uzunluk ve genişliğini ayarladım
    tpp.wm_title("What is Our Project")#pencerinin ismini belirledim
    labelinfo=tk.Label(tpp, text="We are a one group student. We care about street animal"
                                 "cause we made a new project. Our project is cats and dogs classification "
                                 "project...  ", font="helvetica 13") #bir adet label kullanarak
    #istediğim yazıyı yazdım
    labelinfo.pack(side=tk.TOP, pady=5)
    tpp.mainloop()#burayı unutmuyordukk biz kapatana kadar ekran döngüde kalıyor yani karşımızda duruyor


menubar=tk.Menu(window)#yeni bir menu tanımladık
window.config(menu=menubar)#penceremize menübar ekledik
information=tk.Menu(menubar) #menübarı tanımladık
menubar.add_cascade(label="Information", menu=information) #menübarımıza isim verip menünün yerini belirttik
information.add_command(label="What is our project ?", command=informationtext) #menübarımıza bir fonksiyon ekledil
header=tk.Label(text="Welcome Our Image Classification App", fg="black",
                font="Helvetica 30") #başlık ekledik
header.pack(side=tk.TOP, pady=20) #başlığı konumlandırdık


def imageresize(img): #yükleyeceğimiz fotoğrafları yeniden boyutlandıracağımız fonksiyon
    img=img.resize((500, 300), Image.ANTIALIAS) #500x300 oranında  yeniden boyutlandırıyorz
    return img


def loadImage(): #fotoğraf yüklemek için tekrar bir fonksiyon oluşturduk.
    #fonksiyon içinde global değerlerimizi  atadık
    global img_jpg
    global img_name
    global foto
    img_name=filedialog.askopenfilename(initialdir=r"C:\Users\metin\Desktop\PetImages",
                                        title="select an image file")
    """yukarıdaki kodda parantez öncesi kısım bize bilgisayarımız içerisinden bir dosya açtırıyor
    daha sonra seçeneklerimizden ilki initialdir açılan pencerenin nereden açılmasını istediğimizi 
    yol olarak belirtiyoruz title ise pencerede yazan kullanıca göstermek istediğimiz text oluyor"""

    img_jpg=img_name.split("/")[-1].split(".")[0]
    r"""   yukarıdaki kod ile beraber açtığımız fotoğrafın ilk olarak yolunu / bölerek yani
    C:\Users\metin\Desktop\PetImages\photo.jpg burada işaretlerin arasını bölerek elimizde şöyle bir
    liste bırakıyor [C: , Users , Desktop, PetImages, photo.jpg] bu listeden sonuncusunu alıyoruz yani photo.jpg 
    bunu tekrardan . ya bölüyor ve ilk öğeyi alıyoruz yani photo yazan kısmı böyle yaparak şuan elimizde bulunmayan 
    sınıflandırma modeli yerine dosya isminde sınıflandırma çıktısı almayı planladım"""

    img=Image.open(img_name) #fotoğrafı açıyoruz
    img=imageresize(img)#fotoğrafı yeniden boyutlandırıyoruz
    img=ImageTk.PhotoImage(img) #fotoğrafı yüklüyoruz
    foto=tk.Label(window, image=img)# burada grördüğünüz image seçeneği ile widgetlara resim ekleyebiliyorsunuz
    #aşağıda daha net belirttim
    foto.image=img #fotoğrafımı img değerine atadım
    foto.pack(side=tk.TOP, ) #labelımı tanımlayarak yerleştiriyorum



def deleteimage(): #delete butonu için yazmış olduğum fonksiyon
    foto.destroy()#tanımladığımı fotoğraf labelını siliyorum



deletebutton=PhotoImage(file="remove-image.png") #buton için bir resim belirledik burada file kısmına resminizin yolunu belirtin
buttton=tk.Button(window, text="   Delete Image", font="helvetica 12", command=deleteimage,
                  borderwidt=4, image=deletebutton, compound=tk.LEFT)
buttton.pack(side=tk.BOTTOM, pady=5)
"""evett yukarıda bir sürü seçenek görüyorsunuz sakin olalımm ve seçenekleri inceleyelim bilmediğiniz seçeneklerden ilki 
borderwidt= bu butonun kenar çizgisini kalınlaştırmanızı sağlar
image = burada bir fotoğraf belirliyor ve değişkenini yazıyoruz
compound ise fotoğrafın konumunu belirtiyor ben sola almayı tercih ettim
"""

def classification(): #sınıflandırma için fonksiyon
    if img_jpg[0:3] == 'cat': #eğer yukarıdan aldığımız fotoğrafın isminin ilk 3 harfinde cat varsa
        classification_label.config(text=" This is a cat") #sınıflandırma labelımızın textini değiştir
    elif img_jpg[0:3] == 'dog':#eğer yukarıdan aldığımız fotoğrafın isminin ilk 3 harfinde dog varsa
        classification_label.config(text=" This is a dog")#sınıflandırma labelımızın textini değiştir
    else:#eğer yukarıdan aldığımız fotoğrafın isminin ilk 3 harfinde cat veya dog yoksa
        classification_label.config(text=" This is not cat and dog")#sınıflandırma labelımızın textini değiştir

""" aşağıdaki butonlar da yukarıdaki delete butonu gibi yazılmıştır sizden ricam değiştirerek 
bunlar üzerinde yeni şeyler denemeniz olacaktır. Deneyerek en güzelini bulabilirsiniz."""

class_image=PhotoImage(file='euclidean-chart.png')
classification_button=tk.Button(window, text="    Classification", font="helvetica 12", fg="black",
                                command=classification,
                                borderwidt=4, image=class_image, compound=tk.LEFT)
classification_button.pack(side=tk.BOTTOM, pady=30, )
click_btn=PhotoImage(file='photo.png')
loadbutton=tk.Button(window, text="       Load Image", font="helvetica 12", fg="black",
                     compound=tk.LEFT, image=click_btn, command=loadImage, borderwidt=4)
loadbutton.pack(side=tk.BOTTOM, )
classification_label=tk.Label(window, font="helvetica 12", fg="blue")
classification_label.pack(side=tk.BOTTOM, pady=10)

window.mainloop()#ve son olarak göstersin bakalım penceremizi
