eta_list = [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]]
num_epochs = 10
report_step = 5
converged = False
loss_diff = 0.1
threshold_value = 25

for e_list in eta_list:
    iter_list = []
    for eta in e_list:

        converged = False
        iteration = 0
        lr = LogReg(train_set, test_set, lam=3e-9, eta=eta)

        for pp in range(num_epochs):
            if converged:
                break

            # shuffle the data
            np.random.shuffle(lr.train_set)

            # loop over each training example
            for ex in lr.train_set:
                # perform SGD update of weights
                if converged:
                    break

                lr.sgd_update(ex, iteration)

                # record progress
                if iteration % report_step == 1:
                    train_nll, train_acc = lr.compute_progress(lr.train_set)
                    test_nll, test_acc = lr.compute_progress(lr.test_set)
                    lr.train_nll.append(train_nll)
                    lr.test_nll.append(test_nll)
                    lr.train_acc.append(train_acc)
                    lr.test_acc.append(test_acc)

                    if len(lr.train_nll) > 5:
                        # select last 5
                        rec_loss_list = lr.train_nll[-5:]
                        g = True

                        for r in rec_loss_list:
                            if r > threshold_value:
                                g = False

                        if g is True:
                            for r in range(0, len(rec_loss_list) - 1):
                                if abs(rec_loss_list[r] - rec_loss_list[r + 1]) >= loss_diff:
                                    g = False
                                    break

                            if g is True:
                                iter_list.append(iteration)
                                converged = True

                iteration += 1

    plt.plot(e_list, iter_list)
    plt.show()
    plt.clf()
    plt.close()