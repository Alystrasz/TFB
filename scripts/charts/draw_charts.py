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
    perserved_counts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16]
    rmse = [0.6314641367741514, 1.1146964710320633, 1.180393840947527, 1.1243064048857738, 0.8704785344949503, 1.3144519839985178, 0.8223634484510426, 1.1074459050821306, 1.1035328960664683, 1.1207600774249211, 1.2568667044316555]

    fig = plt.figure()
    plt.title("Accuracy of M model regarding training dataset size")
    plt.ylabel('RMSE')
    plt.xlabel('Kept data (1 datum out of X)')
    plt.plot(perserved_counts, rmse)
    fig.savefig("accuracy_on_regular_preserve.pdf", bbox_inches='tight')

def draw_fli_results():
    results = [
        {"error":0.0001,"samples_original_count":12098170, "model_floats_count":35129874, "rmse":0.6314601515947191},
        {"error":0.0002,"samples_original_count":12098170, "model_floats_count":34259349, "rmse":0.631481042189687},
        {"error":0.0004,"samples_original_count":12098170, "model_floats_count":32712252, "rmse":0.6315406494236255},
        {"error":0.0008,"samples_original_count":12098170, "model_floats_count":29821938, "rmse":0.6320992325480655},
        {"error":0.0016,"samples_original_count":12098170, "model_floats_count":25214850, "rmse":0.6334837751323967},
        {"error":0.0032,"samples_original_count":12098170, "model_floats_count":19382682, "rmse":0.6382794062990357},
        {"error":0.0064,"samples_original_count":12098170, "model_floats_count":13857987, "rmse":0.6494726311684359},
        {"error":0.0128,"samples_original_count":12098170, "model_floats_count":9462975, "rmse":0.6782594614475053},
        {"error":0.0256,"samples_original_count":12098170, "model_floats_count":6243417, "rmse":0.7199984145389016},
        {"error":0.0512,"samples_original_count":12098170, "model_floats_count":3668571, "rmse":0.7957877478250986},
        {"error":0.1024,"samples_original_count":12098170, "model_floats_count":1689576, "rmse":1.0329479126754864},
        {"error":0.2048,"samples_original_count":12098170, "model_floats_count":480936, "rmse":3.5305682447298268},
        {"error":0.4096,"samples_original_count":12098170, "model_floats_count":18288, "rmse":13.295452571302976},
        {"error":0.8192,"samples_original_count":12098170, "model_floats_count":2586, "rmse":97.09020836411514},
        {"error":1.6384,"samples_original_count":12098170, "model_floats_count":2586, "rmse":97.09020836411514},
        {"error":3.2768,"samples_original_count":12098170, "model_floats_count":2586, "rmse":97.09020836411514},
        {"error":6.5536,"samples_original_count":12098170, "model_floats_count":2586, "rmse":97.09020836411514},
        {"error":13.1072,"samples_original_count":12098170, "model_floats_count":2586, "rmse":97.09020836411514}
    ]
    perserved_counts = [0, 0.00001, 0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3]
    rmse = [0.6314634158482261, 0.6314634158482261, 0.6314601515947191, 0.6314810423140886, 0.6316329905267445, 0.6323395909646431, 0.6347552157794631, 0.6442626782795469, 0.665219421710249, 0.7174913415079524, 0.8081353280563366, 1.040324541439869, 8.737359548164513, 2.8089075574997477]

    fig = plt.figure()
    plt.title("Accuracy of M model regarding FLI compression")
    plt.ylabel('RMSE')
    plt.xlabel('Compression rate')
    # plt.plot(perserved_counts, rmse)

    # todo: divide model floats count by columns count
    compression_ratios = [r["samples_original_count"] / r["model_floats_count"] for r in results]
    rmses = [r["rmse"] for r in results]
    plt.plot(compression_ratios, rmses)

    fig.savefig("accuracy_on_fli.pdf", bbox_inches='tight')

def draw_electricity_fli_results():
    results = [
        {"error":1,"samples_original_count":6754803, "model_floats_count":18774477, "mse_norm":0.1400560095826792},
        {"error":2,"samples_original_count":6754803, "model_floats_count":18055548, "mse_norm": 0.1400963620391163},
        {"error":4,"samples_original_count":6754803, "model_floats_count":16870407, "mse_norm":0.1403163973194127},
        {"error":8,"samples_original_count":6754803, "model_floats_count":15072492, "mse_norm": 0.1414036463199564},
        {"error":16,"samples_original_count":6754803, "model_floats_count":12692997, "mse_norm":0.1447340496104468},
        {"error":32,"samples_original_count":6754803, "model_floats_count":9946611, "mse_norm":0.152981061418201},
        {"error":64,"samples_original_count":6754803, "model_floats_count":7253976, "mse_norm":0.1618169963218571},
        {"error":128,"samples_original_count":6754803, "model_floats_count":4920978, "mse_norm":0.3289230026226734},
        {"error":256,"samples_original_count":6754803, "model_floats_count":3056589, "mse_norm": 1.5019162730779316},
        {"error":512,"samples_original_count":6754803, "model_floats_count":1717332, "mse_norm": 22.97868517271081},
        {"error":1024,"samples_original_count":6754803, "model_floats_count":907434, "mse_norm": 187.3767091010364},
        {"error":2048,"samples_original_count":6754803, "model_floats_count":470496, "mse_norm":273.93890006586486},
        {"error":4096,"samples_original_count":6754803, "model_floats_count":230667, "mse_norm":226.3062101857673},
        {"error":8192,"samples_original_count":6754803, "model_floats_count":109026, "mse_norm":231.14713357149185}
    ]

    fig = plt.figure()
    plt.title("Accuracy of M model regarding FLI compression")
    plt.ylabel('MSE')
    plt.xlabel('Compression rate')

    # todo: divide model floats count by columns count
    compression_ratios = [r["samples_original_count"] / r["model_floats_count"] for r in results]
    rmses = [r["mse_norm"] for r in results]
    plt.plot(compression_ratios, rmses)

    fig.savefig("accuracy_on_fli_electricity.pdf", bbox_inches='tight')

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
draw_electricity_fli_results()