import sys
from feature_extraction import main as feature_main
from SVM_classifier import extract_features_and_labels, extract_features, create_classifier, classify_data, evaluate
from SVM_classifier import main as main2

#######################################################################################################################################
if len(sys.argv) > 1:
    training_file = sys.argv[1] #this one should be "../DATA/UP_English-EWT/duplicated_train.csv"
    test_file = sys.argv[2]
else:
    training_file = "../DATA/UP_English-EWT/duplicated_trainpiccolo.csv"
    test_file = "../DATA/UP_English-EWT/duplicated_trainpiccolo.csv"
     #this one should be "../DATA/UP_English-EWT/duplicated_test.csv"
print(test_file)
print(training_file)
print()
print()
print()

#1. We extract the features from the raw training set and test set
print("PART 1: FEATURE EXTRACTION FROM THE ORIGINAL TRAINING AND TEST SETS")
print()
print()
print()
print('extracting features from training file')
feature_main(training_file)
print('extracting features from test file')
feature_main(test_file)

#2. We train the SVM classifier on the extracted-features-training file
print("PART 2: TRAINING THE SVM CLASSIFIER ON THE TRAINING FILE (WITH THE FEATURES EXTRACTED)")
print()
print()
print()
main2(training_file.replace('.csv' , '-features_extracted.csv'), test_file.replace('.csv' , '-features_extracted.csv'))

#3. We test the svm classifier on the extracted-features-test file
print("PART 3: TESTING THE CLASSIFIER ON THE TEST FILE (WITH FEATURES EXTRACTED)")
print()
print()
print()

print("SRL EXPERIMENT CARRIED OUT SUCCESSFULLY")