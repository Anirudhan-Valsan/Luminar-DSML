# Support - the count of 0 and 1 in the data

"""
Recall(1) =     TP
             --------
              TP+FN

Recall(0) =     TN
             --------
               TN+FP

Precision(1) =   TP
               -------
                TP+FP

Precision(0) =   TN
               -------
                TN+FN

F1_score


"""

cm = [[79,10],
     [15,30]]

TP = 79

TN = 30

FP = 10

FN = 15



recall_1 = TP/(TP+FN)
recall_0 = TN/(TN+FP)

precision_1 = TP/(TP+FP)
precision_0  = TN/(TN+FN)




"""
Macro_avg_precision = Precision(1)+Precision(0)
                     --------------------------
                                2

Macro_avg_recall = Recall(1) + Recall(0)
                   ---------------------
                             2
                             
Macro_avg_f1_score = F1_score_1 + F1_score_0
                    -------------------------
                                2

"""
f1_score_1 = 2*((precision_1*recall_1)/(precision_1 + recall_1))
f1_score_0 = 2*((precision_0*recall_0)/(precision_0 + recall_0))
macro_avg_recall = (recall_1+recall_0)/2
macro_avg_precision = (precision_1 + precision_0)/2
macro_avg_f1 = (f1_score_0 + f1_score_0)/2

performance = {'recall_1' : recall_1,'recall_0' : recall_0,'precision_1' : precision_1, 'precision_0' : precision_0,
"macro_avg_recall" : {macro_avg_recall}, "macro_avg_precision" : macro_avg_precision, "macro_avg_f1"  : macro_avg_f1}
print(f"macro_avg_recall = {macro_avg_recall}, macro_avg_precision = {macro_avg_precision}, macro_avg_f1 = {macro_avg_f1} ")

"""
Weighted Average

weighted_avg__recall = (Recall(1) * support(1)) + (recall(0) * support(0))
                       ---------------------------------------------------
                                Total number of observation
"""
#assume
support_1 = 74
support_0 = 60



weighted_avg__recall = ((recall_1 * support_1) + (recall_0 * support_0))/134

print(f"weighted_avg__recall : {weighted_avg__recall}")

weighted_avg_precision = ((precision_1 * support_1) + (precision_0 * support_0))/134
weighted_avg_f1 = ((f1_score_1 * support_1)+(f1_score_0 * support_0))/134

print(f"weighted_avg_precision = {weighted_avg_precision} , weighted_avg_f1 = {weighted_avg_f1}")

