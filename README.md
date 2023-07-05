

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


INTRODUCTION

• ASD and ADHD are two common neurodevelopmental disorders that affect millions of

individuals worldwide.

• Deep learning improves medical diagnosis accuracy and efficiency.

• Deep learning algorithms can identify patterns in clinical data which can be trained on

large datasets and can predict neurodevelopmental disorders.

• This approach has the potential to enhance the accuracy and reliability of diagnosis,

which is critical for early intervention and improving outcomes for individuals with these

conditions.


CURRENT PRACTICES IN DIAGNOSIS

• ASD diagnosis involves a comprehensive assessment of an individual's behavioral,

social, and developmental functioning.

• ADHD diagnosis involves a comprehensive assessment of an individual's behavioral,

cognitive, and developmental functioning.

• Current diagnostic practices rely on interviews, observation, and rating scales that can be

time-consuming and require trained professionals.


PROBLEM STATEMENT

• The readings of EEG signals are analyzed by neurologists to detect and

categorize the patterns of the disorder.

• The visual examination is time-consuming and laborious and it requires the

services of an expert.

• Absence of an implemented automated system to detect the neurological

disorders at an early stage of life.

• Diagnosis can be complicated by overlapping symptoms between ASD and

ADHD, as well as comorbid conditions.


OBJECTIVE

• To select an alternative method for the detection of neurological disorder by performing

classification using EEG signals based on deep learning to get a relatively high degree of

accuracy.

• Our work mainly analyzes the performance of various deep convolutional architectures for the

classification of ASD and ADHD.

• Many lives are impacted by undetected neurological disorders in their early stages .Our

project aims to change this through an innovative AI-based classification system.




In the article “ADHD and learning disabilities: Research findings and clinical implications” by

DuPaul et al. [9] the relationship between the symptoms of ADHD and academic

underachievement has been well documented.Children with attention-deficit/hyperactivity disorder

(ADHD) are at higher than average risk for academic achievement difficulties and learning

disabilities (LDs). Several decades of research indicate that about 27% to 31% of students with

ADHD also have LDs, although estimates vary widely depending on the criteria used to define

LDs.


METHODOLOGY

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



MNE-PYTHON

• MNE-Python is a Python-based software package for analyzing EEG and

MEG data.

• It includes functions for loading, preprocessing, visualizing, and analyzing

neurophysiological data.

• Artifact detection and correction functions in MNE-Python can identify and

remove eye blinks, muscle activity, and other unwanted noise.

• Epoching functions can segment the data into smaller time windows for

further analysis.



DATA SEGMENTATION

• As much as more training samples be available, machine

learning models can better estimate the relationships

between features.

• EEG data is typically collected for several minutes at a time

for a single participant.

o By splitting the data into shorter segments, better control

of the complexity of the input is possible

o Much easier for the deep learning model to learn the

relevant patterns in the data.

• Will use **Hanning Window** to split the samples into 1-second

segments with 50% overlap which makes the numbers of samples

will be increased about 27 times for the proposed method.[1]

• Data Segmentation can implemented using tools such as MNE-

Python, EEGLAB

DATASETS

•The datasets received

from ICCONS includes 16

pure ASD and pure ADHD

signals of Childrens between

age group of 2-10 years.

• Each signals consists

of 21 channels and are sampled

at 250Hz.

DEEP LEARNING

• A machine learning technique that teaches computers to do

what comes naturally to humans: learn by example.

• Computer model learns to perform classification tasks

directly from images, text, or sound.

• Most deep learning methods use neural

network architectures

• Given enough amount of Training samples, neural networks

can classify most of the complex relationships.

 

TRAIN TEST SPLIT

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















