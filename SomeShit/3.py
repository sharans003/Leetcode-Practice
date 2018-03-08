from collections import defaultdict

lambda_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lam_powers = [-10, -8, -7, -6, -5, -4, -3]
epoch = 7

convergence_point = 5000  # this is just a random convergence point assumption

accuracy = defaultdict(list)
# print(accuracy)

for power in lam_powers:
    final_lam = []
    for choice in lambda_choices:
        current_lambda = choice * pow(10, power)
        final_lam.append(current_lambda)
        lr = LogReg(train_set, test_set, lam=current_lambda, eta=0.04)
        lr.train(num_epochs=epoch, report_step=convergence_point)
        print('called train with: ', epoch, convergence_point)
        print('test acc is:')
        print(lr.test_acc)
        accuracy[power].append(np.average(lr.test_acc[1:]))
    print('regularization values used -', final_lam)
    acc = []
    for a in accuracy:
        acc.append(accuracy[a])
    print(acc)
    print('final_lam ' + str(final_lam))
    print('accuracy[power] ' + str(accuracy[power]))
    # plt.title('accuracy with different lam choices in the range 10^ raised to power:', power)
    plt.plot(final_lam, accuracy[power])
    plt.xlabel('Lambda')
    plt.ylabel('Accuracy')
    plt.show()

lam_choice = [0.01, 0.1, 0.2, 0.4, 1, 2, 10]
final_lam = []

for choice in lam_choice:
    lr = LogReg(train_set, test_set, lam=choice, eta=0.01)
    lr.train(num_epochs=epoch, report_step=convergence_point, isVerbose=True)
    accuracy[choice].append(np.average(lr.test_acc[1:]))
print('regularization values used -', str(lam_choice))
acc = []
for a in accuracy:
    acc.append(accuracy[a])
print(acc)

# plt.title('accuracy with different lam choices:', str(choice))
plt.plot(lam_choice, accuracy[choice])
plt.xlabel('Lambda')
plt.ylabel('Accuracy')
plt.show()






