# Machine Learning END-TO-END Project to Classify Bank :dollar: *Counterfeit* VS *Non-Counterfeit* Notes :dollar:

## :cinema: Demo :point_down:

![Demo](https://github.com/toushalipal6991/BrainTumor_Detection/blob/master/BrainTumorDetection%20-%20Copy.gif)

:round_pushpin: Production URL for availing this app :arrow_right: [Fake Note Detection](http://ec2-3-22-130-255.us-east-2.compute.amazonaws.com:8080/) (Note: This URL can only be availed if I connect to my AWS EC2 instance)

## Aim of this Project
This project aims to classify Counterfeit and Non-Counterfeit Bank Notes using Machine Learning techniques.

## Datasets:-
- Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.
- Source :arrow_right: [Kaggle](https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data)

## :memo: HLD(High Level Design)
- Features provided in the dataset are:-
  * Variance
  * Skewness
  * Curtosis
  * Entropy
- EDA :arrow_right: After performing EDA on this dataset, it was easy to conclude that the features :arrow_right: Variance and Skewness are the most important features which will help us create a clear distinction between fake and genuine notes. For detailed analysis done via EDA, please refer the BankNoteAuth.ipynb file.
- Train-Test split: The dataset was split into 70(train):30(test) ratio. No cross-validation set was created since the dataset is very small. It contains only 1372 data points.
- Data Pre-processing :arrow_right: The features were simply Standardardized.
- Choosing the Machine Learning models :arrow_right: 3 different ML models were used for analysis and all 3 gave very good results.
- Scoring used :arrow_right: was f1-score. Below table displays all 3 models and the f1-scores obtained:-
![Table](https://github.com/toushalipal6991/BrainTumor_Detection/blob/master/AccuracyTable.PNG)



- Train-CrossValidation-Test split :arrow_right: Entire dataset was split into 80(train + cross validation):20(test) ratio.
- Pre-processing the data :arrow_right: All images were divided into Standard Directories so as to be able to use the [Keras ImageDataGenerator class](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html)
for Image Augmentation.
- Choosing Model Architectures :arrow_right: 4 different CNN archiectures were used. 
- Each of these models were fed with a completely unseen Test set of images and final accuracy was determined on the basis of prediction accuracy.
- Below table respresents each CNN architecture used and their test accuracies:-
![Table](https://github.com/toushalipal6991/BrainTumor_Detection/blob/master/AccuracyTable.PNG)
- Model-4: Transfer Learning for Feature Extraction via VGG16 + Data Augmentation had the highest accuracy of 96.706% and hence, it has been finalized for deployment.
- API used for Deployment :arrow_right: Flask. This simple web-app (as represented in the Demo) helps you upload the image and predicts whether the MRI scan image fed, contains tumor or not.

## :file_folder: Libraries Used
:crayon: matplotlib :crayon: seaborn :crayon: numpy :crayon: pandas :crayon: random :crayon: shutil :crayon: prettytable :crayon: Flask

## :hammer_and_wrench: :toolbox: Tools Used
- Jupyter Notebook
- Sublime Text
