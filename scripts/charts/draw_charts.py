import matplotlib.pyplot as plt

def draw_removal_results():
    removal_counts = [0, 1, 2, 3, 4, 5]
    regular_removal_accuracies = [1, 0.99, 0.97, 0.95, 0.92, 0.85]
    random_removal_accuracies = [1, 0.98, 0.98, 0.96, 0.90, 0.86]

    fig = plt.figure()
    plt.title("Accuracy of M model regarding training dataset size")
    plt.ylabel('Accuracy')
    plt.xlabel('Removal proportion')
    plt.plot(removal_counts, regular_removal_accuracies, label="Regular removal")
    plt.plot(removal_counts, random_removal_accuracies, label="Random removal")
    plt.legend()
    fig.savefig("accuracy_on_removal.pdf", bbox_inches='tight')

def draw_regular_preserve_results():
    perserved_counts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rmse = [0.6314641367741514, 1.1146964710320633, 1.180393840947527, 1.1243064048857738, 0.8704785344949503, 1.3144519839985178, 0.8223634484510426, 1.1074459050821306, 1.1035328960664683, 1.1207600774249211]

    fig = plt.figure()
    plt.title("Accuracy of M model regarding training dataset size")
    plt.ylabel('RMSE')
    plt.xlabel('Kept data (1 datum out of X)')
    plt.plot(perserved_counts, rmse)
    fig.savefig("accuracy_on_regular_preserve.pdf", bbox_inches='tight')

def draw_fli_results():
    perserved_counts = [0, 0.00001, 0.0001, 0.001, 0.01, 0.1, 0.2, 0.3]
    rmse = [0.6314634158482261, 0.6314634158482261, 0.6314601515947191, 0.6323395909646431, 0.665219421710249, 1.040324541439869, 8.737359548164513, 2.8089075574997477]

    fig = plt.figure()
    plt.title("Accuracy of M model regarding FLI compression")
    plt.ylabel('RMSE')
    plt.xlabel('Tolerated error')
    plt.plot(perserved_counts, rmse)
    fig.savefig("accuracy_on_fli.pdf", bbox_inches='tight')

def draw_linear_results():
    tolerated_errors = [x / 100.0 for x in range(0, 110, 10)]
    accuracies = [x / 100.0 for x in range(100, 45, -5)]

    fig = plt.figure()
    plt.title("Accuracy of M model regarding linear compression strength")
    plt.ylabel('Accuracy')
    plt.xlabel('Tolerated error')
    plt.plot(tolerated_errors, accuracies)
    fig.savefig("accuracy_on_linear.pdf", bbox_inches='tight')

draw_removal_results()
draw_linear_results()
draw_regular_preserve_results()
draw_fli_results()
