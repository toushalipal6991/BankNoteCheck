# Machine Learning END-TO-END Project Using Flask API, Docker & AWS to Classify Bank :dollar: *Counterfeit* VS *Non-Counterfeit* Notes :dollar:

## :cinema: Demo :point_down:

![Demo](https://github.com/toushalipal6991/BankNoteCheck/blob/master/demo.gif)

:round_pushpin: Production URL for availing this app :arrow_right: [Fake Note Detection](http://ec2-18-116-62-214.us-east-2.compute.amazonaws.com:8080/) (Note: This URL can only be availed if I connect to my AWS EC2 instance)

## Aim of this Project
- This project aims to classify Counterfeit and Non-Counterfeit Bank Notes using Machine Learning techniques.
- This project was also *Containerized Using Docker*.
- *Deployment* was done using *Flask API on an AWS EC2 instance*.

## Datasets:-
- Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.
- Source :arrow_right: [Kaggle](https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data)

## :memo: HLD(High Level Design)
- Features provided in the dataset are:-
  * Variance
  * Skewness
  * Curtosis
  * Entropy
- EDA :arrow_right: After performing EDA on this dataset, it was easy to conclude that the features :arrow_right: Variance and Skewness are the most important features which will help us create a clear distinction between fake and genuine notes. For detailed analysis done via EDA, please refer the [BankNoteAuth.ipynb](https://github.com/toushalipal6991/BankNoteCheck/blob/master/BankNoteAuth.ipynb) file.
- Train-Test split: The dataset was split into 70(train):30(test) ratio. No cross-validation set was created since the dataset is very small. It contains only 1372 data points.
- Data Pre-processing :arrow_right: The features were simply Standardized.
- Choosing the Machine Learning models :arrow_right: 3 different ML models were used for analysis and all 3 gave very good results.
- Scoring used :arrow_right: was f1-score. Below table displays all 3 models and the f1-scores obtained:-
![Table](https://github.com/toushalipal6991/BankNoteCheck/blob/master/f1-score-table.PNG)
- **Support Vector Machine** resulted the highest f1-score of **1.0**.

## Deployment using Flask API and AWS Containerization using Docker
- A simple web-app has been built using this model (as shown in the Demo) and ***Flask API and Containerized using Docker***.
- This web-app has also been ***Deployed into Production using Flask API on an AWS EC2 instance***.
- Please refer my documentation [Flask_Docker_AWS_Procedures](https://github.com/toushalipal6991/BankNoteCheck/blob/master/Flask_Docker_AWS_Procedures.docx) to see how I deployed and containerized.
- Using this web-app, you can enter variance,skewness,curtosis and entropy features extracted by you and the app will tell you if the Note is fake or genuine.

## :file_folder: Libraries Used
:crayon: matplotlib :crayon: seaborn :crayon: numpy :crayon: pandas :crayon: prettytable :crayon: Flask

## :hammer_and_wrench: :toolbox: Tools and Softwares Used
- Jupyter Notebook
- Sublime Text
- Docker
- AWS
