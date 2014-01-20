def error(preds, targets):
    correct = 0.
    for i,p in enumerate(preds):
        if p == targets[i]: correct += 1
    return correct/len(preds)
