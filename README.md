<a name="br1"></a> 

**APJ Abdul Kalam Technological**

**University**

Government Engineering College, Palakkad

Department of

Electronics and Communication Engineering

**CLASSIFICATION OF AUTISM AND ADHD USING**

**EEG BASED ON DEEP LEARNING**

PRINCIPLE

CO-

INVESTIGATOR :

Assistant Professor

Dr. Jayadevan R

INVESTIGATORS :

Arun J Dev

Femina N

Nikhil K J

Chithira M

1



<a name="br2"></a> 

INTRODUCTION

• ASD and ADHD are two common neurodevelopmental disorders that affect millions of

individuals worldwide.

• Deep learning improves medical diagnosis accuracy and efficiency.

• Deep learning algorithms can identify patterns in clinical data which can be trained on

large datasets and can predict neurodevelopmental disorders.

• This approach has the potential to enhance the accuracy and reliability of diagnosis,

which is critical for early intervention and improving outcomes for individuals with these

conditions.



<a name="br3"></a> 

CURRENT PRACTICES IN DIAGNOSIS

• ASD diagnosis involves a comprehensive assessment of an individual's behavioral,

social, and developmental functioning.

• ADHD diagnosis involves a comprehensive assessment of an individual's behavioral,

cognitive, and developmental functioning.

• Current diagnostic practices rely on interviews, observation, and rating scales that can be

time-consuming and require trained professionals.

3



<a name="br4"></a> 

PROBLEM STATEMENT

• The readings of EEG signals are analyzed by neurologists to detect and

categorize the patterns of the disorder.

• The visual examination is time-consuming and laborious and it requires the

services of an expert.

• Absence of an implemented automated system to detect the neurological

disorders at an early stage of life.

• Diagnosis can be complicated by overlapping symptoms between ASD and

ADHD, as well as comorbid conditions.



<a name="br5"></a> 

OBJECTIVE

• To select an alternative method for the detection of neurological disorder by performing

classification using EEG signals based on deep learning to get a relatively high degree of

accuracy.

• Our work mainly analyzes the performance of various deep convolutional architectures for the

classification of ASD and ADHD.

• Many lives are impacted by undetected neurological disorders in their early stages .Our

project aims to change this through an innovative AI-based classification system.

5



<a name="br6"></a> 

BACKGROUND STUDY

“Global prevalence of autism: A systematic review update” a review article by Jinan etal. [8]

reviewed studies of the prevalence of autism worldwide, considering the impact of geographic,

ethnic, and socioeconomic factors on prevalence estimates. Approximately 1/100 children are

diagnosed with autism spectrum disorder around the world.

In the article “ADHD and learning disabilities: Research findings and clinical implications” by

DuPaul et al. [9] the relationship between the symptoms of ADHD and academic

underachievement has been well documented.Children with attention-deficit/hyperactivity disorder

(ADHD) are at higher than average risk for academic achievement difficulties and learning

disabilities (LDs). Several decades of research indicate that about 27% to 31% of students with

ADHD also have LDs, although estimates vary widely depending on the criteria used to define

LDs.



<a name="br7"></a> 

BACKGROUND STUDY

"Automated EEG-Based Diagnosis of Attention Deficit Hyperactivity Disorder (ADHD)" by M.

Arns et al. [10]: The paper proposes an automated EEG-based diagnostic system for ADHD

using a machine learning algorithm. The authors used EEG data from 102 children with ADHD

and 102 controls to train and test the algorithm. The results show that the algorithm achieved an

accuracy of 89% in classifying ADHD patients from controls.

"EEG-Based Diagnosis of Autism Spectrum Disorder (ASD) Using Machine Learning

Techniques" by G. Ramaswamy et al. [11]: The study presents an EEG-based diagnostic system

for ASD using machine learning techniques. The authors used EEG data from 28 children with

ASD and 28 controls to train and test the algorithm. The results show that the algorithm achieved

an accuracy of 92% in diagnosing ASD patients from controls.

"EEG-Based Classification of Learning Disabilities" by T. Adalı et al. [12]: The paper presents an

EEG-based classification system for learning disabilities. The authors used EEG data from 58

