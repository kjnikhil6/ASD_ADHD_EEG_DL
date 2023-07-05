from flask import Flask, render_template, request
#from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
from keras.models import model_from_json
import re
import sys
from scipy.signal import hann
import os
import mne
import base64
#sys.path.append(os.path.abspath("./model"))
from eeg_classifier_v1 import * 
from sklearn.preprocessing import StandardScaler
scaler =  StandardScaler()

def sliding_window(file_path, l_freq=1.0, h_freq=40.0, decim_factor=2.5):

    raw = mne.io.read_raw_fif(file_path, preload=True)
    raw.filter(l_freq=0.3,h_freq=30)

    data = raw.get_data()

    window_size = 1 * int(raw.info['sfreq'])
    stride = window_size// 2

    windows = []
    for i in range(0, data.shape[1] - window_size + 1, stride):
        window_data = data[:, i:i+window_size]
        # Apply a low-pass anti-aliasing filter to avoid aliasing
        #anti_alias_data = mne.filter.filter_data(window_data, sfreq=raw.info['sfreq'],  l_freq= 40 , h_freq=None,)
        hann_window = hann(window_size, sym=False)
        window_data = window_data*hann_window
        #plt.plot(window_data[20])        
        # Decimate the signal
        decimated_data = mne.filter.resample(window_data, down=1.25, npad='auto')
        windows.append(decimated_data)


    arr = np.array(windows)
    print(arr.shape)
    return arr

global graph, model

UPLOAD_FOLDER = "/home/kjnikhil/Documents/EEG_LEARNING_DISABILITY/CODE/uploads"

#model, graph = init()
json_file = open('/home/kjnikhil/Documents/EEG_LEARNING_DISABILITY/CODE/model_78v4.json','r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
	#load weights into new model
model.load_weights("/home/kjnikhil/Documents/EEG_LEARNING_DISABILITY/CODE/model_78v4.h5")
print("Loaded Model from disk")

	#compile and evaluate loaded model
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
	#loss,accuracy = model.evaluate(X_test,y_test)
	#print('loss:', loss)
	#print('accuracy:', accuracy)
graph = tf.compat.v1.get_default_graph()

app = Flask(__name__)


app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def man():
	return render_template('index.html')


@app.route('/home', methods=['POST'])
def home():

	file = request.files.get('image')
	file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
	file_path = app.config['UPLOAD_FOLDER']+'/'+file.filename
	#with
	test_data_arr = sliding_window(file_path)
	#test_data = np.vstack(test_data_list)
	print(test_data_arr.shape )
	test_features = np.moveaxis(test_data_arr,1,2)
	print(test_features.shape )
	
	#app.config['UPLOAD_FOLDER']

	arr=scaler.fit_transform(test_features.reshape(-1,\
							 test_features.shape[-1])).reshape(test_features.shape)#normalization
	predictions=[]

	preds = np.sum(model.predict(arr))/len(arr)

	return render_template('prediction.html', data=preds)

	#img.save('static/{}.jpg'.format(COUNT))    
	#img_arr = cv2.imread('static/{}.jpg'.format(COUNT))

	#prediction = model.predict(img_arr)

	#x = round(prediction[0,0], 2)
	#y = round(prediction[0,1], 2)
	#preds = np.array([x,y])
	


#@app.route('/load_img')
def load_img():
	global COUNT
	return send_from_directory('static', "{}.jpg".format(COUNT-1))


if __name__ == '__main__':
	app.run(debug="True")

