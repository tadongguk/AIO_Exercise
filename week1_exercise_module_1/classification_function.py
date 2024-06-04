def check_type(TP, FP, FN):
    if type(TP) != int:
        return 'TP must be int'
    elif type(FP) != int:
        return 'FP must be int'
    elif type(FN) != int:
        return 'FN must be int'
    else:
        return TP, FP, FN
def classification_function(TP, FP, FN):
    check = check_type(TP, FP, FN)
    if type(TP) != int:
        return 'TP must be int'
    elif type(FP) != int:
        return 'FP must be int'
    elif type(FN) != int:
        return 'FN must be int'
    elif TP <= 0 or FP <= 0 or FN <= 0:
        return 'TP, FP, FN must be greater than or equal to 0'
    else:
        precision = TP / (TP + FP)
        recall = TP / (TP + FN)
        f1 = 2 * (precision * recall) / (precision + recall)
        return precision, recall, f1
if __name__ == '__main__':
    result = classification_function(2, 3 , 4)
    print(f"Precision: {result[0]}")
    print(f"Recall: {result[1]}")
    print(f"F1 Score: {result[2]}")
