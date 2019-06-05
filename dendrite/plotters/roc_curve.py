import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

from ..converters import TrainTestSplit


class ROCCurve(object):
    """ This only works for a single class classification currently """
    def calc(self, parent, test_size=0.25, **kwargs):
        X = parent.dataset
        y = parent.target
        X_train, X_test, y_train, y_test = TrainTestSplit(X, y, test_size=test_size).split()

        y_score = parent.predictor.fit(X_train, y_train).decision_function(X_test)
        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        fpr[0], tpr[0], _ = roc_curve(y_test.nd_array[:, 0], y_score)
        roc_auc[0] = auc(fpr[0], tpr[0])
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
