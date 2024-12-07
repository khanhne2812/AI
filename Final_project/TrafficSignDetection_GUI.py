import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
#load the trained model to classify sign
from tensorflow.keras.models import load_model
model = load_model('TrafficSign.h5', compile=False)
#dictionary to label all traffic signs class.
classes = { 1:'Cấm đi bộ',
           2:'Cấm dừng - Đỗ xe',
           3:'Cấm đi ngược chiều',
           4:'Cấm ô tô - Ô tô Khách',
           5:'Cấm quay đầu',
           6:'Cấm rẽ phải',
           7:'Cấm rẽ trái',
           8:'Cấm xe đạp',
           9:'Cấm xe máy',
           10:'Cấm xe tải',
           11:'Chạy theo vòng xuyến',
           12:'Chỉ được đi thẳng và rẽ phải',
           13:'Chỉ được đi thẳng và rẽ trái',
           14:'Chỉ được rẽ phải',
           15:'Chỉ được rẽ trái',
           16:'Chỗ ngoặt nguy hiểm',
           17:'Công trường đang thi công',
           18:'Đường dành cho người đi bộ',
           19:'Dốc nguy hiểm',
           20:'Dừng lại',
           21:'Đường hai chiều',
           22:'Đường bị thu hẹp',
           23:'Đường cấm lưu thông',
           24:'Đường cao tốc phía trước',
           25:'Đường có cấp điện',
           26:'Đường có nhiều trẻ em',
           27:'Đường đá lở',
           28:'Đường dành cho ô tô',
           29:'Đường dành cho ô tô - xe máy',
           30:'Đường dành cho xe máy',
           31:'Đường dành cho xe thô sơ',
           32:'Đường đôi',
           33:'Đường giao nhau cùng cấp',
           34:'Đường hầm',
           35:'Đường hay xảy ra tai nạn',
           36:'Đường người đi bộ cắt ngang',
           37:'Đường trơn trượt',
           38:'Đường xe đạp cắt ngang',
           39:'Đường giao nhau với đường sắt có rào',
           40:'Đường giao nhau với đường sắt không rào',
           41:'Đường giao nhau có tín hiệu đèn',
           42:'Giao nhau với đường không ưu tiên',
           43:'Giao nhau với đƯờng ưu tiên',
           44:'Hạn chế chiều cao',
           45:'Hạn chế chiều ngang xe',
           46:'Hạn chế tải trọng',
           47:'Hết đoạn đường dành cho ô tô - xe máy',
           48:'Hết hạn chế tốc độ tối thiểu',
           49:'Hết khu dân cư',
           50:'Hướng đi thẳng phải theo',
           51:'Kè vực sâu',
           52:'Kết thúc đường đôi',
           53:'Khu vực đông dân cư',
           54:'Khu vực đỗ xe',
           55:'Làn đường dành cho ô tô',
           56:'Lề đường nguy hiểm',
           57:'Rẽ trái và phải',
           58:'Tốc độ tối đa',
           59:'Tốc độ tối thiểu cho phép',
           60:'Tuyến đường cầu vượt cắt qua',
           61:'Đường hay ùn tắc giao thông'
        }
#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Traffic sign classification')
top.configure(background='#CDCDCD')
label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)
def classify(file_path):
   global label_packed
   image = Image.open(file_path)
   image = image.resize((100,100))
   image = numpy.expand_dims(image, axis=0)
   image = numpy.array(image)
   pred = model.predict_classes([image])[0]
   sign = classes[pred+1]
   print(sign)
   label.configure(foreground='#011638', text=sign)
def show_classify_button(file_path):
   classify_b=Button(top,text="Classify Image",command=lambda: classify(file_path),padx=  10,pady=5)
   classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
   classify_b.place(relx=0.79,rely=0.46)
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="check traffic sign",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()

