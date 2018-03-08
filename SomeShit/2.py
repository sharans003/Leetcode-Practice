from collections import defaultdict

lam_powers = [-10, -8, -7, -6, -5, -4, -3]

epoch = 7
# Assuming that NLL converges at 5000.
iteration_to_see = 5000
train_set_len = len(train_set)

accuracy = defaultdict(list)
for choice in lam_powers:
    lam_choices = []
    for i in range(1, 10):
        lam_curr = i * pow(10, choice)
        lam_choices.append(lam_curr)
        lr = LogReg(train_set, test_set, lam=lam_curr, eta=0.04)
        lr.train(num_epochs=epoch, report_step=iteration_to_see)
        accuracy[choice].append(np.average(lr.test_acc[1:]))

    print('regularization values used -', lam_choices)
    print('accuracy-', ["{0:.4f}".format(a) for a in accuracy[choice]])
    plt.title('accuracy with different lam choices in the range 10^({})'.format(choice))
    plt.plot(lam_choices, accuracy[choice])
    plt.xlabel('lam')
    plt.ylabel('Accuracy')
    plt.show()

lam_choice = [0.01, 0.1, 0.2, 0.4, 1, 2, 10]
accuracy = []
for choice in lam_choice:
    lr = LogReg(train_set, test_set, lam=choice, eta=0.04)
    lr.train(num_epochs=epoch, report_step=iteration_to_see)
    accuracy.append(np.average(lr.test_acc[1:]))

print('regularization values used -', lam_choice)
print('accuracy-', ["{0:.4f}".format(a) for a in accuracy])
plt.title('accuracy with different lam choices)')
plt.plot(lam_choice, accuracy)
plt.xlabel('lam')
plt.ylabel('Accuracy')
plt.show()

"""
Based on the graph, the value of regularization that gives the highest accuracy lies
in the window [4 * 10^(-6), 9*10^(-6)]. These consistently show good performance. Although sometimes,
random values tend to do well. Based on the former observations
and the graph below, My choice would be be 7 e * 10(-6) . The performance reduces with as the value of
lambda increases from 10^(-2) to greater values.
"""