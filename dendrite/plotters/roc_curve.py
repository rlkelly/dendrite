import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split


class ROCCurve(object):
    def __init__(self, X=None, y=None):
        self.X = X
        self.y = y
        self.n_classes = 0 if not y else len(y[0])

    def __call__(self, X, y):
        self.n_classes = len(y[0])
        self.X = X
        self.y = y

    def calc(self, parent, test_size=0.7, **kwargs):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

        y_score = parent.classifier.fit(X_train, y_train).decision_function(X_test)
        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        for i in range(self.n_classes):
            fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
            roc_auc[i] = auc(fpr[i], tpr[i])
        self.fpr = fpr
        self.tpr = tpr
        self.roc_auc = roc_auc

    def plot(self, parent, **kwargs):
        self.calc(parent, **kwargs)
        plt.figure()
        lw = 2
        for i in range(len(self.fpr)):
            plt.plot(self.fpr[i], self.tpr[i],
                     lw=lw, label='ROC curve (area = %0.2f)' % self.roc_auc[i])
            plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title('Receiver operating characteristic example')
            plt.legend(loc="lower right")
            plt.show()

if __name__ == '__main__':
    ROCCurve(X, y).plot()