children with learning disabilities and 58 controls to train and test the algorithm. The results show

that the algorithm achieved an accuracy of 84% in classifying learning disability patients from

controls.



<a name="br8"></a> 

METHODOLOGY



<a name="br9"></a> 

PRE-PROCESSING

•Noise and artifacts can reduce EEG signal quality and impact

classification.

•Makoto's pre-processing pipeline and the EEGLAB toolbox in

MATLAB will be used to address this.

•Pre-processing improves data quality, reduces noise, and saves

time for more accurate analysis.

1\. Apply a notch filter to remove unwanted frequencies from the data.

2\. Apply a bandpass filter with a range of 0.3-50Hz to isolate frequencies of interest for the

analysis.

3\. Re-referenced the data by converting the reference to average reference



<a name="br10"></a> 

MNE-PYTHON

• MNE-Python is a Python-based software package for analyzing EEG and

MEG data.

• It includes functions for loading, preprocessing, visualizing, and analyzing

neurophysiological data.

• Artifact detection and correction functions in MNE-Python can identify and

remove eye blinks, muscle activity, and other unwanted noise.

• Epoching functions can segment the data into smaller time windows for

further analysis.



<a name="br11"></a> 

D ATA SEGMENTATION

• As much as more training samples be available, machine

learning models can better estimate the relationships

between features.

• EEG data is typically collected for several minutes at a time

for a single participant.

o By splitting the data into shorter segments, better control

of the complexity of the input is possible

o Much easier for the deep learning model to learn the

relevant patterns in the data.

• Will use **Hanning Window** to split the samples into 4-second

segments with 75% overlap which makes the numbers of samples

will be increased about 27 times for the proposed method.[1]

• Data Segmentation can implemented using tools such as MNE-

Python, EEGLAB



<a name="br12"></a> 

DEEP LEARNING

• A machine learning technique that teaches computers to do

what comes naturally to humans: learn by example.

• Computer model learns to perform classification tasks

directly from images, text, or sound.

• Most deep learning methods use neural

network architectures

• Given enough amount of Training samples, neural networks

can classify most of the complex relationships.

12



<a name="br13"></a> 

DEEP LEARNING WORKFLOW

13



<a name="br14"></a> 

TRAIN TEST

SPLIT

• The dataset consisted of EEG recordings from

16 patients with ASD (Autism Spectrum

Disorder) and 16 patients with ADHD (Attention-

Deficit/Hyperactivity Disorder).

• Two patients with ASD and two patients with

ADHD were randomly selected from the dataset

to be part of the testing dataset.

• The remaining 14 patients with ASD and 14

patients with ADHD were used to train and

validate the deep learning model.

• Training dataset trains the model to classify

ASD and ADHD, testing dataset evaluates the

model's performance on new data.



<a name="br15"></a> 

CONVOLUTIONAL NEURAL NETWORK

• CNN takes an image as input and extracts features of the image using convolution

and pooling layers.

• Extracted features are fed into flattening and fully-connected layers for

classification.

• CNN helps to achieve

high accuracy in EEG

classification tasks.

• Training on a large

dataset of EEG images

helps to learn the

complex relationships

between different

frequency bands and

EEG signals.



<a name="br16"></a> 

CNN MODEL ARCHITECTURE



<a name="br17"></a> 

5-FOLD CROSS-VALIDATION FOR

DEEP LEARNING

• Helps to prevent overfitting in deep learning

models.

• Data is divided into 5 equally sized folds.

• Model is trained on 4 folds and evaluated on

the remaining fold.

• Process is repeated 5 times with a different

fold held out each time.

• Results are averaged for a final estimate of

the model's performance.



<a name="br18"></a> 

DATASETS

•The datasets received

from ICCONS includes 16

pure ASD and pure ADHD

signals of Childrens between

age group of 2-10 years.

• Each signals consists

of 21 channels and are sampled

at 250Hz.



<a name="br19"></a> 

PSD OF RAW EEG D ATA

• Power spectral density visualizes EEG frequency content and helps identify

frequency bands of interest (e.g. alpha, beta, theta) or any data artifacts.

Raw PSD data

Filtered PSD data



