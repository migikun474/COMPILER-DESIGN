static int counter;

int classify(int n) {
    switch (n) {
        case 0:
            return 0;
        case 1:
            return 1;
        default:
            break;
    }

    for (counter = 0; counter < n; counter++) {
        if (counter == 5) {
            continue;
        }
        if (counter == 8) {
            break;
        }
    }

    while (counter > 0) {
        counter--;
    }

    do {
        counter++;
    } while (counter < n);

    counter = 0;
    until (counter >= n) {
        counter++;
        if (counter == 100) {
            goto done;
        }
    }

done:
    return counter;
}
