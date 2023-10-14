# task-automation
## Data
The data in the (.xlsx) file is real-world health data. For privacy of 
users, content of the messages received from users has been removed and their
phone numbers redacted. Included, are two worksheets:
1) Messages Raw: Incoming message log.
a. Datetime: Date and time of message
b. UserID: Unique identifier for each user. For privacy of our clients, users’ phone
numbers have been replaced with this ID.
c. Original Text: Incoming message from user (removed for privacy purposes)
d. Translation: Text translated from Swahili (removed for privacy purposes)
e. Intent: As detected by the NLP model
f. Confidence: Confidence score/level assigned to the intent by the NLP model
## Task
1) Use the intents in the Messages Raw worksheet and build a USER JOURNEY for each user
(where relevant.) The User Journey can be defined as follows:
a. Some (not all) users ask more than one question.
b. For those that ask more than one question, we know what date they asked the
question and the “intent” behind each question. An example User Journey would be
something like User X, who asked the following questions:
i. 2020-03-05: nutrition
ii. 2020-03-27: pregnancy_anc_visits
iii. 2020-05-12: headache
iv. 2020-05-18: fetal_movement
v. 2020-08-15: labour_delivery
c. Do the same for all users who have asked more than one question.
d. Output the results in a format such that someone who does not have a technical
background can easily understand.