<a name="br20"></a> 

HANNING WINDOW

• A Hanning window is a type of window function

commonly used in digital signal processing to

reduce spectral leakage when analysing a finite

segment of a longer signal, and can help improve

the accuracy of frequency analysis by reducing

spectral leakage and smoothing the signal at

segment edges.

• The Hanning window is a type of cosine-based

window function that is defined by the formula:

w(n) = 0.5 - 0.5*cos(2*pi\*n/N)



<a name="br21"></a> 

REFERENCE

[1] Moghaddari, M., Lighvan, M. Z., & Danishvar, S. (2020). Diagnose ADHD disorder in

children using convolutional neural network based on continuous mental task EEG.

*Computer Methods and Programs in Biomedicine, 197*, Article 105738. <https://doi.org/>

10\.1016/j.cmpb.2020.105738

[2] Akhtar, M. T. , Mitsuhashi, W., & James, C. J. (2012). Employing spatially constrained ICA

and wavelet denoising, for automatic removal of artifacts from multichannel EEG data.

Signal processing, 92(2), 401-416.

[3] Uyulan, C., Ergüzel, T. T. , Unubol, H., Cebi, M., Sayar, G. H., Nezhad Asad, M., & Tarhan,

N. (2021). Major depressive disorder classification based on different convolutional neural

network models: Deep learning approach. *Clinical EEG and Neuroscience, 52*(1), 38–51.

<https://doi.org/10.1177/1550059420916634>[,](https://doi.org/10.1177/1550059420916634)[ ](https://doi.org/10.1177/1550059420916634)[1550059420916634.](https://doi.org/10.1177/1550059420916634)

[4] Saby, J. N., & Marshall, P. J. (2012). The utility of EEG band Power Analysis in the study

of infancy and early childhood. *Developmental Neuropsychology*, *37*(3), 253–273.

<https://doi.org/10.1080/87565641.2011.614663>



<a name="br22"></a> 

REFERENCE

[5] Bi, X., & Wang, H. (2019). Early Alzheimer’s disease diagnosis based on EEG

spectral images using deep learning. *Neural Networks: The Official Journal of the*

*International Neural Network Society, 114*, 119–135. <https://doi.org/10.1016/j>.

neunet.2019.02.005

[6] Chen, H., Song, Y. , & Li, X. (2019a). A deep learning framework for identifying

children with ADHD using an EEG-based brain network. *Neurocomputing, 356*, 83–96.

https:// doi.org/10.1016/j.neucom.2019.04.058. Scopus.

[7] "Makoto’s preprocessing pipeline." https://sccn.ucsd.edu/wiki/Makoto’s \_

preprocessing \_ pipeline

[8] Zeidan J, Fombonne E, Scorah J, Ibrahim A, Durkin MS, Saxena S, Yusuf A, Shih A,

Elsabbagh M. Global prevalence of autism: A systematic review update. Autism Res.

2022 May;15(5):778-790. doi: 10.1002/aur.2696. Epub 2022 Mar 3. PMID: 35238171;

PMCID: PMC9310578.



<a name="br23"></a> 

REFERENCE

[9] DuPaul, George & Volpe, Robert. (2009). ADHD and learning disabilities: Research

findings and clinical implications. Current Attention Disorders Reports. 1. 152-155.

10\.1007/s12618-009-0021-4.

[10] Arns, M., Conners, C. K., & Kraemer, H. C. (2013). Automated EEG-based diagnosis of

attention deficit hyperactivity disorder: A multi-site validation study. Clinical EEG and

neuroscience, 44(4), 288-297.

[11] G. Ramaswamy et al., "EEG-Based Diagnosis of Autism Spectrum Disorder (ASD)

Using Machine Learning Techniques," Journal of Autism and Developmental Disorders, vol.

47, no. 10, pp. 3345-3355, Oct. 2017

[12] Adalı, T. , Anderson, C., Pierce, D., & Barbour, R. (2015). EEG-Based Classification of

Learning Disabilities. IEEE Transactions on Neural Systems and Rehabilitation Engineering,

23(6), 1027-1035. doi: 10.1109/TNSRE.2015.2421985

