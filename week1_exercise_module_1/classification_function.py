def classification_function(tp, fp, fn):

    if type(tp) != int:
        return 'TP must be int'
    elif type(fp) != int:
        return 'FP must be int'
    elif type(fn) != int:
        return 'FN must be int'
    elif tp <= 0 or fp <= 0 or fn <= 0:
        return 'TP, FP, FN must be greater than or equal to 0'
    else:
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1 = 2 * (precision * recall) / (precision + recall)
        return precision, recall, f1
if __name__ == '__main__':
    result = classification_function(5, 3 , 4)
    if type(result) == str:
        print(result)
    else:
        print(f"Precision: {result[0]}")
        print(f"Recall: {result[1]}")
        print(f"F1 Score: {result[2]}")
